from __future__ import division
import sys
from collections import defaultdict

dictfortokens=defaultdict()
dictfortokens2=defaultdict()
dictfortokens3=defaultdict()

dictforpos4=defaultdict()
dictforpos5=defaultdict()
dictforpos6=defaultdict()

def collector(line):
	tokens = []
	poses = []
	tokens = line.split(' ')
	Len=len(tokens)
	i=0
	left='##'
	for token in tokens:
		token = token.split('/')
		e = len(token)
		if e == 2:
			tokens.append(token[0])
		else:
			tokens.append('/'.join(token[0:e-1]))
		poses.append(token[e-1])

		if i == 0:
			if left not in dictforpos4:
				dictforpos4[left]={}
				dictforpos4[left][poses[i]]=1
			else:
				temp=dictforpos4.get(left)
				if poses[i] not in temp:
					dictforpos4[left][poses[i]]=1
				else:
					dictforpos4[left][poses[i]]+=1
			if left not in dictforpos5:
				dictforpos5[left]=1
			else:
				dictforpos5[left]+=1

		elif i<Len:
			if poses[i-1] not in dictforpos4:
				dictforpos4[poses[i-1]]={}
				dictforpos4[poses[i-1]][poses[i]]=1
			else:
				temp=dictforpos4.get(poses[i-1])
				if poses[i] not in temp:
					dictforpos4[poses[i-1]][poses[i]]=1
				else:
					dictforpos4[poses[i-1]][poses[i]]+=1
			if poses[i-1] not in dictforpos5:
				dictforpos5[poses[i-1]]=1
			else:
				dictforpos5[poses[i-1]]+=1

		if tokens[i] not in dictfortokens:
			dictfortokens[tokens[i]]={}
			dictfortokens[tokens[i]][poses[i]]=1
		else:
			temp=dictfortokens.get(tokens[i])
			if poses[i] not in temp:
				dictfortokens[tokens[i]][poses[i]]=1
			else:
				dictfortokens[tokens[i]][poses[i]]+=1

		if poses[i] not in dictfortokens2:
			dictfortokens2[poses[i]]=1
		else:
			dictfortokens2[poses[i]]+=1

		i+=1

def probabilityforT():
	list2=[]
	for k in dictforpos4:
		dictforpos6[k]={}
		for item in dictforpos5:
			temp=dictforpos4.get(k)
			if item not in temp:
				dictforpos6[k][item]=float(1)/float(dictforpos5[k]+len(dictforpos5))
				list2.append("Tprobability "+k+" "+item+" "+str(dictforpos6[k][item]))
			else:
				dictforpos6[k][item]=float(dictforpos4[k][item])/float(dictforpos5[k]+len(dictforpos5))
				list2.append("Tprobability "+k+" "+item+" "+str(dictforpos6[k][item]))
	handle3=open("model.txt","a")
	handle3.write('\n')
	handle3.write('\n'.join(list2))
	handle3.close()

def probabilityforE():
	list1=[]
	for k in dictfortokens:
		dictfortokens3[k]={}
		for item in dictfortokens2:
			temp=dictfortokens.get(k)
			if item in temp:
				dictfortokens3[k][item]=float(dictfortokens[k][item])/float(dictfortokens2[item])
				list1.append("Eprobability "+k+" "+item+" "+str(dictfortokens3[k][item]))
	handle2=open("model.txt","w")
	handle2.write('\n'.join(list1))
	handle2.close()




file = open(sys.argv[1],"r")#  enter
while file != None:
	line = file.readline()
	if not line:
		break
	line = line.strip()
	collector(line)
probabilityforE()
probabilityforT()
file.close()
