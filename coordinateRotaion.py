
import sys

def main(argv):

    inFile = argv[0]

    CAMERA_AZIMUTH = 45
    CAMERA_PITCH = -10
    CAMERA_ROLL = 0
    CAMERA_EASTING = 10000
    CAMERA_NORTHING = 5000
    CAMERA_ELEVATION = 1000

    with open(inFile) as file:
        for p in file:
                p = p.strip()
                p = p.split(" ")
                x = float(p[0])/float(p[2])
                y = float(p[1])/float(p[2])

if __name__=='__main__':
  main(sys.argv[1:])
