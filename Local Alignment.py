seq = "ATT"
pat = "AATGCT"
cols, rows = (len(seq)+1, len(pat)+1)
match = 2
mm = -1
indel = -1
arr = [[0 for i in range(cols)] for j in range(rows)] 
for i in range(cols):
    arr[0][i] = 0
for i in range(rows):
    arr[i][0] = 0
for i in range(1, rows):
    for j in range(1, cols):
        if pat[i-1] == seq[j-1]:
                           arr[i][j] = arr[i-1][j-1] + match
        else:
            a = arr[i-1][j-1] + mm 
            b = arr[i][j-1] + indel
            c = arr[i-1][j] + indel
            if max(a,b,c) < 0:
                arr[i][j] = 0
            else:
                arr[i][j] = max(a,b,c)
             
print(arr)

#BackTracking

seq1 = []
pat1 = []

def findMax(i ,j):
    maxElement = 0
    max_i = 0
    max_j = 0
    for i in range(rows):
        for j in range(cols):
            if arr[i][j] > maxElement:
                maxElement = arr[i][j]
                max_i = i
                max_j = j
    print(maxElement)
    backtracking(max_i, max_j)

def backtracking(i, j):
    if i!=0 and j!=0:
        if pat[i-1] == seq[j-1]:
            seq1.append(seq[j-1])
            pat1.append(pat[i-1])
            backtracking(i-1, j-1)
        else:
            if arr[i][j] == arr[i][j-1] + indel:
                seq1.append(seq[j-1])
                pat1.append('_')
                backtracking(i, j-1)
            elif arr[i][j] == arr[i-1][j] + indel:
                seq1.append('_')
                pat1.append(pat[i-1])
                backtracking(i-1, j)
            else:
                seq1.append(seq[j-1])
                pat1.append(pat[i-1])
                backtracking(i-1, j-1)
        

findMax(0,0)
seq1 = seq1[::-1]
pat1 = pat1[::-1]
print(seq1)
print(pat1)