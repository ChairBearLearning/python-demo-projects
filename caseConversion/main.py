def convert_to_snake_case(pascal_or_camel_cased_string):
    snake_cased_char_list = []
    for char in pascal_or_camel_cased_string:
        if char.isupper():
           converted_character = "_" + char.lower()
           snake_cased_char_list.append(converted_character)
        else:
           snake_cased_char_list.append(char)
    snake_cased_string = ''.join(snake_cased_char_list)
    clean_snake_cased_string = snake_cased_string.strip('_')
    return clean_snake_cased_string

# same method above changed to list comprehension method
def convert_to_snake_case(pascal_or_camel_cased_string):
    snake_cased_char_list = ["_" + char.lower() if char.isupper() else char for char in pascal_or_camel_cased_string ]
    # example = [letter + 's' for letter in myListOfChar]
    # The above uses the variable letter to iterate over myListOfChar.
    # Each element of the resulting list assigned to 'example' is obtained by
    # evaluating the expression letter * 2 at the current iteration
    # list comprehension even accepts conditional statements
    # ei. [letter + 's' for letter in myListOfChar if letter is 'a']
    # if statement at the end, unless an if/else then it goes at the beginning
    # ei. [letter + 's' if letter is 'a' else 't' for letter in myListOfChar ]
    # return ''.join(words_list).upper() the .upper() method is chained to the .join(x),
    # and so .upper() is called on the result of the .join() call
    # same goes fot strip
    # ''.join(snake_cased_char_list).strip('_')
    return ''.join(snake_cased_char_list).strip('_')

def main():
    user_string = input("Enter a pascal or camel cased string: ")
    converted_string = convert_to_snake_case(user_string)
    print('Converted: ' + converted_string)

main()