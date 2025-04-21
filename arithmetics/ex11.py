# Ex011
# Get the wall width and height in meters
# Calculate the area
# and return the amount of paint needed to paint the entire wall
# Consider: for every 2 m2, 1L of paint is needed. 

def main():
  larg_wall = float(input('Wall width (in meters): '))
  heig_wall = float(input('Wall height (in meters): '))
  m2 = larg_wall * heig_wall

  print(f"Your wall has dimensions of {larg_wall}m x {heig_wall}m, with a total area of {m2}m2.")
  print(f"To paint this wall, you'll need {m2 / 2}l of paint.")

main()