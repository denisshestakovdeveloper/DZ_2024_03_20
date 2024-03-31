AVERAGE_FUEL_RATE = 1.78 #л на 50км

#класс Машина

#Расход топлива на один километр

class Car:
    def __init__(self):
        self._speed = 0
        self._fuelTank = 0

    def getSpeed(self):
        return self._speed
    def setSpeed(self, speed):
        self._speed = speed

    def getFuelTank(self):
        return self._fuelTank
    def setFuelTank(self, fuel_tank):
        self._fuelTank = fuel_tank

    def ride(self, distance):
        if self._speed == 0:
            return -1
        else:
            return round(distance/self._speed, 2)

    def longRide(self, ride_time):
        distance1 = self._speed*ride_time
        distance2 = self._fuelTank/(AVERAGE_FUEL_RATE/50)
        return round(min(distance1,distance2))

car = Car()
car.setSpeed(100)
car.setFuelTank(10)

print(f'Автомобиль проедет 200 км за: {car.ride(200)} ч.')
print(f'За 3 часа автомобиль сможет проехать: {car.longRide(3)} км')

