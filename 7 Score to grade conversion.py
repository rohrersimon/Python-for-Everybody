# Write a program to prompt for a score between 0.0 and
# 1.0. If the score is out of range, print an error message. If the score is
#between 0.0 and 1.0, print a grade using the following table:3.11.
#Score      Grade
#>= 0.9     A
#>= 0.8     B
#>= 0.7     C
#>= 0.6     D
#< 0.6      F

print('Enter score between 0.0 to 1.0')
score_string = input()
try:
    score = float(score_string)
except:
    print('Error, please enter numeric vaule between 0.0 and 1.0')
    quit()
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

print('Grade:', grade)