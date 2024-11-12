from pakuri import Pakuri

class Pakudex:
    def __init__(self, capacity=20):
        self.capacity = capacity
        self.pakuri_list = []

    def get_size(self):
        return len(self.pakuri_list)

    def get_capacity(self):
        return self.capacity

    def get_species_array(self):
        if not self.pakuri_list:
            return None
        return [pakuri.get_species() for pakuri in self.pakuri_list]

    def get_stats(self, species):
        for pakuri in self.pakuri_list:
            if pakuri.get_species() == species:
                return [pakuri.get_attack(), pakuri.get_defense(), pakuri.get_speed()]
        return None

    def sort_pakuri(self):
        self.pakuri_list.sort(key=lambda pakuri: pakuri.get_species())

    def add_pakuri(self, species):
        if (self.get_size() < self.capacity) and (species not in [pakuri.species for pakuri in self.pakuri_list]):
            new_pakuri = Pakuri(species)
            self.pakuri_list.append(new_pakuri)
            return True
        return False

    def evolve_species(self, species):
        for pakuri in self.pakuri_list:
            if pakuri.get_species() == species:
                pakuri.evolve()
                return True
        return False