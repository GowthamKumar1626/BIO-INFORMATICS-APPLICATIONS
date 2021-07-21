
file_list=[]
file=open("stride_result.txt","r")   #File read

secondary_structs=[]
for line in file:
    if(line[0:3] not in ['REM','SRC','AUT','LOC','CMP','CHN','SEQ','STR','HDR']):
        secondary_structs.append(line[28:39])   #structures into list
#print(secondary_structs)

#Count
coil=0
alpha_helix=0
turn=0
bridge=0
threeten_helix=0
strand=0

for i in secondary_structs:
    if "Coil" in i:
        coil=coil+1
    if "Bridge" in i:
        bridge=bridge+1
    if "AlphaHelix" in i and "310" not in i:
        alpha_helix=alpha_helix+1
    if "Turn" in i:
        turn=turn+1
    if "310Helix" in i and "Alpha" not in i:
        threeten_helix=threeten_helix+1
    if "Strand" in i:
        strand=strand+1

total= coil+strand+alpha_helix+turn+threeten_helix+bridge
print("Total Number of residues",total)

#Percentage calculation

alpha_helix_percentage=(alpha_helix*100)/total
threetenhelix_percentage=(threeten_helix*100)/total
strand_percentage=(strand*100)/total
bridge_percentage=(bridge*100)/total
coil_percentage=(coil*100)/total
turn_percentage=(turn*100)/total

print("Alpha helix percentage:", round(alpha_helix_percentage,2))
print("310 helix percentage:", round(threetenhelix_percentage,2))
print("Strand percentage:", round(strand_percentage,2))
print("Bridge percentage:", round(bridge_percentage,2) )
print("Coil percentage:", round(coil_percentage,2) )
print("Turn percentage:", round(turn_percentage,2) )