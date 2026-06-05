#list of 20 no given  by user ask the user to input any other no . remove all the duplicate of this no from the list
# list of 20 numbers

numbers = []
# input of numbers from user

for i in range(5):
    num = int(input("Enter number : ")) 
    numbers.append(num)

# input of number to remove duplicates

numToRemove = int(input("Enter a number to remove duplicates: "))

# check if the number to remove is in the list

if(numToRemove not in numbers):
    print("Number not found in the list.") 

# remove duplicates of the number from the list

uniqueNumbers = []
for num in numbers:
    if (num != numToRemove and num not in uniqueNumbers):
        uniqueNumbers.append(num)

# display the list after removing duplicates elements

print("Original list: ", numbers) 
# add the number to remove to the unique numbers list
 
uniqueNumbers.append(numToRemove)
print("List after removing duplicates: ",uniqueNumbers)
