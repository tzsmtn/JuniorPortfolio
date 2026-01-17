# Tenzin Samten
# HOLIDAY REMIX PROJECT
# description: to make a remix using 123 andres 
from earsketch import *

init()
setTempo(100)

# sounds
vocals1 = ANDRES_NUMEROS_VOCALS_1
vocals2 = ANDRES_NUMEROS_VOCALS_2
vocals3 = ANDRES_NUMEROS_VOCALS_3
bells = RD_WORLD_PERCUSSION_KALIMBA_PIANO_1
bell = OS_COWBELL01
bass = RD_TRAP_BASSDROPS_3
synth = TECHNO_SYNTHPLUCK_001
kick = OS_KICK04
tambourine = OS_CLOSEDHAT01

# beat strings for makebeat
bellPattern1 = "0---0---0---0---"
bellPattern2 = "0-0-0-0-0-0-0-0-"
kickPattern = "0+++0+++0+++0+++"
tambPattern = "----0-------0---"

# this function makes section A
def buildSectionA(start, extras):
    fitMedia(vocals1, 1, start, start + 6)
    fitMedia(bass, 2, start, start + 6)
    
    # loop for the drums
    for m in range(start, start + 6):
        makeBeat(bells, 3, m, bellPattern1)
        makeBeat(tambourine, 8, m, tambPattern)
    
    # if extras is True, add more sounds
    if extras:
        setEffect(1, DELAY, DELAY_TIME, 250)
        setEffect(1, DELAY, DELAY_FEEDBACK, -8)
        setEffect(1, DELAY, MIX, 0.3)
        fitMedia(vocals3, 6, start, start + 6)
        fitMedia(synth, 9, start + 2, start + 6)

# asking the user what vibe they want
mood = input("What vibe do you want? Type 'upbeat' or 'chill': ")

# changes tempo based on what they picked
if mood == "upbeat":
    setTempo(120)
    mainVol = 5
    bassVol = 3
    print("Great Choice!")
else:
    setTempo(90)
    mainVol = 0
    bassVol = -3
    print("Great Choice...")

# section A - basic
buildSectionA(1, False)

# section B
fitMedia(vocals2, 1, 7, 15)
fitMedia(synth, 4, 7, 15)
fitMedia(bell, 5, 7, 11)
fitMedia(bass, 2, 7, 15)

for m in range(7, 15):
    makeBeat(kick, 7, m, kickPattern)
    makeBeat(bells, 3, m, bellPattern2)

setEffect(4, REVERB, MIX, 0.5)
setEffect(5, VOLUME, GAIN, -5)
setEffect(4, FILTER, FILTER_FREQ, 1000)

# section A - with extras
buildSectionA(15, True)

for m in range(15, 21):
    makeBeat(kick, 7, m, kickPattern)

setEffect(1, VOLUME, GAIN, mainVol)
setEffect(2, VOLUME, GAIN, bassVol)
setEffect(1, REVERB, MIX, 0.2)

finish()