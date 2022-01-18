
class SpecificWeather():
    def __init__(self, data):
        self.data = data

    @property
    def type(self):
        return self.data["Type"]

    @property
    def temperature(self):
        return self.data["Temp"]

    @property
    def speed(self):
        return self.data["Speed"]

    @property
    def direction(self):
        return self.data["Direction"]


class Weather():
    def __init__(self, data):  # data is the dictionary
        self.data = data
        

    @property
    def DP(self):
        return SpecPrinter(self.data)

    def __getitem__(self, item):  # for wednesday[22].type
        return SpecificWeather(self.data[item])

    def __getattr__(self, name):  # for wednesday.at22.type
        if name.startswith("at"):
            return SpecificWeather(self.data[int(name[2:])])
        raise AttributeError()

class SpecPrinter(Weather):
    def __init__(self, data):
        super().__init__(data)
        # self.data = data
    # @property
    def dothings(self):
        print('aquiii')
        print(self.data[22])
        return self
wednesday = Weather({
    22: {
        'Type': '1',
        'Temp': 30,
        'Speed': '11',
        'Direction': 'left'
    },
    23: {
        'Type': '2',
        'Temp': 28,
        'Speed': '22',
        'Direction': 'right'
    }
})

print(wednesday.at22.temperature)  # gives 30
print(wednesday[23].temperature)  # gives 28
wednesday.DP.dothings()