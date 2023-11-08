def matrix_mul(m_a, m_b):
    # Validate if m_a and m_b aren't lists of lists of integers or floats
    if not (isinstance(m_a, list) and all(isinstance(row, list) and all(isinstance(val, (int, float)) for val in row) for row in m_a)) or not (isinstance(m_b, list) and all(isinstance(row, list) and all(isinstance(val, (int, float)) for val in row) for row in m_b)):
        raise TypeError("m_a must be a list of lists or m_b must be a list of lists")


    # Validate if m_a or m_b is empty
    if any(not row for row in (m_a, m_b)):
        raise ValueError("m_a can't be empty or m_b can't be empty")

    # Validate if m_a and m_b are the same size
    if not all(len(row) == len(m_a[0]) for row in m_a) or not all(len(row) == len(m_b[0]) for row in m_b):
        raise TypeError("Each row of m_a must be of the same size or each row of m_b must be of the same size")

    # Validate if m_a and m_b can be multiplied
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    return [[sum(m_a[i][k] * m_b[k][j] for k in range(len(m_b))) for j in range(len(m_b[0]))] for i in range(len(m_a))]

    

""" print(matrix_mul([[1, 2], [3, 4]], [[1, 2], [3, 4]]))
print(matrix_mul([[1, 2]], [[3, 4], [5, 6]])) """

# Define the matrices m_a and m_b
m_a = [[1, 2], [3, 4]]
m_b = [[1, 2], [3, 4]]

# Call the matrix_mul function with the defined matrices
result = matrix_mul(m_a, m_b)
print(result)

m_a = [[1, 2]]
m_b = [[3, 4], [5, 6]]

result = matrix_mul(m_a, m_b)
print(result)

print(matrix_mul([[1, 2], [3, 4]], [[1, 2], [3, 4]]))
print(matrix_mul([[1, 2]], [[3, 4], [5, 6]]))














































