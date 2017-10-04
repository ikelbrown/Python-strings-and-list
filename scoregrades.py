import random
def scoreGrades():
    for i in range(0, 10):
        print "Scores and Grades"
        random_num = random.randint(60, 101)
        if random_num >= 60 and random_num < 70:
            print "Score: ", random_num,'; Your grade is D'
        elif random_num >= 70 and random_num < 80:
            print "Score: ", random_num,'; Your grade is C'
        elif random_num >= 80 and random_num < 90:
            print "Score: ", random_num,'; Your grade is B'
        elif random_num >= 90 and random_num < 101:
            print "Score: ", random_num,'; Your grade is A' 
            
        print "End of program. Bye!" 
scoreGrades()




