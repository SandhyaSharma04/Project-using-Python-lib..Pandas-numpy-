#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sb


# In[2]:


# to read csv file 
track = pd.read_csv(r"C:\Users\MSI\Desktop\Spotify\Tracks.csv")


# In[3]:


track.head()


# In[4]:


track.columns


# In[5]:


track.isnull().sum()


# In[6]:


track.info()


# In[7]:


# sort values in asc
track.sort_values('popularity', ascending = True).head(10)


# In[8]:


track.describe().transpose()    # to check all the calculation mean,count std etc


# In[9]:


# check most popular song
track[track.popularity > 90].sort_values('popularity', ascending = False).head(10)


# In[10]:


track.set_index("release_date", inplace=True) #set index 


# In[11]:


#  To find specific row in the data set
track[["artists"]].iloc[18]


# In[12]:


# convert duration_ms to second
track["duration"] = track["duration_ms"].apply(lambda x: round(x/1000))
track.drop("duration_ms", inplace = True, axis = 1)


# In[13]:


track.duration.head()


# In[14]:


# To check null values
track.isnull().sum()


# In[15]:


# visualization of correlation map
corr_track = track.drop(["key","mode", "explicit"],axis = 1).corr(method="pearson") # pearson correlation matrix
plt.figure(figsize=(14,6))
heatmap=sb.heatmap(corr_track,annot=True,fmt='.1g' , vmin=-1, vmax=1, center=0, cmap="inferno", linewidths=1, linecolor="black" )
heatmap.set_title("Correlation heatmap between Variable")
heatmap.set_xticklabels(heatmap.get_xticklabels(),rotation=90)


# In[16]:


# reg plot to visual the complete data b/w loudness and energy
plt.figure(figsize=(10,4))
sb.regplot(data = track, y="loudness", x="energy", color="c").set(title = "loudness vs Energy corelation")


# In[17]:


# to get perfect reg map we use 1/4 data of data 
sample_data = track.sample(int(0.004*len(track)))


# In[18]:


sample_data = track.sample(int(0.004*len(track)))


# In[20]:


plt.figure(figsize=(8,6))
sb.regplot(data = sample_data, y="loudness", x="energy", color="c").set(title = "Loudness vs Energy correlation")


# In[21]:


# reg plot b/w popularity and acousticness to find the relationship
plt.figure(figsize=(10,6))
sb.regplot(data = sample_data, y="popularity", x="acousticness", color="b").set(title = "popularity vs acousticness correlation")


# In[22]:


track["dates"] = track.index.get_level_values('release_date')
track.dates = pd.to_datetime(track.dates)
years = track.dates.dt.year


# In[23]:


#Histogram chart to check the distribution of total number of songs by each year
sb.displot(years,discrete=True,aspect=2,height=5 ,kind="hist").set(title="Number of songs year wise")


# In[24]:


# bar plot
total_duration = track.duration
fig_dimension = (20,6)
fig, ax = plt.subplots(figsize = fig_dimension)
fig = sb.barplot(x = years, y = total_duration, ax = ax, errwidth=False).set(title="Year vs Duration")
plt.xticks(rotation=90)


# In[ ]:


# line chart
total_duration = track.duration
sb.set_style(style="whitegrid")
fig_dimension = (10,5)
fig, ax = plt.subplots(figsize = fig_dimension)
fig = sb.lineplot(x = years, y = total_duration, ax = ax).set(title="Year vs Duration")
plt.xticks(rotation=60)


# In[ ]:




