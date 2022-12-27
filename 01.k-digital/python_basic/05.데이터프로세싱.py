#!/usr/bin/env python
# coding: utf-8

# # 05. Data Processing and File Access
# + 파일 읽어오기
# + 파일 생성
# + 파일 내용 업데이트
# + 파일 수정후 저장

# ### Reading Text Files

# In[1]:


def main():
    file = "C:/07AIProgramming/AIP_05_Data Processing and File Access_data/FirstPresidents.txt"
    displayWithForLoop(file)
    print()
    displayWithListComprehension(file)
    print()
    displayWithReadline(file)

def displayWithForLoop(file):
    infile = open(file,'r')
    for line in infile:
        print(line.strip())
    infile.close()

def displayWithListComprehension(file):
    infile = open(file, 'r')
    listPres = [line.rstrip() for line in infile]
    infile.close()
    print(listPres)

def displayWithReadline(file):
    infile = open(file, 'r')
    line = infile.readline()
    while line != "":
        print(line.rstrip())
        line = infile.readline()
    infile.close()
main()


# ### Creating Text Files

# In[2]:


def main():
    L = ['George Washington', 'John Adams', 'Thomas Jefferson']
    outfile = open("FirstPresidents2.txt", 'w')  # 새로 생성할 파일
    createWithWrite(L, outfile)
    outfile = open("FirstPresidents3.txt", 'w')
    createWithWritelines(L, outfile)

def createWithWrite(L, outfile):
    for i in range(len(L)):
        outfile.write(L[i] + "\n")
    outfile.close()

def createWithWritelines(L, outfile):
    for i in range(len(L)):
        L[i] = L[i] +'\n'
    outfile.writelines(L)
    outfile.close()

main()


# In[3]:


def main():
    statesList = createListFromFile("C:/07AIProgramming/AIP_05_Data Processing and File Access_data/States.txt")
    createSortedFile(statesList, "C:/07AIProgramming/AIP_05_Data Processing and File Access_data/StatesAlpha.txt")

def createListFromFile(fileName):
    infile = open(fileName, 'r')
    desiredList = [line.rstrip() for line in infile]
    infile.close()
    return desiredList

def createSortedFile(listName, fileName):
    listName.sort()
    for i in range(len(listName)):
        listName[i] = listName[i] + "\n"
    outfile = open(fileName, 'w')
    outfile.writelines(listName)
    outfile.close()
main()


# In[4]:


def main():
    vicePresList = createListFromFile("C:/07AIProgramming/AIP_05_Data Processing and File Access_data/VPres.txt")
    createNewFile(vicePresList, "C:/07AIProgramming/AIP_05_Data Processing and File Access_data/USPres.txt", "C:/07AIProgramming/AIP_05_Data Processing and File Access_data/Both.txt")

def createListFromFile(fileName):
    infile = open(fileName, 'r')
    desiredList = [line.rstrip() for line in infile]
    infile.close()
    return desiredList

def createNewFile(listName, oldFileName, newFileName):
    infile = open(oldFileName, 'r')
    outfile = open(newFileName, 'w')
    for person in infile:
        if person.rstrip() in listName:
            outfile.write(person)
    infile.close()
    outfile.close()
main()


# ### Altering Items in a Text File
# + 텍스트 파일의 수정, 추가, 삭제는 바로 할 수 없다.
# + (내부적으로) 파일을 새로 생성하고, 수정/추가/삭제 후 저장해서 새로운 파일에서 업데이트.
# + 기존의 파일 삭제 후 기존파일의 이름으로 새로운 파일 이름을 변경하면 업데이트 완료.

# In[5]:


# 파일 중복생성해보기 
import os.path
if os.path.isfile("ABC.txt"):
    print("File already exists.")
else:
    infile = open("ABC.txt", 'w')
    infile.write("a\nb\nc\n")
    infile.close()


# In[6]:


# 기존 파일 삭제하기
os.remove('ABC.txt')


# In[7]:


# 기존파일 이름 수정하기
os.rename('ABC.txt', 'CBA.txt')


# ### Sets
# + 중복허용 x
# + 인자로 list나 또다른 set은 x
# + immutable
# + 기본적으로 order가 없기 때문에 indexing x, sort x, reverse x

# In[8]:


a = {3,4,7, 'spam'}


# In[9]:


bri = {'brazil', 'russia', 'india'}


# In[10]:


'india' in bri


# In[11]:


'usa' in bri


# In[12]:


