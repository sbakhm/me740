import pyrosim
import random
import copy
import pickle
import matplotlib.pyplot as plt
from population import POPULATION

# enter simulation parameters
N = 10 # number of individuals in a population
G = 1000 # number of generations
pb = True # set play blind setting: True = blind mode (recommended); False = draw to the screen

# create a population of parents
parents = POPULATION(N) # construct a POPULATION class instance : N parents with different genomes
parents.Evaluate(pb, 'doNotSave') # evaluate N unrelated robots in turn

print('Fitness values of the 1st generation of parents:')
parents.Print()
print # end the current line of printing

print('Fitness values of consequent generations of parents:')

for g in range(0, G): # iterate over generations 0 to G

    # create a population of children
    children = copy.deepcopy(parents) # create children which are clones of the parents
    children.Mutate() # add mutations to the children population
    children.Evaluate(pb, 'doNotSave') # evaluate N unrelated robots in turn

    parents.ReplaceWith(children) # replace less fit parents with their more fit children; leave more fit parents in the parent population

    print(g),
    parents.Print()

parents.Evaluate(False, 'save') # re-evaluate the last generation of parents and draw them to the screen


# f = open('lastGen.p', 'w') # open a file called robot.p
# pickle.dump(parents, f) # save the parents class instance into this file
# f.close() # close the file

#f = plt.figure() # create a figure
#panel = f.add_subplot(111) # add a drawing panel inside that figure
#plt.plot(sensorData) # plot the data in the vector to the panel
##panel.set_ylim(-1,2) # move the lower limit of the vertical limit to -1 and the upper limit to +2
#plt.show() # shows the resulting figure