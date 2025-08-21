class Car:
    def __init__(self, model, year,color,for_sale):
        self.model = model
        self.year = year
        self.color = color
        self.for_sale = for_sale
    def drive(self):
        print(f"Driving car {self.model} at {self.year}")
    def stop(self):
        print(f"Stopping car {self.model} at {self.year}")
    def describe(self):
        print(self.model)
        print(self.year)
        print(self.color)
        print(self.for_sale)