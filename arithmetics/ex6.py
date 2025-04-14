# Ex6
# Return the following results for int from user_input 
# 1) The double of "user_input"
# 2) The triple of "user_input"
# 3) The square root of "user_input"

import math

def main():
  user_input = int(input("Type a number: "))
  print(f"The double of {user_input} is {user_input * 2}")
  print(f"The triple of {user_input} is {user_input * 3}")
  print(f"The square root of {user_input} is {round(math.sqrt(user_input), 2)}")
  
main()