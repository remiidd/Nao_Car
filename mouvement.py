#!/usr/bin/env python
# -*- encoding: UTF-8 -*-

import sys, math
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

    # Example showing how to set angles, using a fraction of max speed
    names  = ["RShoulderPitch"]
    angles  = [1]
    fractionMaxSpeed  = 0.5
    motionProxy.setAngles(names, angles, fractionMaxSpeed)
    time.sleep(1)
    
    
    
    
    
    names  = ["RShoulderPitch"]
    angles  = [-1]
    fractionMaxSpeed  = 0.5
    motionProxy.setAngles(names, angles, fractionMaxSpeed)
    time.sleep(1.0)
    motionProxy.setStiffnesses("RShoulderPitch", 0.0)


if __name__ == "__main__":
    robotIp = "192.168.43.31"

    if len(sys.argv) <= 1:
        print "Usage python almotion_setangles.py robotIP (optional default: 127.0.0.1)"
    else:
        robotIp = sys.argv[1]

    main(robotIp)