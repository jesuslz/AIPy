'''
In the real world, labels are in the form of words, because words are human readable. We
label our training data with words so that the mapping can be tracked. To convert word
labels into numbers, we need to use a label encoder. Label encoding refers to the process of
transforming the word labels into numerical form. This enables the algorithms to operate on
our data.'''

import numpy as np
from sklearn import preprocessing
#sample input labels
input_labels = ['red', 'black', 'red', 'green', 'black', 'yellow', 'white']

#create leabel encoding and fit the labels
encoder = preprocessing.LabelEncoder()
encoder.fit(input_labels)

#print the mapping 
print("\nLabel mapping:")
for i, item in enumerate(encoder.classes_):
	print(item, '-->', i)

# Encode a set of labels using the encoder
test_labels = ['green', 'red', 'black']
encoded_values = encoder.transform(test_labels)#transforma a indices pero en un solo elemento de una lista
print("\nEncoded values = ", encoded_values)
print("\nLabels =", test_labels)
print("Encoded values =", list(encoded_values))#Los convierte a una lista


# Decode a set of values using the encoder
encoded_values = [3, 0, 4, 1]
decoded_list = encoder.inverse_transform(encoded_values)
print("\n********Encoded values =", encoded_values)
print("\nDecoded values = ", decoded_list) #Aun no es una lista
print("Decoded labels =", list(decoded_list))