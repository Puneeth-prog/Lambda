#Example 1
data=[10,501,22,37,100,999,87,351]  #Takes the list
result = filter(lambda x:x>4,data) #Filters the given list, filters the number which are less than 4
print(list(result))  #Prints the numbers which are greater than 4

#output, there will be no change in output because all the numbers are greater than 4-[10,501,22137,100,999,87,351]

#Example 2
data=[1,2,3,4,5,6,7]  #Takes the list
result = filter(lambda x:x>4,data) #Filters the given list, filters the number which are less than 4
print(list(result))  #Prints the numbers which are greater than 4
#output, [5,6,7] all the numbers greater than 4