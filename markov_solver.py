
class Node:
    # Constructor for the Node class
    def __init__(self, name=None, reward=0, policy=None, neighbors=None, 
                 neighbors_prob=None, curr_value=0, prev_value=0, 
                 node_type=None):
        # Initialize node properties
        self.name = name        # Name of the node
        self.reward = reward    # Reward of the node
        self.policy = policy    # Policy associated with the node
        self.neighbors = neighbors if neighbors is not None else []      # List of neighbor nodes
        self.neighbors_prob = neighbors_prob if neighbors_prob is not None else {} # Probabilities of transitioning to neighbor nodes
        self.curr_value = curr_value    # Current value of the node (for value iteration)
        self.prev_value = prev_value    # Previous value of the node (for convergence check)
        self.node_type = node_type      # Type of node (Decision or Chance)


def createMap(allNodes, nodes, neighbours, probs):
    # Function to initialize the Markov Decision Process map
    # Initialize nodes with values
    for assignment in nodes:
        nodeName, nodeValue = assignment.split("=")
        temp = nodeName.strip()

        # Create and configure node
        init_node = Node(temp)
        init_node.name = temp
        init_node.reward = float(nodeValue)
        init_node.prev_value = float(nodeValue)
        init_node.curr_value = float(nodeValue)
        allNodes[nodeName] = init_node

    # Configure neighbors for each node
    for assignment in neighbours:
        currNode, neighbourNode = assignment.split(":")
        currNode = currNode.strip()
        neighbourNode = neighbourNode.replace(',', ' ').replace('[', ' ').replace(']', ' ').replace('\n', ' ')
        neighbour_lst = neighbourNode.split(' ')
        neighbour_lst[:] = [x for x in neighbour_lst if x]

        # Set node type and neighbors
        if len(neighbour_lst) == 1:
            allNodes[currNode].node_type = 'Chance'
        if str(currNode) not in allNodes.keys():
            init_node = Node(currNode)
            init_node.name = currNode
            init_node.neighbors = neighbour_lst
            allNodes[currNode] = init_node
            allNodes[currNode].currvalue = 0
        else:
            allNodes[currNode].neighbors = neighbour_lst

    # Set probabilities for transitioning to each neighbor
    for assignment in probs:
        nodeName, nodeProb = assignment.split("%")
        nodeName = nodeName.strip()
        nodeProb.replace('\n', ' ')
        nodeProb = [var for var in nodeProb.split(' ')]
        nodeProb[:] = [float(x) for x in nodeProb if x]

        # Configure node types and probabilities
        if len(allNodes[nodeName].neighbors) == 1:
            allNodes[nodeName].node_type = 'Chance'
            allNodes[nodeName].curr_value = 0

        elif len(nodeProb)==1:
            allNodes[nodeName].node_type = 'Decision'

        elif nodeProb:
            allNodes[nodeName].node_type = 'Chance'
            allNodes[nodeName].curr_value = 0
        probs = dict(zip(allNodes[nodeName].neighbors, nodeProb))
        allNodes[nodeName].neighbors_prob = probs
    
    # Ensure each decision node has a default policy
    for node in allNodes.values():
        if node.neighbors:
            if not node.neighbors_prob:
                if not node.node_type:
                    node.node_type = 'Decision'
                node.neighbors_prob[node.neighbors[0]] = 1
                
# The subsequent functions implement the value iteration and policy iteration algorithms.
# They are used to calculate the optimal policy for each decision node in the MDP.
# Value iteration computes the value of each state, and policy iteration adjusts the policy based on the computed values.
# The algorithm iterates until the value changes are below a specified tolerance or a maximum number of iterations is reached.

def value_iteration(allNodes, gamma, iter, tolerance, tolFlag):
    # Base case for recursion: stop if maximum iterations reached or no significant change in values
    if iter==0 or tolFlag == 1:
        return allNodes

    for node in allNodes.values():
        temp = 0
        # Process nodes based on their type
        if node.node_type == 'Decision':
            # Compute value for decision nodes
            my_dict = node.neighbors_prob
            var = list(my_dict.values())
            success = var[0]     # Probability of successful outcome
            if len(node.neighbors)>1:
                # Probability of failure divided among other outcomes
                failue = (1-success)/(len(node.neighbors) - 1)
            temp = 0
            for neigh in node.neighbors:
                # Calculate expected value based on current policy
                if neigh == node.policy:
                    temp += success * allNodes[neigh].prev_value
                else:
                    temp += failue * allNodes[neigh].prev_value

            # Update node values for next iteration
            node.prev_value = node.curr_value
            node.curr_value = node.reward + gamma * temp

        elif node.node_type == 'Chance':
            # Compute value for chance nodes
            temp = 0
            for neigh in node.neighbors:
                temp += node.neighbors_prob[neigh] * allNodes[neigh].prev_value

            # Update node values for next iteration
            node.prev_value = node.curr_value
            node.curr_value = node.reward + gamma * temp

    # Check for convergence
    check = 1
    for node in allNodes.values():
        if node.node_type:
            if abs(node.curr_value - node.prev_value) < tolerance:
                pass
            else:
                check = 0
                break        
    # Recursive call for next iteration
    return value_iteration(allNodes, gamma, iter - 1, tolerance, tolFlag = check)

def initiate_value_iteration(allNodes, gamma, iter, tolerance):
    # Initiates value iteration process
    tolFlag = 0     # Flag to indicate convergence
    return value_iteration(allNodes, gamma, iter, tolerance, tolFlag)

def policy_computation(allNodes, gamma, ismin, iter, tolerance):
    # Compute policy for each decision node
    allNodes = initiate_value_iteration(allNodes, gamma, iter, tolerance)
    currentPolicylst = []   # List to keep track of current policies
    newPolicylst = []       # List for new policies

    # change policy
    for node in allNodes.values():

        if node.node_type == 'Decision':
            currentPolicylst.append(node.policy)
            newPolicy = node.policy

            # Choose new policy based on minimizing or maximizing the value
            if ismin:
                minNode = allNodes[node.policy].curr_value
                # Select policy with minimum value for node
                for neigh in node.neighbors:
                    if allNodes[neigh].curr_value < minNode:
                        minNode = allNodes[neigh].curr_value
                        newPolicy = neigh
            else:
                # Select policy with maximum value for node
                maxNode = allNodes[node.policy].curr_value
                for neigh in node.neighbors:
                    if allNodes[neigh].curr_value > maxNode:
                        maxNode = allNodes[neigh].curr_value
                        newPolicy = neigh
            # Update policy
            node.policy = newPolicy
            newPolicylst.append(node.policy)

    # Check if policies have changed
    # If policies changed, recompute them
    # If policies have stabilized, finalize values and return
    if currentPolicylst != newPolicylst:
        return policy_computation(allNodes, gamma, ismin, iter, tolerance)
    else:
        for node in allNodes.values():
            temp = 0
            if node.node_type == 'Chance':
                temp = 0
                for neigh in node.neighbors:
                    temp += node.neighbors_prob[neigh] * allNodes[neigh].curr_value

                node.prev_value = node.curr_value
                node.curr_value = node.reward + gamma * temp
        return dict(sorted(allNodes.items()))
    
def MarkovSolver(allNodes, gamma, ismin, iter, tolerance):
    # Main function to solve the Markov Decision Process
    # Set initial policy for each decision node
    for node in allNodes.values():
        if node.node_type == 'Decision':
            node.policy = node.neighbors[0]
     # Begin policy computation
    return policy_computation(allNodes, gamma, ismin, iter, tolerance)


    

    
    






