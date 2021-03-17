class Rectangle:
  def __init__(self, width, height, name="Rectangle"):
    self.width = width
    self.height = height
    self.name = "Rectangle"
  def __str__(self):
    output = str(self.name)
    if output == "Rectangle":
      output += "(width=" + str(self.width) + ", height=" + str(self.height) + ")"
    else:
      output += "(side=" + str(self.width) + ")"
    return(output)
  def set_width(self, width):
    self.width = width
  def set_height(self, height):
    self.height = height
  def get_area(self):
    area = self.width * self.height
    return(area)
  def get_perimeter(self):
    perimeter = 2 * self.width + 2 * self.height
    return(perimeter)
  def get_diagonal(self):
    diagonal = (self.width ** 2 + self.height ** 2) ** .5
    return(diagonal)
  def get_picture(self):
    output = ""
    if self.width > 50 or self.height > 50:
      output = "Too big for picture."
    else:
      counter = 0
      while counter < self.height:
        counter1 = 0
        while counter1 < self.width:
          output += "*"
          counter1 += 1
        output += "\n"
        counter += 1
    return(output)
  def get_amount_inside(self, name):
    name = name
    width1 = self.width
    height1 = self.height
    width2 = name.width
    height2 = name.height
    widthQuo = width1 / width2
    widthQuo = int(widthQuo)
    heightQuo = height1 / height2
    heightQuo = int(heightQuo)
    output = heightQuo * widthQuo
    return(output)
  
class Square(Rectangle):
  def __init__(self, width, name="Square"):
    self.width = width
    self.height = width
    self.name = "Square"
  def __str__(self):
    return(Rectangle.__str__(self))
  def set_width(self, width):
    Rectangle.set_width(self, width)
    Rectangle.set_height(self, width)
  def set_height(self, width):
    Rectangle.set_width(self, width)
    Rectangle.set_height(self, width)
  def set_side(self, width):
    Rectangle.set_width(self, width)
    Rectangle.set_height(self, width)
  def get_area(self):
    return(Rectangle.get_area(self))
  def get_perimeter(self):
    return(Rectangle.get_perimeter(self))
  def get_diagonal(self):
    return(Rectangle.get_diagonal(self))
  def get_picture(self):
    return(Rectangle.get_picture(self))
  def get_amount_inside(self, name):
    name = name
    return(Rectangle.get_amount_inside(self, name))