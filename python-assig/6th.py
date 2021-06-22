def catch_unique(list_in):
   # intilize an empty list
   unq_list = []

   # Check for elements
   for x in list_in:
      # check if exists in unq_list
      if x not in unq_list:
         unq_list.append(x)
         # print list
   for x in unq_list:
      print(x)

Alist = ['Red', 'Blue', 'Red', 'Green', 90, 90]
print("Distinct values from the list is")
catch_unique(Alist)
