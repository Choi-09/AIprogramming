#!/usr/bin/env python
# coding: utf-8

# In[3]:


def print_max(a,b):
    """
    이 함수는 print_max라는 이름의 함수이다.
    """
    if a >b:
        print(a, 'is max')
    elif a==b:
        print(a, 'is equal to', b)
    else:
        print(b, 'is max')


# In[4]:


help(print_max)


# In[5]:


print_max.__doc__


# In[6]:


print_max(5,7)


# In[7]:


def f():
    return  #함수가 즉시 끝나고 돌아간다.
print(f())


# In[13]:

x = 50  # global variable

def func(x):  # 새로운 함수의 인자 x. 
    print('x is', x)
    x = 2
    print('changed local x to', x)  # loval variable
func(x)  # func함수의 인자 x.
print('x is still', x)   # global variable 

# In[14]:


def main():
    x = 2
    print(str(x) + ": function main")
    trivial()
    print(str(x) + ": function main")

def trivial():
    x = 3
    print(str(x) + ": function trivial")
main()


# In[16]:


x = 50

def main():
    func() # func 함수 먼저 
    print('Value of x is', x)
def func():
    global x        # 변수 앞에 global이라고 선언해주면  뒤에 나오는 변수에 global설정된다. 
    print('x is', x)
    x = 2
    print('Changed global x to', x)
main()


# 

# In[17]:


PI = 3.141592
r1 = 1
r2 = 2
r3 = 3

area1= PI*r1*r1
area2= PI*r2*r2


# In[ ]:

def main():
    fullName = input("Enter a person's full name: ")
    print("First name:", firstName(fullName))

def firstName(fullName):
    firstSpace = fullName.index(" ")  # " "가 나오는 부분에 index를 반환
    givenName = fullName[:firstSpace] 
    return givenName
main()



# In[ ]:

def main():
    hourlyWage = float(input("Enter the hourly wage: "))
    hoursWorked = int(input("Enter # hours worked: "))
    earnings = pay(hourlyWage, hoursWorked)
    print("Earnings: ${0:,.2f}".format(earnings))

def pay(wage, hours):
    if hours <= 40:
        amount = wage * hours
    else: 
        amount = (wage * 40) + ((1.5) * wage * (hours-40))
    return amount
main()




# In[ ]:

def main():
    word = input("Enter a word: ")
    listOfVowels = occuringVowels(word)
    print("the following vowels occur in the word:", end= ' ')
    stringOfVowels = " ".join(listOfVowels)
    print(stringOfVowels)

def occuringVowels(word):
    word = word.upper()
    vowels = ('A', 'E', 'I', 'O','U')
    includedVowels = []
    for vowel in vowels:
        if vowel in word:
            includedVowels.append(vowel)
    return includedVowels
main()

# In[ ]:
INTEREST_RATE = 0.4

def main():
    (deposit, numberOfYears) = getInput()
    bal, intEarned = balAndInterest(deposit, numberOfYears)
    displayOutput(bal, intEarned)

def getInput():
    deposit = int(input("Enter the amount of deposit: "))
    numberOfYears = int(input("Enter # of years: "))
    return (deposit, numberOfYears)
def balAndInterest(principal, numYears) :
    balance = principal * ((1 + INTEREST_RATE) ** numYears)
    interestEarned = balance - principal
    return (balance, interestEarned)
def displayOutput(bal, intnEarned):
    print("Balance: ${0:,.2f}  Interest Earned: ${1:,.2f}".format(bal, intnEarned))

main()


# In[ ]:

def main():
    list1 = ["democratic","sequoia","equals","brrr","break","two"]
    list1.sort(key = len)  # sort함수에 key를 지정해준다. 
    print("Sorted by length in ascending order: ")
    print(list1, '\n')
    list1.sort(key=numberOfVowels, reverse=True) #reverse=T: 내림차순정렬 
    print("Sorted by number of vowels in descending order:")
    print(list1)
    
def numberOfVowels(word):
    vowels = ('a', 'e', 'i', 'o','u')
    total = 0
    for vowel in vowels:
        total += word.count(vowel)
    return total
main()


