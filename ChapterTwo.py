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

        player.post.playFile("/home/nao/ChapterTwoMp3/AmTraitAstfel.mp3")

        names = [ "LWristYaw", "LElbowYaw", "LElbowRoll", "LHand","LShoulderRoll", 
                  "RWristYaw", "RElbowYaw", "RElbowRoll", "RHand","RShoulderRoll",
                  "HeadPitch"]
        
        for i in range(2):
            angles = [-1.2, -0.8, -1.5, 0.8,  0.3,
                       1.2,  0.8,  1.5, 0.8, -0.3,
                       -0.1]  
            motion.setAngles(names, angles, 0.2)
            time.sleep(3)

            angles = [-1.5, -1.6, -0.6, 1.0,  0.6,
                       1.5,  1.6,  0.6, 1.0, -0.6,
                      -0.1] 
            motion.setAngles(names, angles, 0.2)
            time.sleep(3)

            angles = [-0.8, -1.2, -1.0, 1.0,  0.0,
                       0.8,  1.2,  1.0, 1.0,  0.0,
                      -0.4] 
            motion.setAngles(names, angles, 0.2)
            time.sleep(3)

            angles = [-0.3, -1.0, -1.3, 0.9,  0.8,
                       0.3,  1.0,  1.3, 0.9, -0.8,
                      -0.2] 
            motion.setAngles(names, angles, 0.2)
            time.sleep(3)

            angles = [-0.5, -1.6, -0.6, 1.0,  0.6,
                       0.5,  1.6,  0.6, 1.0, -0.6,
                       0.1] 
            motion.setAngles(names, angles, 0.2)
            time.sleep(3)
            angles = [-1.2, -1.9, -0.6, 1.0,  0.6,
                       1.2,  1.9,  0.6, 1.0, -0.6,
                       0.1] 
            motion.setAngles(names, angles, 0.2)
            time.sleep(3)

        posture.goToPosture("StandInit", 0.5)

        time.sleep(4)

        motion.setAngles(["HeadYaw", "HeadPitch"], [0.9 , -0.1 ], 0.2)

        time.sleep(7)

        player.post.playFile("/home/nao/ChapterTwoMp3/Poftim.mp3")

        time.sleep(7)

        posture.goToPosture("StandInit", 0.5)

        time.sleep(1)

        player.post.playFile("/home/nao/ChapterTwoMp3/AmSaritInPicioare.mp3") 

        time.sleep(3)

        names = [ "RWristYaw", "RElbowYaw", "RElbowRoll", "RHand","RShoulderRoll","RShoulderPitch",
                  "HeadPitch"]
        angles = [1.2, -0.3,  1.3, 1.0, 0.3, -1.6,
                  0.1]
        
        motion.setAngles(names, angles, 0.2)

        time.sleep(2)

        posture.goToPosture("StandInit", 0.5)


        time.sleep(3)

        names = ["RShoulderPitch","RShoulderRoll", "RElbowRoll", "RHand"]
        angles = [-1.2, -0.8, 0.1, 1.0]  
        motion.setAngles(names, angles, 0.3)

        time.sleep(2)

        posture.goToPosture("StandInit", 0.5)

        time.sleep(1)

        names = [ "LWristYaw", "LElbowYaw", "LElbowRoll", "LHand", 
                  "RWristYaw", "RElbowYaw", "RElbowRoll", "RHand"]

        for i in range(5):
            angles = [-1.0, -1.0, -1.4, 1.0,
                      1.0, 1.0,  1.4, 1.0]  
            motion.setAngles(names, angles, 0.2)
            time.sleep(2)

            angles = [-0.50, -2.0, -0.04, 1.0,
                      0.50, 2.0, 0.04, 1.0]
            motion.setAngles(names, angles, 0.2)
            time.sleep(2)

            angles = [-0.2, -1.4, -0.8, 1.0,
                       0.2, 1.4,  0.8, 1.0] 
            motion.setAngles(names, angles, 0.2)
            time.sleep(2)

        time.sleep(12)    


        player.post.playFile("/home/nao/ChapterTwoMp3/DarCeFaci.mp3")

        names = ["LShoulderRoll", "LElbowRoll", "LElbowYaw" ,"LWristYaw", "LHand", 
                 "RShoulderRoll", "RElbowRoll", "RElbowYaw" ,"RWristYaw", "RHand",
                 "HeadPitch", "HeadYaw"]


        angles = [0.35, -0.04, -2.0, -0.50, 1.0,
                  -0.35, 0.04, 2.0, 0.50, 1.0,
                  0.0, 0.9]  

        motion.setAngles(names, angles, 0.2)

        time.sleep(4)

        posture.goToPosture("StandInit", 0.5)

        time.sleep(8)

        player.post.playFile("/home/nao/ChapterTwoMp3/CandMisterul.mp3")

        names = [ "LWristYaw", "LElbowYaw", "LElbowRoll", "LHand","LShoulderRoll", 
                  "RWristYaw", "RElbowYaw", "RElbowRoll", "RHand","RShoulderRoll",
                  "HeadPitch"]
        
        for i in range(2):
            angles = [-0.9, -1.3, -1.0, 0.8,  0.2,
                       0.9,  1.3,  1.0, 0.8, -0.2,
                       -0.1]  
            motion.setAngles(names, angles, 0.2)
            time.sleep(2)

            angles = [-1.1, -1.0, -1.2, 1.0,  0.4,
                       1.1,  1.0,  1.2, 1.0, -0.4,
                      -0.05]
            motion.setAngles(names, angles, 0.2)
            time.sleep(2)

            angles = [-1.0, -1.2, -0.9, 0.7,  0.3,
                       1.3,  1.5,  1.0, 0.9, -0.6,
                       -0.15] 
            motion.setAngles(names, angles, 0.2)
            time.sleep(2)

            angles = [-1.2, -1.4, -0.7, 0.8,  0.1,
                       1.2,  1.4,  0.7, 0.8, -0.1,
                      -0.05]
            motion.setAngles(names, angles, 0.2)
            time.sleep(2)

            angles = [-0.8, -1.0, -1.1, 0.6,  0.2,
                       0.8,  1.0,  1.1, 0.6, -0.2,
                       0.1]
            motion.setAngles(names, angles, 0.2)
            time.sleep(2)
            angles = [-1.2, -1.9, -0.6, 1.0,  0.6,
                       1.2,  1.9,  0.6, 1.0, -0.6,
                       0.1] 
            motion.setAngles(names, angles, 0.2)
            time.sleep(2)

        names = ["HeadPitch", "HeadYaw"]
        angles = [0.0, 0.9]  

        motion.setAngles(names, angles, 0.2)

        time.sleep(5)
            

        posture.goToPosture("StandInit", 0.5)

        time.sleep(4)

        player.post.playFile("/home/nao/ChapterTwoMp3/CumNuDesenasem.mp3")

        time.sleep(8)

        names = ["HeadPitch", "HeadYaw"]
        angles = [0.0, 0.9]  

        motion.setAngles(names, angles, 0.2)

        time.sleep(15)

        posture.goToPosture("StandInit", 0.5)

        time.sleep(7)

        player.post.playFile("/home/nao/ChapterTwoMp3/AtunciAmCreeat.mp3")

        names = ["LShoulderPitch","LShoulderRoll", "LElbowRoll", "LHand"]
        angles = [-1.0, 0.8, -0.06, 1.0]  
        motion.setAngles(names, angles, 0.5)

        time.sleep(2)

        posture.goToPosture("StandInit", 0.5)

        time.sleep(8)

        player.post.playFile("/home/nao/ChapterTwoMp3/AmDesenatDinnou.mp3")

        time.sleep(1)

        names = ["HeadPitch", "HeadYaw"]
        angles = [0.0, 0.9]  

        motion.setAngles(names, angles, 0.2)

        time.sleep(1)

        posture.goToPosture("StandInit", 0.5)

        time.sleep(10)

        player.playFile("/home/nao/ChapterTwoMp3/AmRefacut.mp3")

        time.sleep(12)

        player.post.playFile("/home/nao/ChapterTwoMp3/AtunciFaraSa.mp3")

        time.sleep(5)

        names = ["RShoulderPitch","RShoulderRoll", "RElbowRoll", "RHand"]
        angles = [-1.2, -0.8, 0.1, 1.0]  

        motion.setAngles(names, angles, 0.3)

        time.sleep(2)

        posture.goToPosture("StandInit", 0.5)

        time.sleep(14)

        player.playFile("/home/nao/ChapterTwoMp3/DeCe.mp3")

        time.sleep(7)

        player.playFile("/home/nao/ChapterTwoMp3/VaFiDeAjuns.mp3")

        time.sleep(6)

        player.playFile("/home/nao/ChapterTwoMp3/SiAstfel.mp3")

        time.sleep(3)

        posture.goToPosture("StandInit", 0.5)




    except Exception as e:
        print("Eroare:", e)


if __name__ == "__main__":
    talk_and_move()
