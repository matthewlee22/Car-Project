class Car:
    def __init__ (self, model, miles = 0, used = False):
        self.used = used
        self.miles = miles
        self.model = model

    def set_model(self, model):
        self.model = model

    def get_model(self):
        return self.model
    
    def set_miles(self, miles):
        self.miles = miles

    def add_miles(self, new_miles):
        self.miles += new_miles
        self.updateUse()

    def get_miles(self):
        return self.miles
    
    def updateUse(self, miles):
        if self.miles > 0:
            self.used = True
    