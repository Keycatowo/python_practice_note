"""
    範例2: 用 dis.dis 來反組譯一個函數
    以及使用 dis.show_code 來顯示函數的原始程式碼(會包含常數表)
"""
def f(x):
    if x % 2 == 0:
        return True
    else:
        return False
    
import dis
dis.dis(f)
dis.show_code(f)