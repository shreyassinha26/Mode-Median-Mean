import csv
with open("txt/SOCR-HeightWeight1.csv",newline="") as f:
    reader=csv.reader(f)
    filedata=list(reader)
filedata.pop(0)
heights=[]
weights=[]
for i in filedata:
    heights.append(i[1])
    weights.append(i[2])

totalHeights=0
totalWeights=0
numHeights=len(heights)
numWeights=len(weights)
for i in heights:
    totalHeights+=float(i)
for i in weights:
    totalWeights+=float(i)
heightsMean=totalHeights/numHeights
WeightsMean=totalWeights/numWeights
print("Mean of Heights : " + str(heightsMean) + ", and weights : " + str(WeightsMean))
def switch(n,a,b):
    placeholder=n[a]
    n[a]=n[b]
    n[b]=placeholder
    return n

def sort(n):
    sort=[]
    for i in range(len(n)-1,0,-1):
        for j in range(0,i):
            if(n[j]>n[j+1]):
                n=switch(n,j,j+1)
    sort=n
    return sort
heights.sort()
weights.sort()
medianHeights=0
medianWeights=0
if(len(heights)%2==0):
    a=int(len(heights)/2)
    medianHeights=float((float(heights[a])+float(heights[a-1])))/2
else:
    medianHeights=heights[int(len(heights)/2)]
if(len(weights)%2==0):
    a=int(len(weights)/2)
    medianWeights=float((float(weights[a])+float(weights[a-1])))/2
else:
    medianWeights=weights[int(len(weights)/2)]
print("Median of Heights : " + str(medianHeights) + ", and weights : " + str(medianWeights))
modeDictHeights={'60-70':0,'70-80':0,'80-90':0}
modeDictWeights={'100-110':0,'110-120':0,'120-130':0,'130-140':0,'140-150':0,'150-160':0}
for i in heights:
    if(60<float(i)<70):
        modeDictHeights['60-70']+=1
    elif(70<float(i)<80):
        modeDictHeights['70-80']+=1
    elif(80<float(i)<90):
        modeDictWeights['80-90']+=1
for i in weights:
    if(100<float(i)<110):
        modeDictWeights['100-110']+=1
    elif(110<float(i)<120):
        modeDictWeights['110-120']+=1
    elif(120<float(i)<130):
        modeDictWeights['120-130']+=1
    elif(130<float(i)<140):
        modeDictWeights['130-140']+=1
    elif(140<float(i)<150):
        modeDictWeights['140-150']+=1
    elif(150<float(i)<160):
        modeDictWeights['150-160']+=1
if(modeDictHeights['60-70']>modeDictHeights['70-80']):
    if(modeDictHeights['80-90']>modeDictHeights['60-70']):
        print("Mode of heights : " + "80-90")
    else:
        print("Mode of heights : " + "60-70")
else:
    if(modeDictHeights['80-90']>modeDictHeights['70-80']):
        print("Mode of heights : " + "80-90")
    else:
        print("Mode of heights : " + "70-80")
x='100-110'
for i in modeDictWeights:
    
    if(modeDictWeights[i] >modeDictWeights[x]):
        x=i
print("Mode of Weights : " + str(x))    
    
        