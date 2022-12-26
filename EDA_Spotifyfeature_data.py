#!/usr/bin/env python
# coding: utf-8

# In[5]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sb


# In[15]:


# second data set 
feature =pd.read_csv(r"C:\Users\MSI\Desktop\Spotify\SpotifyFeatures.csv")


# In[16]:


feature.head(2)


# In[17]:


plt.title("Duration of the song in different genre")
sb.color_palette("rocket",as_cmap= True)
sb.barplot(y='genre', x='duration_ms', data=feature)
plt.xlabel("Duration in milli seconds")
plt.ylabel("genre")


# In[20]:


# find top 5 gener
sb.set_style(style = "darkgrid")
plt.figure(figsize=(10,5))
famous = feature.sort_values("popularity",ascending = False).head(10)
sb.barplot(x = "popularity", y = "genre",data = famous).set(title="Top 5 gener by popularity")
plt.xticks(rotation=90)


# In[ ]:




