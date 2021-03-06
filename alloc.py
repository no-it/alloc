import random
import sys

def preparenames():
  try:
    names = [];
    with open('girls.dat', 'r') as stream:
      for line in stream:
        name = line.strip()
        if len(name) != 0:
          names.append(name)
    return names
  except IOError:
    sys.stderr.write("Oh CRAP! The file 'girls.dat' was not found.")
    return None

def main():
  print('Please wait while preparing data...')
  names = preparenames()
  if names != None:
    if len(names) == 0:
      sys.stderr.write("Sorry, but... Seems that you don't have a girlfriend.")
    else:
      nextIndex = random.randint(0, len(names) - 1)
      print("Congrats! %s is now your girlfriend. Ask her out!" % names[nextIndex])
      
if __name__ == '__main__':
  main()
