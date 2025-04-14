# Ex008
# Input a value in meters and print the result
# by converting to the following measures
# km, hm, dam, dm, cm and mm

def main():
  user_input = float(input('Type a distance in meters: '))

  print(f"{user_input} meters is equivalent to: ")
  print(f"{user_input / 1000}km")
  print(f"{user_input / 100}hm")
  print(f"{user_input / 10}dam")
  
  print(f"{(user_input * 10):.0f}dm")
  print(f"{(user_input * 100):.0f}cm")
  print(f"{(user_input * 1000):.0f}mm")

main()