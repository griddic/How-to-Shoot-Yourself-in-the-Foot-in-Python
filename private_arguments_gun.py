class Base:
    def __init__(self):
        self.__name = 'undefined'

    def great(self):
        return f'I am {self.__name}.'


class Heir(Base):
    def __init__(self, name):
        super().__init__()
        self.__name = name


if __name__ == '__main__':
    heir = Heir('Ivan')
    print(heir.great())
