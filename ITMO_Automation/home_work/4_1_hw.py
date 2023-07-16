class Car:
    def __init__(self, color, type, year):
        self.color = color
        self.type = type
        self.year = year

    def start(self):
        return "автомобиль заведен"
    def end(self):
        return "автомобиль заглушен"
    def years(self, new_year):
        self.years = new_year
        return self.years
    def colors(self, new_color):
        self.colors = new_color
        return self.colors
    def types(self, new_type):
        self.types = new_type
        return self.types
car1 = Car('white', 'petrol', '2023')
print(car1.start())
print(car1.year)
print(car1.color)
print(car1.type)
print(car1.end())
print(car1.years(new_year='2022'))
print(car1.colors(new_color='black'))
print(car1.types(new_type='diesel'))
