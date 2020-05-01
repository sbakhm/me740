import pyrosim
import matplotlib.pyplot as plt
import random
import constants as c

class ROBOT: # define the class ROBOT

    def __init__(self, sim, wts, A, B, leg): # define the constructor for this class

        self.send_objects(sim, A, B, leg )
        self.send_joints(sim, A, B, leg)
        self.send_sensors(sim)
        self.send_neurons(sim)
        self.send_synapses(sim, wts)

    def send_objects(self, sim, A, B, leg): # create objects

        self.O0 = sim.send_box(x=0, y=0, z=leg + c.R, length=A, width=B, height=2 * c.R, r=0.5, g=0.5, b=0.5)
        self.O1 = sim.send_cylinder(x=0, y= A/2 + leg/2, z=leg + c.R, length=leg, radius=c.R, r1=0, r2=1, r3=0, r=1.0, g=0, b=0)
        self.O2 = sim.send_cylinder(x=B/2 + leg/2, y=0, z=leg + c.R, length=leg, radius=c.R, r1=1, r2=0, r3=0, r=0, g=1.0, b=0)
        self.O3 = sim.send_cylinder(x=0, y=0 -A/2 - leg/2, z=leg + c.R, length=leg, radius=c.R, r1=0, r2=1, r3=0, r=0, g=0,
                                    b=1)
        self.O4 = sim.send_cylinder(x=0 - B/2 - leg/2, y=0, z=leg + c.R, length=leg, radius=c.R, r1=1, r2=0, r3=0, r=1, g=0,
                                    b=1)
        self.O5 = sim.send_cylinder(x=0, y=leg + (A / 2), z=(leg / 2) + c.R, length=leg, radius=c.R, r1=0, r2=0, r3=1,
                                    r=1, g=0, b=0)
        self.O6 = sim.send_cylinder(x=leg + (B / 2), y=0, z=(leg / 2) + c.R, length=leg, radius=c.R, r1=0, r2=0, r3=1,
                                    r=0, g=1, b=0)
        self.O7 = sim.send_cylinder(x=0, y=-(leg + (A / 2)), z=(leg / 2) + c.R, length=leg, radius=c.R, r1=0, r2=0,
                                    r3=1, r=0, g=0, b=1)
        self.O8 = sim.send_cylinder(x=-(leg + (B / 2)), y=0, z=(leg / 2) + c.R, length=leg, radius=c.R, r1=0, r2=0,
                                    r3=1, r=1, g=0, b=1)

        # for evolution of neural controller only

        #self.O0 = sim.send_box(x=0, y=0, z=c.L + c.R, length=c.L, width=c.L, height=2 * c.R, r=0.5, g=0.5, b=0.5)
        # self.O1 = sim.send_cylinder(x=0, y=c.L, z=c.L + c.R, length=c.L, radius=c.R, r1=0, r2=1, r3=0, r=1.0, g=0, b=0)
        # self.O2 = sim.send_cylinder(x=c.L, y=0, z=c.L + c.R, length=c.L, radius=c.R, r1=1, r2=0, r3=0, r=0, g=1.0, b=0)
        # self.O3 = sim.send_cylinder(x=0, y=0 - c.L, z=c.L + c.R, length=c.L, radius=c.R, r1=0, r2=1, r3=0, r=0, g=0,
        #                             b=1)
        # self.O4 = sim.send_cylinder(x=0 - c.L, y=0, z=c.L + c.R, length=c.L, radius=c.R, r1=1, r2=0, r3=0, r=1, g=0,
        #                             b=1)
        # self.O5 = sim.send_cylinder(x=0, y=c.L + (c.L / 2), z=(c.L / 2) + c.R, length=c.L, radius=c.R, r1=0, r2=0, r3=1,
        #                             r=1, g=0, b=0)
        # self.O6 = sim.send_cylinder(x=c.L + (c.L / 2), y=0, z=(c.L / 2) + c.R, length=c.L, radius=c.R, r1=0, r2=0, r3=1,
        #                             r=0, g=1, b=0)
        # self.O7 = sim.send_cylinder(x=0, y=-(c.L + (c.L / 2)), z=(c.L / 2) + c.R, length=c.L, radius=c.R, r1=0, r2=0,
        #                             r3=1,
        #                             r=0, g=0, b=1)
        # self.O8 = sim.send_cylinder(x=-(c.L + (c.L / 2)), y=0, z=(c.L / 2) + c.R, length=c.L, radius=c.R, r1=0, r2=0,
        #                             r3=1,
        #                             r=1, g=0, b=1)

    def send_joints(self, sim, A, B, leg): # create joints

        self.J0 = sim.send_hinge_joint(first_body_id=self.O0, second_body_id=self.O1, x=0, y=A/2,
                                       z=leg+c.R, n1=-1, n2=0, n3=0, lo=-3.14159 / 2, hi=3.14159 / 2)

        self.J1 = sim.send_hinge_joint(first_body_id=self.O1, second_body_id=self.O5, x=0, y=leg + (A/2),
                                       z=leg + c.R, n1=-1, n2=0, n3=0, lo=-3.14159 / 2, hi=3.14159 / 2)

        self.J2 = sim.send_hinge_joint(first_body_id=self.O0, second_body_id=self.O2, x=B/2, y=0,
                                       z=leg + c.R, n1=0, n2=1, n3=0, lo=-3.14159 / 2, hi=3.14159 / 2)

        self.J3 = sim.send_hinge_joint(first_body_id=self.O2, second_body_id=self.O6, x=leg + (B/2), y=0,
                                       z=leg + c.R, n1=0, n2=1, n3=0, lo=-3.14159 / 2, hi=3.14159 / 2)

        self.J4 = sim.send_hinge_joint(first_body_id=self.O0, second_body_id=self.O3, x=0, y=-(A/2),
                                       z=leg + c.R, n1=1, n2=0, n3=0, lo=-3.14159 / 2, hi=3.14159 / 2)

        self.J5 = sim.send_hinge_joint(first_body_id=self.O3, second_body_id=self.O7, x=0, y=-(leg + (A/2)),
                                       z=leg + c.R, n1=1, n2=0, n3=0, lo=-3.14159 / 2, hi=3.14159 / 2)

        self.J6 = sim.send_hinge_joint(first_body_id=self.O0, second_body_id=self.O4, x=-(B/2), y=0,
                                       z=leg + c.R, n1=0, n2=-1, n3=0, lo=-3.14159 / 2, hi=3.14159 / 2)

        self.J7 = sim.send_hinge_joint(first_body_id=self.O4, second_body_id=self.O8, x=-(leg + (B/2)), y=0,
                                       z=leg + c.R, n1=0, n2=-1, n3=0, lo=-3.14159 / 2, hi=3.14159 / 2)

        # for evolution of neural controller only

        # self.J0 = sim.send_hinge_joint(first_body_id=self.O0, second_body_id=self.O1, x=0, y=c.L/2,
        #                                z=c.L+c.R, n1=-1, n2=0, n3=0, lo=-3.14159 / 2, hi=3.14159 / 2)
        #
        # self.J1 = sim.send_hinge_joint(first_body_id=self.O1, second_body_id=self.O5, x=0, y=c.L + (c.L/2),
        #                                z=c.L + c.R, n1=-1, n2=0, n3=0, lo=-3.14159 / 2, hi=3.14159 / 2)
        #
        # self.J2 = sim.send_hinge_joint(first_body_id=self.O0, second_body_id=self.O2, x=c.L/2, y=0,
        #                                z=c.L + c.R, n1=0, n2=1, n3=0, lo=-3.14159 / 2, hi=3.14159 / 2)
        #
        # self.J3 = sim.send_hinge_joint(first_body_id=self.O2, second_body_id=self.O6, x=c.L + (c.L/2), y=0,
        #                                z=c.L + c.R, n1=0, n2=1, n3=0, lo=-3.14159 / 2, hi=3.14159 / 2)
        #
        # self.J4 = sim.send_hinge_joint(first_body_id=self.O0, second_body_id=self.O3, x=0, y=-(c.L/2),
        #                                z=c.L + c.R, n1=1, n2=0, n3=0, lo=-3.14159 / 2, hi=3.14159 / 2)
        #
        # self.J5 = sim.send_hinge_joint(first_body_id=self.O3, second_body_id=self.O7, x=0, y=-(c.L + (c.L/2)),
        #                                z=c.L + c.R, n1=1, n2=0, n3=0, lo=-3.14159 / 2, hi=3.14159 / 2)
        #
        # self.J6 = sim.send_hinge_joint(first_body_id=self.O0, second_body_id=self.O4, x=-(c.L/2), y=0,
        #                                z=c.L + c.R, n1=0, n2=-1, n3=0, lo=-3.14159 / 2, hi=3.14159 / 2)
        #
        # self.J7 = sim.send_hinge_joint(first_body_id=self.O4, second_body_id=self.O8, x=-(c.L + (c.L/2)), y=0,
        #                                z=c.L + c.R, n1=0, n2=-1, n3=0, lo=-3.14159 / 2, hi=3.14159 / 2)

    def send_sensors(self, sim): # add sensors to objects and joints

        self.T0 = sim.send_touch_sensor(body_id=self.O5)
        self.T1 = sim.send_touch_sensor(body_id=self.O6)
        self.T2 = sim.send_touch_sensor(body_id=self.O7)
        self.T3 = sim.send_touch_sensor(body_id=self.O8)
        self.P4 = sim.send_position_sensor(body_id=self.O0)

    def send_neurons(self, sim): # attach sensor neurons to sensors and motor neurons to joints

        self.O = {}
        self.O[0] = self.O0
        self.O[1] = self.O1
        self.O[2] = self.O2
        self.O[3] = self.O3
        self.O[4] = self.O4
        self.O[5] = self.O5
        self.O[6] = self.O6
        self.O[7] = self.O7
        self.O[8] = self.O8

        self.J={}
        self.J[0] = self.J0
        self.J[1] = self.J1
        self.J[2] = self.J2
        self.J[3] = self.J3
        self.J[4] = self.J4
        self.J[5] = self.J5
        self.J[6] = self.J6
        self.J[7] = self.J7

        self.S = {}
        self.S[0] = self.T0
        self.S[1] = self.T1
        self.S[2] = self.T2
        self.S[3] = self.T3

        self.SN = {} # create a dictionary to store the IDs of sensor neurons
        self.MN = {} # create a dictionary to store the IDs of motor neurons

        for s in self.S:

            self.SN[s] = sim.send_sensor_neuron(sensor_id=self.S[s]) # attach a sensor neuron to each sensor

        for j in self.J:

            self.MN[j] = sim.send_motor_neuron(joint_id=self.J[j], tau=0.3) # attach a motor neuron to each joint

    def send_synapses(self, sim, wts): # add synapses: use a for loop to connect ALL s synapses to ALL m motor neurons

        for j in self.SN:

            for i in self.MN:

                sim.send_synapse(source_neuron_id=self.SN[j], target_neuron_id=self.MN[i], weight=wts[j, i])