bric = bri.copy()
bric.add('china')


# In[13]:


bri.remove('russia')


# In[14]:


bri


# In[15]:


bric


# In[16]:


bric.issuperset(bri)


# In[17]:


bri.issuperset(bric)


# In[18]:


bri & bric


# In[19]:


bric.difference(bri)


# In[20]:


bric - bri


# In[21]:


bric.union(bri)


# In[22]:


words = ['nudge', 'nudge', 'wink', 'wink']


# In[23]:


tuple(words)


# In[24]:


terms = set(words)
print(terms)


# In[25]:


list(terms)


# In[26]:


tuple(terms)


# In[27]:


alpha = ('a','b','c', 'a')
set(alpha)


# In[28]:


terms.clear()
terms


# In[29]:


lst = list(words)
lst.clear()
lst


# In[30]:


brick = {'brazil', 'china', 'india', 'russia', ''}
brick


# In[31]:


sorted(bric)  # sorted function을 사용하면 리스트로 출력 
              # sorted은 원본이 변하지 않는다.


# In[32]:


sorted(bric, key=len, reverse=True)


# In[33]:


def main():
    vicePresSet = createSetFromFile("C:/07AIProgramming/AIP_05_Data Processing and File Access_data/VPres.txt")
    presSet = createSetFromFile("C:/07AIProgramming/AIP_05_Data Processing and File Access_data/USPres.txt")
    bothPresAndVPresSet = createIntersection(vicePresSet, presSet)
    writeNamesToFile(bothPresAndVPresSet, "C:/07AIProgramming/AIP_05_Data Processing and File Access_data/PresAndVPres.txt")

def createSetFromFile(fileName):
    infile = open(fileName, 'r')
    namesSet = {name for name in infile}
    infile.close()
    return namesSet

def createIntersection(set1, set2):
    return set1.intersection(set2)

def writeNamesToFile(setName, fileName):
    outfile = open(fileName, 'w')
    outfile.writelines(setName)
    outfile.close()

main()


# In[34]:


def main():
    continent = input("Enter the name of a continent: ")
    continent = continent.title()
    if continent !="Antarctica":
        infile = open("./AIP_05_Data Processing and File Access_data/UN.txt", 'r')
        for line in infile:
            data = line.split(',')
            if data[1] == continent:
                print(data[0])
    else:
        print("There are no contries in Acratcira")
main()


# In[35]:


def main():
    countries = palceRecordsIntoList("./AIP_05_Data Processing and File Access_data/UN.txt")
    countries.sort(key=lambda country:country[3], reverse = True)
    displayFiveLargestCountries (countries)
    createNewFile(countries)

def palceRecordsIntoList(fileName):
    infile = open(fileName, 'r')
    listOfRecords = [line.rstrip() for line in infile]
    infile.close()
    for i in range(len(listOfRecords)):
        listOfRecords[i] = listOfRecords[i].split(',')
        listOfRecords[i][2] = eval(listOfRecords[i][2]) # eval(): 명령어를 실행하는 함수. 조심해서 사용!
        listOfRecords[i][3] = eval(listOfRecords[i][3])
    return listOfRecords

def displayFiveLargestCountries(countries):
    print("{0:20}{1:9}".format("Country", 'Area (sq. mi. )'))
    for i in range(5):
        print("{0:20}{1:9,d}".format(countries[i][0], countries[i][3]))

def createNewFile(countries):
    outfile = open("./AIP_05_Data Processing and File Access_data/UNbyArea.txt", 'w')
    for country in countries:
        outfile.write(country[0] + ',' + str(country[3]) + '\n')
    outfile.close()

main()


# ### Dictionary
# + 형태: {key: value}
# + kyes: immutable (values: mutable)
# + indexing 가능

# In[36]:


addr = {
    'Swaroop' : 'swaroop@swaroopch.com',
    'Larry' : 'larry@wall.org',
    "Matsumoto" : 'matz@ruby-lang.org',
    'Spammer' : 'spammer@hotmail.com'
}

print("Swaroop's address is", addr['Swaroop'])


# In[37]:


del addr['Spammer']
print('\nThere are {} contacts in the address-book\n'.format(len(addr)))

for name, address in list(addr.items()):
    print('Contact {} at {}'.format(name, address))


# In[38]:


addr['Guido'] = 'guido@python.org'
if 'Guido' in addr:
    print("\nGuido's address is", addr['Guido'])


# In[39]:


a = {}
type(a)


