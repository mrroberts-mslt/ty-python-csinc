#copy this code to replit.com
#list examples
numbers = [1,2,3,4,5]
letters = ['a','e','i','o','u']
names = ['John', 'Jacob', 'Ann']
pairs = [[1,2],[3,4],[5,6]]

# add a item to a list
numbers.append('a')
print(numbers)
numbers.insert(2, 'i')

#challenge 1 add a name to the names list

# index of first occurrence1
li = ['a', 'b', 'c', 'b']
print(li.index('b'))     
# number of occurrences2
print(li.count('b')) 

#challenge 2 count and find fisrst occurence in the list called letters


# remove first occurrence
li.remove('b')    
print(li)

#challenge 3 remove 'o' from letters list


# reverse the list *in place*
li = [5, 2, 6, 8]
li.reverse()    
print(li)

# challenge 4 reverse the list numbers

# sort the list *in place*
li.sort()       
print(li)

# challenge 5 reverse the list names
