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

        time.sleep(3)

        motion.setAngles(["HeadPitch"], [ -0.55 ], 0.2)

        time.sleep(9)

        names = ["LShoulderPitch","LShoulderRoll", "LElbowRoll", "LHand"]
        angles = [-1.2, 0.8, -0.1, 1.0]  
        motion.setAngles(names, angles, 0.3)

        time.sleep(2)

        posture.goToPosture("StandInit", 0.5)


        player.post.playFile("/home/nao/LeAmAratatOamenilor.mp3")

        time.sleep(6)

        motion.setAngles(["HeadYaw", "HeadPitch"], [0.9 , -0.1 ], 0.2)

        time.sleep(5) 

        posture.goToPosture("StandInit", 0.5)

        time.sleep(2)

        player.post.playFile("/home/nao/DesenulMeu.mp3")

        time.sleep(15)


        names = ["RShoulderPitch","RShoulderRoll", "RElbowRoll", "RHand"]
        angles = [-1.2, -0.8, 0.1, 1.0]  
        motion.setAngles(names, angles, 0.3)

        time.sleep(3)

        posture.goToPosture("StandInit", 0.5)


        time.sleep(1)

        player.post.playFile("/home/nao/OameniiMariMau.mp3")

        time.sleep(3)


        names = [ "LWristYaw", "LElbowYaw", "LElbowRoll", "LHand","LShoulderRoll", 
                  "RWristYaw", "RElbowYaw", "RElbowRoll", "RHand","RShoulderRoll",
                  "HeadPitch"]

        
        for i in range(5):
            angles = [-1.2, -0.8, -1.5, 0.8,  0.3,
                       1.2,  0.8,  1.5, 0.8, -0.3,
                       -0.1]  
            motion.setAngles(names, angles, 0.2)
            time.sleep(2)

            angles = [-0.5, -1.6, -0.6, 1.0,  0.6,
                       0.5,  1.6,  0.6, 1.0, -0.6,
                      -0.1] 
            motion.setAngles(names, angles, 0.2)
            time.sleep(2)

            angles = [-0.8, -1.2, -1.0, 1.0,  0.0,
                       0.8,  1.2,  1.0, 1.0,  0.0,
                      -0.4] 
            motion.setAngles(names, angles, 0.2)
            time.sleep(2)

            angles = [-0.3, -1.0, -1.3, 0.9,  0.8,
                       0.3,  1.0,  1.3, 0.9, -0.8,
                      -0.2] 
            motion.setAngles(names, angles, 0.2)
            time.sleep(2)

            angles = [-0.5, -1.6, -0.6, 1.0,  0.6,
                       0.5,  1.6,  0.6, 1.0, -0.6,
                       0.1] 
            motion.setAngles(names, angles, 0.2)
            time.sleep(2)

        posture.goToPosture("StandInit", 0.5)

        time.sleep(3)

        motion.setAngles(["HeadYaw", "HeadPitch"], [0.9 , -0.1 ], 0.2)

        time.sleep(4)

        posture.goToPosture("StandInit", 0.5)


        time.sleep(3)

        motion.setAngles(["HeadPitch"], [ -0.55 ], 0.2)

        time.sleep(3)

        posture.goToPosture("StandInit", 0.5)






    except Exception as e:
        print("Eroare:", e)


if __name__ == "__main__":
    talk_and_move()
