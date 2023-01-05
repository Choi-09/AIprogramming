#!/usr/bin/env python
# coding: utf-8

# # 2. Multiple Linear Regression

# ### 원 핫 인코딩

# In[18]:


import pandas as pd


# In[19]:


dataset = pd.read_csv('MultipleLinearRegressionData.csv')
X = dataset.iloc[:,:-1].values
y = dataset.iloc[:,-1].values


# In[20]:


X


# In[21]:


from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
ct = ColumnTransformer(transformers=[('encoder', OneHotEncoder(drop='first'), [2])], remainder = 'passthrough')
X = ct.fit_transform(X)
X

# 1  0 = Home
# 0  1 = Library
# 0  0 = Cafe


# ### 데이터 세트 분리

# In[23]:


from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)


# ### 학습(다중선형회귀)

# In[25]:


from sklearn.linear_model import LinearRegression
reg = LinearRegression()
reg.fit(X_train, y_train)


# ### 예측값과 실제 값 비교 (테스트세트)

# In[26]:


y_pred = reg.predict(X_test)
y_pred


# In[27]:


y_test


# In[28]:


reg.coef_


# In[29]:


reg.intercept_


# ### 모델 평가

# In[31]:


reg.score(X_train, y_train) # 훈련세트


# In[32]:


reg.score(X_test, y_test)


# ### 다양한 평가 지표 (회귀모델)
# 
# 1. MAE (Mean Absolute Error) : 실제값과 예측값 차이의 절대값
# 2. MSE (Mean Squared Error) : 차이의 제곱
# 3. RMSE (Root Mean Squared Error) : 차이의 제곱의 근 
# 2. R square : 결정계수 
#     + R square는 1에 가까울수록, 나머지는 0에 가까울수록 좋다.

# In[33]:


from sklearn.metrics import mean_absolute_error
mean_absolute_error(y_test, y_pred) # 실제 값과 예측 값의 MAE 


# In[35]:


from sklearn.metrics import mean_squared_error
mean_squared_error(y_test, y_pred)  # 실제 값과 예측 값의 MSE


# In[37]:


from sklearn.metrics import mean_squared_error
mean_squared_error(y_test, y_pred, squared=False)  # 실제 값과 예측 값의 RMSE


# In[39]:


from sklearn.metrics import r2_score
r2_score(y_test, y_pred)  # r2 
# linear regression 모델 값과 같다 


# 
