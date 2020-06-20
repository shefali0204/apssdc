#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas as pd
df=pd.read_csv("income.csv")   #to read the csv file
df

Combined Average Income of all states from 2005 to 2013
State with highest average income in the last three years
State with lowest average income from 2007 to 2010(inclusive)
Print the list of all states in the same line with average income less than California
Print the names of states based on descending order of income in the year 2009
State with the lowest recorded income from 2005 to 2013
# #### Combined Average Income of all states from 2005 to 2013

# In[8]:


df[0:1]


# In[9]:


df.iloc[:,2:]  #income from 2005 to 2013


# In[11]:


df.iloc[0:5,2:12]


# In[13]:


avg=df.iloc[0:5,2:12].mean()  #  column wise average
avg


# In[15]:


avg=df.iloc[0:5,2:12].mean(1)   #  row wise average
avg


# In[17]:


#mean()----
#mean(1)----
avg=df.iloc[0:5,2:12].mean(1).mean()
avg


# In[18]:


avg=df.iloc[0:5,2:12].mean().mean()
avg


# #### State with highest average income in the last three years

# In[19]:


df


# In[20]:


df.index=df["State"]
df


# In[21]:


df.iloc[:,-3:]    #data of last three years


# In[24]:


a=df.iloc[:,-3:].mean(1)  #row wise avg of last three years
a


# In[26]:


a.idxmax()


# In[27]:


a.max()


# In[29]:


df.iloc[:,-3:].mean(1).idxmax()


# #### State with lowest average income from 2007 to 2010(inclusive)

# In[30]:


df


# In[35]:


df.iloc[:,4:8].mean(1).idxmin()


# In[36]:


df.iloc[:,4:8]


# In[37]:


df.iloc[:,4:8].mean(1)


# In[40]:


df.iloc[:,4:].mean(1).idxmin()


# #### Print the names of states based on descending order of income in the year 2009

# In[39]:


df


# In[42]:


df["2009"]


# In[46]:


df["2009"].sort_values(ascending=False)


# In[47]:


df["2009"].sort_values(ascending=False).index


# In[49]:


a=df["2009"].sort_values(ascending=False).index
a


# In[51]:


a=list(df["2009"].sort_values(ascending=False).index)
a


# #### State with the lowest recorded income from 2005 to 2013

# In[52]:


df


# In[54]:


df.iloc[:,2:]


# In[55]:


df.iloc[:,2:].mean(1)


# In[56]:


df.iloc[:,2:].mean(1).sort_values(ascending=False)


# In[57]:


a=list(df.iloc[:,2:].mean(1).sort_values(ascending=False).index)
a


# In[59]:


df.iloc[:,2:].min()


# In[60]:


df.iloc[:,2:].idxmin()


# #### Print the list of all states in the same line with average income less than California

# In[61]:


a=df.iloc[:,2:]
a


# In[67]:


b=a.mean(1)   #row wise
print(type(b))
print(b)


# In[64]:


calavg=b["California"]
calavg


# In[65]:


b<calavg


# In[69]:


list((b<calavg).index)


# In[71]:


df[b<calavg]


# In[72]:


df[b<calavg].index


# In[73]:


list(df[b<calavg].index)


# #### matplotplotlib

# In[77]:


import matplotlib.pyplot as plt
x=[1,2,3,4,5]
y=[10,20,23,45,6]
plt.title("basic graph")
plt.xlabel("x--axis")
plt.ylabel("y--axis")
plt.plot(x,y)
plt.grid()
plt.show()


# In[78]:


plt.plot(x,y,"r")


# In[79]:


plt.plot(x,y,"ro")


# In[80]:


plt.plot(x,y,"g--")


# In[81]:


plt.bar(x,y)


# In[82]:


plt.scatter(x,y)


# In[83]:


df


# In[89]:


#years-----x-axis
#alaska-----y-axis
import matplotlib.pyplot as plt
x=df.columns[2:]
y=df.iloc[1,2:]
plt.title("Income values of the stata Alaska")
plt.xlabel("years")
plt.ylabel("Income")
plt.plot(x,y)
plt.show()


# In[ ]:




