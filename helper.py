def getInput(file_path):
    # Function to read input data from a file
    input = []
    with open(file_path, 'r') as file:
        lines = file.readlines()    # Read all lines from the file

    # Clean and process each line from the file
    for line in lines:
        input.append(line.replace("\r", "").replace("\n", ""))
    while("" in input):
        input.remove("")
    
    # Initialize lists to store different types of data
    nodes = []       # List to store node information
    neighbors = []   # List to store neighbor information
    probs = []       # List to store probability information

    # Categorize each line into nodes, neighbors, or probabilities
    for line in input:
        if line[0] == '#':
            pass
        elif '=' in line:
            nodes.append(line)
        elif ':' in line:
            neighbors.append(line)
        elif '%' in line:
            probs.append(line)
    
    # Return the categorized lists
    return nodes, neighbors, probs

def printAnswer(dic):
    # Function to print the results of the Markov Decision Process
    policies = []
    nodeValues =[]
    # Process each node in the dictionary
    for node in dic.values():
        # Format the value of the node for printing
        valuetemp = node.name + '=' + str(round(node.curr_value, 3))
        nodeValues.append(valuetemp)
        # Format the policy of decision nodes for printing
        if node.node_type == 'Decision':
            policytemp = str(node.name)+' -> '+str(node.policy)
            policies.append(policytemp)
    # Print all policies
    for i in policies:
        print(i)
    print()
    # Print all node values
    for j in nodeValues:
        print(j, end = ' ')
    print()


