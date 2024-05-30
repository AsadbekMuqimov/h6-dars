"""r=(1,2,3,4,5,6)
r_iteratration = iter(r)
print(next(r_iteratration))
print(next(r_iteratration))
print(next(r_iteratration))
print(next(r_iteratration))
print(next(r_iteratration))
for a in r:
    print(a)"""
    
#1-misol
"""class Car:
    def __init__(self):
        self.color = "red"
        self.model = "BMW"
        self.year = 2020
    def __iter__(self):
        return self
    def __next__(self):
        if  input(str)  :
            return self.year
        else:
            raise StopIteration()
for i in Car():
    print(i)"""



#2-misol
"""class Car:
    objects = []
    counter = 0

    def __init__(self, f_name):
            self.f_name = f_name
            self.objects.append(self)

    def __iter__(self):
            return self

    def __next__(self):
        try:
            object = self.objects[self.counter]
            self.counter += 1
            return object.f_name
        except IndexError:
            self.counter = 0
            raise StopIteration
Car('Nexia')
Car('Lasetti')
Car('Gentra')
Car('Cobalt')
for car in Car('Damas'):
    print(car)"""
    
"""   
class Car:
    def __init__(self,model):
        self.model =model

    def __iter__(self):
        self.id = 0
        return self

    def __next__(self):
        if self.id < len(self.model):
            result = self.model[self.id]
            self.id += 1
            return result
        else:
            raise StopIteration

objekt = Car(" BMW X7")
for i in objekt:
    print(i)
"""



