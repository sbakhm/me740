import pyrosim
import random
import math
import numpy
from robot import ROBOT
import constants as c

class INDIVIDUAL:

    def __init__(self, i): # define the constructor

        self.ID = i # assign ID to the individual
        self.A = c.L
        self.B = c.L
        self.leg = c.L

        self.genome = numpy.random.random((4,8)) * 2 - 1
        #self.genome = numpy.random.random(4) * 2 - 1 # local variable storing a single randomly generated synaptic weights from -1 to 1

        self.fitness = 0 # initial fitness = fitness of the parent

    def Start_Evaluation(self, pb):

        # create a Pyrosim simulator
        self.sim = pyrosim.Simulator(play_paused=False, eval_time=1500, play_blind = pb, xyz=[1.0,-2.6,1.5], window_size = (415, 280), hpr = [110,-18,0] )

        # create a robot inside the simulator called sim
        self.robot = ROBOT( self.sim , self.genome, self.A, self.B, self.leg ) # create a class instance of the ROBOT class

        # start the simulation
        self.sim.start()

    def Compute_Fitness(self): # wait until the simulation ends, capture sensor data and use them to compute the robots fitness

        self.sim.wait_to_finish()  # pause execution here until the simulation finishes running

        # capture data from the position sensor
        # x = sim.get_sensor_data(sensor_id=robot.P4, svi=0)
        y = self.sim.get_sensor_data(sensor_id=self.robot.P4, svi=1)  # position INTO the screen
        # z = sim.get_sensor_data(sensor_id=robot.P4, svi=2)
        # print(y[-1])  # print the final position into the screen

        # sensorData = sim.get_sensor_data( sensor_id = R3 ) # store the data from the first sensor in a vector called sensorData after the simulation finishes
        # print(sensorData)

        self.fitness = y[-1]

        del self.sim
        del self.robot

    def Mutate(self): # method for introducing a random mutation to specified gene(s)

        # mutate box dimensions

        self.A = random.gauss(self.A, 0.3*math.fabs(self.A)) # change A to a variable randomaly distributed around current value of A
        self.B = random.gauss(self.B, 0.3*math.fabs(self.B))

        if self.A < 2*c.R:
            self.A = 2*c.R  # impose minimum allowable dim A

        if self.B < 2*c.R:
            self.B = 2*c.R  # impose minimum allowable dim B

        if self.A > 5*c.L:
            self.A = 5*c.L  # impose maximum allowable dim A

        if self.B > 5*c.L:
            self.B = 5*c.L  # impose maximum allowable dim B

        # mutate leg segment length

        self.leg = random.gauss(self.A, 0.3*math.fabs(self.A)) # change A to a variable randomaly distributed around current value of A

        if self.leg > 5*c.L:
            self.leg = 5*c.L    # impose maximum allowable leg segment length

        if self.leg < 0:
            self.leg = 0        # impose minimum allowable leg segment length

        # mutate synaptic weights

        geneToMutateRow = random.randint(0, 3) # generate a random integer from 0 up to and including 3 to choose the gene to mutate
        geneToMutateCol = random.randint(0, 7) # generate a random integer from 0 up to and including 7 to choose the gene to mutate

        self.genome[geneToMutateRow][geneToMutateCol] = random.gauss(self.genome[geneToMutateRow][geneToMutateCol],
                                                    math.fabs(self.genome[geneToMutateRow][geneToMutateCol]))

        if self.genome[geneToMutateRow][geneToMutateCol] > 1:
            self.genome[geneToMutateRow][geneToMutateCol] = 1

        if self.genome[geneToMutateRow][geneToMutateCol] < 1:
            self.genome[geneToMutateRow][geneToMutateCol] = -1

        #self.genome = random.gauss( self.genome , math.fabs(self.genome) ) # assign a new value to the child's genome which is a random number with a Gaussian distribution centered around the current value
        #self.genome[geneToMutate] = random.gauss( self.genome[geneToMutate] , math.fabs(self.genome[geneToMutate]) ) # create a vector of 4 random numbers from -1 up to and including 1

    def Print(self): # print the fitness value of an individual

        #print(self.ID, self.fitness),
        print('[ {} {} ]'.format(self.ID, self.fitness)),