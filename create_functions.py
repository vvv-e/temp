class MultiAttr:
    def __init__(self):
        self.about = "Тестовый экземпляр для множественной инициации атрибутов в цикле"

    def set_attribute(self, turn):
        for num in range(turn):
            setattr(self, f"variable_{num}", num ** 2)

    def get_attribute(self, turn):
        for num in range(turn):
            print(getattr(self, f"variable_{num}"), end=" ")

if __name__ == '__main__':
    turn = 10
    a = MultiAttr()
    a.set_attribute(turn)
    print(dir(a)[-turn - 3:])
    a.get_attribute(turn)
