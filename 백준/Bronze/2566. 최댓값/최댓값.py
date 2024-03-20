num_list = []

for i in range(9):
    num = list(map(int, input().split()))
    num_list.append(num)

max_value = max(max(row) for row in num_list)

for i, row in enumerate(num_list):
    if max(row) == max_value:  # if max_value in row:
        max_index = (i * 9) + row.index(max(row))

    # if max_value in row:
    #     max_index = (i * 9) + row.index(max_value)

# max_index = num_list.index(max(num_list)) + 1


row_position = max_index // len(num_list) 
column_position = max_index % len(num_list) 

print(max_value)
print(row_position + 1, end = " ")
print(column_position + 1)