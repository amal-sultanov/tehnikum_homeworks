class Laptop:
    def __init__(self, main_memory, disk_volume, operating_system, weight):
        self.main_memory = main_memory
        self.disk_volume = disk_volume
        self.operating_system = operating_system
        self.weight = weight

    def change_main_memory(self, new_main_memory):
        self.main_memory = new_main_memory

    def change_operating_system(self, new_operating_system):
        self.operating_system = new_operating_system
