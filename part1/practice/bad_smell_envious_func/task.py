class Cube:
    x: int
    y: int
    z: int

    def __init__(self, x: int, y: int, z: int):
        # ВОПРОС!!!!! Почему x: int при инициализации пропускает буквенное значение?
        # пришлось проверять чз преобразование в интеджер
        self.x = int(x)
        self.y = int(y)
        self.z = int(z)

    def _get_x(self):
        return self.x

    def _get_y(self):
        return self.y

    def _get_z(self):
        return self.z

    def get_volume(self):
        return self._get_x() * self._get_y() * self._get_z()


class CubeVolumeCalculator:

    @staticmethod
    def calc_cube_volume(cube):
        return cube.get_volume()

