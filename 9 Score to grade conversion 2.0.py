#Rewrite the grade program from the previous chapter using
#a function called computegrade that takes a score as its parameter and
#returns a grade as a string.

def computegrade(score):
    if score >1.0:
        print('Error, entered vaule above 1.0')
        quit()
    elif score <0.0:
        print('Error, entered vaule below 0.0')
        quit()
    elif score >= 0.9:
        grade = 'A'
    elif score >= 0.8:
        grade = 'B'
    elif score >= 0.7:
        grade = 'C'
    elif score >= 0.6:
        grade = 'D'
    elif score <0.6:
        grade = 'F'
    else:
        print('Error in score to grade loop')
        quit()
    return grade

print('Enter score between 0.0 to 1.0')
score_string = input()
try:
    score = float(score_string)
except:
    print('Error, please enter numeric vaule between 0.0 and 1.0')
    quit()
grade = computegrade(score)

print('Grade:', grade)