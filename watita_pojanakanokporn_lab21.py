
# main function
def main():
    
    grade1 = float(input('Please enter score: '))
    printLetterGrade(grade1)
    grade2 = float(input('Please enter score: '))
    printLetterGrade(grade2)
    grade3 = float(input('Please enter score: '))
    printLetterGrade(grade3)
    grade4 = float(input('Please enter score: '))
    printLetterGrade(grade4)
    grade5 = float(input('Please enter score: '))
    printLetterGrade(grade5)

    totalGrade = averageGrade(grade1, grade2, grade3, grade4, grade5)
    
    print('\nYour average grade is', format(totalGrade, '.2f'),'%.') 

def averageGrade(a, b, c, d, e):
    return (a + b + c + d + e) / 5

def printLetterGrade(numGrade):
    
    if numGrade >= 90:
        print("that is an A\n")
    elif numGrade >= 80:
        print("That is a B\n")
    elif numGrade >= 70:
        print("That is a C\n")
    elif numGrade >= 60:
        print("That is a D\n")
    else:
        print("That is an F\n")
# call to main function
main()
    