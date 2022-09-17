from dataclasses import dataclass
from operator import sub


@dataclass
class MatrixString:
    numbers: list[int]
    main_number: int


@dataclass
class Matrix:
    strings: list[MatrixString]


class CannotWithoutFraction(Exception):
    def __init__(self, message="Matrix can't be solved without using fractions"):
        self.message = message
        super(CannotWithoutFraction, self).__init__(message)


class Gauss:
    def __init__(self, matrix: Matrix):
        self.begin_matrix = matrix
        self.current_matrix: Matrix = matrix
        self.matrix_border: int = len(self.begin_matrix.strings)

    def print_matrix(self) -> None:
        string_matrix = str()

        for string in self.current_matrix.strings:
            for num in string.numbers:
                if 0 > num > -10 or num > 9:
                    string_matrix += f" {num} "
                elif num < -9:
                    string_matrix += f"{num} "
                else:
                    string_matrix += f"  {num} "

            if string.main_number < 0 or string.main_number > 9:
                string_matrix += f"| {string.main_number}\n"
            else:
                string_matrix += f"|  {string.main_number}\n"
        print(string_matrix)

    def __get_pivot_string(self, pivot: int) -> tuple[MatrixString, int]:
        for i in range(pivot, self.matrix_border + 1):
            try:
                string = self.current_matrix.strings[i]
            except IndexError:
                raise CannotWithoutFraction

            string_nums = (
                    string.numbers
                    + [string.main_number]
            )
            devide = True
            for num in string_nums:
                if not num % string_nums[pivot] == 0:
                    devide = False
            if devide:
                self.current_matrix.strings[i].numbers = [
                    i//string_nums[pivot] for i in string_nums[:-1]
                ]
                self.current_matrix.strings[i].main_number = int(string_nums[-1] // string_nums[pivot])
                return self.current_matrix.strings[i], i

    def __shuffle_strings(
            self,
            pos_to: int,
            string: MatrixString,
            pos_from: int
    ):
        old_string = self.current_matrix.strings[pos_to]

        self.current_matrix.strings[pos_to], \
        self.current_matrix.strings[pos_from] = string, old_string
        self.print_matrix()

    def _calculate_row(self, pivot: int):
        self.__shuffle_strings(pivot, *self.__get_pivot_string(pivot))
        main_string = self.current_matrix.strings[pivot]

        for i, string in enumerate(self.current_matrix.strings):
            if i == pivot:
                continue

            difference = string.numbers[pivot] // main_string.numbers[pivot]
            if difference > 0:
                sub_iter = map(
                    sub,
                    [i*difference for i in main_string.numbers],
                    [i for i in string.numbers]
                )
                string.numbers = list(sub_iter)
                string.main_number = main_string.main_number * difference - string.main_number
            else:
                sub_iter = map(
                    sum,
                    zip(
                        [i*-difference for i in main_string.numbers],
                        [i for i in string.numbers]
                    )
                )
                string.numbers = list(sub_iter)
                string.main_number = main_string.main_number * difference + string.main_number
        self.print_matrix()

    def count(self):
        self.print_matrix()
        for pivot_pos in range(self.matrix_border):
            self._calculate_row(pivot_pos)
        for i, string in enumerate(self.current_matrix.strings):
            for num in string.numbers:
                if num < 0:
                    string.numbers = [i * (-1) for i in string.numbers]
                    string.main_number *= (-1)
                    break
        self.print_matrix()


Gauss(
    Matrix(
        [
            MatrixString([1, 1, 1], 6),
            MatrixString([1, -1, 2], 5),
            MatrixString([2, -1, -1], -3)
        ]
    )
).count()

