dict_1 = {
  "Roll_No1": 76.00,
  "Roll_No2": 45.00,
  "Roll_No3": 58.00,
  "Roll_No4": 98.00
}
print("First Semester marks: \n",dict_1)

dict_2 = {
  "Roll_No1": 65.00,
  "Roll_No2": 75.00,
  "Roll_No3": 48.00,
  "Roll_No4": 90.00
}
print("Second Semester marks: \n",dict_2)

dict_3={}
for value in dict_2:
    if value in dict_1:
        sum = dict_1[value] + dict_2[value]
        dict_3[value] = sum/2 
print("Average marks of both semesters: \n",dict_3)
