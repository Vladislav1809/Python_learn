class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f"{self.name} is going")

    def stop(self):
        print(f"{self.name} is stopping")

    def turn(self, direction):
        print(f"{self.name} is turning to the {direction}")

    def show_speed(self):
        print(f"Current speed: {self.speed}")


class TownCar(Car):
    def show_speed(self):
        super().show_speed()
        if self.speed > 60:
            print('Your speed is more than max')


class SportCar(Car):
    def max_speed(self):
        print('your max speed is 300 km/h')


class WorkCar(Car):
    def show_speed(self):
        print(f'current speed = {self.speed}')
        if self.speed > 40:
            print('Attention, your speed is more than limit')


class PoliceCar(Car):
    def this_is_police(self):
        if self.is_police is True:
            print('This is police car')
        else:
            print('This is not police car')


my_car = SportCar(300, 'black', 'Ferrari', False)
print(my_car.name)
print(my_car.speed)
print(my_car.color)
my_car.max_speed()

friend_car = TownCar(80, 'green', 'Audi', False)
print(friend_car.name)
friend_car.show_speed()

police = PoliceCar(70, 'white', 'BMW', True)
police.this_is_police()

work_car = WorkCar(40, 'yellow', 'Renault', False)
work_car.show_speed()

