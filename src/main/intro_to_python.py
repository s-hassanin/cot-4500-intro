#This code is written by: Salma Hassanin

import numpy as np



array = np.zeros((3, 3), dtype=int)


for i in range (3):
  for j in range (3):
    if i == j:
      array[i][j] = 1

for a in array:
    print (*a)

print("\n")
# ------------------------------------
for i in range (3):
  for j in range (3):
    if i != j:
      array[i][j] = 3 + array[i][j]
for a in array:
    print (*a)

print("\n")
# ------------------------------------


array =np.delete(array, 2, 1)
for a in array:
    print (*a)
