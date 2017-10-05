def drawStars():
    x = [10, 1, 9, 2, 8, 3, 7, 4, 6, 5] 
    for i in x:
        print '*' * i
drawStars()
###############Part 2 ########################################
def drawStarsNums():
    y = [4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"]
    for i in y:
        if isinstance(i, int):
            print "*" * i
        elif isinstance(i, str):
            word = len(i)
            letter = i[0].lower()
            print letter * word
drawStarsNums()
        

#############################################################################
