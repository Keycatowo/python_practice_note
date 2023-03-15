# 00-PyTorchFundamentals

## 本章節目錄(Table of contents)
+ [Tensor介紹(Introduction to tensors)](#tensor介紹introduction-to-tensors)
+ [建立Tensor(Creating tensors)](#建立tensorcreating-tensors)
+ [從Tensor獲得資訊(Getting information from tensors)](#從tensor獲得資訊getting-information-from-tensors)
+ [操控Tensor(Manipulating tensors)](#操控tensormanipulating-tensors)
+ [Tensor的形狀(Dealing with tensor shapes)](#tensor的形狀dealing-with-tensor-shapes)
+ [Tensor的索引(Indexing on tensors)](#tensor的索引indexing-on-tensors)
+ [混合PyTorch tensors和NumPy(Mixing PyTorch tensors and NumPy)](#混合pytorch-tensors和numpymixing-pytorch-tensors-and-numpy)
+ [再現性(Reproducibility)](#再現性reproducibility)
+ [在GPU上執行(Running tensors on GPU)](#在gpu上執行running-tensors-on-gpu)


## Tensor介紹(Introduction to tensors)
+ tensor是機器學習和深度學習的基本組成元素
+ tensor可以表示幾乎任何類型的資料(圖像、文字、數字表格)
+ 例如：圖像可以用tensor表示，圖像的高度、寬度、顏色通道數量

> Tensor是什麼：[What's a Tensor? - YouTube](https://www.youtube.com/watch?v=f5liqUk0ZTw)
> ![](https://i.imgur.com/UDZXmkb.png)

## 建立Tensor(Creating tensors)
+ 用`torch.tensor()`建立一個tensor
+ 其中比較特別的幾個dim有特殊的名稱
    + 0-dim tensor(scalar)
    + 1-dim tensor(vector)
    + 2-dim tensor(matrix)
```python
scalar = torch.tensor(4)
vector = torch.tensor([1, 2, 3, 4])
matrix = torch.tensor([[1, 2, 3], [4, 5, 6]])
tensor = torch.tensor([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
```

## 從Tensor獲得資訊(Getting information from tensors)
+ `.shape`：獲得tensor的形狀
    + 即每一層`[]`所包含的元素個數
    + 例如：`torch.Size([2, 3])`
+ `.ndim`：獲得tensor的維度
    + 即`[]`最深的層數
    + 例如：`2`
+ `.numel()`：獲得tensor的元素個數，例如：`6`
    + `numel`是`number of elements`的縮寫
    + 例如：`torch.Size([2, 3])`的元素個數為`2*3=6`
+ `.dtype`：獲得tensor的資料型態
    + 例如：`torch.int64`
    + 其他資料型態：[torch.dtype](https://pytorch.org/docs/stable/tensors.html#torch-tensor-dtype)
+ `.device`：獲得tensor的裝置
    + 例如：`cpu`
    + 其他裝置：[torch.device](https://pytorch.org/docs/stable/tensor_attributes.html#torch.device)


```python
# shape
print(scalar.shape) # torch.Size([])
print(vector.shape) # torch.Size([4])
print(matrix.shape) # torch.Size([2, 3])
print(tensor.shape) # torch.Size([2, 2, 3])

# ndim
print(scalar.ndim) # 0
print(vector.ndim) # 1
print(matrix.ndim) # 2
print(tensor.ndim) # 3

# numel
print(scalar.numel()) # 1
print(vector.numel()) # 4
print(matrix.numel()) # 6
print(tensor.numel()) # 12

# dtype
print(scalar.dtype) # torch.int64

# device
print(scalar.device) # cpu
```

## 操控Tensor(Manipulating tensors)
### 基本操作(Basic operations)
+ 加法(Addition)
    + `torch.add(tensorA, tensorB)`
    + `tensorA + tensorB`
+ 減法(Subtraction)
    + `torch.sub(tensorA, tensorB)`
    + `tensorA - tensorB`
+ 乘法(Multiplication)
    + `torch.mul(tensorA, tensorB)`
    + `tensorA * tensorB`
+ 除法(Division)
    + `torch.div(tensorA, tensorB)`
    + `tensorA / tensorB`

### 矩陣運算(Matrix operations)
+ 轉置(Transpose)
    + `torch.t(tensor)`
    + `tensor.t()`
    + `tensor.T`
+ 矩陣乘法有多種不同的類型
    + 逐元素相乘(Element-wise Multipulation)
        + `torch.mul(tensorA, tensorB)`
        + `tensorA * tensorB`
        + 兩個矩陣維度必須相同，輸出為相同維度的矩陣
    + 矩陣乘法(Matrix Multipulation)
        + `torch.matmul(tensorA, tensorB)`
        + 等價於`tensorA @ tensorB`
            + 只有兩維時候可以簡化成：`torch.mm(tensorM, tensorN)`
        + 若為$M_{a,b}, N_{b,c}$相乘，會得到$R_{a,c}$
        + > Shape Error是做tensor計算時候最常出現的錯誤
    + 批量矩陣乘法(Batch Matrix Multipulation)
        + `torch.bmm(tensorA, tensorB)`
        + 若為$M_{b,m,n}, N_{b,n,p}$相乘，會得到$R_{b,m,p}$

## Tensor的形狀(Dealing with tensor shapes)

## Tensor的索引(Indexing on tensors)

## 混合PyTorch tensors和NumPy(Mixing PyTorch tensors and NumPy)

## 再現性(Reproducibility)

## 在GPU上執行(Running tensors on GPU)



| **Topic** | **Contents** |
| ----- | ----- |
| **Introduction to tensors** | Tensors are the basic building block of all of machine learning and deep learning. |
| **Creating tensors** | Tensors can represent almost any kind of data (images, words, tables of numbers). |
| **Getting information from tensors** | If you can put information into a tensor, you'll want to get it out too. |
| **Manipulating tensors** | Machine learning algorithms (like neural networks) involve manipulating tensors in many different ways such as adding, multiplying, combining. | 
| **Dealing with tensor shapes** | One of the most common issues in machine learning is dealing with shape mismatches (trying to mixed wrong shaped tensors with other tensors). |
| **Indexing on tensors** | If you've indexed on a Python list or NumPy array, it's very similar with tensors, except they can have far more dimensions. |
| **Mixing PyTorch tensors and NumPy** | PyTorch plays with tensors ([`torch.Tensor`](https://pytorch.org/docs/stable/tensors.html)), NumPy likes arrays ([`np.ndarray`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html)) sometimes you'll want to mix and match these. | 
| **Reproducibility** | Machine learning is very experimental and since it uses a lot of *randomness* to work, sometimes you'll want that *randomness* to not be so random. |
| **Running tensors on GPU** | GPUs (Graphics Processing Units) make your code faster, PyTorch makes it easy to run your code on GPUs. |