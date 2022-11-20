class Cookie:
    def __init__(self, color) -> None:
        self.color = color
    
    def get_color(self):
        return self.color

    def set_color(self,color):
        self.color = color


cookie_one = Cookie("green")

cookie_two = Cookie("blue")

print("Cookie one is {}".format(cookie_one.get_color()))
print("Cookie two is {}".format(cookie_two.get_color()))


cookie_one.set_color("red")

print("Cookie one is {}".format(cookie_one.get_color()))
print("Cookie two is {}".format(cookie_two.get_color()))
