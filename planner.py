import numpy as np
from math import e

# Type of planner
POINT_PLANNER=0; TRAJECTORY_PLANNER=1



class planner:
    def __init__(self, type_):

        self.type=type_

    
    def plan(self, goalPoint=[-1.0, -1.0]):
        
        if self.type==POINT_PLANNER:
            return self.point_planner(goalPoint)
        
        elif self.type==TRAJECTORY_PLANNER:
            return self.trajectory_planner()


    def point_planner(self, goalPoint):
        x = goalPoint[0]
        y = goalPoint[1]
        return x, y

    # TODO Part 6: Implement the trajectories here
    def trajectory_planner(self):
        trajectory = [[], []]

        # Parabola
        for x in np.arange(0.0, 1.6, 0.1):
            trajectory[0].append(x)
            trajectory[1].append(x^2)

        # Sigmoid
        # for x in np.arange(0.0, 2.6, 0.1):
        #     trajectory[0].append(x)
        #     trajectory[1].append(2/(1 + e^(-2*x)) - 1)

        # the return should be a list of trajectory points: [ [x1,y1], ..., [xn,yn]]
        return trajectory

