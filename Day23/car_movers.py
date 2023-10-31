COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("turtle")
        self.x_move = STARTING_MOVE_DISTANCE
        self.y_move = MOVE_INCREMENT
        

      