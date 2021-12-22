class Obj:
    ##
    # тут представлено поведение четырех различных игровых объектов:
    # - воина
    # - лекаря
    # - дерева
    # - ловушки
    def defense(self):
        pass

    def move(self):
        pass

class Knight(Obj):
    def attack(self):
        pass

class Healer(Obj):
    def heal(self):
        pass

class Tree(Obj):
    def on_fire(self):
        pass

class Trap(Obj):
    def trap_attack(self):
        print("It's a trap!")

