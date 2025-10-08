



import re
import sys
import math
import matplotlib.pyplot as plot



if __name__=="__main__":

    inputFile = sys.argv[1]
    index = int(sys.argv[2])

    lines = open(inputFile, 'r').read().splitlines()

    line = lines[index]
    distancesText = re.findall(r"\[(.*?)\]", line)[0].replace(" ", "").split(",")
    distances = [float(text) for text in distancesText]
    angularSpacing = float(re.findall(r".*, (.*?), [0-9]*, $", line)[0])

    angles = []
    for index, distance in enumerate(distances):
        angles.append(angularSpacing * index)

    xValues = []
    yValues = []
    for index, (distance, angle) in enumerate(zip(distances, angles)):

        if (distance == float('inf')):
            continue

        xValues.append(distance * math.cos(angle))
        yValues.append(distance * math.sin(angle))

    plot.scatter(xValues, yValues)
    plot.xlabel("X-Position [m]")
    plot.ylabel("Y-Position [m]")
    plot.title("LiDAR Frame Data")
    plot.show()