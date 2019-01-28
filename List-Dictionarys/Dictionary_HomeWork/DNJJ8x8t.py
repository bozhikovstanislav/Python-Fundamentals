#4
input_data = input()
dict_ = {}


while not input_data == 'end':
   key, value = input_data.split(' = ')

   try:
       value = int(value)
       dict_[key] = int(value)
   except:
       if value in dict_.keys():
           dict_[key] = dict_[value]

   input_data = input()

for key, value in dict_.items():
   print(f'{key} === {value}')