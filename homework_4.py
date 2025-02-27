# Lambda-функция
first = 'Мама мыла раму'
second = 'Рамена мало было'

print(list(map(lambda x, y: x == y, first, second)))

# Замыкание
def get_advanced_writer(file_name):
    def write_everything(*data_set):
        with open(file_name, "w") as file:
            for i in data_set:
                file.write(str(i) + '\n')
    return write_everything

write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])

from random import choice

# Метод __call__
class MysticBall:
    def __init__(self, *args):
        self.list_ = args

    def __call__(self):
        return choice(self.list_)

first_ball = MysticBall('Да', 'Нет', 'Наверное')
print(first_ball())
print(first_ball())
print(first_ball())