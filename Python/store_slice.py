"""
    在Python中，除了可以直接對list等序列進行切片操作之外，
    也可以將切片的slice儲存起來，以便之後使用。
"""
# list 和 str 都是可以切片的對象
numbers: list[int] = list(range(1,11))
text: str = 'Hello, world!'

# 一般情況下
print(numbers[::-1])
print(text[::-1])

# 切片設定可以儲存起來，多個地方使用
rev: slice = slice(None, None, -1) # same to ::-1
f_five: slice = slice(None, 5) # same to :5

# 之後就可以直接取用
print(numbers[rev])
print(text[f_five])