from random import randint

CAR_SPECS = {
    'ferrary': {"max_speed": 340, "drag_coef": 0.324, "time_to_max": 26},
    'bugatti': {"max_speed": 407, "drag_coef": 0.39, "time_to_max": 32},
    'toyota': {"max_speed": 180, "drag_coef": 0.25, "time_to_max": 40},
    'lada': {"max_speed": 180, "drag_coef": 0.32, "time_to_max": 56},
    'sx4': {"max_speed": 180, "drag_coef": 0.33, "time_to_max": 44},
}

class Car:
    
    def __init__(self, name):
        if name in CAR_SPECS:
            self.spec = name
            self.max_speed = CAR_SPECS[name]["max_speed"]
            self.drag_coef = CAR_SPECS[name]["drag_coef"]
            self.time_to_max = CAR_SPECS[name]["time_to_max"]
        else: print("Wrong car name")
    
class Weather:
    
    def __init__(self, wind_speed):
        self.wind_speed = randint(0, wind_speed)
    
class Competition:
    
    once = True
    def __new__(cls, *args):
        if cls.once is True:
            cls.once = False
            return super(Competition, cls).__new__(cls)
        else: print("ONLY ONE COMPETITION ALLOWED!")
    
    def __init__(self, ds):
        self.distance = ds
    
    def start(self, competitors, weather):
        print("Competition on distance %s:" % self.distance)
        for competitor_name in competitors:
            competitor_time = 0
            competitor_speed = 0
            car = Car(competitor_name)


            for distance in range(self.distance):
                _wind_speed = weather.wind_speed

                if competitor_time == 0:
                    _speed = 1
                else:
                    _speed = (competitor_time / car.time_to_max) * car.max_speed
                    if _speed > _wind_speed:
                        _speed -= (car.drag_coef * _wind_speed)

                competitor_time += float(1) / _speed

            print("Car <%s> result: %f" % (competitor_name, competitor_time))


competitors = ('ferrary', 'bugatti', 'toyota', 'lada', 'sx4')
weather = Weather(20)
comp1 = Competition(10000)
#comp2 = Competition(1000)
#comp3 = Competition(100)
comp1.start(competitors, weather)
#comp2.start(competitors, weather)
#comp3.start(competitors, weather)
