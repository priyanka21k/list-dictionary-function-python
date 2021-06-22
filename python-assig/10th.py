def merge(ini_dictionary1,ini_dictionary2):
    dict_3=ini_dictionary1+ini_dictionary2
    return dict_3

from collections import Counter

ini_dictionary1 = Counter({'Monday':2, 'Tuesday':10, 'Sunday':20})
ini_dictionary2 = Counter({'Monday':2, 'Wesnday':2, 'Sunday':5})
  
print ("1st dictionary: ", str(ini_dictionary1))
print ("2nd dictionary: ", str(ini_dictionary2))

final_dictionary = merge(ini_dictionary1,ini_dictionary2)  
print ("Final dictionary:",str(final_dictionary))
