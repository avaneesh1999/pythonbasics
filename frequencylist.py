from collections import Counter
list = ['Mon', 'Tue', 'Wed', 'Mon','Mon','Tue']

# Finding count of each element
list_freq= (Counter(list))

#Printing result of counter
print(list_freq)

# Printing it using loop
for key, value in list_freq.items():
   print(key, " has count ", value)
