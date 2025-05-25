import ast

def arithmetic_arranger(num_list, is_calculated = False):
    input_list = ast.literal_eval(num_list) # turn the string list to actual list
    plus = "+"
    minus = "-"
    formatted_num_list = [] # will contain a set of formatted sublists for each passed set of arithmetic problem
    arranged_num = ['', '', '', ''] if is_calculated else ['', '', ''] # will hold the 3 or 4 output lines as elements - 4 lines only if the user wants the output of the calculations
    spacing = ' ' * 4 # simply the spacing between the listed arithmetic operations, so they are clear to read in the console

    if len(input_list) > 5: # to hit rule 1
        return "Error: Too many equations have been passed"

    for equation in input_list:
        if plus not in equation and minus not in equation: #to hit rule 2
            return "Error: Accepted opperations are addition or subtraction"

        char = equation.split()
        line_one = char[0]
        operator = char[1]
        line_two = char[2]
        length_a, length_b = len(line_one), len(line_two)
        if length_a > 4 or length_b > 4: # for rule 4
            return "Error: Entered digits cannot be greater than four digits"

        try: # for rule 3
            int(line_one)
            int(line_two)
        except Exception:
            return "Error: Equations can only contain digits and + or -"

        longest = max(length_a, length_b)
        shortest = min(length_a, length_b)
        size_diff = longest - shortest # needed to right justify the numbers below

        if length_a < length_b: # if line one is shorter
            line_one = " " * (size_diff + 2) + line_one
        else: # line two is shorter or equal
            line_two = " " * (size_diff) + line_two
            line_one = " " * 2 + line_one # justify line one 2 additional spaces to account for operator
        line_two = operator + ' ' + line_two
        line_three = "-" * (longest + 2) # create the divider
        formatted_num_list.append([line_one, line_two, line_three])

        if is_calculated:
            result = 0
            if operator == plus:
                result = int(char[0]) + int(char[2])
            elif operator == minus:
                 result = int(char[0]) - int(char[2])
            else:
                return "Operator not recognised"
            line_four = str(result)
            length_c = len(line_four)
            result_diff = longest - length_c
            line_four = " " * (result_diff + 2) + line_four
            formatted_num_list[-1].append(line_four) # adds the line to the most recent list in the list (-1 = last)

    for i, line in enumerate(arranged_num):
        for x, y in enumerate(formatted_num_list):
            if x < len(formatted_num_list) - 1:
                line += y[i] + spacing
            else:
                line += y[i]
        arranged_num[i] = line

    arranged_num_string = ''
    for i, x in enumerate(arranged_num):
        arranged_num_string += x
        if i < len(arranged_num) - 1:
            arranged_num_string += '\n'
    return arranged_num_string


def main():
    print('Welcome to the Freecodecamp challange: Arithmetic calculations \n \nThis python file accepts input in the form of ["digit operator digit", "..."] \nei ["32 + 698", "3801 - 2", "45 + 43", "123 + 49"] \nThe basic mode up hits the rules for the challenge, whilst the advanced introduces additional operators')
    user_math = input("Enter your arithmetic: ")
    to_calculate = input("Would you like the results of the submitted arithmetic shown? Please enter True or False: ")
    user_input = arithmetic_arranger(user_math, to_calculate)
    print(user_input)

main()