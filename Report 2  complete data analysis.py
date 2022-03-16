#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


get_ipython().system('pip install yfinance')


# In[3]:


import yfinance as yf


# In[5]:


JWN = yf.Ticker("JWN")


# In[6]:


JWN.info


# In[10]:


hist = JWN.history(period="10y")


# In[11]:


hist


# In[18]:


hist.plot(kind="line", figsize=(12, 12), subplots=True);


# In[26]:


ticker_list = ["JWN","XRT","M","NKE"]


# In[31]:


df =  yf.download(ticker_list,period="m",start="2000-1-1", end="2022-1-1")


# In[32]:


df


# In[34]:


df.columns


# In[35]:


adj_close = df.dropna(thresh=10,axis=1)['Adj Close']


# In[36]:


adj_close.head()


# In[37]:


adj_close.describe().T


# In[55]:


adj_close.plot(figsize=(12, 12), subplots=True);


# In[40]:


JWN = adj_close['JWN']


# In[41]:


JWN.resample("4M").mean()


# In[43]:


JWN_per_change = JWN / (JWN.shift(1) - 1)


# In[44]:


JWN_per_change.plot(figsize=(12, 12))


# In[50]:


JWN_log_returns_shift = np.log(JWN/JWN.shift(1))


# In[52]:


JWN_log_returns_shift.plot(figsize=(12,12));


# In[53]:


JWN.hist(bins=50, figsize=(12,12));


# In[ ]:




