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
        posture.goToPosture("Stand", 0.5)


        time.sleep(43)

        player.playFile("/home/nao/appMiculPrint/ChapterTwoMp3/TeRogDeseneaza.mp3")

        time.sleep(6)

        player.playFile("/home/nao/appMiculPrint/ChapterTwoMp3/DeseneazaMi.mp3")

        time.sleep(72)

        player.playFile("/home/nao/appMiculPrint/ChapterTwoMp3/TeRogMiel.mp3")

        time.sleep(29)

        player.playFile("/home/nao/appMiculPrint/ChapterTwoMp3/NuiNimic.mp3")

        time.sleep(18)

        player.playFile("/home/nao/appMiculPrint/ChapterTwoMp3/NuNu.mp3")

        time.sleep(10)

        player.playFile("/home/nao/appMiculPrint/ChapterTwoMp3/NuAstaE.mp3")

        time.sleep(7)

        player.playFile("/home/nao/appMiculPrint/ChapterTwoMp3/VeziBine.mp3")

        time.sleep(10)

        player.playFile("/home/nao/appMiculPrint/ChapterTwoMp3/AstaEPrea.mp3")

        time.sleep(20)

        player.playFile("/home/nao/appMiculPrint/ChapterTwoMp3/ExactCeVroiam.mp3")

        time.sleep(4)

        player.playFile("/home/nao/appMiculPrint/ChapterTwoMp3/PentruCa.mp3")


        time.sleep(7)

        player.playFile("/home/nao/appMiculPrint/ChapterTwoMp3/NuChiarAsa.mp3")





    except Exception as e:
        print("Eroare:", e)


if __name__ == "__main__":
    talk_and_move()
