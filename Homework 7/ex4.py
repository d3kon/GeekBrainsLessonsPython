from typing import List


class Matrix:
    def __init__(self, matrix_data: List[List]):
        self.matrix_data = matrix_data
        m_rows = len(self.matrix_data)
        self.matrix_size = frozenset([(m_rows, len(row)) for row in self.matrix_data])
        if len(self.matrix_size) != 1:
            raise ValueError("Невозможно сделать матрицу! ")

    def __add__(self, other: List[List]) -> List[List]:
        result = []
        for item in zip(self.matrix_data, other.matrix_data):
            result.append([sum([j, k]) for j, k in zip(*item)])
        return Matrix(result)

    def __str__(self) -> str:
        return '\n'.join(['\t'.join(map(str, row)) for row in self.matrix_data])


if __name__ == '__main__':
    matrix1 = Matrix([[5, 4], [6, 2]])
    print(matrix1, '\n')

    matrix2 = Matrix([[7, 2], [5, 412]])
    print(matrix2, '\n')

    print(matrix1 + matrix2)
