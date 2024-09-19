#!/usr/bin/env python
# coding: utf-8

# # Perform the EDA on Super Market Sales.
In my EDA of the Superstore_USA dataset, I cleaned the data and analyzed profit,
customer segments, and sales trends. I identified opportunities to boost profit
through better pricing strategies, cost management, and targeted customer segments. 
Insights from sales patterns and customer behavior will help refine strategies to increase profitability.
# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns


# In[2]:


df=pd.read_excel('Superstore_USA.xlsx')
df


# In[3]:


df.head()


# # Do some Basic Operation of dataset.

# In[4]:


type(df)


# In[5]:


df.count()


# In[6]:


df.shape


# # Check the missing value firstly.

# In[7]:


df.isnull().sum()


# In[8]:


df['Product Base Margin']


# In[9]:


# 1. Here we can see that the column of "Product Base Margin" have 72 missing value.
#  so that we have to fill this by mean of the value of "Product Base Margin"

df['Product Base Margin'].mean()


# In[10]:


df['Product Base Margin'].fillna(df['Product Base Margin'].mean(),inplace=True)


# In[11]:


df.isnull().sum()


# #  Analysis on Order Priority

# In[12]:


df["Order Priority"].value_counts()


# In[ ]:





# In[13]:


df['Order Priority'].unique()


# # There is two types of [ 'Critical', 'Critical '] column which is parts of data cleaning.

# In[14]:


df['Order Priority']=df["Order Priority"].replace('Critical ','Critical')


# In[15]:


df['Order Priority'].unique()


# In[ ]:





# In[16]:


plt.figure(figsize=(5,4))
sns.countplot(x="Order Priority",data=df)
plt.title("count of order priority")
plt.show()


# In[17]:


df["Order Priority"].value_counts().plot(kind='bar',color="black",x="mmm")


# # Analysis of shiping mode

# In[18]:


df["Ship Mode"]


# In[19]:


df["Ship Mode"].value_counts()


# In[20]:


df["Ship Mode"].value_counts().index


# In[21]:


df["Ship Mode"].value_counts().plot(kind='pie',autopct='%0.2f%%')


# # Bivarient analysis with (Product Category vs  Ship Mode )

# In[22]:


plt.figure(figsize=(5,4))
sns.countplot(x='Ship Mode', data=df, hue ="Product Category")
plt.show()


# # Customer segments

# In[23]:


plt.figure(figsize=(5,4))
sns.countplot(x="Customer Segment",data=df)
plt.title("count of order priority")
plt.show()


# # Product category

# In[24]:


plt.figure(figsize=(5,4))
sns.countplot(x="Product Category",data=df)
plt.title("count of order priority")
plt.show()


# In[25]:


plt.figure(figsize=(10,12))
sns.countplot(x="Product Category",data=df[df['Product Category']=="Office Supplies"],hue="Product Sub-Category")
plt.title("count of order priority")
plt.show()


# # Sales per Year

# In[26]:


df.info()


# In[27]:


df["order year"]=df["Order Date"].dt.year


# In[28]:


df["order year"].value_counts().plot(kind="bar")


# In[29]:


plt.figure(figsize=(5,4))
sns.countplot(x="order year",data=df)
plt.show()


# # Profit analysis

# In[32]:


plt.figure(figsize=(6,4))
sns.barplot(x="Product Category",y="Profit",data=df, estimator="sum")
plt.show()


# In[42]:


df["State or Province"].value_counts().head(5).plot(kind="bar")
# df["State or Province"].value_counts()[:5].plot(kind="bar"), both are same code


# # Profit base Margin

# In[45]:


plt.figure(figsize=(6,4))
sns.barplot(x="Product Category",y="Product Base Margin",data=df, estimator="sum")
plt.show()


# # Thank you
