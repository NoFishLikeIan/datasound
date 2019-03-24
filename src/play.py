import numpy as np

from pyo import midiToHz, Choice, Port, Sine, SuperSaw, FM, Delay, STRev  # pylint: disable=E0611

from load_data import fetch_data_iter
from pyo_server import server as s

pitches = [midiToHz(np.mean(m)) for m in fetch_data_iter]

# Add more voices here to generate a simple counterpoint
choice = Choice(choice=pitches, freq=1)
ch_port = Port(choice, risetime=.001, falltime=.001)

# Two simple instruments
lfdetune = Sine(freq=0.1, mul=.07, add=.07)
instrument1 = SuperSaw(freq=ch_port, detune=lfdetune, mul=.1)
lfind = Sine(freq=0.1, phase=0.5, mul=3, add=3)
instrument2 = FM(carrier=ch_port, ratio=1.0025, index=lfind, mul=.025)

# Send instruments output to delay
src_sum = instrument1.mix(2) + instrument2.mix(2)
lfdel = Sine(.1, mul=.003, add=.005)
comb = Delay(src_sum, delay=lfdel, feedback=.5)

# Send two resulting signals to reverb and output
out_sum = src_sum + comb
rev = STRev(out_sum, cutoff=3500, bal=.5, roomSize=2).out()

s.gui(locals())
