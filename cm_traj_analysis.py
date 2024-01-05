#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib
matplotlib.use('pdf')
import matplotlib as mpl
import matplotlib.pyplot as plt
plt.style.use('classic')
mpl.rcParams['xtick.major.size'] = 8
mpl.rcParams['xtick.major.width'] = 2
mpl.rcParams['ytick.major.size'] = 8
mpl.rcParams['ytick.major.width'] = 2
mpl.rcParams['xtick.minor.size'] = 6
mpl.rcParams['xtick.minor.width'] = 1
mpl.rcParams['ytick.minor.size'] = 6
mpl.rcParams['ytick.minor.width'] = 1
mpl.rcParams['axes.linewidth']= 2


# In[2]:



data=pd.read_csv("contact_map_less.dat", header=None, delimiter="\t")
#sorting the dataframe based on first column values
sorted_df = data.sort_values(by=[0], ascending=True)
#joining all the rows which has same values
aggregated_df = sorted_df.groupby(0)[1].agg(''.join).reset_index()

total_aa=aggregated_df.shape[0]
print(f"Total number of amino acids {total_aa}")
print(f"Total number of frames {data.shape[0]/total_aa}")

##**Capturing the first frame: Here I will loop to only one frame
resnumber_array_initial=np.array([])
contacts_array_initial=np.array([])
counts_array_initial=np.array([])

i=0
while i<total_aa:
    # Convert the string to a NumPy array of integers
    data_array = np.fromstring(data.iloc[i,1], sep=' ', dtype=int)
    # Count the occurrences of each number
    unique_numbers, counts = np.unique(data_array, return_counts=True)
    resnumber_array_initial=np.append(resnumber_array_initial, np.full((1, unique_numbers.size), data.iloc[i,0], dtype=int).flatten())
    contacts_array_initial=np.append(contacts_array_initial, unique_numbers)
    counts_array_initial=np.append(counts_array_initial, counts)
    i+=1



##**Capturing the trajectory: Here I will loop through all the frames

#creating empty numpy arrays to store values
resnumber_array=np.array([])
contacts_array=np.array([])
counts_array=np.array([])

i=0
while i<aggregated_df.shape[0]:
    # Convert the string to a NumPy array of integers
    data_array = np.fromstring(aggregated_df.iloc[i,1], sep=' ', dtype=int)
    # Count the occurrences of each number
    unique_numbers, counts = np.unique(data_array, return_counts=True)
    resnumber_array=np.append(resnumber_array, np.full((1, unique_numbers.size), aggregated_df.iloc[i,0], dtype=int).flatten())
    contacts_array=np.append(contacts_array, unique_numbers)
    counts_array=np.append(counts_array, counts)

    i+=1
#print(aggregated_df.shape[0]) #shape of dataframe
#print(aggregated_df.iloc[0,0],unique_numbers, counts)


# In[29]:


plt.figure(figsize=(30,11),facecolor='white')
plt.subplot(1,2,1)
plt.title("Initial configuration", fontsize=20, fontweight="bold")
plt.scatter(resnumber_array_initial, contacts_array_initial, c=counts_array_initial, cmap='viridis', s=100, edgecolors='k')
# Add colorbar
cbar = plt.colorbar()
cbar.set_label('Number of contacts', fontsize=20, fontweight="bold")
cbar.ax.tick_params(labelsize=20)
plt.xticks(np.arange(1,aggregated_df.shape[0]+1,aggregated_df.shape[0]//10), fontsize=18)
plt.yticks(np.arange(1,aggregated_df.shape[0]+1,aggregated_df.shape[0]//10), fontsize=18)
plt.xlim(0,aggregated_df.shape[0]+1)
plt.ylim(0,aggregated_df.shape[0]+1)
plt.gca().invert_yaxis()
plt.xlabel("Residue Number", fontsize=20, fontweight="bold")
plt.ylabel("Residue Number", fontsize=20, fontweight="bold")
plt.minorticks_on()
plt.subplot(1,2,2)
plt.title("Trajectory Analysis", fontsize=20, fontweight="bold")
plt.scatter(resnumber_array, contacts_array, c=counts_array, cmap='viridis', s=100, edgecolors='k')
# Add colorbar
cbar = plt.colorbar()
cbar.set_label('Number of contacts', fontsize=20, fontweight="bold")
cbar.ax.tick_params(labelsize=20)
plt.xticks(np.arange(1,aggregated_df.shape[0]+1,aggregated_df.shape[0]//10), fontsize=18)
plt.yticks(np.arange(1,aggregated_df.shape[0]+1,aggregated_df.shape[0]//10), fontsize=18)
plt.xlim(0,aggregated_df.shape[0]+1)
plt.ylim(0,aggregated_df.shape[0]+1)
plt.gca().invert_yaxis()
plt.xlabel("Residue Number", fontsize=20, fontweight="bold")
plt.ylabel("Residue Number", fontsize=20, fontweight="bold")
'''plt.axhline(y = 22, color = 'r', linestyle = '-')
plt.axvline(x = 22, color = 'r', linestyle = '-')
plt.axhline(y = 38, color = 'r', linestyle = '-')
plt.axvline(x = 38, color = 'r', linestyle = '-')'''
plt.minorticks_on()

plt.subplots_adjust(left=0.1,
                    bottom=0.1,
                    right=0.9,
                    top=0.9,
                    wspace=0.1,
                    hspace=0.4)

plt.savefig("contact_map-trajectory_analysis.png", dpi=300)
#plt.show()
