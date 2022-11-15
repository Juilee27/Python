# ----------------------------healthy programmer------------------------------

# date time module
# water = water.mp3 (3.5 liters) 9am - 5 pm- 200 ml ke glasses k hisab se divide krna he
# - utne time ka loop lgado
# 18 times drink water, concluding 2 times/ hour i.e. every 30 mins
# eyes and water every 30 mins hora it is clashing toh water every 40 mins krte he
# every 30-40 mins, play water mp3, also after person had water he/she needs to provide input as drank-
# generate log file containing time at which drank water
# eyes = eyes.mp3 = run this every 30 mins - likhdo EyDone - log
# physical activity = physical.mp3 - every 45 mins - ExDone - log
# jabtak user feedback nai deta tabtak song bachta rhega
#
# times can clash, wo take care kerna hoga
#
# rules: use pygame module to play audio
# directory me jake code pe click kia ki vo backend me program chalu rhega not needed to run from pycharm

from datetime import datetime
from time import time
from pygame import mixer
mixer.init()

def musicOnLoop(audio, stopper):
    mixer.music.load(audio)
    mixer.music.set_volume(0.3)
    mixer.music.play()
    while 1:
        a = input()
        if a == stopper: #***do not hardcode here
            mixer.music.stop()
            break

def logNow(msg):
    with open('myLogs.txt',"a") as f:
        f.write(f"{datetime.now()} {msg}\n")

if __name__ == '__main__':
    init_water = time() #time in sec - mind it
    init_eyes = time()
    init_exercise = time()
    watersecs =  40*60
    eyessecs = 30*60
    exsecs = 45*60

    while True:
        ## ----------------------------------------WATER------------------------------------------------- #
        if time() - init_water > watersecs:
            print('''Drink water. Enter 'drank' if u had water''')
            musicOnLoop("water.mp3", "drank")
            logNow("\tDrank water")
            init_water = time()

        ## ----------------------------------------EYES------------------------------------------------- #
        if time() - init_eyes > eyessecs:
            print('''Blink eyes. Enter 'done' when blinked''')
            musicOnLoop("eyes.mp3", "done")
            logNow("\tBlinked eyes")
            init_eyes = time()

        ## ----------------------------------------EXERCISE------------------------------------------------- #
        if time() - init_exercise > exsecs:
            print('''Time to exercise. Enter 'exercised' when done''')
            musicOnLoop("physical.mp3", "exercised")
            logNow("\tCompleted exercise")
            init_exercise = time()













