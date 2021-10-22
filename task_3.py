input_data = [
    [1, 5, 7, 2],
    [3, 2, 6, 9],
    [10, 62, 4, 3],
    [5, 13, 7, 84]
]


def diagonals_sum(matrix: list[list[int]]):
    row_length = len(matrix)
    col_length = len(max(matrix, key=len))
    if row_length != col_length:
        raise ValueError("Переданная матрица не квадратная")

    left_idx, right_idx = 0, col_length - 1
    sum_left_diagonal, sum_right_diagonal = 0, 0
    for row in input_data:
        sum_left_diagonal += row[left_idx]
        sum_right_diagonal += row[right_idx]
        left_idx += 1
        right_idx -= 1

    return sum_left_diagonal, sum_right_diagonal


sum_general_diagonal, sum_additional_diagonal = diagonals_sum(matrix=input_data)
print(f'Сумма элементов на главной диагонали = {sum_general_diagonal}')
print(f'Сумма элементов на побочной диагонали = {sum_additional_diagonal}')
