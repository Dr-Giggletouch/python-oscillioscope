#you must run this in terminal or else matplotlib will not do its graphing thing
#cd downloads then cd matplotlibtest then python3 test.py
#you also need pyaudio and matplotlib
#just run this on my computer at this point its not worth it




import pyaudio


import numpy as np

import matplotlib.pyplot as plt

import time

#sample rate
RATE = 44100

CHUNK = int(RATE/20)

#this gets audio from systemm
def soundplot(stream):

    #i have no clue what half of this code does some of it is from the pyaudio examples and online

    t1=time.time()

    #had to include a exeption for the overflow thing or else i would get input overflows from pyaudio
    data = np.fromstring(stream.read(CHUNK, exception_on_overflow = False),dtype=np.int16)

    #this is when we start graphing stuff in matplotlib

    plt.pause(0.1)

    plt.clf()

    plt.plot(data)

    plt.draw()

    plt.axis([0,len(data),-2**16/2,2**16/2])

if __name__=="__main__":
    p=pyaudio.PyAudio()

    stream=p.open(format=pyaudio.paInt16,channels=1,rate=RATE,input=True,
                  frames_per_buffer=CHUNK)
    for i in range(int(20*RATE/CHUNK)):
        soundplot(stream)

    stream.stop_stream()

    stream.close()

    p.terminate()