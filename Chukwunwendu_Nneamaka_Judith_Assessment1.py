#!/usr/bin/env python
# coding: utf-8

# In[3]:


#the following codes import the libraries: pandas, numpy and matplotlib.pyplot
import pandas as pd   
import numpy as np
import matplotlib.pyplot as plt


# In[4]:


StudPerf = pd.read_csv('C:/Users/ADMIN/OneDrive/Desktop/TS ACADEMY/StudentsPerformance.csv') #reads the StudentsPerformance file into the notebook


# In[5]:


display(StudPerf.head(10)) #Displays the first 10 rows of the StudentsPerfomance file


# In[6]:


display(StudPerf.tail(10)) #Displays the last 10 rows


# In[7]:


StudPerf.info() #displays the StudentsPerformance dataset overview


# In[8]:


print("The shape of the dataset is:", StudPerf.shape) #displays the shape of the dataset in terms of the number of rows and columns


# In[9]:


print(list(StudPerf.columns)) #displays the column names as a list


# In[10]:


#to check the data type of each colummn
StudPerf.dtypes


# In[11]:


#Identifies numerical comlumns and displays them in a list
StudPerf.select_dtypes(include=['int64']).columns.tolist()


# In[12]:


# Identify categorical columns (category dtype)
StudPerf.select_dtypes(include=['category']).columns.tolist()


# In[13]:


# Identify categorical columns (object dtype)
StudPerf.select_dtypes(include=['object']).columns.tolist()


# In[14]:


StudPerf.describe()


# In[16]:


#Check if there are missing values in the dataset, then returns TRUE is there are and returns FALSE if there is no missing value
print('Is there any missing value in the dataset?',StudPerf.isnull().values.any(), "\n")


# In[17]:


# Filters students who completed the test preparation course and display them
StudPerf[StudPerf['test preparation course'].str.lower() == 'completed']


# In[22]:


# Filter students with Math score > 70 and displays them
StudPerf[StudPerf["math score"] > 70]


# In[26]:


# Filter the Female students with >=65 in all subjects and displays the result
StudPerf[
    (StudPerf['gender'] == 'female') &
    (StudPerf['math score'] >= 65) &
    (StudPerf['reading score'] >= 65) &
    (StudPerf['writing score'] >= 65)
]


# In[34]:


# the code below counts how many students having free/reduced lunch and prints the number
print('\nNumber of students with free lunch is',(StudPerf['lunch'].str.lower() == 'free/reduced').sum())


# In[50]:


#Compute average math score by gender ===
average_scores = ( StudPerf.groupby('gender')['math score']
    .mean()
        .reset_index()
                 )
#Displays result
display(average_scores)


# In[44]:


# Compute average math, writing and reading scores by parental level of education
avg_scores = (
    StudPerf.groupby('parental level of education')[['math score', 'reading score', 'writing score']]
    .mean()
    #.reset_index()
)

#Display results
display(avg_scores)  



# In[63]:


# Calculate average score per student
average_score= StudPerf[['math score', 'reading score', 'writing score']].mean()


# Group by test preparation course
average_by_prep = StudPerf.groupby('test preparation course')['average_score'].mean()


# Displays result
display(average_by_prep)


# In[85]:


plt.figure(figsize=(12, 8))
plt.hist(StudPerf["math score"], bins=8, alpha=0.8, label="math score")
plt.hist(StudPerf["writing score"], bins=8, alpha=0.8, label="writing score")
plt.hist(StudPerf["reading score"], bins=8, alpha=0.5, label="reading score")
plt.xlabel("Scores") #labels the x axis
plt.ylabel("Frequency") # labels the y axis
plt.title("Score Distributions")
plt.legend()
plt.grid(axis='y', linestyle='--')
plt.show() #displays the plotted histogram


# In[101]:


# Group by gender and calculate average score
average_score= StudPerf[['math score', 'reading score', 'writing score']].mean()

avg_scores = StudPerf.groupby('gender')['average_score'].mean()

# Plot bar chart
plt.figure(figsize=(12, 8))
avg_scores.plot(kind='bar', color=['#1f77b4', '#ff7f0e'])

# Add labels and title
plt.title('Average Score by Gender', fontsize=14)
plt.xlabel('Gender', fontsize=12)
plt.ylabel('Average Score', fontsize=12)
plt.xticks(rotation=0)
plt.ylim(0, 100)

# Display values on top of bars
for index, value in enumerate(avg_scores):
    plt.text(index, value + 1, f"{value:.1f}", ha='center', fontsize=10)


# The average scores of students with test preparation as compared to those without preparation was obtained to be 72.669460 and 65.038941 respectively.
# Clearly, the average scores of student with test preparation is higher than those without test preparation with an approximate difference of 7.63.
# This shows that test preparation improves performance.

# In[ ]:




