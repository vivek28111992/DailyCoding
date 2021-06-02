# [-9, -2, 0, 2, 3]

def square(arr):
  sq_arr = [i * i for i in arr]
  sq_arr.sort()
  return sq_arr

print(square([-9, -2, 0, 2, 3]))