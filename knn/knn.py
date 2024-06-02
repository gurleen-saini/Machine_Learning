from numpy import *
import operator

def createDataSet():
    group = array([[1.0, 1.1], [1.0, 1.0], [0, 0], [0, 0.1]])
    labels = ['A', 'A', 'B', 'B']
    return group, labels

def classify0(inX, dataSet, labels, k):
    dataSetSize = dataSet.shape[0]

    print(dataSetSize)
    
    diffMat = tile(inX, (dataSetSize, 1)) - dataSet
    
    print(diffMat)
    
    sqDiffMat = diffMat ** 2
    
    print(sqDiffMat)
    
    sqDistances = sqDiffMat.sum(axis=1)
    
    print(sqDistances)
    
    distances = sqDistances ** 0.5
    
    print(distances)

    sortedDistIndices = distances.argsort()

    print(sortedDistIndices)

    classCount = {}
    for i in range(k):
        voteIlabel = labels[sortedDistIndices[i]]
        classCount[voteIlabel] = classCount.get(voteIlabel, 0) + 1

    print(classCount)

    sortedClassCount = sorted(classCount.items(), key=operator.itemgetter(1), reverse=True)

    return sortedClassCount[0][0]


def file2matrix(filename):
    fr = open(filename)
    numberoflines = len(fr.readlines())
    returnmat = zeros((numberoflines,3))
    classlabelvector = []
    fr = open(filename)
    index=0
    for line in fr.readlines():
        line = line.strip()
        listfromline = line.split('\t')
        returnmat[index,:] = listfromline[0:3]
        classlabelvector.append(int(listfromline[-1]))
        index += 1
    return returnmat,classlabelvector


def autoNorm(dataSet):
    minVals = dataSet.min(0)
    maxVals = dataSet.max(0)
    ranges = maxVals - minVals
    normDataSet = zeros(shape(dataSet))
    m = dataSet.shape[0]
    normDataSet = dataSet - tile(minVals, (m,1))
    normDataSet = normDataSet/tile(ranges, (m,1))    
    return normDataSet, ranges, minVals


def datingClassTest():
    hoRatio = 0.10      
    datingDataMat, datingLabels = file2matrix('datingTestSet2.txt')
    normMat, ranges, minVals = autoNorm(datingDataMat)
    m = normMat.shape[0]
    numTestVecs = int(m * hoRatio)
    errorCount = 0.0
    for i in range(numTestVecs):
        classifierResult = classify0(normMat[i, :], normMat[numTestVecs:m, :], datingLabels[numTestVecs:m], 3)
        print("the classifier came back with: %d, the real answer is: %d" % (classifierResult, datingLabels[i]))
        if classifierResult != datingLabels[i]:
            errorCount += 1.0
    print("the total error rate is: %f" % (errorCount / float(numTestVecs)))


def classifyPerson():
    resultList = ['not at all','in small doses', 'in large doses']
    percentTats = float(input("percentage of time spent playing video games?"))
    ffMiles = float(input("frequent flier miles earned per year?"))
    iceCream = float(input("liters of ice cream consumed per year?"))
    datingDataMat,datingLabels = file2matrix('datingTestSet2.txt')
    normMat, ranges, minVals = autoNorm(datingDataMat)
    inArr = array([ffMiles, percentTats, iceCream])
    classifierResult = classify0((inArr-\
                   minVals)/ranges,normMat,datingLabels,3)
    print ("You will probably like this person: ",\
                   resultList[classifierResult - 1])
 