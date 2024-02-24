import sys
from markov_solver import *     # Importing the Markov solver functions
from helper import *            # Importing helper functions

if __name__ == "__main__":
    # Main execution block
    # Extract command line arguments
    commandLst = sys.argv[1:]
    '''
    -df : a float discount factor [0, 1] to use on future rewards, defaults to 1.0 if not set
    -min : minimize values as costs, defaults to false which maximizes values as rewards
    -tol : a float tolerance for exiting value iteration, defaults to 0.01 or 0.001 (matches test outputs)
    -iter : an integer that indicates a cutoff for value iteration, defaults to 100
    '''
    # Define default parameters
    tolerance = 0.001   # Default tolerance for value iteration
    iter = 100          # Default number of iterations for value iteration
    gamma = 1           # Default discount factor
    ismin = 0           # Default behavior to maximize values as rewards

    # Parse command line arguments and set parameters
    for i in range(len(commandLst)):
        arg = commandLst[i]
        if arg == '-df':
            index = commandLst.index(arg)
            gamma = float(commandLst[index+1])
        if arg == '-min':
            ismin = 1
        if arg == '-tol':
            index = commandLst.index(arg)
            tolerance = float(commandLst[index+1])
        if arg == '-iter':
            index = commandLst.index(arg)
            iter = float(commandLst[index+1])
        if arg[-4:] == '.txt':
            file = arg
    
    # Initialize a dictionary to store the Nodes/States of the MDP
    global allNodes

    # initialize a dictionary to store the Nodes/States
    allNodes = {}
    
    # Read inputs from the file
    nodes, neighbors, probs = getInput(file)
    
    # Create the MDP map with the read data
    createMap(allNodes, nodes, neighbors, probs)

    # Solve the MDP using the Markov solver
    allNodes = MarkovSolver(allNodes, gamma, ismin, iter, tolerance)

    # Print the solution
    printAnswer(allNodes)





    
