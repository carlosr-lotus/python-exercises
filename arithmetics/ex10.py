# Ex010
# Get an amount of money in BRL from user
# and return it converted to USD

def main():
  user_input = float(input('Your amount in BRL: R$'))
  print(f"With R${user_input:.2f}, you can buy US${(user_input / 5.87):.2f}")

main()