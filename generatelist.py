import numpy as np

def genInputIncrement():
    incrementArray = []
    increment = 0

    for i in range(50+1):
        incrementArray.append(increment)
        increment += 20000
    
    return incrementArray

def genRandomDataset(datasetSize):
    return np.random.randint(1, datasetSize, datasetSize)
