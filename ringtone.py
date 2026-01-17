#Author: Tenzin Samten
#11/26
#description: make a ringtone

from earsketch import *

setTempo(100)
Drum = RD_ELECTRO_DRUM_PART_12
trap = CIARA_SET_BASSLINE_1
lead = Y53_ELECTRO_2
piano = RD_WORLD_PERCUSSION_KALIMBA_PIANO_1
bass = YG_TECHNO_BASS_1

def secA(start,end):
    #intro
    fitMedia(Drum, 1, start, end)
    fitMedia(trap, 2, start, end)
    fitMedia(piano, 3, start, end)
def secB(start, end):
    fitMedia(Drum, 1, start, end)
    fitMedia(trap, 2, start, end)
    fitMedia(lead, 4, start, end)
    fitMedia(bass, 5, start, end)

def transitions(start, end):
    #fade in 
    setEffect(3, VOLUME, GAIN, -20, 4, 0, 5)
    #fade out
    setEffect(4, VOLUME, GAIN, -12, 9, 0, 13)

def outro(start, end):
    #ending
    fitMedia(piano, 3, start, end)
    setEffect(3, VOLUME, GAIN, 0, start, -25, end)

secA(1,5)
secB(5,9)
secA(9,13)
outro(13,15)

