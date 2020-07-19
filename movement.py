
# Here we all created the class of movement. all fighting styles will inherit mehods and attributes from here


class Movement():

    stamina = 100
    def __init__(self, move_forward, move_back, slip, stamina, duck):
        self.move_forward = move_forward
        self.move_back = move_back
        self.slip = slip
        self.duck = duck
        self.stamina = stamina


    def current_stamina(self):
        self.stamina = 100

    def charging_forward(self):
        return "Moving forward hands up"


    def retreating(self):
        return "Retreating, moving back"


    def inandout(self):
        return "Moving in", "Moving out"

    def recover(self):
        self.stamina += 5

    def head_movement(self):
        self.slip = "slip left, slip right"
        self.stamina -= 2

    def defend(self):
        self.duck = "Fighter ducks"
        self.slip = "Slip left, slip right"


# Here will create differant objects to resemble differant styles of moving

aggresive = Movement()

print(aggresive)
