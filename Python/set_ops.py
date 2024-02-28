"""
    在 Python 中，對於集合之間可以直接用符號進行操作。
"""
a = {1, 2, 3}
b = {3, 4, 5}
print(f"a: {a}", "\t", f"b: {b}")


# 交集 
print(f"交集(intersection): a & b = {a & b}")

# 聯集
print(f"聯集(union): a | b = {a | b}")

# 差集
print(f"差集(difference): a - b = {a - b}")

# 對稱差集
print(f"對稱差集(symmetric difference): a ^ b = {a ^ b}")

c = {1, 2, 3, 4}
d = {2, 3}
print(f"c: {c}", "\t", f"d: {d}")

# 子集
print(f"d 是否為 c 的子集: d <= c = {d <= c}")

# 真子集
print(f"d 是否為 c 的真子集: d < c = {d < c}")
