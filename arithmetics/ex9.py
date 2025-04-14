# Ex009
# Type a number and return it's multiplication table

def main():
  user_input = int(input('Type a number: '))
  MAX = 11

  print('-' * 12)
  for i in range(MAX):
    if i == 0:
      continue 

    print(f"{user_input} x {i:2} = {user_input * i}")
  print('-' * 12)

main()