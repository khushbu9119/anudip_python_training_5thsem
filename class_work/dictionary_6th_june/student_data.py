#to create a dictionay to store student data
student_data = { "std101":"akash",'std102':"sneha", 'std103':"rohit", 'std104':"priya"}
#to display the data
print("student data :")
print(student_data)
print("----------------------")
#to update record fo student whose roll no is std102
student_data['std102'] = "khushi"
#to update record fo student whose roll no is std105
student_data['std105'] = "rakesh"
print("updated student data :")
print(student_data)
print("----------------------")
for x in student_data:
    print(x, ":", student_data[x])