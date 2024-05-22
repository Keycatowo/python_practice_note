"""
    範例：讀取一個內含攻擊程的 pickle 檔案
    注意執行結果，偷偷執行了 ls 指令
"""
import pickle   

with open('data.pickle', 'rb') as f:
    d = pickle.load(f)