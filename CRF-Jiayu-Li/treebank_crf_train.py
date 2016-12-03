#!/usr/bin/python3
# coding = UFT-8 
import pycrfsuite
import os.path  
import sys, os
import io
from nltk.corpus import treebank
from nltk.corpus import brown
# from nltk.corpus import twitter_samples

#treebank
#case1 just current word 
# x_train = []
# y_train = []
# for token, pos in treebank.tagged_words():
# for token, pos in treebank.tagged_words()[:80000]:
	# x = []
	# y_train.append(pos)
	# f1 = 'token_' + token
	# x.append(f1)
	# x_train.append(x)
# print(len(y_train))
# print(y_train)

#brown
# x1_train = []
# y1_train = []
# for token, pos in brown.tagged_words()[100:100000]:
# 	x1 = []
# 	y1_train.append(pos)
# 	f1 = 'token_' + token
# 	# f2 = 'pos_' + pos
# 	x1.append(f1)
# 	# x.append(f2)
# 	x1_train.append(x1)
# # print(len(y_train))
# print(y1_train)

#case2 just previous word
# x_train = []
# y_train = []
# pre_token = 'BEGIN'
# for token, pos in treebank.tagged_words():
# for token, pos in treebank.tagged_words()[:80000]:
	# x = []
	# y_train.append(pos)
	# x.append(pre_token)
	# x_train.append(x)
	# pre_token = token

#case3 current word and previous word
# x_train = []
# y_train = []
# pre_token = "pre"
# for token, pos in treebank.tagged_words():
# for token, pos in treebank.tagged_words()[:80000]:
	# x = []
	# y_train.append(pos)
	# x.append(pre_token + '-' + token)
	# x.append(token)
	# pre_token = token
	# x_train.append(x)

#case4 current word shape
# x_train = []
# y_train = []
# for token, pos in treebank.tagged_words():
# for token, pos in treebank.tagged_words()[:80000]:
	# x = []
	# y_train.append(pos)
	# token = token.lower()
	# x.append(token)
	# x_train.append(x)
# print(x_train)

#case5 current word shape
# x_train = []
# y_train = []
# for token, pos in treebank.tagged_words():
# for token, pos in treebank.tagged_words()[:80000]:
	# x = []
	# y_train.append(pos)
	# token = token.upper()
	# x.append(token)
	# x_train.append(x)
# print(x_train)

#case6 Previous word shape 
# x_train = []
# y_train = []
# pre_token = 'BEGIN'
# for token, pos in treebank.tagged_words():
# for token, pos in treebank.tagged_words()[:80000]:
	# x = []
	# y_train.append(pos)
	# x.append(pre_token)
	# x_train.append(x)
	# pre_token = token.lower()

#case7 previous word shape and current word shape
# x_train = []
# y_train = []
# pre_token = "pre"
# for token, pos in treebank.tagged_words():
# for token, pos in treebank.tagged_words()[:80000]:
	# x = []
	# y_train.append(pos)
	# x.append(pre_token + '-' + token.lower())
	# x.append(token.lower())
	# pre_token = token.lower()
	# x_train.append(x)

#case8 Word contains a digit
# x_train = []
# y_train = []
# list1 = ['0', '1', '2', '3', '4', '5', '6', '7', '8','9']
# for token, pos in treebank.tagged_words():
# # for token, pos in treebank.tagged_words()[:80000]:
# 	x = []
# 	y_train.append(pos)
# 	x.append(token)
# 	for item in list1:
# 		if item in token:
# 			x.append(token)
# 		else:
# 			x.append('no')
# 	x_train.append(x)

#case9 Word contains a capital letter and current word
# x_train = []
# y_train = []
# list1 = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I','J','K', 
# 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S','T','U', 'V', 'W', 'X', 
# 'Y', 'Z']
# for token, pos in treebank.tagged_words():
# # for token, pos in treebank.tagged_words()[:80000]:
# 	x = []
# 	y_train.append(pos)
# 	x.append(token)
# 	for item in list1:
# 		if item in token:
# 			x.append('yes')
# 		else:
# 			x.append('no')
# 	x_train.append(x)

#case10 Word contains a digit, current word and word contains a capital letter
# x_train = []
# y_train = []
# list1 = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I','J','K', 
# 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S','T','U', 'V', 'W', 'X', 
# 'Y', 'Z']
# list2 = ['0', '1', '2', '3', '4', '5', '6', '7', '8','9']
# for token, pos in treebank.tagged_words():
# for token, pos in treebank.tagged_words()[:80000]:
	# x = []
	# y_train.append(pos)
	# x.append(token)
	# for item in list1:
	# 	if item in token:
	# 		x.append('capital_yes')
	# 	else:
	# 		x.append('capital_no')
	# for i in list2:
	# 	if i in token:
	# 		x.append('digit_yes')
	# 	else:
	# 		x.append('digit_no')
	# x_train.append(x)

#case11 Word contains a digit, current word, word contains a capital letter and previous word
x_train = []
y_train = []
list1 = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I','J','K', 
'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S','T','U', 'V', 'W', 'X', 
'Y', 'Z']
list2 = ['0', '1', '2', '3', '4', '5', '6', '7', '8','9']
pre_token = 'first'
for token, pos in treebank.tagged_words():
# for token, pos in treebank.tagged_words()[:80000]:
	x = []
	y_train.append(pos)
	x.append(pre_token + '-' + token)
	x.append(token)
	pre_token = token
	for item in list1:
		if item in token:
			x.append('capital_yes')
		else:
			x.append('capital_no')
	for i in list2:
		if i in token:
			x.append('digit_yes')
		else:
			x.append('digit_no')
	x_train.append(x)


