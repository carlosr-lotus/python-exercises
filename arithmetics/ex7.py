# Ex007
# Get two grades and return the median value

def main():
  n1 = float(input('Type first grade: '))
  n2 = float(input('Type second grade: '))

  print(f'The median grade is: {round((n1 + n2) / 2, 1)}')

main()