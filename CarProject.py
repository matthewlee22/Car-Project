class Employee:
    
    def __init__(self, cars_sold, revenue_generated, position, name):
        self.cars_sold = cars_sold
        self.revenue_generated = revenue_generated
        self.position = position
        self.name = name

    def set_position(self, positionname):
        self.position = positionname
    
    def get_position(self):
        return self.position

    def increment_cars_sold(self, cars_sold):
        self.cars_sold += cars_sold
    
    def get_cars_sold(self):
        return self.cars_sold

    def generate_revenue(self, amount):
        self.revenue_generated += amount

    def get_revenue_generated(self):
        return self.revenue_generated

