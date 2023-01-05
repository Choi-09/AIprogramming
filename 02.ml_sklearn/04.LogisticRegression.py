#!/usr/bin/env python
# coding: utf-8

# # 4. Logistic Regression

# ### 공부 시간에 따른 자격증 시험 합격 가능성

# In[2]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# In[3]:


dataset = pd.read_csv('LogisticRegressionData.csv')


# In[4]:


X = dataset.iloc[:,:-1].values
y = dataset.iloc[:, -1].values


# ### 데이터 분리

# In[6]:


from sklearn.model_selection import train_test_split


# In[12]:


X_train, X_test, y_train, y_test = train_test_split(X,y,test_size = 0.2, random_state = 0)


# ### 학습 (로지스틱 회귀모델)

# In[13]:


from sklearn.linear_model import LogisticRegression
classifier = LogisticRegression()
classifier.fit(X_train, y_train)


# ### 6시간 공부 했을 때 예측

# In[14]:


classifier.predict([[6]])
# 결과 1: 합격할 것으로 예측


# In[20]:


# 합격할 확률 정보 출력
classifier.predict_proba([[6]])
# 결과: 불합격 확률, 합격확률 순 


# In[18]:


classifier.predict([[4]])
# 결과 0: 불합격할 것으로 예측


# In[27]:


classifier.predict_proba([[4]])


# ### 분류 결과 예측(테스트 세트)

# In[22]:


y_pred = classifier.predict(X_test)
y_pred


# In[23]:


y_test  # 실제 값 (테스트 세트)


# In[25]:


X_test  # 공부시간(테스트 세트)


# In[29]:


classifier.score(X_test, y_test)  #모델 평가
# 전체 testset4개 중에서 분류 예측을 올바로 한 갯수 3개 = 75% 


# ### 데이터 시각화(훈련 세트)

# In[30]:


X_range = np.arange(min(X), max(X), 0.1)  # X의 최솟값 ~ 최댓값 까지를 0.1 단위로 잘라서 데이터 생성
X_range


# In[31]:


p = 1 / (1+ np.exp(-(classifier.coef_*X_range+classifier.intercept_)))  # y = mx+b. m = coef, b = intercept


# In[34]:


p.shape  # 2차원 데이터


# In[36]:


X_range.shape  # 1차원 데이터


# In[37]:


# p와 X_range의 shape을 맞춰준다.
p = p.reshape(-1)  # 1차원 배열 형태로 변경. -1: 원래 배열의 길이와 남은 차원으로부터의 추정
p.shape


# In[41]:


plt.scatter(X_train,y_train, color = 'blue')
plt.plot(X_range, p, color = 'g')
plt.title("probability by hours")
plt.xlabel('hours')
plt.ylabel('p')
plt.plot(X_range, np.full(len(X_range), 0.5), 'r') # X_range갯수만큼 0.5가 가득찬 배열 만들기 
plt.show()


# ### 데이터 시각화 (테스트 세트)

# In[42]:


plt.scatter(X_test,y_test, color = 'blue')
plt.plot(X_range, p, color = 'g')
plt.title("probability by hours(test)")
plt.xlabel('hours')
plt.ylabel('p')
plt.plot(X_range, np.full(len(X_range), 0.5), 'r') # X_range갯수만큼 0.5가 가득찬 배열 만들기 
plt.show()


# In[44]:


classifier.predict_proba([[4.5]])  # 4.5시간 공부했을 때 확률(모델에서는 합격 예측 but 실제로는 불합격)


# ### 혼동 행렬 (Confusion Matrix)

# In[47]:


from sklearn.metrics import confusion_matrix
con = confusion_matrix(y_test, y_pred)
con

# 결과 확인 [[1,1], [0,2]] => 1: 불합격예측 실제 불합격(TN)  1: 합격예측 실체 불합격(FP)
#                             0: 불합격 예측 실제 합격(FN)   2: 합격 예측 실제 합격(TP)

