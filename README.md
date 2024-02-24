# MarkovStrategist-Advanced-MDP-for-Trailblazing-Decisions


QuantumStrategist is a cutting-edge repository dedicated to solving complex Markov Decision Processes (MDP) with applications in game theory and economic models. Our solver leverages sophisticated probabilistic mathematics to analyze and optimize strategic decisions in uncertain environments.

## Theoretical Background

Markov Decision Processes (MDP) provide a mathematical framework for modeling decision making in situations where outcomes are partly random and partly under the control of a decision maker. MDPs are characterized by four key elements:

- **States**: The different situations in which the system or decision-maker can be.
- **Actions**: The choices available to the decision-maker in each state.
- **Transition Probabilities**: The probabilities of moving from one state to another, given an action.
- **Rewards**: The immediate payoff received from moving between states, given an action.

The goal within an MDP framework is to find a policy (a strategy for choosing actions based on the current state) that maximizes the expected sum of rewards, often discounted over time to account for the uncertainty of future rewards.

MDPs apply the principle of **dynamic programming** to solve complex decision-making problems by breaking them down into smaller, manageable sub-problems. The solution involves computing the **value function**, which represents the maximum expected return from each state, and the **policy function**, which indicates the best action to take in each state.

### Value Iteration Algorithm

One common method to solve MDPs is the **value iteration** algorithm, which iteratively updates the value of each state until the values converge to a stable set, indicating the optimal strategy. The algorithm uses the **Bellman equation** to update the value of each state based on the expected rewards and the values of subsequent states.


## Probabilistic Mathematics of MDPs

Markov Decision Processes are grounded in probabilistic mathematics, offering a robust framework for modeling decision-making under uncertainty. The foundational elements involve:

### Transition Probabilities

Transition probabilities, denoted as \(P(s' | s, a)\), represent the probability of transitioning from state \(s\) to state \(s'\) given action \(a\). These probabilities are core to the Markov property, which posits that the future state depends only on the current state and the action taken, not on the sequence of events that led to the current state.

### Reward Function

The reward function, \(R(s, a, s')\), defines the immediate reward received after transitioning from state \(s\) to state \(s'\) due to action \(a\). The objective in an MDP is often to maximize the cumulative reward over time.

### Value Functions


The **value function** \(V(s)\) represents the expected cumulative reward from state \(s\), under a particular policy \(\pi\), across all future time steps. It is defined as:

\[V^\pi(s) = E \left[ \sum_{t=0}^{\infty} \gamma^t R_{t+1} | S_0 = s \right]\]

where \(\gamma\) is the discount factor, determining the present value of future rewards.

### Bellman Equation

The **Bellman equation** provides a recursive decomposition to calculate the value function. For the optimal value function \(V^*(s)\), it is expressed as:

\[V^*(s) = \max_a \sum_{s'} P(s' | s, a) \left[ R(s, a, s') + \gamma V^*(s') 
ight]\]

This equation states that the value of a state under an optimal policy is the maximum expected return achievable, considering immediate rewards and the discounted value of future states.

### Policy Function

The **policy function** \(\pi^*(s)\) maps states to actions and determines the best action to take in each state under the optimal policy:

\[\pi^*(s) = rg\max_a \sum_{s'} P(s' | s, a) \left[ R(s, a, s') + \gamma V^*(s') 
ight]\]

This optimal policy maximizes the expected cumulative reward from each state over time.


## Project Examples

### Market Competition Model Example

**File:** `market_competition.txt`

This example models a simplified scenario of market competition between two firms, Firm A and Firm B, each deciding between high and low investment strategies. The model captures the strategic dynamics and payoffs associated with each combination of choices.

```
# Market Competition Model
# Nodes represent strategic decisions made by the firms
# Rewards represent the net payoff for each firm under each strategy combination
# Edges represent possible strategic shifts
# Probabilities represent the likelihood of each strategic shift, influenced by external market conditions

# Firm A's strategic decisions
A_HI = 0
A_LI = 0

# Firm B's strategic decisions
B_HI = 0
B_LI = 0

# Outcome states based on combined strategies
HI_HI = 2  # Both firms choose High Investment
HI_LI = 4  # Firm A chooses High Investment, Firm B chooses Low Investment
LI_HI = 4  # Firm A chooses Low Investment, Firm B chooses High Investment
LI_LI = 3  # Both firms choose Low Investment

# Transitions from firm strategies to outcomes
A_HI : [HI_HI, HI_LI]
A_LI : [LI_HI, LI_LI]
B_HI : [HI_HI, LI_HI]
B_LI : [HI_LI, LI_LI]

# Probabilities of transitions
# Assuming probabilities influenced by market conditions and competitor's strategy
A_HI % 0.6 0.4
A_LI % 0.5 0.5
B_HI % 0.6 0.4
B_LI % 0.5 0.5
```

### Game Theory:  Territory Conquest Game Example

In the Territory Conquest game, each player aims to capture territories on a board by making strategic decisions based on their current positions, the positions of their opponents, and probabilistic outcomes of their actions. The game is played in turns, with each player deciding to either expand, fortify, or negotiate in each turn. The outcome of each decision is influenced by the current state of the board and the actions of other players.

```
# Territory Conquest Game
# Nodes represent players' decisions in their turn
# Rewards represent the net benefit of holding territories and successful negotiations
# Edges represent possible actions and their outcomes
# Probabilities represent the likelihood of successful actions based on current board state

# Players' decisions
Expand = 0
Fortify = 0
Negotiate = 0

# Outcome states based on decisions
Success_Expand = 3  # Successfully capturing a neighboring territory
Fail_Expand = -1    # Failing to capture, losing resources
Success_Fortify = 2 # Successfully increasing defense, preventing loss
Fail_Fortify = -1   # Failing to fortify, wasted resources
Success_Negotiate = 4 # Successfully negotiating with another player for mutual benefit
Fail_Negotiate = -2  # Failing to negotiate, resulting in loss of trust or resources

# Transitions from decisions to outcomes
Expand : [Success_Expand, Fail_Expand]
Fortify : [Success_Fortify, Fail_Fortify]
Negotiate : [Success_Negotiate, Fail_Negotiate]

# Probabilities of transitions
# These probabilities can be adjusted based on the specific game dynamics and player strategies
Expand % 0.6 0.4
Fortify % 0.7 0.3
Negotiate % 0.5 0.5
```

This example introduces a strategic board game where decision-making under uncertainty is key to conquering territories and achieving victory. The game's dynamics allow for analysis and optimization using MDPs, providing insights into effective strategies for expansion, defense, and negotiation.


## General Usage

To effectively utilize the QuantumStrategist MDP solver, follow these steps:

1. Ensure that Python 3.x is installed on your system. The solver is compatible with Python 3.x versions.
2. Prepare an input file according to the specifications detailed in the "Input File and State Types" section. This file should describe the problem scenario, including states, actions, rewards, and transitions.
3. Save the solver script as `main.py` (or any preferred filename).
4. Execute the script from the command line, passing the input file and optional flags as arguments to customize the solving process.

### Command-Line Arguments

The solver supports the following optional flags to adjust its behavior:

- `-df`: Specify a discount factor (between 0 and 1) to apply to future rewards. Default is `1.0`.
- `-min`: Opt to minimize costs instead of maximizing rewards. By default, the solver maximizes rewards.
- `-tol`: Set a tolerance level for the convergence criterion in value iteration. Default is `0.01`.
- `-iter`: Indicate a maximum number of iterations for the value iteration process. Default is `100`.

### Example Terminal Command

```shell
python main.py -df 0.9 -tol 0.0001 -iter 100 some-input.txt
```

This command runs the solver with a discount factor of 0.9, a tolerance of 0.0001, a maximum of 100 iterations, and uses `some-input.txt` as the input problem definition.

## Output Interpretation

Upon successful execution, the solver outputs:

- **Optimal Policy**: The recommended action for each decision state to achieve the best possible outcome, based on the specified criteria (maximizing rewards or minimizing costs).
- **State Values**: The value of each state under the optimal policy, approximated to three decimal places. These values represent the expected cumulative reward (or cost) starting from that state and following the optimal policy.

### Output Example

```
Policy:
State1 -> ActionA
State2 -> ActionB

Values:
State1=2.456 State2=1.123
```

This output indicates the optimal actions for states `State1` and `State2` and provides their corresponding values, reflecting the expected cumulative reward from following these actions.

Note: In scenarios modeled with only chance nodes, the output will focus solely on state values, as no explicit policy decisions are required.

## Contributing

Contributions are welcome! Please read the contribution guidelines for more information.
