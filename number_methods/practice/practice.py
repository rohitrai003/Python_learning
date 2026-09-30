# Program to check the prime numbers

def is_prime(num):
  if num <=1:
    return False
  for i in range(2,num):
    if num%i == 0:
      return False
  return True


# Check the max of 3 numbers
def max_of_three(a, b, c):
    return max(a, b, c)

print(max_of_three(3, 7, 5))  # Output: 7