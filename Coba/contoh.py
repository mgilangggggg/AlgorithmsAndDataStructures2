a = {1, 2, 3, 4, 5}
b = {4, 5, 6, 7, 8}
print("Himpunan A: ", a)
print("Himpunan B: ", b)
union = a.union(b) # a | b
print("Union : ",union)
intersect = a.intersect(b) # a & b
print("Intersection : ", intersect)
diff = a.difference(b) # a - b
print("Difference : ", diff)
syndiff=a.symmetric_difference(b) # a ^ b
print("Symmetric Diff : ",syndiff)