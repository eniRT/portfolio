class Shape:
  def what_am_i(self):
    print("I am a shape")
 
class Rectangle(Shape):
    def __init__(self, w, l):
        self.width = w
        self.length = l
    
    def calculate_perimeter(self):
        return (2 * self.length + 2 * self.width)
 
class Square(Shape):
    def __init__(self, s1):
        self.s1 = s1
    
    def calculate_perimeter(self):
        return 4*self.s1
    
    def change_size(self, num):
      num = int(num)
      self.s1 += num
 
rect = Rectangle(25, 25)
square = Square(5)
 
rect.what_am_i()
square.what_am_i()