seq = input("Enter sequence:")
pat = input("Enter pattern:")
cols, rows = (len(seq)+1, len(pat)+1)
match = int(input("Enter Score of match:"))
mm = int(input("Enter Score of miss match:"))
indel = int(input("Enter Score of Indel:"))
arr = [[0 for i in range(cols)] for j in range(rows)]
j = 0
for i in range(cols):
    arr[0][i] = j
    j += indel
for i in range(rows):
    arr[i][0] = -i
for i in range(1, rows):
    for j in range(1, cols):
        if pat[i-1] == seq[j-1]:
                           arr[i][j] = arr[i-1][j-1] + match
        else:
            a = arr[i-1][j-1] +mm
            b = arr[i][j-1] + indel
            c = arr[i-1][j] + indel
            arr[i][j] = max(a,b,c)
print(arr)


seq1 = []
pat1 = []

def backtracking(i, j):
    if i!=0 and j!=0:
        if pat[i-1] == seq[j-1]:
            seq1.append(seq[j-1])
            pat1.append(pat[i-1])
            backtracking(i-1, j-1)
        else:
            if arr[i][j] == arr[i][j-1] + indel:
                seq1.append('_')
                pat1.append(seq[j-1])
                backtracking(i, j-1)
            elif arr[i][j] == arr[i-1][j] + indel:
                seq1.append(pat[i-1])
                pat1.append('_')
                backtracking(i-1, j)
            else:
                seq1.append(seq[j-1])
                pat1.append(pat[i-1])
                backtracking(i-1, j-1)
        
backtracking(len(pat), len(seq))
seq1 = seq1[::-1]
pat1 = pat1[::-1]
print(seq1)
print(pat1)