class Temperature:
    min_temperature = 0
    max_temperature = 1000
    def __init__(self, kelvin):
        self.kelvin = kelvin
        if Temperature.min_temperature > self.kelvin or Temperature.max_temperature < self.kelvin:
       
            raise Exception("Exception: Invalid temperature.")

    @classmethod
    def update_min_temperature(cls, temps):
        cls.min_temperature = temps
        if cls.min_temperature >cls.max_temperature:
            raise Exception("Exception: Invalid temperature")

    @classmethod
    def update_max_temperature(cls, temps):
        cls.max_temperature = temps
        if cls.max_temperature < cls.min_temperature:
            raise Exception("Exception: Invalid temperature.")