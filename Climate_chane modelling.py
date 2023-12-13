#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Gayatri_Pardeshi
import random
import matplotlib.pyplot as plt

# Constants
GRID_SIZE = 100
NUM_STEPS = 1000

# Initialize temperature grid
temperature_grid = [[0 for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
temperature_grid[GRID_SIZE // 2][GRID_SIZE // 2] = 1  # Initial heat source at the center

# Random walk function
def random_walk(x, y):
    direction = random.choice(['up', 'down', 'left', 'right'])
    if direction == 'up' and y > 0:
        y -= 1
    elif direction == 'down' and y < GRID_SIZE - 1:
        y += 1
    elif direction == 'left' and x > 0:
        x -= 1
    elif direction == 'right' and x < GRID_SIZE - 1:
        x += 1
    return x, y

# Simulate climate change using random walks
for _ in range(NUM_STEPS):
    x, y = random_walk(GRID_SIZE // 2, GRID_SIZE // 2)
    temperature_grid[y][x] += 1

# Visualize temperature grid
plt.imshow(temperature_grid, cmap='hot', interpolation='nearest')
plt.colorbar()
plt.title("Climate Change Simulation")
plt.xlabel("X")
plt.ylabel("Y")
plt.show()


# In[ ]:




