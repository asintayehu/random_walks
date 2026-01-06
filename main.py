# Example implementation of random walks

import random
import matplotlib.pyplot as plt
position = 0
walk = [position]
steps = 30
for _ in range(steps):
    step = 1 if random.randint(0,1) else -1
    position += step
    walk.append(position)

print(walk)
