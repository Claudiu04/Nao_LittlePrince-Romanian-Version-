# -*- coding: utf-8 -*-
from __future__ import print_function
import sys
from naoqi import ALProxy
import time

IP = "127.0.0.1"   
PORT = 9559

def talk_and_move():
    try:
        
        player = ALProxy("ALAudioPlayer", IP, PORT)
        motion = ALProxy("ALMotion", IP, PORT)
        posture = ALProxy("ALRobotPosture", IP, PORT)

        motion.wakeUp()
        posture.goToPosture("StandInit", 0.5)


       

        


    except Exception as e:
        print("Eroare:", e)


if __name__ == "__main__":
    talk_and_move()
