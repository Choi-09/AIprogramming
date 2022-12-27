#!/usr/bin/env python
# coding: utf-8

# ## 2. 함수 연습문제

# (1) Analyze a Sentence : Write a program that displays the first and last words 
# of a sentence input by the user. Assume that the only punctuation is a period 
# at the end of the sentence.

# In[ ]:


def func(  ):
    sentence = input("Enter a sentence: ")
    print("First word:", sentence.split()[0])
    print("Last word: ", sentence.replace(".","").split()[-1])
func()


# In[ ]:


# 교수님 풀이
sentence = input("Enter a sentence: ")
words = sentence.split()
print("Fist word:", words[0])
print("Fist word:", words[-1][:-1])


# (2)  Name Write a program that requests a three-part name and then displays 
# the middle name.

# In[ ]:


def main():
    fullName = input("Enter a 3-part name: ")
    print("Middle name:", middleName(fullName))

def middleName(fullName):
    middleName = fullName.split()[1]
    return middleName
main()


# In[ ]:


# 교수님 풀이
name = input("Enter a 3-part name: ")
name = name.split()
print("Middle name: ", name[1])


# (3) Median: The median of an ordered set of measurements is a number 
# separating the lower half from the upper half.<br/> If the number of measurements 
# is odd, the median is the middle measurement. <br/>If the number of measurements 
# is even, the median is the average of the two middle measurements. <br/>Write a 
# program that requests a number n and a set of n measurements (not necessarily
# ordered) as input and then displays the median of the measurements.

# In[ ]:


number = int(input("How many numbers do you want to enter?"))
outputs=[]
outputs.append(int(input("Enter a number:"))*i for i range(number))


# In[ ]:


# 교수님 풀이
num = int(input("How many numbers do you want to enter?: "))

numbers =[]
for k in range(num):
    v = eval(input('Enter a number:'))
    numbers.append(v)

# 입력 순서가 정렬되어있지 않기 때문에 정렬먼저 해준다. 
numbers.sort()

l = len(numbers)
if l % 2 ==0:
    # 짝수
    v_med = (numbers[l //2-1] + numbers[l // 2])/2
else:
    # 홀수
    v_med = numbers[l //2 ]

print("Median:", v_med)


# (4) A Puzzle : The following puzzle is known as The Big Cross-Out Swindle. <br/>
# “Beginning with the word ‘NAISNIENLGELTETWEORRSD,’ cross out nine 
# letters in such a way that the remaining letters spell a single word”. <br/>
# Write a program that creates variables named startingWord, crossedOutLetters, and remainingLetters. <br/>
# The program should assign to startingWord the string given 
# in the puzzle, assign to crossedOutLetters a list containing every other letter of 
# startingWord beginning with the initial letter N, and assign to remainingLetters
# a list containing every other letter of startingWord beginning with the second 
# letter, A. <br/> The program should then display the values of the three variables.

# In[ ]:


word = input("Starting Word: ")
Crossed_out_letters = []
Remaining_letters =[]

[Crossed_out_letters.append(word[i]) for i in range(len(word)) if i % 2 == 0 ]
[Remaining_letters.append(word[i]) for i in range(len(word)) if i % 2 == 1]

print('Crossed_out_letters: ', ' '.join(Crossed_out_letters))
print('Remaining_letters:', ' '.join(Remaining_letters))


# In[ ]:


# 교수님 풀이
starting_word = 'NAISNIENLGELTETWEORRSD'
crossed_out = starting_word[::2]  # 처음부터 끝까지 가는데 2칸씩 띄워서
remaining = starting_word[1::2]  # 두번째부터 끝까지 가는데 2칸씩 띄워서 

print('String word:', starting_word)
print('crossed_out:', ' '.join(crossed_out))
print('remaining:', ' '.join(remaining))


# (5) Special Number: Write a program to find the four-digit number, call it 
# abcd, whose digits are reversed when the number is multiplied by 4. <br/>
# That is, 4 x abcd = dcba.

# In[ ]:


num = input("Enter the four-digit number: ")
rv_num = eval(num[::-1])
print("Since 4 times", num, "is", rv_num, ",")
print("the special number is", num)


# In[ ]:


# 교수님 풀이
def special_number(num):
    num_rev = list(str(num))
    num_rev.reverse()
    num_rev =int(''.join(num_rev))

    if 4*num == num_rev:
        return True
    else:
        return False

for i in range(1000,10000):
    if special_number(i) == True:
        print(f"Since 4 time {i} is {i*4}, the special number is {i}")


# (6) Count Function: Suppose the count function for a string didn’t exist.<br/> Define 
# a function that returns the number of non-overlapping occurrences of a 
# substring in a string.

# In[ ]:


# 교수님 풀이
def my_count(str_orig, str_sub):
    l_orig = len(str_orig)
    l_sub = len(str_sub)

    # 버그잡기 (무한루프에 빠지는 오류)
    if l_sub == 0:
        return l_orig+1

    idx = 0
    count = 0
    while idx  <= l_orig - l_sub:
        p_orig = str_orig[idx:idx+l_sub]

        if p_orig == str_sub:
            count += 1  # 카운트 1증가
            idx += l_sub  # 찾은 단어 길이만큼 뛰어넘고 다음 차례단어부터 찾는다
        else:
            idx += 1
    return count
print(my_count('abcdeefghijkleemnop', ''))


# (7) Pay Raise: Write a pay-raise program that requests a person’s first name, 
# last name, and current annual salary, and then displays the person’s salary for 
# next year.<br/> People earning less than $40,000 will receive a 5% raise, and those 
# earning $40,000 or more will receive a raise of $2,000 plus 2% of the amount 
# over $40,000.<br/> Use functions for input and output, and a function to calculate 
# the new salary.

# In[ ]:


first = input('First name: ')
last = input('Last name: ')
salary = eval(input('Current salary: '))

if salary < 40000:
    new_salary = salary*1.05
else:
    new_salary = salary + 2000 + (salary -40000)*0.02

print("New salary: ${:,.2f}".format(new_salary))

