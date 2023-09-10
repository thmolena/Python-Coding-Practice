list = []
number_of_elements = input("How many elements do you want to put in a list?")
for i in range(int(number_of_elements)):
  i = input("Enter an element")
  list.append(i)
print(list)
a = input("Which element do you want to see (starting from 1 to nth element): ")
print(list[int(a)-1])
