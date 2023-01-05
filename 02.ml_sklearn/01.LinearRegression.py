#!/usr/bin/env python
# coding: utf-8

# # 1. Linear Regression
# ### 공부 시간에 따른 시험 점수

# In[5]:


import matplotlib.pyplot as plt
import pandas as pd


# In[8]:


dataset = pd.read_csv('LinearRegressionData.csv')


# In[9]:


dataset.head()


# In[12]:


X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, -1].values


# In[13]:


X,y


# In[15]:


from sklearn.linear_model import LinearRegression
reg = LinearRegression() # 객체생성
reg.fit(X,y)  # 학습하면서 모델 생성


# In[16]:


y_pred = reg.predict(X) # X에 대한 예측값 
y_pred


# In[20]:


plt.scatter(X,y, color = 'blue')
plt.plot(X,y_pred, color = 'g')
plt.title('Score by hours ')
plt.xlabel('hours'),
plt.ylabel('score')
plt.show()


# In[21]:


print('9시간 공부 후 예상 점수: ', reg.predict([[9]]))


# In[22]:


reg.coef_  # 기울기(m)


# In[23]:


reg.intercept_ # y절편 (b)


# In[26]:


y = 10.4436 - 0.2184
print(y)


# ### 데이터 세트 분리

# In[27]:


import matplotlib.pyplot as plt
import pandas as pd


# In[28]:


dataset = pd.read_csv('LinearRegressionData.csv')
dataset


# In[29]:


X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, -1].values


# In[31]:


from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X,y, test_size = 0.2, random_state = 0) # test 세트를 20%


# In[32]:


X, len(X)


# In[33]:


X_train, len(X_train) #훈련세트 X 


# In[34]:


X_test, len(X_test)  # test세트 X


# In[35]:


y, len(y)


# In[36]:


y_train, len(y_train)


# In[37]:


y_test, len(y_test)


# ### 분리된 데이터를 통한 모델링

# In[38]:


from sklearn.linear_model import LinearRegression
reg = LinearRegression()


# In[39]:


reg.fit(X_train, y_train)  #훈련세트 학습


# ### 데이터 시각화 (훈련 세트)

# In[40]:


plt.scatter(X_train,y_train, color = 'blue')
plt.plot(X_train,reg.predict(X_train), color = 'g')
plt.title('Score by hours (train data)')
plt.xlabel('hours'),
plt.ylabel('score')
plt.show()


# ### 데이터 시각화 (test 세트)

# In[42]:


plt.scatter(X_test,y_test, color = 'blue')
plt.plot(X_train,reg.predict(X_train), color = 'g')
plt.title('Score by hours (test data)')
plt.xlabel('hours'),
plt.ylabel('score')
plt.show()


# In[43]:


reg.coef_


# In[44]:


reg.intercept_


# ### 모델 평가

# In[45]:


reg.score(X_test, y_test) # 테스트 세트를 통한 모델 평가


# In[48]:


reg.score(X_train, y_train) # 훈련세트를 통한 모델 평가


# ### 경사하강법 (Gradient Descent)

# + max_iter: 훈련 세트 반복 횟수(epoch 횟수)
# + eta0 : 학습률 (learning rate)
# + 지수표기법
#    + 1e-3 = 0.001 (10^-3)
#    + 1e-4 = 0.0001 (10^-4)
#    + 1e+3 = 1000 (10^3)
#    + 1e+4 = 10000 (10^4)

# In[94]:


from sklearn.linear_model import SGDRegressor
sr = SGDRegressor(max_iter=1000, eta0=1e-3, random_state=0, verbose=1)
sr.fit(X_train, y_train)


# In[95]:


plt.scatter(X_train,y_train, color = 'blue')
plt.plot(X_train,sr.predict(X_train), color = 'g')
plt.title('Score by hours (train data), SGD')
plt.xlabel('hours'),
plt.ylabel('score')
plt.show()


# In[85]:


sr.coef_


# In[78]:


sr.intercept_


# In[79]:


sr.score(X_test, y_test)


# In[80]:


sr.score(X_train, y_train)

