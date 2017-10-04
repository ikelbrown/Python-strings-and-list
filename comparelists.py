#list_one = [1,2,5,6,2]
#list_two = [1,2,5,6,2]
#list_one = [1,2,5,6,5]
#list_two = [1,2,5,6,5,3]
#list_one = [1,2,5,6,5,16]
#list_two = [1,2,5,6,5]
list_one = ['celery','carrots','bread','milk']
list_two = ['celery','carrots','bread','cream']
for i in list_two:
     if i not in list_one:
            print "The list are not the same"
for idx in list_two:
    if idx in list_one:
        print "The list are the same"

#First way I tried to solve it
#list_one = [1,2,5,6,2]
#list_two = [1,2,5,6,2]
#list_one = [1,2,5,6,5]
#list_two = [1,2,5,6,5,3]
list_one = [1,2,5,6,5,16]
#list_two = [1,2,5,6,5]
#list_one = ['celery','carrots','bread','milk']
list_two = ['celery','carrots','bread','cream']
for element in list_two:
    for idx in list_two:
        if element not in list_one:
            print "The list are not the same"
        else:
            print "The list are the same"      