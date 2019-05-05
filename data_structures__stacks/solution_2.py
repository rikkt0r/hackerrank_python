current_max = 0  # x <= 1
stack = []

queries = int(input().strip())

for _ in range(queries):
    query = input().strip().split()

    if query[0] == '1':
        val = int(query[1])
        current_max = max(val, stack[-1][1]) if stack else val
        stack.append((val, current_max),)

    elif query[0] == '2':
        stack.pop()
        current_max = stack[-1][1] if stack else 0

    elif query[0] == '3':
        print(current_max)

# cat solution_2_input_1.txt | python3 solution_2.txt
# cat solution_2_input_2.txt | python3 solution_2.txt
