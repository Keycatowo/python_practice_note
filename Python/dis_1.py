"""
    dis 模組是用來反組譯 Python bytecode 的模組
    基本的使用方式為：
        dis.dis(code)
    此程式示範 dis.dis 的基本使用方式
"""
import dis
dis.dis("my_dict = {'a': 1, 'b': 2, 'c': 3}")