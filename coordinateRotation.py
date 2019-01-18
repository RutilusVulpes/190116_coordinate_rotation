
import sys
import numpy as np
import matplotlib.pyplot as plt

def main(argv):

    inFile = argv[0]

    CAMERA_AZIMUTH = 45
    cosAz= np.cos(CAMERA_AZIMUTH)
    sinAz= np.sin(CAMERA_AZIMUTH)

    CAMERA_PITCH = -10
    cosPch= np.cos(CAMERA_PITCH)
    sinPch= np.sin(CAMERA_PITCH)
    CAMERA_ROLL = 0
    cosRoll= np.cos(CAMERA_ROLL)
    sinRoll= np.sin(CAMERA_ROLL)
    CAMERA_EASTING = 10000
    CAMERA_NORTHING = 5000
    CAMERA_ELEVATION = 1000

    T = [
    [1, 0, 0,-CAMERA_EASTING],
    [0, 1, 0,-CAMERA_NORTHING],
    [0, 0, 1,-CAMERA_ELEVATION],
    [0, 0, 0, 1]
    ]

    Ryaw = [
    [cosAz, -sinAz, 0, 0],
    [sinAz, cosAz, 0, 0],
    [0, 0, 1, 0]
    ]

    Rpitch = [
    [1, 0, 0],
    [0, cosPch, sinPch],
    [0, -sinPch, cosPch]
    ]

    Rroll = [
    [cosRoll, 0, -sinRoll],
    [0, 1, 0 ],
    [sinRoll, 0 , cosRoll]
    ]

    Raxis = [
    [1, 0, 0],
    [0, 0, -1],
    [0, 1 , 0]
    ]
    #C = Raxis, Rroll, Rpitch, Ryaw, T
    xList = []
    yList = []
    with open(inFile) as file:
        for p in file:
                p = p.strip()
                p = p.split(" ")
                x = float(p[0])
                y = float(p[1])
                z = float(p[2])
                point = [x,y,z,1]

                translated = np.matmul(T,point)
                yawed = np.matmul(Ryaw,translated)
                pitched = np.matmul(Rpitch,yawed)
                rolled = np.matmul(Rroll,pitched)
                swapped = np.matmul(Raxis,rolled)

                xList.append(swapped[0])
                yList.append(swapped[1])

    plt.scatter(xList,yList, c=yList, s=100)
    plt.gray()

    plt.show()
if __name__=='__main__':
  main(sys.argv[1:])
