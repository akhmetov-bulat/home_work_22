
class Unit:
    def __init__(self, field, x_coord :int, y_coord: int, state: str, speed: int):
        self.field = field
        self.x_coord = x_coord
        self.y_coord = y_coord
        self.state = state
        self.speed = speed

    def _get_coord(self):
        x = self.x_coord
        y = self.y_coord
        return tuple((x, y))

    def _set_coord(self, coord: tuple):
        x, y = coord
        self.x_coord = x
        self.y_coord = y

    def _get_speed(self):
        if self.state.casefold() == "fly":
            speed = self.speed * 1.2
        elif self.state.casefold() == "crowl":
            speed = self.speed * 0.5
        else:
            speed = self.speed
        return speed

    def move(self ,direction):
        speed = self._get_speed()
        if direction == 'UP':
            self._set_coord((self.x_coord, self.y_coord + speed))
        elif direction == 'DOWN':
            self._set_coord((self.x_coord, self.y_coord - speed))
        elif direction == 'LEFT':
            self._set_coord((self.x_coord - speed, self.y_coord))
        elif direction == 'RIGTH':
            self._set_coord((self.x_coord + speed, self.y_coord))
