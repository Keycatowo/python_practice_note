"""
    re.sub 函數可以接收一個函數作為替換參數。
    
    當 re.sub 的第二個參數是一個函數時，對於每一個正則表達式匹配項，re.sub 會將 match 對象作為唯一參數調用該函數。
    該函數應返回一個字符串，該字符串將用於替換當前的匹配項。這使得在替換過程中可以對匹配到的文本進行更複雜的處理。
"""
import re

# 替換函數
def uppercase(match):
    """
    將匹配的文本轉換為大寫。

    Args:
        match (re.Match): 匹配的文本對象。

    Returns:
        str: 轉換為大寫的文本。
    """
    return match.group().upper()

# 使用 re.sub() 函數，將匹配的文本 傳入 uppercase 函數，轉換為大寫
result = re.sub(r'\b[a-z]+\b', uppercase, 'hello world')

print(result)  # 輸出: HELLO WORLD