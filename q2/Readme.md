class PSHS_Galaxy:
    def __init__(self, name, size, color, system_type="Solar System"):
        self.__name = name
        self.__size = size
        self.__color = color
        self.__system_type = system_type
        self.__is_habitable = False
        self.__moons = []

    @property
    def name(self):
        return self.__name

    @property
    def size(self):
        return self.__size

    @property
    def color(self):
        return self.__color

    @property
    def system_type(self):
        return self.__system_type

    @property
    def is_habitable(self):
        return self.__is_habitable

    @is_habitable.setter
    def is_habitable(self, value: bool):
        if isinstance(value, bool):
            self.__is_habitable = value

    def add_moon(self, moon_name):
        self.__moons.append(moon_name)

    def get_moons(self):
        return self.__moons


class VerityPlanet(PSHS_Galaxy):
    def __init__(self, atmosphere="Nitrogen-Rich"):
        super().__init__(name="Verity Planet", size="Big", color="Yellow")
        self.__atmosphere = atmosphere
        self.__has_rings = True

    @property
    def atmosphere(self):
        return self.__atmosphere

    @property
    def has_rings(self):
        return self.__has_rings

    def rotate(self):
        pass

    def orbit(self):
        pass


class BaterboniaPlanet(PSHS_Galaxy):
    def __init__(self, core_temperature=1500):
        super().__init__(name="Baterbonia Planet", size="Small", color="Blue")
        self.__core_temperature = core_temperature
        self.__water_percentage = 85.0

    @property
    def core_temperature(self):
        return self.__core_temperature

    @property
    def water_percentage(self):
        return self.__water_percentage

    def generate_magnetic_field(self):
        pass

    def emit_signal(self):
        pass