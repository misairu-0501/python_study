# 九九の表を作成してみよう

def multiply(x, y):
    return x * y

for row in range(1, 10):
    for num in range(1, 10):
        print(multiply(row, num), end="")
        if num < 9:
            print(", ", end="")
        else:
            print()
