import math
import re
def RawScore(a,b,c,d,text,pat):
    I,X,O,G = 0,0,0,0
    for i in range(len(pat)):
        if pat[i] == text[i]:
            I += 1
        elif pat[i] == '-' or text[i] == '-':
            G += 1
        else:
            X += 1
    temp = re.split('\-+',pat)
    O = len(temp)-1
    print(I,X,O,G)
    return (a*I)+(b*X)-(c*O)-(d*G)
def bitScore(l,R,k):
    return (l*R-math.log(k))/math.log(2)
def EValue(m,n,S):
    return (m*n)*math.pow(2,-S)

text = "GATTACGCTA"
pat =  "AACTA---G-"

R = RawScore(1,-3,5,2,text,pat)
S = bitScore(1.37,R,0.711)
E = EValue(len(pat),5854611841,S)
print("Raw Score:"+str(R))
print("Bit Score:"+str(S))
print("E Value Score:"+str(E))

