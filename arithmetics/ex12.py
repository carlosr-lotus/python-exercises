# Ex012
# Return the final price of a product with a discount of 5%

def main():
  price = float(input('What is the price of the product? R$'))
  print(f"The product that costs R${price:.2f}, and now applied with the 5% discount is: R${price - (price * 0.05):.2f}")

main()