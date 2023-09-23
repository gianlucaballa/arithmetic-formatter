#define the function
def arithmetic_arranger(list, show_answer):

    #return result if the second argument of the function is True
    if show_answer==True:

        #output of the first line
        for string in list:
            new_string = string.split()
            number1 = new_string[0]
            operator = new_string[1]
            number2 = new_string[2]
            if operator == '+':
                sum = int(number1) + int(number2)
            else:
                sum = int(number1) - int(number2)
            len1 = len(number1)
            len2 = len(number2)
            max_width = max(len1, len2)
            print(' ', number1.rjust(max_width), end='    ')
        print('')

        #output of the second line
        for string in list:
            new_string = string.split()
            number1 = new_string[0]
            operator = new_string[1]
            number2 = new_string[2]
            if operator == '+':
                sum = int(number1) + int(number2)
            else:
                sum = int(number1) - int(number2)
            len1 = len(number1)
            len2 = len(number2)
            max_width = max(len1, len2)
            print(operator, (str(abs(int(number2)))).rjust(max_width), end='    ' )
        print('')

        #output of the third line (dashes)
        for string in list:
            new_string = string.split()
            number1 = new_string[0]
            operator = new_string[1]
            number2 = new_string[2]
            if operator == '+':
                sum = int(number1) + int(number2)
            else:
                sum = int(number1) - int(number2)
            len1 = len(number1)
            len2 = len(number2)
            max_width = max(len1, len2)
            dashes = '-'*max_width+'--'
            print(dashes, end='    ')
        print('')

        #output of the last line (result)
        for string in list:
            new_string = string.split()
            number1 = new_string[0]
            operator = new_string[1]
            number2 = new_string[2]
            if operator == '+':
                sum = int(number1) + int(number2)
            else:
                sum = int(number1) - int(number2)
            len1 = len(number1)
            len2 = len(number2)
            lensum = len(str(sum))
            max_width = max(len1, len2, lensum)
            if max_width <= 4:
                print(' ', str(sum).rjust(max_width), end='    ')
            else:
                print('', str(sum).rjust(max_width), end='    ')

    #do not return result if the second argument of the function is False
    else:

        #output of the first line
        for string in list:
            new_string = string.split()
            number1 = new_string[0]
            operator = new_string[1]
            number2 = new_string[2]
            len1 = len(number1)
            len2 = len(number2)
            max_width = max(len1, len2)
            print(' ', number1.rjust(max_width), end='    ')
        print('')

        #output of the second line
        for string in list:
            new_string = string.split()
            number1 = new_string[0]
            operator = new_string[1]
            number2 = new_string[2]
            len1 = len(number1)
            len2 = len(number2)
            max_width = max(len1, len2)
            print(operator, (str(abs(int(number2)))).rjust(max_width), end='    ' )
        print('')

        #output of the third line (dashes)
        for string in list:
            new_string = string.split()
            number1 = new_string[0]
            operator = new_string[1]
            number2 = new_string[2]
            len1 = len(number1)
            len2 = len(number2)
            max_width = max(len1, len2)
            dashes = '-'*max_width+'--'
            print(dashes, end='    ')

#insert input
list = []
while True:
    problem = input('Insert an arithmetic problem with two natural numbers (4 digits max each) as "a + b" or "a - b", or type stop: ')
    if problem.lower() == 'stop':
        break
    try:
        num1, operator, num2 = problem.split()
        num1 = int(num1)
        num2 = int(num2)
    except:
        print ('Error: Please, follow the instructions above using the right spaces in between numbers and the operator.')
        quit()
    if len(str(num1)) > 4 or len(str(num2)) > 4:
        print('Error: Numbers cannot be more than four digits.')
        quit()
    elif operator != '+' and operator != '-':
        print('Error: Operator must be "+" or "-".')
        quit()
    else:
        list.append(problem)
        if len(list) > 5:
            print('Error: Too many problems.')
            quit()
        else:
            print(list)

#decide if the second argument of the function is True or False
question = input('Do you want to visualise the result? y/n: ')
show_answer = question == 'y'

#call the function
arithmetic_arranger(list, show_answer)
