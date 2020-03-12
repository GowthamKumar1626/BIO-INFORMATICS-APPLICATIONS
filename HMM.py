from random import random

def ATSeq():
    seq = ''
    value = random()
    if value < 0.4:
        seq += 'A'
    elif value > 0.4 and value < 0.8:
        seq += 'T'
    elif value > 0.8 and value < 0.9:
        seq += 'G'
    else:
        seq += 'C'               
    return seq
def GCSeq():
    seq = ''
    value = random()
    if value < 0.4:
        seq += 'G'
    elif value > 0.4 and value < 0.8:
        seq += 'C'
    elif value > 0.8 and value < 0.9:
        seq += 'T'
    else:
        seq += 'A'
    return seq

def frequency_calc(seq):
    nucleotide_freq = {'A':0,'T':0,'G':0,'C':0}
    for i in seq:
        nucleotide_freq[i] += 1
    print(nucleotide_freq)
i = 0
seq = ''
state = ''
while i<100:
    selection = random()
    if selection <0.5:
        seq += ATSeq()
        state += 'L'
        i += 1
    else:
        seq += GCSeq()
        i += 1
        state += 'H'
print(seq)
print(state)
frequency_calc(seq)
