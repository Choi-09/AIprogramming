#!/usr/bin/env python
# coding: utf-8

# # 연습문제

# ## Ⅰ. Operators Control Flow

# ### 1. Word Replacement Write a program that requests a sentence, a word in  the sentence, and another word and then displays the sentence with the first word replaced by the second. Do not use the format method.

# In[150]:


str_input = input("Enter a sentence:")
word1 = input("Enter word to replace:")
word2 = input("Enter replacement word: ")

str_output = str_input.replace(word1, word2)
print(str_output)


# ### 2. 현재가치: pv, 이자율: ir, 년수: ny, 미래가치: fv
# pv = fv / (1+ir/100)**ny

# In[200]:


fv = eval(input('Enter future value: '))
ir = eval(input('Enter interest rate(as %): '))
ny = eval(input('Enter number of years: '))

pv= (fv/(1+ir/100)**ny)
print("pv=", '${0:,.2f}'.format(pv))
        


# ### 3. Pig Latin

# In[206]:


# 내 코드(1) *오류: 자음3개인 단어에 버그
word = input("Enter word to translate: ")
vw = 'aeiou'

for vws in vw:
    if word.startswith(vws):
        PL = word + 'way'
        break
        
    if word[:2] not in (vws) :
        PL = word[2: ]+ word[:2] + 'ay'
print(PL)


# In[198]:


# 내 코드(2) *오류: 자음3개인 단어에 버그
word = input("Enter word to translate: ")
vw = 'aeiou'
g = word[:2]

if word[0] in vw:
    print(word + 'way')
elif g not in (vws) :
    print(word[2: ]+ word[:2] + 'ay')


# In[207]:


#교수님 풀이

word = input("Enter word to translate: ")

if word[0] in 'aeiou':
    print(word + 'way')
else:
    idx = 0
    while True:
        # Short-Circuit 
        if len(word) == idx or word[idx] in 'aeiou':
        # if word[idx] in 'aeiou':
            break
        else:
            idx+= 1
    g = word[:idx]
    word = word[idx:] + g + 'ay'
    print(word)
    print(idx) 


# ### 4. Bouncing Ball

# In[210]:


# 내 코드  * 그냥 오류.ㅎ
import math
coeff = float(input('Enter coefficient of restitution:'))
initial_height = float(input('Enter initial height in meters: '))

while (h>=0.1):
    paths = 0
    bounces = 1
    for i in range(bounces):
        bounces = int((initial_height / 2)/(coeff*10))
        if height >= 10:
            height = initial_height - coeff**i
            paths.append(initial_height - coeff*i)
            path = sum(paths)
        else: 
            break
        print("Number of bounces:", bounces)
        print(path)


# In[169]:


# 교수님 풀이
r = eval(input('Enter coefficient of restitution:'))  # r: 탄력
h = eval(input('Enter initial height in meters: '))   # h: 처음 떨어뜨리는 높이

# 처음 h에서 떨어졌을 때
d = h  # d:거리
bounces = 1

# 왕복 거리를 고려해야 한다. 
h *= r
while(h>=0.1):
    d += 2*h
    bounces += 1
    h *= r
print("Number of bounces: {}".format(bounces))
print("Meters traveled: {:.2f}".format(d))


# ### 5. Digit sum
# Write a program to calculate the total sum of the digits in the integers from 1 to a million.

# In[187]:


s = 0
for i in range(1, 1000001):
  while(i>0):
    s += i% 10
    i = i// 10

print('Sum: {:,}'.format(s))


# In[182]:


s = 0
for i in range(1,1000001):
    # 정수를 문자열로 변환
    val = str(i)
    for c in val:
        # 각 문자열에 들어있는 문자형 숫자를 숫자형으로 변환 
        s+=int(c)
print('Sum: {:,}'.format(s) )


# # ============================================

# ## Ⅱ. 함수

# ### 6. Analyze a Sentence
# Write a program that displays the first and last words of a sentence input by the user. Assume that the only punctuation is a period at the end of the sentence.

# In[191]:


st = input("Enter a sentence:")
fst = st.split(" ")[0]
last = st.split(" ")[-1]

print("First word:", fst)
print("Last word:", last)


# ### 7. Name
# Write a program that requests a three-part name and then displays the middle name.

# In[193]:


full_name = input("Enter a 3-part name:")
mid = full_name.split(" ")[1]

print("Middle name: ", mid)


# ### 8. Median
# The median of an ordered set of measurements is a number separating the lower half from the upper half. <br/>
# If the number of measurements is odd, the median is the middle measurement.<br/>
# If the number of measurements is even, the median is the average of the two middle measurements. <br/> 
# Write a program that requests a number n and a set of n measurements (not necessarily- 123 -ordered) as input and then displays the edian of the measurements.

# In[45]:


number = int(input("How many numbers do you want to enter?"))
outputs=[]
for i in range(number):
    int(input("Enter a number:"))*i
    

      

        


# In[ ]:




