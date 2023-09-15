# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""
import collections
import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem: SearchProblem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()
##################################
def breadthFirstSearch(problem: SearchProblem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"

    myQueue = util.Queue()
    done = set()  # store passed state

    startNode = (problem.getStartState(), 0, [])  # start contains node, cost, and path

    myQueue.push(startNode)

    while not myQueue.isEmpty():

        (node, cost, path) = myQueue.pop()
        if problem.isGoalState(node):
            return path
        
        if not node in done:
            done.add(node)


            for next_node, next_action, next_cost in problem.getSuccessors(node):

                print(f'cost: {cost}')
                print(f'path: {path}')


                totalCost = cost + next_cost
                totalPath = path + [next_action]
                totalState = (next_node, totalCost, totalPath)
                myQueue.push(totalState)

    util.raiseNotDefined()
###################################
def uniformCostSearch(problem: SearchProblem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem: SearchProblem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    # create edge to store nodes

    edge = util.PriorityQueue()
    # track visited nodes
    visited = []

    # push initial state to edge
    edge.push((problem.getStartState(), [], 0), heuristic(problem.getStartState(), problem))

    while not edge.isEmpty():
        node = edge.pop()
        state = node[0]
        actions = node[1]

        print(f'STATE: {state}')

        # goal check
        if problem.isGoalState(state):
            return actions
        
        if state not in visited:
            visited.append(state)
            # visit childNode nodes
            successors = problem.getSuccessors(state)

            for childNode in successors:
                # store state, action and cost = 1
                print(f'CHILD NODE LENGTH: {len(childNode)}')

                childNode_state = childNode[0]
                childNode_action = childNode[1]
                if childNode_state not in visited:

                    # add childNode nodes
                    childNode_action = actions + [childNode_action]
                    cost = problem.getCostOfActions(childNode_action)
                    edge.push((childNode_state, childNode_action, 0), cost + heuristic(childNode_state, problem))


    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
