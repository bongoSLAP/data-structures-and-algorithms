from generatelist import genRandomDataset
from time import time
randomDataset = genRandomDataset(25000)

#merge sort
def mergeSort(dataset):
    if len(dataset)>1:
        mid = len(dataset)//2
        lefthalf = dataset[:mid]
        righthalf = dataset[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)

        i=0
        j=0
        k=0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] <= righthalf[j]:
                dataset[k]=lefthalf[i]
                i=i+1
            else:
                dataset[k]=righthalf[j]
                j=j+1
            k=k+1

        while i < len(lefthalf):
            dataset[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            dataset[k]=righthalf[j]
            j=j+1
            k=k+1

def selectionSort(dataset, size):
    for step in range(size):
        min_idx = step

        for i in range(step + 1, size):
            if dataset[i] < dataset[min_idx]:
                min_idx = i

        (dataset[step], dataset[min_idx]) = (dataset[min_idx], dataset[step])

def insertionSort(dataset):
    for i in range(1, len(dataset)):
        key = dataset[i]
        j = i-1

        while j >=0 and key < dataset[j] :
                dataset[j+1] = dataset[j]
                j -= 1
        dataset[j+1] = key

def bubble_sort(dataset):
    for i in range(len(dataset)):
        for j in range(len(dataset) - 1):
            if dataset[j] > dataset[j+1]:
                dataset[j], dataset[j+1] = dataset[j+1], dataset[j]

mergeStart = time()
mergeSort(randomDataset)
mergeRuntime = time() - mergeStart
print('mergesort runtime: ', mergeRuntime)

#selection sort

