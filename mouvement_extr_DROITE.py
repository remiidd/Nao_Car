#!/usr/bin/env python

import sys
from math import radians
from naoqi import ALProxy
import time

def main(robotIP):
    
    PORT = 9559

    try:
        motionProxy = ALProxy("ALMotion", robotIP, PORT)
    except Exception,e:
        print "Could not create proxy to ALMotion"
        print "Error was: ",e
        sys.exit(1)
        
    motionProxy.setStiffnesses("RShoulderPitch", 1.0)
    motionProxy.setStiffnesses("RShoulderRoll", 1.0)
    motionProxy.setStiffnesses("RElbowRoll", 1.0)
    motionProxy.setStiffnesses("RElbowYaw", 1.0)
    motionProxy.setStiffnesses("LShoulderPitch", 1.0)
    motionProxy.setStiffnesses("LShoulderRoll", 1.0)
    motionProxy.setStiffnesses("LElbowRoll", 1.0)
    motionProxy.setStiffnesses("LElbowYaw", 1.0)
    motionProxy.setAngles("RShoulderPitch", radians(24.3), 0.5)
    motionProxy.setAngles("RShoulderRoll", radians(6.6), 0.5)
    motionProxy.setAngles("RElbowRoll", radians(3.5), 0.5)
    motionProxy.setAngles("RElbowYaw", radians(93.9), 0.5)
    motionProxy.setAngles("LShoulderPitch", radians(84.6), 0.5)
    motionProxy.setAngles("LShoulderRoll", radians(-6.7), 0.5)
    motionProxy.setAngles("LElbowRoll", radians(-88.5), 0.5)
    motionProxy.setAngles("LElbowYaw", radians(-91.4), 0.5)
    time.sleep(1)
    
if __name__ == "__main__":
    robotIp = "192.168.43.31"

    if len(sys.argv) <= 1:
        print "Usage python almotion_setangles.py robotIP (optional default: 127.0.0.1)"
    else:
        robotIp = sys.argv[1]

    main(robotIp)