trainer = pycrfsuite.Trainer(verbose=False)
trainer.append(x_train, y_train)

trainer.set_params({
    'c1': 1.0,   # coefficient for L1 penalty
    'c2': 1e-3,  # coefficient for L2 penalty
    'max_iterations': 70,  # stop earlier

    # include transitions that are possible, but not observed
    'feature.possible_transitions': True,
    'feature.possible_states': True
})
trainer.train('haha.crfsuite')
tagger = pycrfsuite.Tagger()
tagger.open('haha.crfsuite')

#case1
# x1_train = []
# y1_train = []
# for token, pos in treebank.tagged_words()[80000:]:
# 	x1 = []
# 	y1_train.append(pos)
# 	f1 = 'token_' + token
# 	x1.append(f1)
# 	x1_train.append(x1)
# act_tag = tagger.tag(x1_train)

#case2 
# x1_train = []
# y1_train = []
# pre_token1 = 'BEGIN'
# for token, pos in treebank.tagged_words()[80000:]:
# 	x1 = []
# 	y1_train.append(pos)
# 	x1.append(pre_token1)
# 	x1_train.append(x1)
# 	pre_token1 = token
# act_tag = tagger.tag(x1_train)

#case3
# x1_train = []
# y1_train = []
# pre1_token = "pre"
# for token, pos in treebank.tagged_words()[80000:]:
# 	x1 = []
# 	y1_train.append(pos)
# 	x1.append(pre1_token + '-' + token)
# 	x1.append(token)
# 	pre1_token = token
# 	x1_train.append(x1)
# act_tag = tagger.tag(x1_train)

#case4
# x1_train = []
# y1_train = []
# for token, pos in treebank.tagged_words()[80000:]:
# 	x1 = []
# 	y1_train.append(pos)
# 	token = token.lower()
# 	x1.append(token)
# 	x1_train.append(x1)
# act_tag = tagger.tag(x1_train)

#case5
# x1_train = []
# y1_train = []
# for token, pos in treebank.tagged_words()[80000:]:
# 	x1 = []
# 	y1_train.append(pos)
# 	token = token.upper()
# 	x1.append(token)
# 	x1_train.append(x1)
# act_tag = tagger.tag(x1_train)

#case6
# x1_train = []
# y1_train = []
# pre1_token = 'BEGIN'
# for token, pos in treebank.tagged_words()[80000:]:
# 	x1 = []
# 	y1_train.append(pos)
# 	x1.append(pre1_token)
# 	x1_train.append(x1)
# 	pre1_token = token.lower()
# act_tag = tagger.tag(x1_train)

#case7
# x1_train = []
# y1_train = []
# pre1_token = "pre"
# for token, pos in treebank.tagged_words()[80000:]:
# 	x1 = []
# 	y1_train.append(pos)
# 	x1.append(pre1_token + '-' + token.lower())
# 	x1.append(token.lower())
# 	pre1_token = token.lower()
# 	x1_train.append(x1)
# act_tag = tagger.tag(x1_train)

#case8
# x1_train = []
# y1_train = []
# for token, pos in treebank.tagged_words()[80000:]:
# 	x1 = []
# 	y1_train.append(pos)
# 	x1.append(token)
# 	for item in list1:
# 		if item in token:
# 			x1.append(token)
# 		else:
# 			x1.append('no')
# 	x1_train.append(x1)
# act_tag = tagger.tag(x1_train)

#case9
# x1_train = []
# y1_train = []
# for token, pos in treebank.tagged_words()[80000:]:
# 	x1 = []
# 	y1_train.append(pos)
# 	x1.append(token)
# 	for item in list1:
# 		if item in token:
# 			x1.append('yes')
# 		else:
# 			x1.append('no')
# 	x1_train.append(x1)
# act_tag = tagger.tag(x1_train)

#case10
# x1_train = []
# y1_train = []
# for token, pos in treebank.tagged_words()[80000:]:
# 	x1 = []
# 	y1_train.append(pos)
# 	x1.append(token)
# 	for item in list1:
# 		if item in token:
# 			x1.append('capital_yes')
# 		else:
# 			x1.append('capital_no')
# 	for i in list2:
# 		if i in token:
# 			x1.append('digit_yes')
# 		else:
# 			x1.append('digit_no')
# 	x1_train.append(x1)
# act_tag = tagger.tag(x1_train)

#case11
x1_train = []
y1_train = []
pre1_token = 'first'
for token, pos in treebank.tagged_words()[80000:]:
	x1 = []
	y1_train.append(pos)
	x1.append(pre1_token + '-' + token)
	x1.append(token)
	pre1_token = token
	for item in list1:
		if item in token:
			x1.append('capital_yes')
		else:
			x1.append('capital_no')
	for i in list2:
		if i in token:
			x1.append('digit_yes')
		else:
			x1.append('digit_no')
	x1_train.append(x1)
act_tag = tagger.tag(x1_train)


count = 0
total = 0
for i in range(len(y1_train)):
	total += 1
	if y1_train[i] == act_tag[i]:
		count += 1

accuracy = count / total
print(accuracy)
