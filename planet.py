import pygame
class Istota(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
class Water(Istota):
    pass
class Land(Istota):
    pass
class People(Istota):
    pass
class Planet(object):
    def __init__(self):
        self.water = []
        self.land = []
        self.people = []
        
    def add(self, new_object):
        if(type(new_object) == water)
            self.water.append(self.water)
        if(type(new_object) == land)
            self.land.append(self.land)
        if(type(new_object) == people)
            self.people.append(self.people)
        
                    
