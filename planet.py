import pygame
import random
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
    def update():
        self.new_generation = set()
        for i in range(len(self.people)):
            self.new_generation.insert(self.people[i])
            if ([self.people[i].x + 1, self.people[i].y not in set(self.water) and [self.people[i].x + 1, self.people[i].y not in set(self.people)):
                chance = random.randint(1, 1000)
                if (chance < 13):
                    self.new_generation.insert([self.people[i].x + 1, self.people[i].y])
            if ([self.people[i].x - 1, self.people[i].y] not in set(self.water) and [self.people[i].x - 1, self.people[i].y] not in set(self.people)):
                chance = random.randint(1, 1000)
                if (chance < 13):
                    self.new_generation.insert([self.people[i].x - 1, self.people[i].y])
            if ([self.people[i].x, self.people[i].y + 1] not in set(self.water) and [self.people[i].x, self.people[i].y + 1] not in set(self.people)):
                chance = random.randint(1, 1000)
                if (chance < 13):
                    self.new_generation.insert([self.people[i].x, self.people[i].y + 1])
            if ([self.people[i].x, self.people[i].y - 1] not in set(self.water) and [self.people[i].x, self.people[i].y - 1] not in set(self.people)):
                chance = random.randint(1, 1000)
                if (chance < 13):
                    self.new_generation.insert([self.people[i].x, self.people[i].y - 1])
        self.people = list(self.new_generation)

        
                    
