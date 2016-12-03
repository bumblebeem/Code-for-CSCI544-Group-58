from keras.models import model_from_json
from keras.utils.np_utils import to_categorical
from keras.preprocessing.text import Tokenizer
from keras.preprocessing import sequence

from nltk.corpus import treebank
# from nltk.corpus import brown


# filter只忽略空格,标点符号需要保留
def base_filter():
    f = ' '
    return f


# window_size should be an odd number
# 还没处理最前边的左边和最后边的右边几个可能空白的位置
def chop_words_into_windows(window_size, tagged_words):
    X_train = []
    y_train = []
    regular_index_begin = window_size // 2
    regular_index_end = len(tagged_words) - 1 - window_size // 2
    for i in range(regular_index_begin, regular_index_end + 1):
        temp_list = []
        for j in range(i - window_size // 2, i + window_size // 2 + 1):
            # temp_list.append(tagged_words[j]) 这里只需要token,不需要对应的tag,所以这行代码是错的。。
            temp_list.append(tagged_words[j][0])
        X_train.append(temp_list)
        y_train.append(tagged_words[i][1])
    return X_train, y_train


# convert words in X_train into integers
def convert_words_to_integers(tokens, sequences, X_train):
    res = []
    word_integer_dict = {}
    for i in range(0, len(tokens)):
        if tokens[i] not in word_integer_dict:
            word_integer_dict[tokens[i]] = sequences[i]
    for element in X_train:
        temp_list = []
        # for word, pos in element:         因为X_train里边的数据应该是只有token,而不是(token, pos)的tuple
        #     temp_list.extend(word_integer_dict[word])
        for word in element:
            temp_list.extend(word_integer_dict[word])
        res.append(temp_list)
    return res

# test how to use nltk corpus
# print(treebank.tagged_words())
# print(treebank.tagged_sents())

# DEFINE VARIABLES
# tokens is a list of all individual words
# tags is a list of all individual pos tags
# distinct_tags are distinct pos tags in corpus
tokens = []
tags = []
distinct_tags = []
# dictionary mapping pos tag name to numeric id
tag_index = {}
# id of corresponding tag
tag_id = []
# represent pos tags in y_train/y_test with integers
y_train_in_integers = []
y_test_in_integers = []
# define window size
window_size = 3

print('Phrase 1: Dividing data into training set and testing set...')
train = []
test = []
train = treebank.tagged_words()[:90677]
test = treebank.tagged_words()[90677:]
# print(len(treebank.tagged_words()))
# print(treebank.tagged_words())
# print(train)
# print(test)
print('Phrase 1: END\n')

X_train, y_train = chop_words_into_windows(window_size, train)
X_test, y_test = chop_words_into_windows(window_size, test)
# test if chop_words_into_windows is correctly implemented
# for i in range(0, 50):
#     print(X_train[i])
#     print(y_train[i])
#     print('*****')

# could rewrite the following part as a function later...
for token, pos in treebank.tagged_words():
    tokens.append(token)
    tags.append(pos)
    if pos not in tag_index:
        distinct_tags.append(pos)
        tag_index[pos] = len(distinct_tags) - 1

# test if read the tokens and tags properly
# print(len(treebank.tagged_words()))
# print(len(tokens))
# print(len(tags))
# print(len(distinct_tags))
# print(len(tag_index))
# print(distinct_tags)
# print(tag_index)

# 需要自己写个filter作为filters的参数
tokenizer = Tokenizer(nb_words=None,
                      filters=base_filter(),
                      lower=False,
                      # split=' ',
                      char_level=False)
tokenizer.fit_on_texts(tokens)
# 怎么能让每次生成出来的sequences是固定的而不是随机的呢。。。??
sequences = tokenizer.texts_to_sequences(tokens)
# tokens和sequences是一一对应的关系,只不过sequences里的元素是tokens里边对应元素的整数表示。。
# print(sequences)
# for i in range(0, 50):
#     print(sequences[i])
#     print(tokens[i])
#     print('**************************************')

# word_index = tokenizer.word_index
# print('Found %s unique tokens.' % len(word_index))

# number of possible output classes, i.e. number of possible pos tags
nb_classes = len(distinct_tags)

X_train_in_integers = convert_words_to_integers(tokens, sequences, X_train)
X_test_in_integers = convert_words_to_integers(tokens, sequences, X_test)
# print(X_train_in_integers)

# convert pos tags in y_train/y_test into corresponding integers in y_train_in_integers/y_test_in_integers
for element in y_train:
    y_train_in_integers.append(tag_index[element])
for element in y_test:
    y_test_in_integers.append(tag_index[element])
# print(tag_index)
# print(y_train)
# print(y_train_in_integers)

# convert integers in y_train_in_integers into vectors(i.e. binary matrix representation)
y_train_as_vectors = to_categorical(y_train_in_integers, nb_classes)
y_test_as_vectors = to_categorical(y_test_in_integers, nb_classes)
# print(y_train_as_vectors)

maxlen = window_size
# max_features应该取多少呢?不是很清楚啊。。??
max_features = 200000
# batch_size也不知道应该取多少。。??
batch_size = 32

X_train_final = sequence.pad_sequences(X_train_in_integers, maxlen=maxlen)
X_test_final = sequence.pad_sequences(X_test_in_integers, maxlen=maxlen)
# 下边这四个正是最后model里用到的数据!!
# print(X_train_final.shape)
# print(X_test_final.shape)
# print(y_train_in_integers)
# print(y_test_in_integers)

# ABOVE CODE IS COPIED FROM TRAIN_MODEL.PY, BELOW IS THE DIFFERENCE

# load json and create model
json_file = open('my_model.json', 'r')
loaded_model_json = json_file.read()
json_file.close()
loaded_model = model_from_json(loaded_model_json)
# load weights into new model
loaded_model.load_weights("my_model1.h5")
print("Loaded model from disk.")

# evaluate loaded model on test data
loaded_model.compile(loss='categorical_crossentropy',
                     optimizer='adadelta',
                     metrics=['accuracy'])
score, acc = loaded_model.evaluate(X_test_final,
                                   y_test_as_vectors,
                                   batch_size=batch_size)
print('Test score:', score)
print('Test accuracy:', acc)
