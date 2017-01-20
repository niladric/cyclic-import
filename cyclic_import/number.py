#from alphabet import my_alphabet
#import alphabet

def my_number(n):
  return n
  
def import_alphabet():
  from alphabet import __my_alphabet
  return __my_alphabet
  
if __name__ == '__main__':
  niladri = import_alphabet()
  print niladri('A')
#print my_alphabet('A')
#print my_number(4)
