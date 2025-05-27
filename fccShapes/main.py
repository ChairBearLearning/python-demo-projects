class Rectangle: # our rectangle class
    def __init__(self, width, height): # constructor method that initialises a Rectangle object with 2 attr - width and height
        self.width = width
        self.height = height

    def set_width(self, width): # this allows us to change the width of the rectangle after instantiation
        self.width = width

    def set_height(self, height): # similar as above but with height
        self.height = height

    def get_area(self): # returns the area of the rectangle
        return self.width * self.height

    def get_perimeter(self): # returns the perimeter of the rec
        return 2 * self.width + 2 * self.height

    def get_diagonal(self): # this is the pythagorean theorem for the diagonal length of the rectangle
        return (self.width ** 2 + self.height ** 2) ** 0.5

    def get_picture(self): # draws shape with astrisks
        if self.width > 50 or self.height > 50: # checks if the rec is too big to be drawn otherwise create rectangle with * symbols
            return "Too big for picture."
        picture = ""
        for _ in range(self.height): # repeats a line of * for the hieght of the rec and each line has a num of * equal to the width
            picture += "*" * self.width + "\n"
        return picture

    def get_amount_inside(self, shape):
        # check how many times the other shape fits in, by width and height (// is int division)
        return (self.width // shape.width) * (self.height // shape.height)

    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"


class Square(Rectangle): # creates a new class Square that inherits (extends) all prop and methods of Rectangle class
    def __init__(self, side):
        super().__init__(side, side) #super called to call Rectangles constructor - squares takes only one side length as squares are equal side length. Passes this to the Rec constructor

    def set_side(self, side): # set both as side as squares are eqaul
        self.width = side
        self.height = side

    def set_width(self, width):
        self.set_side(width)

    def set_height(self, height):
        self.set_side(height)

    def __str__(self):
        return f"Square(side={self.width})"
