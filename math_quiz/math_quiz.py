import random

def Limitfunc(v_min, v_max):                  #create random integer ranging from v_min to v_max.
    """
    Random integer.
    """
    return random.randint(v_min, v_max)       #returns a random variable between the specified integers.


def Operatorfunc():                           #picks a random arithmetic operation.
    """"
    picks a random arithmetic operation.
    """
    return random.choice(['+', '-', '*'])     #returns operator as string.


def Mathfunc(number1, number2, operator):     #function for creating problem and solving it.
    """
    function for creating problem and solving it.
    """
    q = f"{number1} {operator} {number2}"             #displays the equation.
    if operator == '+': answer = number1 + number2    #addition operation.
    elif operator == '-': answer = number1 - number2  #subtraction operation.
    else: answer = number1 * number2                  #multiplication operation.
    return q, answer                                  #returns two values.

def quiz():                                           #function for the questions.
    """
    function for the questions.
    """
    mark = 0                                          #displays your score.
    number_of_questions = 3                           #displays number of questions.

    print("Welcome to the Math Quiz Game!")           #displays welcome message.
    print("You will be presented with math problems, and you need to provide the correct answers.") # Displys message.

    for _ in range(number_of_questions):
        number1 = Limitfunc(1, 10); number2 = Limitfunc(1, 5); Operator = Operatorfunc() #assigning number and operation.

        prob, ans = Mathfunc(number1, number2, Operator)  #question represented as string and the corect answer.
        try:                                              #check for invalid inputs.
            print(f"\nQuestion: {prob}")                  #displays problem.
            useranswer = input("Your Answer: ")           #asks user to give input.
            useranswer = int(useranswer)                  #converts the previous input from string to integer.
            
        except ValueError:                                #check for invalid inputs.
           print("Invalid input.Try entering a number")   #Error Message.
           break                                          #Exits in case of invalid input.

        if useranswer == ans:                             #checks answer.
            print("Correct! You earned a point.")         #if correct executes this line
            mark += 1                                     #get +1 mark
        else:
            print(f"Wrong answer. The correct answer is {ans}.")       #if wrong no mark and displays this message

    print(f"\nGame over! Your score is: {mark}/{number_of_questions}") #game over message.

if __name__ == "__main__": #checks and run the following function.
    quiz()
