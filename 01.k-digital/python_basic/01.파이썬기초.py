#!/usr/bin/env python
# coding: utf-8

# In[136]:


x = "this is the first line. \
    this is the secone line. \
        'what's jour name?' I asked. He said 'Bond, james bond.'"
print(x)


# In[137]:


print('ha' * 3)

a = 'good' + 'day'
print(a)


# In[138]:


x = 5
eval('23 + (2*x)')

# eval : 스트링도 숫자로 계산해준다. 출력까지 해준다. 


# In[139]:


exec('x=2')
#exec: 스트링도 숫자로 계산해 준다. but 실행만 하고 출력은 안함.
x


# In[141]:


str(5.0)


# In[142]:


a = "python"

a.upper()
a.capitalize()


# In[143]:


len(a)


# In[144]:


str2 = 'ab        '
str2.strip()


# In[145]:


p = "Good Doggie"
p.upper().count('G')


# In[146]:


print("Python")
print("Python"[1], "Python"[5], "Python"[2:4])
str1 = 'Hello World!'
print(str1.find('l'))
print(str1.rfind('l'))


# In[147]:


print("Python")
print("Python"[-1], "Python"[-4], "Python"[-5:-2])
str1 = 'spam & eggs'
print(str1[-5])
print(str1[-8:-3])
print(str1[0:-1])


# In[148]:


x = 5; y = 7
print(x,y, sep='*')

print("Hello", "World", sep="")

print('1', 'two', 3, sep= '     ')


# In[149]:


age = 20
name = 'Swaroop'

print('''{0} was {1} years old when he wrote the book A Byte of Python.'''.format(name, age))
print(f'{name} is {age} years old when he wrote the book A Byte of Python')


# In[ ]:


print('How can you prevent \\n from being printed?')
print('How can you prevent \n from being printed?')
print('A backslash at the end of the line\
     indicates line continuation')


# In[150]:


print("0123456789012345678901234567")
print("{0:^5}{1:<20}{2:>3}".format("Rank", "Player", "HR"))
print("{0:^5}{1:<10}{2:>1}".format("Rank", "Player", "HR"))
# ^5 : 가운데정렬 5칸 할당 
# <20 : 왼쪽정렬 20칸 할당
# >3 : 오른쪽 정렬 3칸 할당


# In[151]:


print('{0:10.2f}'.format(1234.5678))    # 숫자 10칸을 할당하는데  소숫점 2째자리까지 출력
print('{0:10,.2f}'.format(1234.5678))   # 숫자 10칸을 할당하는데 소숫점 2째자리까지 출력, 세자리마다 콤마 입력


# In[152]:


print('{0:.3f}'.format(1.0/3))
print('{0:.3f}'.format(1/3))


# In[153]:


print('by\n')
print(r'by\n')  # r: raw 


# In[154]:


text = input('what is your name?')
text


# In[161]:


prompt = input('what is the airspeed velocity of a swallo?\n')
speed = int(prompt)
speed


# In[156]:


14//3
13%3


# In[ ]:


13%3


# In[ ]:


2<<2  # 2를 왼쪽(이진법: 10)으로 두칸 1000
# 2의 거듭제곱을 계산할 때 편리하다.
2 >> 2


# In[ ]:


5&3  # 2진법에서 5: 101, 3: 011 => 001 
5|3  # 101|011 => 111


# In[ ]:


3<5<7


# In[ ]:


x = False
y = True
x & y


# In[ ]:


5^3


# In[ ]:


~5


# In[161]:


number = 23
guess = int(input("Enter an integer: "))

if guess == number:
    print("Contrats")
else:
    if guess < number:
        print("go higher")
    else: print("go lower")


# In[135]:


number = 23
guess = int(input("Enter an integer: "))

if guess == number:
    print("Contrats")
elif guess < number:
    print("go higher")
else: 
    print("go lower")


# In[8]:


fnum = eval(input('Enter the first number:'))
snum = eval(input('Enter the second number:'))
thnum = eval(input('Enter the third number:'))

largest = fnum
if snum > largest:
    largest = snum
if thnum > largest:
    largest = thnum

print('the largest number is', str(largest) + '.')


# In[10]:


number = 23
running = True

while running:
    guess = int(input("Enter an integer: "))
    if guess == number:
        print("Contrats")
        running = False
    elif guess < number:
        print("go higher")
    else: 
        print("go lower")
else:
    print('the while loop is over')
    


# In[166]:


for i in range(1,10):
    print(i)


# In[170]:


print(range(0,10))


# In[175]:


for i in range(10):
    for i in range(i + 1):
        print('*', end = '')
    print()


# In[177]:


word = input('Enter a word')
reversedWord = ' '
for i in word:
    reversedWord = i + reversedWord
print('The reversed word is "' + reversedWord + '".')


# In[7]:


firstName = input('Enter a first name: ')
foundFlag = False
infile = open('C:/07AIProgramming/AIP_02_Operators and Control Flow_data/USPresidents.txt', 'r', encoding = 'cp949')

for line in infile:
    if line.startswith(firstName + ' '):
        print(line.rstrip())
        foundFlag = True
infile.close()
if not foundFlag:
    print('No president had the first name', firstName + '.')


# In[15]:


print('Enter QUIT to terminate entering something')
while True:
    s = input('Enter something: ')
    if s == 'QUIT':
        break
    if len(s) <1:
        print('Too short')
        continue
    print('Length of the string is', len(s))
print('Done')


# In[23]:


a = ['abvv', 'cdds']
a.reverse()
a


# In[27]:


a = [3,2,4,1]
print(a.sort())
a


# In[43]:


shoplist = ['apple', 'mango', 'carrot','banana']
print("I have {0} items to purchase".format(len(shoplist)))


# In[49]:


print('These items are:', end = '')
for item in shoplist:
    print(item, end=' ')

print('\nI also have to buy rice')
shoplist.append('rice')
shoplist

shoplist.sort()
shoplist


# In[50]:


del shoplist[-3:]


# In[51]:


shoplist


# In[52]:


shoplist.insert(0,'bana')


# In[54]:


shoplist.sort()
shoplist


# In[78]:


lst = []
for i in 'zeus':
    lst.append(i)
lst.reverse()
lst

lst[0]


# In[77]:


a = ','.join(lst)
a


# In[80]:


tuple1 = ( 'a','b','c')


# In[84]:


tuple2 = 'a','b','c'
type(tuple2)


# In[86]:


t3 = 1,
type(t3)


# In[122]:


zoo = ('giraffe', 'rabbit','pig', 'monkey')
print(len(zoo))


# In[121]:


new_zoo = ('camel', 'penguin',zoo)
new_zoo


# In[132]:


a = list(new_zoo)
a.append('horse')
a
a = tuple(a)
new_zoo = a
new_zoo


# In[138]:


'zeus'[::]


# In[146]:


print('Simple Assignment')
shoplist=['apple', 'mango', 'carrot', 'banana']


# In[147]:


mylist = shoplist


# In[149]:


mylist = shoplist[:]


# In[150]:


del mylist[0]


# In[151]:


print('shoplist is', shoplist)
print('mylist', mylist)


# In[152]:


x = [1,2,3,4]
y = x
z = x[:]
x.append(5)


# In[155]:


print(z)
print(y)


# In[157]:


w = y.copy()
del w[0]


# In[160]:


print(w)
print(y)


# In[ ]:





# In[ ]:




