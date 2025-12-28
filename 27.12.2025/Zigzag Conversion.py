def convert(s, numRows):
    if numRows == 1:
        return s
    res = [''] * numRows
    row, step = 0, 1
    for char in s:
        res[row] += char
        if row == 0 or row == numRows - 1:
            step = -step
        row += step
    return ''.join(res)
