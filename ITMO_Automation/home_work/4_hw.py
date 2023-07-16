class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def square(self):
        return self.width * self.height
    def len(self):
        return (self.width + self.height) * 2
r1 = Rectangle( 20, 30)
print(r1.square())
print(r1.len())
r2 = Rectangle( 10, 10)
print(r2.square())
print(r2.len())
r3 = Rectangle( 20, 20)
print(r3.square())
print(r3.len())

class Math:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def addition(self):
        return self.a + self.b
    def multiplication(self):
        return self.a * self.b
    def division(self):
        return self.b / self.a
    def subtraction(self):
        return self.b - self.a
c = Math( 10, 12)
print(c.addition())
print(c.multiplication())
print(c.division())
print(c.subtraction())

class Button:
    def __init__(self, text, type, loc):
        self.text = text
        self.type = type
        self.loc = loc

    def click(self):
        return "Клик по кнопке {}".format(self.text)

Button1 = Button('Text Box', 'button', ' ')
print(Button1.text)
print(Button1.click())
Button2 = Button('Check Box', 'button', ' ')
print(Button2.text)
print(Button2.click())
Button3 = Button('Radio Button', 'button', ' ')
print(Button3.text)
print(Button3.click())
Button4 = Button('Web Tables', 'button', ' ')
print(Button4.text)
print(Button4.click())
Button5 = Button('Buttons', 'button', ' ')
print(Button5.text)
print(Button5.click())
Button6 = Button('Links', 'button', ' ')
print(Button6.text)
print(Button6.click())
Button7 = Button('Broken Links-Images', 'button', ' ')
print(Button7.text)
print(Button7.click())
Button8 = Button('Upload and Download', 'button', ' ')
print(Button8.text)
print(Button8.click())
Button9 = Button('Dynamic Properties', 'button', ' ')
print(Button9.text)
print(Button9.click())







