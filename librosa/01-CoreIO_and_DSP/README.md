# Core IO and DSP


## Audio loading
+ `load(path)`：讀取音檔
    + `sr=22050`：預設取樣頻率為22050，如果需要採用檔案原始的取樣頻率需要設定`sr=None`
+ `to_mono(y)`：轉換成單通道
+ `get_duration()`：取得長度(sec)
    + `sr`：取樣頻率，記得要設定，不然會採用22050可能會算錯
    + `path`：計算檔案
    + `y`：計算時間序列長度
    + `S`：計算STFT類型(Chromagram、mel-Spectrogram)舉證的長度
        + 記得要給`n_fft`，預設為2048
        + 如果為半個的話，可以設定`center=False`
    + 