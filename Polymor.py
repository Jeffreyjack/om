class Car:
    def __init__(self, name):    
        self.name = name
 
    def drive(self):             
        raise NotImplementedError("Subclass must implement abstract method")
 
    def stop(self):             
        raise NotImplementedError("Subclass must implement abstract method")
 
class Sportscar(Car):
    def drive(self):
        return 'Sportscar driving!'
 
    def stop(self):
        return 'Sportscar braking!'
 
class Truck(Car):
    def drive(self):
        return 'Truck driving slowly because heavily loaded.'
 
    def stop(self):
        return 'Truck braking!'
 
 
cars = [Truck('Bananatruck'),
        Truck('Orangetruck'),
        Sportscar('Z3')]
 
for car in cars:
    print car.name + ': ' + car.drive()

carss = [Sportscar('BMW'),
         Sportscar('Audi'),
         Sportscar('Ferrari')]    

for car1 in carss:
    print car1.name + ': ' + car1.stop()
    print car1.name + ': ' + car1.drive()

