from generateList import genRandomDataset, genInputIncrement
from time import time
from inhibitOSSleep import WindowsInhibitor
import os

#get an array of input sizes to increment by
inputIncrementArray = genInputIncrement()

#merge sort https://runestone.academy/runestone/books/published/pythonds/SortSearch/TheMergeSort.html
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

#selection sort https://stackabuse.com/selection-sort-in-python
def selectionSort(dataset):
    for i in range(len(dataset)-1):
        min_index = i

        for j in range(i+1, len(dataset)-1):
            if dataset[j] < dataset[min_index]:
                min_index = j
        dataset[i], dataset[min_index] = dataset[min_index], dataset[i]

#THIS IS WAY TOO FAST FOR INSERTION SORT AND IM CONFUSED?????
#insertion sort https://www.geeksforgeeks.org/python-program-for-insertion-sort/
def insertionSort(dataset):
    for i in range(1, len(dataset)):
        key = dataset[i]
        j = i-1

        while j >=0 and key < dataset[j] :
                dataset[j+1] = dataset[j]
                j -= 1
        dataset[j+1] = key

#bubble sort https://stackabuse.com/bubble-sort-in-python
def bubbleSort(dataset):
    for i in range(len(dataset)):
        for j in range(len(dataset) - 1):
            if dataset[j] > dataset[j+1]:
                dataset[j], dataset[j+1] = dataset[j+1], dataset[j]

def recordResults():
    print('RECORDING RESULTS\n*****************')
    repeatRunCount = 10
    #HAVE 4 DICTIONARIES WITH 2 KEYS AVERAGES AND DATAPOINTS. CLEAR currentRunDatapoints after average calculated
    """
    mergeRuntimeDict = {
        averages: [],
        currentRunDatapoints:[],
    }
    """       
    runtimeAverageDict = {
        'increment': [0].append(inputIncrementArray),
        'mergeAverages': [0],
        'selectionAverages': [0],
        'insertionAverages': [0],
        'bubbleAverages': [0]
    }

    def sortAndMeasureRuntime(sortAlgorithm, datasetToSort):
        start = time()
        sortAlgorithm(datasetToSort)
        algorithmRuntime = time() - start
        return algorithmRuntime

    #DONT LOOP FOR ALL NAMES JUST HAVE 4 ARRAYS AND AVERAGE ONE OF THEM PER FUNCTION CALL
    def calcAvgAndAppendAvgDict():
        print('calculating averages...')
        algorithmNames = ['merge', 'selection', 'insertion', 'bubble']

        def findAverages(datapoints):
            total = 0
            for i in range(repeatRunCount):
                total += datapoints[i]
            
            finalAverage = total / repeatRunCount
            return finalAverage
        
        for j in range(len(algorithmNames)):
            runtimeAverageDict[algorithmNames[j]+'Averages'].append(findAverages(runtimeDatapointDict[algorithmNames[j]+'Datapoints']))
        
        print('averages collected so far: ', runtimeAverageDict)
        

    for i in range(len(inputIncrementArray)):
        print('input size of current run: ', inputIncrementArray[i])
        randomDataset = genRandomDataset(inputIncrementArray[i])
        runtimeDatapointDict = {
            'mergeDatapoints': [],
            'selectionDatapoints': [],
            'insertionDatapoints': [],
            'bubbleDatapoints': []
        }

        #PASS VARIABLE INTO HERE TO DO RUNS ONE AT A TIME, BUBBLE TOO SLOW
        for j in range(repeatRunCount):
            print('running sort algorithms and collecting datapoints for averaging... run count: ', j+1)
            print('running MERGE sort...')
            mergeRuntime = sortAndMeasureRuntime(mergeSort, randomDataset)
            runtimeDatapointDict['mergeDatapoints'].append(mergeRuntime)

            """
            print('running SELECTION sort...')
            selectionRuntime = sortAndMeasureRuntime(selectionSort, randomDataset)
            runtimeDatapointDict['selectionDatapoints'].append(selectionRuntime)

            print('running INSERTION sort...')
            insertionRuntime = sortAndMeasureRuntime(insertionSort, randomDataset)
            runtimeDatapointDict['insertionDatapoints'].append(insertionRuntime)

            print('running BUBBLE sort...')
            bubbleRuntime = sortAndMeasureRuntime(bubbleSort, randomDataset)
            runtimeDatapointDict['bubbleDatapoints'].append(bubbleRuntime)
            """
            print('datapoints collected so far: ', runtimeDatapointDict)
        
        calcAvgAndAppendAvgDict()
        print(runtimeAverageDict)
           
    print('**************\nFINAL RESULTS: ', runtimeAverageDict)


osSleep = None

#in windows, prevent the OS from sleeping while we run process
if os.name == 'nt':
    osSleep = WindowsInhibitor()
    osSleep.inhibit()

recordResults()

#allow windows to sleep again
if osSleep:
    osSleep.uninhibit()