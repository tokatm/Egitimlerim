import math
import random

class SA:
    def __init__(self, matrix, T = -1, alpha = -1, stopping_T = -1, stoppingIter = -1):
        self.matrix = matrix
        self.N = len(matrix)
        self.T = math.sqrt(self.N) if T == -1 else T
        self.T_save = self.T
        self.alpha = 0.90 if alpha == -1 else alpha
        self.stoppingTemperature = 1e - 8 if stopping_T == -1 else stopping_T
        self.stoppingIter = 100000 if stoppingIter == -1 else stoppingIter
        self.iteration = 1
        self.nodes = [i for i in range(self.N)]
        self.bestSolution = None
        self.bestFitness = float("Inf")
        self.fitnessList = []

    def initialSolution(self):
        curNode = random.choice(self.nodes)
        solution = [curNode]
        freeNodes = set(self.nodes)
        freeNodes.remove(curNode)

        while freeNodes:
            nextNode = min(freeNodes, key=lambda x: self.dist(curNode, x))
            freeNodes.remove(nextNode)
            solution.append(nextNode)
            curNode = nextNode
        curFit = self.fitness(solution)
        
