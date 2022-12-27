#!/usr/bin/env python
# coding: utf-8

# In[1]:


list1 = ['white', 'blue', 'red']
list2 = sorted(list1) 
list2
sorted(list1, reverse=True)  # sorted: 원본을바꾸지않고 정렬 , sort: 원본을 바꾸고. 
list1
sorted('spam')


# In[2]:


list1 = ['2','5','7','8']
[ int(x) for x in list1]


# In[3]:


def g(x):
    return( int(x) ** 2)
[g(x) for x in list1]


# In[4]:


[g(x) for x in list1 if int(x) % 2 ==1]


# In[5]:


[ord(x) for x in "abc"]  # ord: 문자열을 아스키코드로 바꿔준다.


# In[6]:


[x ** .5 for x in (4,-1,9) if x >=0]


# In[7]:


[x**2 for x in range(3)]


# In[8]:


print(ord('a'))


# In[9]:


print(chr(97))


# ### 디폴트값 설정

# In[10]:


def main():
    say('Hello')
    say('World',8)

def say(message, times=1):  
    print(message * times)
main()


# ### 키워드 args

# In[11]:


def main():
    func(3,7)
    func(25, c=24)
    func(c=50, a =100)
def func(a, b=5, c=10):
    print('a is: ', a, 'b is: ',b, 'c is: ',c)

main()


# ### 람다식
# 한 줄짜리 미니 함수

# In[12]:


names = ["Dennis Ritchie", "Alan Kay", "John Backus", "James Gosling"]
names.sort(key = lambda name: name.split()[-1])  # 성을 기준으로 정렬하는 람다식
nameString=", ".join(names)
print(nameString)


# ### Top-Down design
# + 1 함수 1 기능만
# + 함수는 작을수록 좋다
# + 첫번째 함수 이름은 name, 함수전체의 끝은 main()으로 끝나야 호출.
