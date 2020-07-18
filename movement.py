
# Here we all created the class of movement. all fighting styles will inherit mehods and attributes from here


class movement():

    def __init__(self, move_forward, move_back, slip, duck, circle):
        self.move_forward = move_forward
        self.move_back = move_back
        self.slip = slip
        self.duck = duck
        self.circle = circle


    def