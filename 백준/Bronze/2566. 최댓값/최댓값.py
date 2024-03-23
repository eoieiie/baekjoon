num_list = [list(map(int, input().split())) for _ in range(9)]

max_value = max(max(row) for row in num_list)

for i, row in enumerate(num_list):
    if max(row) == max_value:  # if max_value in row:
        max_index = (i * 9) + row.index(max(row))

row_position = max_index // len(num_list) + 1
column_position = max_index % len(num_list) + 1

print(max_value)
print(row_position, column_position)