# In[ ]:


def main():
    print("Enter the person's age group", end='')
    ageGroup = input("(child,minor,adult, or senior): ")
    print("The admission fee is", determineAdmissionFee(ageGroup), "dollars.")

def determineAdmissionFee(ageGroup):
    if ageGroup == 'child':
        return 0
    elif ageGroup == 'minor':
        return 5
    elif ageGroup == 'adult':
        return 10
    elif ageGroup == 'senior':
        return 8

main()


# In[ ]:


def main():
    print("Enter the person's age group", end='')
    ageGroup = input("(child,minor,adult, or senior): ")
    Group = int(input("how many people in your group?: "))
    totalFee =  determineAdmissionFee(ageGroup) * Group
    print("The admission fee is", determineAdmissionFee(ageGroup), "dollars.")
    print(f"The total fee is {totalFee} dollars.")

def determineAdmissionFee(ageGroup) :
    dict = {"child":0, "minor":5, "adult":10, "senior":8}
    return dict[ageGroup]

main()


# ### Using a Dictionary as a Frequency Table

# In[ ]:


def main():
    listOfWords = formListOfWords("./AIP_05_Data Processing and File Access_data/Gettysburg.txt")
    freq = createFrequencyDictionary(listOfWords)
    displayWordCount(listOfWords, freq)
    displayMostCommonWords(freq)

def formListOfWords(fileName):  # words의 
    infile = open(fileName)
    originalLine = infile.readline().lower()

    line = ''
    for ch in originalLine:
        if('a' <= ch <= 'z') or (ch ==' '):
            line += ch
    
    listOfWords = line.split()
    return listOfWords

def createFrequencyDictionary(listOfWords):
    freq = {}
    for word in listOfWords:
        freq[word] = 0
    for word in listOfWords:
        freq[word] = freq[word] + 1
    return freq

def displayWordCount(listOfWords, freq):
    print("The Gettysburg Address contains", len(listOfWords), "words.")
    print("The Gettysburg Address contains", len(freq), "different words.")
    print()

def displayMostCommonWords(freq):
    print("The most common words and thei frequencies are: ")
    listOfMostCommonWords =[]
    for word in freq.keys():
        if freq[word] >= 6:
            listOfMostCommonWords.append((word, freq[word]))
    listOfMostCommonWords.sort(key=lambda x:x[1], reverse =True)
    for item in listOfMostCommonWords:
        print("     ", item[0] + ":", item[1])

main()


# # Storing Dictionaries in Binary Files
# import pickle

# In[ ]:


import pickle

def main():
    nations = getDictionary('./AIP_05_Data Processing and File Access_data/UNdict.dat')
    print("Enter the name of a continent", end='')
    continent = input("other than Antarctica: ")
    continentDict = constructContinentNations(nations, continent)

    displaySortedResults(continentDict)

def getDictionary(fileName):
    infile = open(fileName, 'rb')
    countries = pickle.load(infile)
    infile.close()
    return countries

def constructContinentNations(nations, continent):
    continentDict = {}
    for nation in nations:
        if nations[nation]["cont"] == continent:
            continentDict[nation] = nations[nation]
    return continentDict

def displaySortedResults(dictionaryName):
    continentList = sorted(dictionaryName.items(), key = lambda k: k[1]["popl"], reverse=True)
    for k in continentList:
        print("  {0:s}: {1:,.2f}".format(k[0], k[1]["popl"]))

main()


# ### Usinf a Dictionary with Tuples as Keys

# In[ ]:


def main():
    presDict = createDictFromBinaryFile("./AIP_05_Data Processing and File Access_data/USpresStatesDict.dat")
    state = getState(presDict)
    displayOutput(state, presDict)

def createDictFromBinaryFile(fileName):
    infile = open(fileName, 'rb')
    dictionary = pickle.load(infile)
    infile.close()
    return dictionary

def getState(dictName):
    state = input("Enter the name of a state: ")
    if state in dictName.values():
        return state
    else:
        return "There are no presidents from " + state + '.'

def displayOutput(state, dictName):
    if state.startswith("There"):
        print(state)
    else:
        print("Presidents from", state + ':')
        for pres in sorted(dictName) :
            if dictName[pres] == state:
                print("  " + pres[1] + " " + pres[0])

main()


# In[ ]:


a = ['a', 'b', 'c', 'd', 'e']
a[::-1]


# In[ ]:


a = 'abcde'
list(a[::-1])


# In[ ]:




