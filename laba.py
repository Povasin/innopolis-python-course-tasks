# Расширьте код этой программы, добавив новые классы Grass, Flower, Vine, Snail, Rabbit, Wolf. Интегрируйте их в экосистему, заменив обобщенные Animal и Plant  
 
import matplotlib.pyplot as plt 
import random 
 
class Creature: 
    def __init__(self, name, count): 
        self.name = name 
        self.count = count 
 
    def step(self, ecosystem=None): 
        pass 
 
 
class Plant(Creature): 
    def __init__(self, name, count, growth_rate=0.2, max_count=100): 
        super().__init__(name, count) 
        self.growth_rate = growth_rate 
        self.max_count = max_count 
 
    def step(self, ecosystem=None): 
        B = self.count 
        self.count += self.growth_rate * B * (1 - B / self.max_count)   # simple constant growth 
 
 
class Animal(Creature): 
    def __init__(self, name, count, bite_size, diet): 
        super().__init__(name, count) 
        self.bite_size = bite_size 
        self.diet = diet 
 
    def step(self, ecosystem): 
        edible = [c for c in ecosystem.creatures  
                  if isinstance(c, tuple(self.diet)) and c.count > 0] 
 
        if not edible: 
            return 
 
        target = random.choice(edible) 
        eaten = min(target.count, self.bite_size) 
        target.count -= eaten 
        self.count += eaten * 0.5 
 
 
class Ecosystem: 
    def __init__(self, creatures): 
        self.creatures = creatures 
        self.history = {c: [] for c in creatures} 
 
    def step(self): 
        for c in self.creatures: 
            if isinstance(c, Plant): 
                c.step() 
        for c in self.creatures: 
            if isinstance(c, Animal): 
                c.step(self) 
 
        # remove dead creatures 
        self.creatures = [c for c in self.creatures if c.count > 0] 
 
        for c in list(self.history.keys()): 
            if c in self.creatures: 
                self.history[c].append(c.count) 
            else: 
                # creature died → keep count at 0 
                self.history[c].append(0) 
 
    def plot(self): 
        for creature, biomass_list in self.history.items(): 
            plt.plot(biomass_list, label=creature.name) 
 
        plt.xlabel("Step") 
        plt.ylabel("Biomass") 
        plt.legend() 
        plt.show() 
 
 
# Example usage: 
if name == "__main__": 
    eco = Ecosystem([ 
        Plant("Grass1", 5), 
        Plant("Grass2", 6), 
        Animal("Rabbit", 4, bite_size=2, diet=[Plant]) 
    ]) 
 
    for _ in range(50): 
        eco.step() 
 
    eco.plot()