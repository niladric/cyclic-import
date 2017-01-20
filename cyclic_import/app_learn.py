from english import English
from bengali import Bengali

b = Bengali()
e = English(b.learn_bengali)
print e

if e._learn:
  print e._learn('00')
  

#e1 = English()
#b1 = Bengali(e1)
#print e.learn_bengali('00')
#print b1.learn_english('A')

#print e.learn_english('A')
#print b.learn_bengali('00')
