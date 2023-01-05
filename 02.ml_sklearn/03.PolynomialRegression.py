#!/usr/bin/env python
# coding: utf-8

# # 3. Polynomial Regression
# + 참고사이트: https://arachnoid.com/polysolve/

# ### 공부 시간에 따른 시험 점수(우등생)

# In[1]:


import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


# In[2]:


dataset = pd.read_csv('PolynomialRegressionData.csv')
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, -1].values


# ### 3-1) 단순 선형회귀 (Simple Linear Regression)

# In[3]:


from sklearn.linear_model import LinearRegression
reg = LinearRegression()
reg.fit(X,y) # 전체 데이터로 학습


# ### 데이터 시각화 (전체)

# In[4]:


plt.scatter(X,y, color = 'blue') # 산점도 그래프
plt.plot(X,reg.predict(X),color = 'g') # 선그래프
plt.title('scor by hours_ Genius')
plt.xlabel('hours')
plt.ylabel('score')


# In[5]:


reg.score(X, y) # 전체 데이터를 통한 모델 평가


# ### 3-2) 다항회귀 (Polynomial Regression)

# In[6]:


from sklearn.preprocessing import PolynomialFeatures
poly_reg = PolynomialFeatures(degree=4) # 4차 다항식
X_poly = poly_reg.fit_transform(X) # 다항식에 맞게 변형 
X_poly[:5]  # [X] -> [X^0, X^1, X^2] -> X=3 : [1,3,9]으로 변환 


# In[7]:


X[:5]


# In[8]:


poly_reg.get_feature_names_out()


# In[9]:


lin_reg = LinearRegression() # 2차 다항식
lin_reg.fit(X_poly, y)  #변환된 X와y를 가지고 모델 생성 (학습)


# ### 데이터 시각화 (변환된 X와 y)

# In[10]:


plt.scatter(X, y, color = 'b')
plt.plot(X, lin_reg.predict(poly_reg.fit_transform(X)), color = 'g')
plt.title('scor by hours_ Genius')
plt.xlabel('hours')
plt.ylabel('score')


# In[11]:


X_range = np.arange(min(X), max(X),0.1)  # x의 최소값에서 최대값까지의 범위를 0.1단위로 잘라서 데이터 생성
X_range


# In[12]:


X_range.shape


# In[13]:


X.shape


# In[14]:


# X_range의 shape을 X와 같이 맞춰준다.
X_range = X_range.reshape(-1, 1)  # 행의 길이를 자동으로 맞출 때 -1 사용 len(X_range)도 가능
X_range.shape


# In[15]:


X_range[:5]


# In[16]:


# X_range로 그래프 그리기 (부드러운 곡선)
plt.scatter(X, y, color = 'b')
plt.plot(X_range, lin_reg.predict(poly_reg.fit_transform(X_range)), color = 'g')
plt.title('scor by hours_ Genius')
plt.xlabel('hours')
plt.ylabel('score')


# ### 공부 시간에 따른 시험 성적 예측

# In[17]:


# 선형회귀모델 예측
reg.predict([[2]])  # 2시간 공부했을 때 선형회귀모델 예측


# In[18]:


# 다항회귀모델 예측
lin_reg.predict(poly_reg.fit_transform([[2]]))  # 2시간 공부했을 때 다항 회귀모델의 예측


# In[19]:


lin_reg.score(X_poly, y)

