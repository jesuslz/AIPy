import numpy as np 
from sklearn import preprocessing


input_data = np.array([[5.1, -2.9, 3.3], [-1.2, 7.8, -6.1], [3.9, 0.4, 2.1], [7.3, -9.9, -4.5]])
''' We will be talking about several different preprocessing techniques. Let's start with
binarization:
Binarization
Mean removal
Scaling
Normalization '''


'''
#Binarize data
data_binarized = preprocessing.Binarizer(threshold = 2.1).transform(input_data)
print("\nBinarized data:\n", data_binarized)
'''


#print mean and standard deviation 
print("\nBEFORE: ")
print("\nMean = ", input_data.mean(axis = 0))
print("\nStd deviation = ", input_data.std(axis = 0))
'''
#remove mean
data_scaled = preprocessing.scale(input_data)
print("\nAFTER: ")
print("\nMean = ", data_scaled.mean(axis = 0))
print("\nStd deviation = ", data_scaled.std(axis = 0))

# Min max scaling
data_scaler_minmax = preprocessing.MinMaxScaler(feature_range=(0, 1))
data_scaled_minmax = data_scaler_minmax.fit_transform(input_data)
print("\nMin max scaled data:\n", data_scaled_minmax)
'''


'''
#Esta es la forma en la que la escala, usando la formula: 
xnew = (x-xmin)/(xmax - xmin)
def escalar(inputData):
  matrix = np.empty((len(inputData), len(inputData[0]))) 
  for i in range(len(inputData)):
    for j in range(len(inputData[i])):
      matrix[i, j] = (inputData[i, j] - min(inputData[:,j]))/(max(inputData[:,j]) - min(inputData[:,j])) 
  return matrix

c = escalar(input_data)
print("\nel valor escalado es: \n", c)

'''
'''
# Normalize data
data_normalized_l1 = preprocessing.normalize(input_data, norm='l1')
data_normalized_l2 = preprocessing.normalize(input_data, norm='l2')
print("\nL1 normalized data:\n", data_normalized_l1)
print("\nL2 normalized data:\n", data_normalized_l2)
'''

'''
Normalizar
'''

def Normalizar(inputData):
  matrix = np.empty((len(inputData), len(inputData[0])))
  promedio, s = calculate_s(inputData)

  for i in range(len(inputData)):
    for j in range(len(inputData[i])):
      matrix[i, j] = (inputData[i, j] - promedio[j])/s[j]
  return matrix, promedio, s

def calculate_s(inputData):
  promedio = np.empty(len(inputData[0]))
  for i in range(len(inputData[0])):
    promedio[i] = sum(inputData[:,i])/len(inputData)


  sDeviation = np.empty(len(inputData[0]))
  
  for k in range(len(inputData[0])):
    aux = 0
    for l in range(len(inputData)):
      aux += (inputData[:,k][l] - promedio[k]) ** 2

    sDeviation[k] = (aux / (len(inputData))) ** 0.5

  return promedio, sDeviation

normalized, promedio, s = Normalizar(input_data)

print("\nmatriz normalizada", normalized)
print("\npromedio = ", promedio)
print("\ndstd = ", s)



