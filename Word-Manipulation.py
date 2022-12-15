
def main():
    
    print("Assignment 7 by Luke Buckner")
    print()
    word_and_phrase_processing()
    print()
    enter_student_grades()
    

def word_and_phrase_processing():
    """prompts the user for a word and then calls word_triangle, passing it the word that was entered"""

    word=input('Enter the word:')
    word_triangle(word)
    print()
    phrase = input("Enter a Phrase : ")
    to_replace = input("Letter to replace? ")
    replace_with = input("Replace it with? ")
    replaced_phrase = replace_letters(phrase, to_replace, replace_with)
    print(f"The new phrase is : {replaced_phrase}")


def word_triangle(word):
    """takes a string input and outputs a word triangle of the word"""
    
    for i in range(0,len(word)):
        
        for j in range(i):
            print(word[j],end='')
            
        print(word[i])
        

def replace_letters(phrase, to_replace, replace_with):
    """find and replaces all letters in the phrase specified by user input with the inputted replacement letter"""
    
    new_str = ""
    
    for i in phrase:
        if i == to_replace:
            new_str += replace_with
        else:
            new_str += i
            
    return new_str


def count_grades(lst):
    """takes a list of grades and returns a list of the number each letter grades in the list"""
    
    grade = [0,0,0,0,0]
    
    for num in lst: 
        if num >= 90 and num <= 100:    
            grade[0] = grade[0]+1     
        elif num >= 80 and num < 90:    
            grade[1] = grade[1]+1    
        elif num >= 70 and num < 80:   
            grade[2]=grade[2]+1    
        elif num >= 60 and num < 70:   
            grade[3] = grade[3]+1     
        elif num >= 0 and num < 60:    
            grade[4]=grade[4]+1
            
    return grade

# the instructinos for this assignment say to copy this function from Lab 8, which we have not gotten to yet,
# so I created this function. If this is not correct, would you mind leaving some feedback on it for
# me? Thank you so much! - Luke

def enter_student_grades():
    """takes user input for a number of grades and grade scores and then calls count_grades"""

    numGrades = int(input("Enter the number of grades: "))    
    lst=[]      
    print("Enter grades: ")
    
    for i in range(numGrades):  
        num = int(input())        
        lst.append(num)
        
    grade = count_grades(lst)     
    letterGrade = ['A','B','C','D','F']
    
    for i in range(5):  
        print("{}:{}".format(letterGrade[i],grade[i]))




        
main()
