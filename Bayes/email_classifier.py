from numpy import *
import random
import zipfile

def loadDataSet():
    postingList=[['my', 'dog', 'has', 'flea', \
                  'problems', 'help', 'please'],
                 ['maybe', 'not', 'take', 'him', \
                  'to', 'dog', 'park', 'stupid'],
                 ['my', 'dalmation', 'is', 'so', 'cute', \
                   'I', 'love', 'him'],
   ['stop', 'posting', 'stupid', 'worthless', 'garbage'],
                 ['mr', 'licks', 'ate', 'my', 'steak', 'how',\
                   'to', 'stop', 'him'],
   ['quit', 'buying', 'worthless', 'dog', 'food', 'stupid']]
    classVec = [0,1,0,1,0,1]    #1 is abusive, 0 not
    return postingList,classVec

lines,labels = loadDataSet()
print(lines)
print(labels)

def createVocabList(dataSet):
    vocabSet = set([])                         
    for document in dataSet:
        vocabSet = vocabSet | set(document)          
    return list(vocabSet)

vocablist = createVocabList(lines)
print(vocablist)

def setOfWords2Vec(vocabList, inputSet):
    returnVec = [0]*len(vocabList)             
    for word in inputSet:
        if word in vocabList:
            returnVec[vocabList.index(word)] = 1
        else: print ("the word: %s is not in my Vocabulary!" % word)
    return returnVec

trainmatrix = []
for posts in lines:
    trainmatrix.append(setOfWords2Vec(vocablist,posts))

print(trainmatrix)

def trainNB0(trainMatrix,trainCategory):
    numTrainDocs = len(trainMatrix)
    numWords = len(trainMatrix[0])
    pAbusive = sum(trainCategory)/float(numTrainDocs)
    p0Num = ones(numWords); p1Num = ones(numWords) 
    p0Denom = 2.0; p1Denom = 2.0                     
    for i in range(numTrainDocs):
        if trainCategory[i] == 1:
            p1Num += trainMatrix[i]            
            p1Denom += sum(trainMatrix[i])            
        else:
            p0Num += trainMatrix[i]
            p0Denom += sum(trainMatrix[i])
    # p1Vect = p1Num/p1Denom          #change to log()      
    # p0Vect = p0Num/p0Denom          #change to log()
    p1Vect = log(p1Num/p1Denom)
    p0Vect = log(p0Num/p0Denom)
    return p0Vect,p1Vect,pAbusive

p0prob,p1prob,probabusive = trainNB0(trainmatrix,labels)
print(p0prob)
print(p1prob)
print(probabusive)

def classifyNB(vec2Classify, p0Vec, p1Vec, pClass1):
    p1 = sum(vec2Classify * p1Vec) + log(pClass1)         
    p0 = sum(vec2Classify * p0Vec) + log(1.0 - pClass1)
    if p1 > p0:
        return 1
    else: 
        return 0
    
def testingNB():
    listOPosts,listClasses = loadDataSet()
    myVocabList = createVocabList(listOPosts)
    trainMat=[]
    for postinDoc in listOPosts:
        trainMat.append(setOfWords2Vec(myVocabList, postinDoc))
    p0V,p1V,pAb = trainNB0(array(trainMat),array(listClasses))
    testEntry = ['love', 'my', 'dalmation']
    thisDoc = array(setOfWords2Vec(myVocabList, testEntry))
    print (testEntry,'classified as: ',classifyNB(thisDoc,p0V,p1V,pAb))
    testEntry = ['stupid', 'garbage']
    thisDoc = array(setOfWords2Vec(myVocabList, testEntry))
    print (testEntry,'classified as: ',classifyNB(thisDoc,p0V,p1V,pAb))

testingNB()
testentry = ['my','love','cute']
thisDoc = array(setOfWords2Vec(vocablist, testentry))
ans = classifyNB(thisDoc,p0prob,p1prob,probabusive)
if ans==0:
    ans = "Not abusive"
else:
    ans = "Abusive"
print (testentry,'classified as: ',ans)

# classifier for bag of words

def bagOfWords2VecMN(vocabList, inputSet):
    returnVec = [0]*len(vocabList)
    for word in inputSet:
        if word in vocabList:
            returnVec[vocabList.index(word)] += 1
    return returnVec

def textParse(bigString):    
    import re
    listOfTokens = re.split(r'\W*', bigString)
    return [tok.lower() for tok in listOfTokens if len(tok) > 2]


def spamTest():
    docList=[]; classList = []; fullText =[]
    for i in range(1,26):
        wordList = textParse(open(f'C:/Users/91951/OneDrive/Desktop/Bayes/spam/{i}.txt').read())
        docList.append(wordList)                                    
        fullText.extend(wordList)                                   
        classList.append(1)                                         
        wordList = textParse(open(f'C:/Users/91951/OneDrive/Desktop/Bayes/spam/{1}.txt').read())
        docList.append(wordList)                                    
        fullText.extend(wordList)
        classList.append(0)
    vocabList = createVocabList(docList)
    trainingSet = range(50); testSet=[] 
    trainingSet = list(trainingSet)
    for i in range(10):                                    
        randIndex = int(random.uniform(0,len(trainingSet)))   
        testSet.append(trainingSet[randIndex])             
        del(trainingSet[randIndex])                        
    trainMat=[]
    trainClasses = []
    for docIndex in trainingSet:
        trainMat.append(setOfWords2Vec(vocabList, docList[docIndex]))
        trainClasses.append(classList[docIndex])
    p0V,p1V,pSpam = trainNB0(array(trainMat),array(trainClasses))
    errorCount = 0
    for docIndex in testSet:                                           
        wordVector = setOfWords2Vec(vocabList, docList[docIndex])      
        if classifyNB(array(wordVector),p0V,p1V,pSpam) != classList[docIndex]:
            errorCount += 1
    print ('the error rate is: ',float(errorCount)/len(testSet))

for i in range(10):
    spamTest()