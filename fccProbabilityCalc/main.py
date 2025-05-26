import random
import copy

class Hat:
    # **kwargs in python is used as a shorthand for any number of arguments
    # it can be used in any func to accept n of named arguments
    # the result is a dictionary: {'a': 1, 'b': 2, 'c': 3}
    # hat = Hat(red=4, blue=3)
    # kwargs = {'red': 4, 'blue': 3}
    def __init__(self, **kwargs):
        self.contents = [] # will store the string list of balls
        for color, count in kwargs.items():
            self.contents.extend([color] * count)
            # adds number of that colour to the hat
            # ei 'red': 4 -> [color] * count => ['red', 'red', 'red', 'red']
            # extend adds these 'red' strings to the contents list

    def draw(self, num_balls_drawn): # randomly draws x num (num_balls_drawn) of balls from the hat
        if num_balls_drawn >= len(self.contents): # check you're not trying to remove more (or equal to) balls than what the hat holds
            drawn = self.contents.copy() # if you are just return a copy of the hat. Copy is used instead of the original list, as we can mod that later
            self.contents.clear() # empty the hat now of all items as they've been removed
            return drawn
        drawn = random.sample(self.contents, num_balls_drawn) # however, if you pick a number suitable, then remove those without replacing them in the hat
        for ball in drawn:
            self.contents.remove(ball)
        return drawn


#note not part of the Class Hat
def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    success_count = 0

    for _ in range(num_experiments):
        # make a copy of the hat so we don't mutate the original
        # this is important for when doing multiple tests with one hat, so you don't have a differnt hat at the start of each one. This is different to doing more tests on one hat,
        hat_copy = copy.deepcopy(hat) # deepcopy recursively copies everything inside the object (ei nested lists, dictionaries, ect)

        # draw balls
        drawn_balls = hat_copy.draw(num_balls_drawn)

        # count the balls drawn
        # ei you drew drawn_balls = ['red', 'green', 'red', 'blue']
        # loop will loop over each ball in the drawn_balls list
        # drawn_counts.get(ball, 0) checks if the color already exists in the drawn_counts dictionary
        # if true add 1 to the count of the key, else return 0
        drawn_counts = {}
        for ball in drawn_balls:
            drawn_counts[ball] = drawn_counts.get(ball, 0) + 1

        # check if the drawn balls satisfy the expected balls condition
        success = True
        for color, count in expected_balls.items():
            if drawn_counts.get(color, 0) < count:
                success = False
                break

        if success:
            success_count += 1

    return success_count / num_experiments

#def parse_hat_input(input_str):
#    color_dict = {}
#    parts = input_str.split(',')
#    for part in parts:
#        if '=' in part:
#            color, count = part.strip().split('=')
#            color_dict[color.strip()] = int(count.strip())
#    return color_dict
def parse_input_dict(input_str):
    result = {}
    parts = input_str.split(',')
    for part in parts:
        if '=' in part:
            key, value = part.strip().split('=')
            result[key.strip()] = int(value.strip())
    return result

def main():
    print('Welcome to the Freecodecamp challange: Probability calculations \n')
    user_hat_question = input("Enter colors and amounts to generate your hat(e.g. blue=5, red=4, green=2): ")
    user_hat_colours =  parse_input_dict(user_hat_question)
    hat = Hat(**user_hat_colours)

    expected_balls_question = input("Enter expected balls(e.g. blue=5, red=4, green=2): ")
    expected_balls = parse_input_dict(expected_balls_question)

    num_balls_drawn = int(input("How many balls do you want to draw from your hat? "))
    num_experiments = int(input("How many experiments would you like to run on your hat? "))

    probability = experiment(hat, expected_balls, num_balls_drawn, num_experiments)
    print("Hat contents: ", hat.contents) # comma instead of + as can only concatenate str (not "list") to str
    print('Estimated probability: ', probability)

main()