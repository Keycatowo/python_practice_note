"""
    範例3: 使用 dis 反組譯一個類別
"""
class MyClass:
    """Some description"""
    
    def __init__(self, x):
        self.x = x
    def f(self):
        return self.x

import dis
dis.dis(MyClass)
