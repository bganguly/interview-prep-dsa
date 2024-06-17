# write some python recursive functions

#  print first k numbers
def generate_linear_recursive(k):
  if(k > 1):
    result = 1 + generate_linear_recursive(k - 1)
  else:
    result = 1
    
  return result

# generate_linear_recursive(6)  

#  print sequence of 1,2,3,.. k numbers
def generate_linear_sequence(k):
  for x in range (1, k+1):
    print(generate_linear_recursive(x))
  

# generate_linear_sequence(6)  

#  print kth fibonacci numbers
def generate_fibonacci_recursive(k):
  if k == 1:
    result= 0
  elif k ==2:
    result = 1
  else:
    result = generate_fibonacci_recursive(k-2) + generate_fibonacci_recursive(k - 1)
  
  return result

# print(generate_fibonacci_recursive(6)) 

#  print sequence of k fibonacci numbers
def generate_fibonacci_sequence(k):
  for x in range (1, k+1):
    print(generate_fibonacci_recursive(x))
  

# generate_fibonacci_sequence(6)  