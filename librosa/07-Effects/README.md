# Librosa Effects 筆記
+ 作者：[owo](https://blog.o-w-o.cc)
+ 日期：2023/03/15
+ 授權：[CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/)
+ 參考文檔：[Effects — librosa 0.10.0 documentation](https://librosa.org/doc/0.10.0/effects.html)

## Overview
| Function | Description |
|----------|-------------|
| hpss(y, **kwargs) | Decompose an audio time series into harmonic and percussive components. |
| harmonic(y, **kwargs) | Extract harmonic elements from an audio time-series. |
| percussive(y, **kwargs) | Extract percussive elements from an audio time-series. |
| time_stretch(y, *, rate, **kwargs) | Time-stretch an audio series by a fixed rate. |
| pitch_shift(y, *, sr, n_steps[, ...]) | Shift the pitch of a waveform by n_steps steps. |
| remix(y, intervals, *[, align_zeros]) | Remix an audio signal by re-ordering time intervals. |
| trim(y, *[, top_db, ref, frame_length, ...]) | Trim leading and trailing silence from an audio signal. |
| split(y, *[, top_db, ref, frame_length, ...]) | Split an audio signal into non-silent intervals. |
| preemphasis(y, *[, coef, zi, return_zf]) | Pre-emphasize an audio signal with a first-order differencing filter. |
| deemphasis(y, *[, coef, zi, return_zf]) | De-emphasize an audio signal with the inverse operation of preemphasis(). |

## Harmonic and Percussive Source Separation
在音訊處理中，Harmonic-percussive source separation (HPSS) 是一種常用的技術，用於將音訊訊號區分為具有較強和較弱音高特徵的音訊元素，以及具有節奏和振幅變化的音訊元素。

+ `hpss(y)`：將聲音分成**諧波**和**打擊**部分
    + `harmonic`: 只回傳諧波部分
    + `percussive`: 只回傳打擊部分

## Time and frequency
+ `time_stretch(y, rate)`：時間拉伸
    + `rate`：拉伸倍率
    + 不會改變聲音的頻率
+ `pitch_shift(y, sr, n_steps)`：音高變換
    + `sr`：取樣頻率
    + `bins_per_octave`：每個八度的半音數，預設為12
    + `n_steps`：音高變換的半音數

## Miscellaneous
+ `remix(y, intervals)`：重新排列時間間隔
    + `intervals`：時間間隔
        + 例如： `array([[ 1536, 10752],[10752, 20480],...])`
+ `trim(y, top_db)`：去除開頭和結尾的靜音
    + `top_db`：靜音的閾值，預設為60
+ `split(y, top_db)`：將音訊分割為非靜音區間
    + `top_db`：靜音的閾值，預設為60
+ `preemphasis(y, coef)`：預強調
    + $y[n] = x[n] - \alpha x[n-1]$
    + `coef`：預強調係數，預設為0.97
+ `deemphasis(y, coef)`：反預強調
    + $y[n] = x[n] + \alpha y[n-1]$
    + `coef`：預強調係數，預設為0.97
