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



        player.post.playFile("/home/nao/PeVremeaMea.mp3")

        time.sleep(8)

        motion.moveTo(0.0, 0.0, 1.5)  

        player.post.playFile("/home/nao/copiaAcestuiDesen.mp3")

        names = ["LShoulderPitch","LShoulderRoll", "LElbowRoll", "LHand"]
        angles = [-1.0, 0.8, -0.06, 1.0]  
        motion.setAngles(names, angles, 0.5)
        
        time.sleep(2)

        motion.setAngles("LHand", 0.0, 0.5)

        motion.moveTo(0.0, 0.0, -1.7)

        player.post.playFile("/home/nao/incartea.mp3")

        names = [ "LWristYaw", "LElbowYaw", "LElbowRoll", "LHand", 
                  "RWristYaw", "RElbowYaw", "RElbowRoll", "RHand"]

        time.sleep(2)
        
        for i in range(4):
            angles = [-1.0, -1.0, -1.4, 1.0,
                      1.0, 1.0,  1.4, 1.0]  
            motion.setAngles(names, angles, 0.2)
            time.sleep(1)

            angles = [-0.2, -1.4, -0.8, 1.0,
                       0.2, 1.4,  0.8, 1.0] 
            motion.setAngles(names, angles, 0.2)
            time.sleep(1)

        motion.setAngles("LHand", 0.0, 0.5)
        motion.setAngles("RHand", 0.0, 0.5)


        time.sleep(4)

        names = ["LShoulderPitch","LShoulderRoll", "LElbowRoll", "LHand"]
        angles = [-1.2, 0.8, -0.06, 1.0]  
        motion.setAngles(names, angles, 0.5)

        posture.goToPosture("StandInit", 0.5)

    except Exception as e:
        print("Eroare:", e)


if __name__ == "__main__":
    talk_and_move()
