import numpy
from individual import INDIVIDUAL
import pickle

class POPULATION:

    def __init__(self, popSize): # define the constructor

        self.p = {} # create a single internal variable p which stores a dictionary

        for i in range(0, popSize):

            from individual import INDIVIDUAL
            self.p[i] = INDIVIDUAL(i) # call the INDIVIDUAL constructor

    def Evaluate(self, pb, s): # method which iterates over each individual and call its Evaluate() method

        for i in self.p:
            self.p[i].Start_Evaluation(pb) # True = blind mode; False = draw to the screen

        for i in self.p:
            self.p[i].Compute_Fitness()
            fitness = self.p[i].fitness

            if s == 'save':
                f = open('robot.p_'+str(fitness), 'w') # open a file called robot.p
                pickle.dump(self.p[i], f) # save the parents class instance into this file
                f.close() # close the file
                # print "fitness=", fitness

    def Mutate(self):

        for i in self.p:
            self.p[i].Mutate()

    def ReplaceWith(self,other):

        for i in self.p: # iterate over each parent
            if ( self.p[i].fitness < other.p[i].fitness ): # test if parents fitness is less than that of its child
                self.p[i] = other.p[i] # if the parent is less fit than its child, replace it with that child

    def Print(self):  # method which iterates over each individual and calls its Print() method

        for i in self.p:
            self.p[i].Print()

        print  # end the current line of printing