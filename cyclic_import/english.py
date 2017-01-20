#from bengali import Bengali

class English(object):
  def __init__(self, learn=None):
    self._learn = learn
    #print self._learn
    #return self._learn
  def learn_english(self, letter):
    self.letter = letter
    return self.letter

	
'''
  def import_bengali(self):
    from bengali import Bengali
    return Bengali.learn_bengali('OO')
'''	
'''
if __name__ == '__main__':
  e = English()
  print e.import_bengali()
  #b('OO')
'''
    
    
