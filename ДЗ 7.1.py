# Реализовать класс Matrix (матрица).
# Обеспечить перегрузку конструктора класса (метод __init__()),
# который должен принимать данные (список списков) для формирования матрицы.
# Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов
# класса Matrix (двух матриц). Результатом сложения должна быть новая матрица.


class Matrix:
    def __init__(self, list_1, list_2):
        self.matrx = [list_1, list_2]
        self.list_1 = list_1
        self.list_2 = list_2

    def __add__(self):
        matrx = [[0, 0, ],
                [0, 0, ],
                [0, 0, ]]

        for i in range(len(self.list_1)):

            for el in range(len(self.list_2[i])):
                matrx[i][el] = self.list_1[i][el] + self.list_2[i][el]

        return str('\n'.join(['\t'.join([str(el) for el in i]) for i in matrx]))


my_matrix = Matrix([[1, 2],
                    [3, 4],
                    [5, 6]],
                   [[7, 8],
                    [9, 10],
                    [11,12]])

print(my_matrix.__add__())