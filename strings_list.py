#Find and Replace
'''words = "It's thanksgiving day. It's my birthday, too!"
print words.find('day')

words = "It's Thanksgiving day. It's my birthday, too!"
new_str = words.replace("day", 'month', 18)
print new_str'''


#Min and max
'''x = [2,54,-2,7,12,98]
print min([2,54,-2,7,12,98])
print max([2,54,-2,7,12,98])'''

#First and Last
'''x = ["hello",2,54,-2,7,12,98,"world"]
print x[0], x[-1]
new_list = x[0], x[-1]
print new_list'''

#New List
'''x = [19,2,54,-2,7,12,98,32,10,-3,6]
sorted([19,2,54,-2,7,12,98,32,10,-3,6])
print sorted([19,2,54,-2,7,12,98,32,10,-3,6])'''

def split_list(a_list):
    half = len(a_list)/2
    return a_list[:half], a_list[half:]

'''A = [-3, -2, 2, 6, 7, 10, 12, 19, 32, 54, 98]
B, C = split_list(A)
print split_list(A)'''

a = [-3, -2, 2, 6, 7]
b = [10, 12, 19, 32, 54, 98]
print a, b
b.insert(0, a)
print b
