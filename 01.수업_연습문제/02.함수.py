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





# In[ ]:





# In[ ]:




