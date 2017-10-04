#Type list
l = ['magical unicorns',19,'hello',98.98,'world']
count = 0
new_l = ''
for val in l:
    if isinstance(val, int) or isinstance(val, float):
        count +=val
    elif isinstance(val, str):
        new_l += val

if new_l and count:
    print "The list you entered is of mixed type"
    print "String:", new_l
    print "Count:", count

elif new_l:
    print "The list you entered is of string type"
    print "String:", new_l


    
