
class Unit:
    def __init__(self, field, x_coord: int, y_coord: int, state: str, speed: int):
        self.field = field
        self.x_coord = x_coord
        self.y_coord = y_coord
        self.state = state
        self.speed = speed

    def _get_speed(self):
        if self.state.casefold() == "fly":
            speed = self.speed * 1.2
        elif self.state.casefold() == "crowl":
            speed = self.speed * 0.5
        else:
            speed = self.speed
        return speed

    def _get_coord(self):
        return tuple((self.x_coord, self.y_coord))

    def _set_coord(self, coord):
        x, y = coord
        self.x_coord = x
        self.y_coord = y

    def move_unit(self,direction):
        speed = self._get_speed()
        x, y = self._get_speed()
        if direction == 'UP':
            self._set_coord((x, y + 1))
        elif direction == 'DOWN':
            self._set_coord((x, y - 1))
        elif direction == 'LEFT':
            self._set_coord((x - 1, y))
        elif direction == 'RIGHT':
            self._set_coord((x + 1, y))
