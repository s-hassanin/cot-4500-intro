import numpy as np

# Print a specific 3x3 matrix where a cell is 1 if i == j, else 0
# 2. Print the 3x3 matrix from #1 and then add 3 to every cell where i ≠j
# 3. Print the 3x3 matrix from #2 as a 3x2 by deleting the last column from the matrix created


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


array =np.delete(array, 0, 1)
for a in array:
    print (*a)
