from collections import defaultdict
import sys
import math

dictionaryforwords1=defaultdict()
dictionaryforwords2=defaultdict()

dictionaryforpos1=defaultdict()
dictionaryforpos2=defaultdict()

def helper(i,dictionaryforpos1):
    m=-sys.maxint-1
    t=''
    for k in dictionaryforpos1.get(i):
            if m<dictionaryforpos1[i][k]:
                m=dictionaryforpos1[i][k]
                t=k
    return t

def calculator(i,v,word,dictionaryforpos1):
    mm=-sys.maxint-1
    temp=''
    for k in dictionaryforpos1.get(i-1):
            if dictionaryforwords1.has_key(word):
                temp=dictionaryforwords1.get(word)
                if v in temp:
                    he=dictionaryforpos1[i-1][k]+math.log(dictionaryforwords2[k][v])+math.log(dictionaryforwords1[word][v])
                    if mm<he:
                        mm=he
                        temp=k
                else:
                    he=dictionaryforpos1[i-1][k]+math.log(dictionaryforwords2[k][v])
                    if mm<(he):
                        mm=he
                        temp=k
            else:
                he=dictionaryforpos1[i-1][k]+math.log(dictionaryforwords2[k][v])
                if mm<(he):
                    mm=he
                    temp=k
    return str(mm)+" "+temp


def tagger(line):
    left='##'
    words=line.split(' ')
    i=0
    dictionaryforpos1={}
    dictionaryforpos2={}
    for word in words:
        dictionaryforpos1[i]={}
        dictionaryforpos2[i]={}
        if i==0:
            if dictionaryforwords1.has_key(word):
                for k in dictionaryforwords1.get(word):
                    dictionaryforpos1[0][k]=math.log(float(dictionaryforwords2[left][k]))+math.log(float(dictionaryforwords1[word][k]))
            else:
                for k in dictionaryforwords2:
                    if k!='##':
                        dictionaryforpos1[0][k]=math.log(float(dictionaryforwords2[left][k]))
        else:
            if dictionaryforwords1.has_key(word):
                for k in dictionaryforwords1.get(word):
                    arr=calculator(i,k,word,dictionaryforpos1)
                    res=arr.split(" ")
                    dictionaryforpos1[i][k]=float(res[0])
                    dictionaryforpos2[i][k]=res[1]
            else:
                for k in dictionaryforwords2:
                    if k!='##':
                        arr=calculator(i,k,word,dictionaryforpos1)
                        res=arr.split(" ")
                        dictionaryforpos1[i][k]=float(res[0])
                        dictionaryforpos2[i][k]=res[1]
        i+=1

    j=0
    list1=[]
    for word in words:
        list1.append(word+"/"+helper(j,dictionaryforpos1)+" ")
        j+=1

    return (''.join(list1))

file1 = open("model.txt","r")
while True:
    strline = file1.readline()
    if not strline:
        break
    strline = strline.strip()
    insert(strline)
file1.close()
file2=open(sys.tempv[1],"r")
listforoutput=[]
while True:
    line = file2.readline()
    if not line:
        break
    line = line.strip()
    listforoutput.append(str(tagger(line)))
file3=open("output.txt","w")
file3.write('\n'.join(listforoutput))
file3.close()
file2.close()