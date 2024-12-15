class Matrix_Operations:
    def __init__(
            self, N: int, M: int, matrix: list[list[int]] #На вход классу подаются размерность матрицы и сама матрица
    ):
        self.N = N
        self.M = M
        self.matrix = self.de_format_matrix(matrix) #Хранение матрицы с самого начала осуществляется в разряжено-строчном формате

    #Функция для превращения из матричного формата хранения в разряжено-строчное
    def de_format_matrix(self, matrix: list[list[int]]) -> tuple[list, list, list]:
        values = []
        cols = []
        rows = [0] * (len(matrix)+1)

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] != 0:
                    values.append(matrix[i][j])
                    cols.append(j)
            rows[i + 1] = len(values)

        return values, cols, rows

    #Функция для превращения из разряжено-строчного формата хранения в матричный
    def format_matrix(self, tuple_matrix: tuple[list, list, list]) -> list[list[int]]:
        values, cols, rows = tuple_matrix
        n, m = len(rows)-1, max(cols)+1

        matrix = [[0 for _ in range(m)] for _ in range(n)]
        for i in range(n):
            start = rows[i]
            end = rows[i+1]
            for j in range(start, end):
                col = cols[j]
                matrix[i][col] = values[j]

        return matrix

    #Функция для создания новых матриц с клавиатуры (хранение сразу происходит в разряжено-строчном формате)
    def create_matrix(self) -> tuple[list, list, list]:

        print("Введите числа N и M через пробел, чтобы задать структуру матрицы")
        print("N - количество строк | M - количество столбцов")
        N, M = map(int, input().split())

        new_matrix = []
        for _ in range(N):
                print("Введите значения массива через пробел")
                lst = list(map(int, input().split()))
                new_matrix.append(lst)
        return self.de_format_matrix(new_matrix)

    #Задание 1
    #Функция для подсчета Следа матрицы
    def counting_sled(self, matrix: tuple[list, list, list]) -> int:

        matrix = self.format_matrix(matrix) #Перевод из разряжено-строчного формата для работы
        if len(matrix) != len(matrix[0]): #След можно посчитать только для квадратной матрицы
            return 0
        sum = 0
        for i in range(len(matrix)):
            sum += matrix[i][i]
        return sum

    #Вывод элемента матрицы по двум индексам
    def find_element(self, index_row: int, index_col: int, matrix: tuple[list, list, list]) -> int:
        matrix = self.format_matrix(matrix) #Перевод из разряжено-строчного формата для работы
        return matrix[index_row][index_col]

    #Задание 2
    #Функция для суммирования двух матриц
    def sum_matrix(self,
                   matrix1: tuple[list, list, list],
                   matrix2: tuple[list, list, list]) -> tuple[list, list, list]:
        matrix1 = self.format_matrix(matrix1) #Перевод из разряжено-строчного формата для работы
        matrix2 = self.format_matrix(matrix2)

        if len(matrix1) != len(matrix2) or len(matrix1[0]) != len(matrix2[0]): #Проверяем, одинаковые ли структуры у двух матриц
            return 0

        matrix3 = [[0] * len(matrix1[0]) for _ in range(len(matrix1))]
        for i in range(len(matrix1)):
            for j in range(len(matrix1[0])):
                matrix3[i][j] = matrix1[i][j] + matrix2[i][j]

        return self.de_format_matrix(matrix3)

    #Функция для произведения двух матриц
    def multiplication_matrix(self,
                              matrix1: tuple[list, list, list],
                              matrix2: tuple[list, list, list]) -> tuple[list, list, list]:
        matrix1 = self.format_matrix(matrix1) #Перевод из разряжено-строчного формата для работы
        matrix2 = self.format_matrix(matrix2)


        if len(matrix1[0]) != len(matrix2): #Проверяем на равенство столбцов одного и строк другого
            return 0
        matrix3 = [[0] * (len(matrix2[0])) for _ in range(len(matrix1))] #Инициализация итоговой матрицы

        for i in range(len(matrix1)):
            for j in range(len(matrix2[0])):
                for k in range(len(matrix2)):
                    matrix3[i][j] += matrix1[i][k] * matrix2[k][j]
        return self.de_format_matrix(matrix3)

    #Функция для произведения скаляра на матрицу
    def multiplication_skal_matrix(self,
                                   matrix: tuple[list, list, list],
                                   skal: int) -> tuple[list, list, list]:
        matrix = self.format_matrix(matrix) #Перевод из разряжено-строчного формата для работы

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                matrix[i][j] *= skal
        return self.de_format_matrix(matrix)

    #Задание 3
    #Функция по поиску определителя матрицы
    def det(self) -> None:

        matrix = self.create_matrix()
        matrix = self.format_matrix(matrix) #Перевод из разряжено-строчного формата для работы

        if len(matrix) != len(matrix[0]): #Для нахождения определителя матрица должна быть квадратной
            return 0

        def det_recursion(matrix: list[list[int]]) -> int: #Функция для рекурсии - реализация Минора

            if len(matrix) == 1: #Если условие выполняется, значит мы дошли до "конца" рекурсивного вызова
                return matrix[0][0]

            summ = 0
            for i in range(len(matrix[0])):
                M = [row[:i] + row[i + 1:] for row in matrix[1:]]
                elem = ((-1) ** i) * matrix[0][i] * det_recursion(M)
                summ += elem

            return summ #Возвращаем промежуточную сумму

        summ = det_recursion(matrix)

        flag = "Существует ли матрица, обратная данной? -- Да"
        if summ == 0:
            flag = "Существует ли матрица, обратная данной? -- Нет"
        print(summ)
        print(flag)


#------------------------------Поле для взаимодействий с проектом -----------------------------------------

print("Введите числа N и M через пробел, чтобы задать структуру матрицы")
print("N - количество строк | M - количество столбцов")
N, M = map(int, input().split())

matrix = []
for _ in range(N):
    print("Вводите значения массива через пробел")
    lst = list(map(int, input().split()))
    matrix.append(lst)

matrix_operation = Matrix_Operations(N, M, matrix)
matrix = matrix_operation.matrix

#Задание 1
sled = matrix_operation.counting_sled(matrix)
print("Итог подсчета Следа:")
print(sled)
print()

print("Введите два индекса: Строка и Столбец")
i, j = map(int, input().split())
index = matrix_operation.find_element(i - 1, j - 1, matrix)
print("Элемент по указанным индексам:")
print(index)
print()

#Задание 2
print("Создайте новую матрицу для реализации суммы и произведения")
print()
new_matrix = matrix_operation.create_matrix()

summ = matrix_operation.sum_matrix(matrix, new_matrix)
format_summ = matrix_operation.format_matrix(summ)
print(format_summ)
print()

multi = matrix_operation.multiplication_matrix(matrix, new_matrix)
format_multi = matrix_operation.format_matrix(multi)
print(format_multi)
print()

print("Введите скаляр K")
k = int(input())
skalyar = matrix_operation.multiplication_skal_matrix(matrix, k)
format_skalyar = matrix_operation.format_matrix(skalyar)
print(format_skalyar)
print()

#Задание 3
matrix_operation.det()
