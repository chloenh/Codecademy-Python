# Create a function called double_list 
# that takes a single argument x (which will be a list) 
# and multiplies each element by 2 and returns that list.

n = [3, 5, 7]

def double_list(x):
  for i in range(0, len(x)):
    x[i] = x[i] * 2
  return x

print double_list(n)

