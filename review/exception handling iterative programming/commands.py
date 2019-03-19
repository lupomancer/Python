import sys


def quit():
  sys.exit()


def frog():
  print('ribbit ribbit ribbit')
  #! has an anooying "returned: None" message
  return


def get_int(prompt='Enter an integer'):

  while True:
    # Activity 6
    n = input('\n%s: ' % prompt)
    return int(n)


def get_range():
  low = get_int('Enter a lower bound for the range')
  high = get_int('Enter an upper bound for the range')

  while True:
    try:
      prompt = 'Enter a value that is in range {} - {}'.format(low, high)
      value = get_int(prompt)
      check_range(low, high, value)
      break
    except IndexError:
      print('Value %i is not in range.' % value)
  return (value, low, high)


def check_range(low, high, value):
  if (value < low) or (value > high):
      #TODO: actually make the error return something
    raise IndexError


def get_path():
    #! doesn't actually do anything
  pass


def find_file(filename, pathname):
    #! not giving a filename and path breaks this
    #! can't actually take a filename
  pass
