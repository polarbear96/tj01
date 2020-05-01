##                                                Pandas

> 以下内容节选自*简书*    网页链接： [Pandas教程](https://www.jianshu.com/p/3f852141764e) 

> Pandas是一种Python数据分析利器，一个开源的数据分析包，最初是应用于金融分析工具而开发出来的，因此Pandas为时间序列分析提供了很好的支持。Pandas是PyData项目的一部分。

**Series** 

```python
import numpy as np
import pandas as pd
import matplotlib

a = pd.Series([1,2,3,4,"hello",True])
# 通过数组创建一个系列，此时会自动提娜佳索引值，从0开始递增
print(a)

b = pd.Series(np.array([1,2,3,4,"world"]))
# 通过Ndarry创建一个系列，和通过数组创建的结果没什么区别
print(b)

c = pd.Series([1,2,3,4,5],index=["A","B","C","D","E"])
print(c)
# 创建一个系列并将其中的数据相应的index，此时A-E将成为5个数字的索引

d = pd.Series({"a":1, "b":2, "c":3})
print(d)
# 通过字典创建一个系列 ，key自动成为索引

f = pd.Series({"a":1, "b":2, "c":3}, index=["c","a","b","g"])
print(f)
# 通过字典创建序列并提供索引，和索引匹配的value会被依次拉出，"g"并没有匹配到字典中任何value,其value
# 自动取NaN.  注意NaN, 意为not a number，代表“不是数”，通常是除0错误而得到，然而虽然意为"不是数"
# 但它却属于浮点数(float)类型，这里dtype自动强转成float 
# 注意，如果这里字典中有一个value是string类型，那么dtype会自动转为object.
# 注意，如果series的第一个参数是list，那么index的list也要是同样长度，第一个是dict的话，index的
# list可以比dict长.

e = pd.Series(5, index=[1,2,3,4,5])
print(e)
# 这里是通过一个值而非可迭代对象来创建系列.看结果，不赘述

g = pd.Series([1,2,3,4,5],index=[2,4,1,6,8])
print(g[2], g[4], g[1], g[6], g[8])
# 要注意，只有在索引都是string的时候，g[int]才会被解释器认定为下标操作，e.g print(g[3]，index中不包含3，并且index不满足都是string这个要求，所以g[3]也不能作为下标记，程序直接挂）

h = pd.Series([1,2,3,4,5],index=["a","b","c","d","e"])
print(h[2])
# 此时2并没有在索引中出现，并且index都是string, 所以[2]被视为下标操作
print(h["a":"c"])
print(h["a":"d":2])
# 切片操作不赘述，一看就懂 注意下标操作只能取出value而没有索引，切片二者当然都会出现
print(h[["a","c"]])
# 这种取法也是一种切片，可以不连续的切.

"""
为了区分将运行结果用分割线分开 

0        1
1        2
2        3
3        4
4    hello
5     True
dtype: object
------------------------------------------
0        1
1        2
2        3
3        4
4    world
dtype: object
------------------------------------------
A    1
B    2
C    3
D    4
E    5
dtype: int64
-----------------------------------------
a    1
b    2
c    3
dtype: int64
----------------------------------------
c    3.0
a    1.0
b    2.0
g    NaN
dtype: float64
1    5
2    5
3    5
4    5
5    5
dtype: int64
----------------------------------------
1 2 3 4 5
----------------------------------------
3
a    1
b    2
c    3
dtype: int64
----------------------------------------
a    1
c    3
dtype: int64
--------------------------------------
a    1
c    3
dtype: int64
"""
```

**Series的运算**

```python
import pandas as pd
import numpy as np
import math

P = pd.Series([1, 2, 3, 4], index=["a", "b", "c", "d"])
print(P + 10)  # series和一个数字进行加减乘除很简单，不赘述
print("*" * 100)
print(P[P > 2])     # series有一个很trick的用发就是可以当作一个引用value的变量
print("*" * 100)     
m = [1, 3, 5]
n = np.array([1, 3, 5])
print(np.exp(m), "--", np.exp(n))  
# np.abs, np.exp等np中的函数都可以对list或者ndarray型数据中的元素集体操作
# 但是math中的函数不可以，e.g    此处用math.fabs(m) 会报错

print("*" * 100)
serA = pd.Series([1, 2, 3], index=['a', 'b', 'c'])
serB = pd.Series([4, 5, 6], index=['b', 'c', 'd'])
print(serB + serA)
# 两个series之间的运算满足


"""
运行结果：
a    11
b    12
c    13
d    14
dtype: int64
****************************************************************************************************
c    3
d    4
dtype: int64
****************************************************************************************************
[  2.71828183  20.08553692 148.4131591 ] -- [  2.71828183  20.08553692 148.4131591 ]
****************************************************************************************************
a    NaN
b    6.0
c    8.0
d    NaN
dtype: float64
"""
```

**DataFrame** 

```python
# 用字典创建一个DataFrame

import pandas as pd
import numpy as np

a = [1,3]
print(a * 2)
df2 =pd.DataFrame({'A' : 1.,
   'B': pd.Timestamp('20130102'),
   'C': pd.Series(1, index=[5,6,7,8], dtype='float32'),
   'D': np.array([3]*4,dtype='int32'),
   'E': pd.Categorical(["test","train","test","train"]),
   'F':'foo' })

print(df2)

"""
输出结果：
[1, 3, 1, 3]
     A          B    C  D      E    F
5  1.0 2013-01-02  1.0  3   test  foo
6  1.0 2013-01-02  1.0  3  train  foo
7  1.0 2013-01-02  1.0  3   test  foo
8  1.0 2013-01-02  1.0  3  train  foo

首先注意list * n是将列表中的元素重复n遍，并不是变成了n个列表
这里用字典创建了一个DataFrame  
key变成了列标 vlaue成为了具体的column value. 对于1和20130102显然要自动扩展成4个  
至于行标，这里由于C的value是一个series,所以沿用其索引作为行标
如果将"C"以及它对应的series删除那么显然行标从0开始自动填充
"""

```

```python
# 用列表创建一个DataFrame
import pandas as pd

data = [1,2,3,4]
df02 = pd.DataFrame(data)
print(df02)

"""
结果：
   0
0   1
1   2
2   3
3   4

"""
 
# 用字典列表创建DataFrame
data1 = {'Name':['Tom','Jack','Steve'],'Age':[19,18,20]}
#指定行索引和列索引
df04 = pd.DataFrame(data1,index = ['rank1','rank2','rank3'],columns = ['Name','Age','Sex'])
print(df04)

"""
运行结果：
        Name  Age  Sex
rank1    Tom   19  NaN
rank2   Jack   18  NaN
rank3  Steve   20  NaN

即，pd.DataFrame接受index和columns参数，二者分别设置DataFrame的行标和列标.
"""

# 从系列字典创建数据帧
data2 = {
    'one':pd.Series([1,2,3],index = ['a','b','c']),
    'two':pd.Series([1,2,3,4],index = ['a','b','c','d'])
}
df06 = pd.DataFrame(data2)
print(df06)


```



**DataFrame数据操作**

```python
# 列的增删改

import pandas as pd

data = {
    'one':pd.Series([1,2,3],index = ['a','b','c']),
    'two':pd.Series([1,2,3,4],index = ['a', 'b', 'c', 'd'])
}
df06 = pd.DataFrame(data)
print(df06['one'])
print("*" * 100)
# 增加列：
df06["three"] = pd.Series([1,9,6], index=["a", "b", "c"])
print(df06)
print("*" * 100)
# 修改列：
df06["two"] = pd.Series([1, 3, 5], index=["a", "b", "d"])
print(df06)
print("*" * 100)
# 删除列：
df06.pop("three")
print(df06)


"""
运行结果：
a    1.0
b    2.0
c    3.0
d    NaN
Name: one, dtype: float64
*******************************************************************************************
   one  two  three
a  1.0    1    1.0
b  2.0    2    9.0
c  3.0    3    6.0
d  NaN    4    NaN
*******************************************************************************************
   one  two  three
a  1.0  1.0    1.0
b  2.0  3.0    9.0
c  3.0  NaN    6.0
d  NaN  5.0    NaN
******************************************************************************************
   one  two
a  1.0  1.0
b  2.0  3.0
c  3.0  NaN
d  NaN  5.0

注意一个很重要的细节：DataFrame一旦确定之后，对其进行的增删改操作并不会对此DataFrame的行标和列表产生影响，影响的只是具体的值. 即行标列表不会随着增删改操作而更新自己的行标和列标.
"""

```



```python
# DataFrame基础的行列索引以及利用loc来索引

import pandas as pd
data = {
    'one':pd.Series([1,2,3],index = ['a','b','c']),
    'two':pd.Series([4,5,6,7],index = ['a', 'b', 'c', 'd']),
    "three" : pd.Series([5,6,7,8], index=["a", 'b', 'c', 'd'])
}

df = pd.DataFrame(data)
print(df['one'])   # 选取一列，成一个series      [1]
print("*" * 100)
print(df[['two']])  # 选取一列，成为一个dataframe   [2]
print("*" * 100)
print(df[['two','three']]) # 选取多列，成为一个DataFrame, 多列名字要放在list里  [3]
print("*" * 100)
print(df[0:])  #第0行及之后的行，相当于df的全部数据，注意冒号是必须的
print("*" * 100)
print(df[0:1]) #第0行
print("*" * 100)
print(df[1:3]) #第1行到第2行（不含第3行）
# print(df[1])                            [4] 报错
# print(df[['one': "three"]])             [5] 报错
# print(df["one" : "three"])              [6] 空列表

# loc的使用
print(">" * 80)
print(df.loc["a",'one'])  # 单纯的得到一个元素
print(">" * 80)
print(df.loc["a":"c", ['one','two']])
print(">" * 80)          # [7] 选取第1行到第3行，one列和two列的数据, 注意这里的行选取是包含下标的
print(df.loc[["a","c"],'one'])         # 选取指定的第1行和第3行，one列的数据
print(">" * 80)
print(df.loc[df['two']==4,'three'])   # [8] 得到一个series，因为满足df["two"==4]条件的可能有多行
print(">" * 80)

"""
运行结果：

a    1.0
b    2.0
c    3.0
d    NaN
Name: one, dtype: float64
***************************************************************************************
   two
a    4
b    5
c    6
d    7
****************************************************************************************
   two  three
a    4      5
b    5      6
c    6      7
d    7      8
***************************************************************************************
   one  two  three
a  1.0    4      5
b  2.0    5      6
c  3.0    6      7
d  NaN    7      8
*****************************************************************************************
   one  two  three
a  1.0    4      5
******************************************************************************************
   one  two  three
b  2.0    5      6
c  3.0    6      7
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
1.0
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
   one  two
a  1.0    4
b  2.0    5
c  3.0    6
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
a    1.0
c    3.0
Name: one, dtype: float64
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
a    5
Name: three, dtype: int64
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# 自带的基础操作(不使用函数)
注意[1]处的索引方式得到的是series, 而[2], [3]处得到的DataFrame, 此外，对于行的切片操作得到的也是DataFrame
对比之前对series的操作，[1]处这种写法会得到单纯的数值，[2]处会得到series. (对比记忆比较容易)
[4] [5] [6]处的写法会报错，其中[5][6]报错是因为DataFrame的列不支持切片操作（除非用iloc）
对于行的切片除了用数字以外还可以用index的名称，并且此时末位下标是可以取到的
注意，基础的索引操作每次只能操作行或者列，并不能同时操作

注意loc的使用，接受的参数可以同时对行和列进行索引:
  对行进行索引可以使用 1.单行的名称 2.多行的名称 3.行的切片  其中只有第2中需要加[],连切片都不用加[]
  对列进行索引可以使用 1.单列的名称 2.多列的名称 其中第2种需要加[]
  当参数为单行单列时单纯的获取一个元素值
  当列索引为单列，行索引为多行名称或者切片时  返回一个series
  当行索引为单行，列索引为多列时，返回一个series
  当行索引不为单行并且列索引不为单列时，返回一个DataFrame
  
[7]处注意，是可以取到末位的下标的
[8]处，这种trick的用法也是可以的.
"""
```



```python
# DataFrame中利用iloc索引  
# 注意loc只能用名称索引，以上面代码中30row为例：print(df.loc["a":"c", ['one','two']])
# 将"a":"c"写为数字切片是会报错的   而iloc相反，完全接受数字作为参数而非名称

print(df.iloc[1,2])
print(df.iloc[[1,3],0:2])
print(df.iloc[1:3,[1,2]])

# 第一句返回第2行第3列的数值
# 第二句返回第2、4行中第1列和第2列的值  （组成一个DataFrame）
# 第三句不赘述
```



**赋值（缺省值NaN处理方法）** 及以下的部分没看  暂时只了解基础知识，没有深度了解的需求，不花时间.



##                                                    Numpy

> Numpy是一个开源的Python科学计算库，它是python科学计算库的基础库，许多其他著名的科学计算库如Pandas，Scikit-learn等都要用到Numpy库的一些功能。

**Numpy数组的优势:**

- Numpy数组通常是由相同种类的元素组成的，即数组中的数据项的类型一致。这样有一个好处，由于知道数组元素的类型相同，所以能快速确定存储数据所需空间的大小。
- Numpy数组能够运用向量化运算来处理整个数组，速度较快；而Python的列表则通常需要借助循环语句遍历列表，运行效率相对来说要差。
- Numpy使用了优化过的C API，运算速度较快



```python
# 基于list 和 tuple创建一维数组
import numpy as np

# 基于list
arr1 = np.array([1,2,3,4])
print(arr1)

# 基于tuple
arr_tuple = np.array((1,2,3,4))
print(arr_tuple)

# 二维数组 (2*3)
arr2 = np.array([[1,2,4], [3,4,5]])
print(arr2)

"""
运行结果：
[1 2 3 4]
[1 2 3 4]
[[1 2 4]
 [3 4 5]]
"""



# 基于arange创建一维数组
import numpy as np

# 一维数组
arr1 = np.arange(5)
print(arr1)

# 二维数组
arr2 = np.array([np.arange(3), np.arange(3)])
print(arr2)

"""
运行结果：
[0 1 2 3 4]
[[0 1 2]
 [0 1 2]]
"""



# 基于arange和reshape创建
import numpy as np

arr = np.arange(24).reshape(2,3,4)
print(arr)

"""
运行结果：
[[[ 0  1  2  3]
  [ 4  5  6  7]
  [ 8  9 10 11]]

 [[12 13 14 15]
  [16 17 18 19]
  [20 21 22 23]]]
  
  这里2,3,4的意义一目了然
"""

# 用random函数创建  略
```



**Numpy的数据类型包括Bool int8 int16 int 32 int64 unit8 unit16 unit32 unit64 float16 float32 float64 complex64 complex128  数据之间可以进行相互转换(复数和实数之间不能相互转换)**  



```python
# numpy数组的属性

import numpy as np

print(np.int8(12.334))
print(np.float64(12))
a = np.arange(5, dtype=float)
print(a)
b = np.array([1,2,3], dtype=float)
print(b)
c = np.arange(24).reshape(2, 3, 4)
print(c)
# c.shape返回一个tuple ndim是数组维度 size是元素个数 itemsize是每个元素占用字节数
print(c.shape, c.ndim, c.size, c.itemsize)
print("*" * 80)
d = np.arange(12).reshape(2,6)
print(d)
# d.T是d的转置
print("d的转置", d.T)

"""
输出结果：

12
12.0
[0. 1. 2. 3. 4.]
[1. 2. 3.]
[[[ 0  1  2  3]
  [ 4  5  6  7]
  [ 8  9 10 11]]

 [[12 13 14 15]
  [16 17 18 19]
  [20 21 22 23]]]
(2, 3, 4) 3 24 4
********************************************************************************
[[ 0  1  2  3  4  5]
 [ 6  7  8  9 10 11]]
d的转置 [[ 0  6]
 [ 1  7]
 [ 2  8]
 [ 3  9]
 [ 4 10]
 [ 5 11]]
"""

```





[numpy数组-简书](https://www.jianshu.com/p/60bf50100c2f) 