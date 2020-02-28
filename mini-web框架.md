

#                             mini-web框架

## 02 闭包

```python
def line_6(k, b):
	def create_y(x):
		print(k*x+b)
	return create_y


line_6_1 = line_6(1, 2)
line_6_1(0)
line_6_1(1)
line_6_1(2)
line_6_2 = line_6(11, 22)
line_6_2(0)
line_6_2(1)
line_6_2(2)

# 外部的k,b参数是可以传到闭包内部的，因为闭包内部找不到k,b它会先在外面包裹的函数中寻找.
# 可见闭包的使用可以和面对对象很相似  
```

**修改闭包中数据** 

```python
x = 100
def double():
    x = 200
    print(x) 
double()        # 输出200，这里函数内的定义相当于是声明了一个局部变量，并非修改全局变量 
---------------------------------------------------------------------------------------------
x = 300
def test1():
	x = 200
	def test2():
		print("----1----x=%d" % x)
	return test2

t1 = test1()
t1()                # 同样的道理，这里会输出200而非300
--------------------------------------------------------------------------------------------

def test1():
    x = 200
    def test2():
        nonlocal x
        x = 100
        print("----1----x=%d" % x)
    return test2

t1 = test1()
t1()
# 此时输出为100 ，nonlocal可以指定参数为上一级变量。  
# 默认情况下闭包中内嵌函数只能读取上一级的参数而不能修改，通过nonlocal声名可以修改其值
```



## 03 装饰器

**无参无返回值：** 

```python
def set_func(func):
	def call_func():
		print("---这是权限验证1----")
		print("---这是权限验证2----")
		func()
	return call_func  # 等价于test1 = set_func(test1) 

@set_func
def test1():
	print("-----test1----")

test1()

# 无参无返回值函数
```



```python
import time

def set_func(func):
	def call_func():
		start_time = time.time()
		func()
		stop_time = time.time()
		print("alltimeis %f" % (stop_time - start_time))
	return call_func

@set_func  # 等价于test1 = set_func(test1) 
def test1():
	print("-----test1----")
	for i in range(10000):
		pass

test1()


# 此装饰器可以统计函数执行所耗费的时间
```

**有参无返回值：**

```python
def set_func(func):
    # print("装饰完毕")                    # [0]
	def call_func(num):                   # [1]
		print("---这是权限验证1----")
		print("---这是权限验证2----")
		func(num)                         # [2]
	return call_func

@set_func  # 等价于test1 = set_func(test1)   
def test1(num):
	print("-----test1----%d" % num)      # [3]

test1(5)

# 计算结果：
# ---这是权限验证1----
# ---这是权限验证2----
# -----test1----5
# [1] [2]处的的num显然可以统一换成其它形参
# 装饰器在函数调用之前就已经装饰完毕，即在[3]处已经完成了对test1的装饰，此时若[0]处未被注释那么就会打印出[0]的内容
```

**对不定长参数的函数进行装饰：** 

```python
def set_func(func):
    def call_func(num, *args, **kwargs):   # [1]
        print("---这是权限验证1----")
        print("---这是权限验证2----")
        func(num, *args, **kwargs)         # [2]

    return call_func

@set_func
def test1(num, *args, **kwargs):           
    print("-----test1----%d" % num)
    print("-----test1----", args)
    print("-----test1----", kwargs)

test1(100, 200, 300, mm = 100)             # [4]

# 这里[1],[2]处的不定长参数和关键字参数同样需要加*，原因很简单.
# 注意一个细节，这里[4]处的mm会自动转成字典中的"mm"
# 这里的call_func函数可以直接写为：
#    def call_func(*args, **kwargs):   
#        print("---这是权限验证1----")
#        print("---这是权限验证2----")
#        func(*args, **kwargs)
#    即这两个不定长参数其实可以适用于装饰带参数的函数和不带参数的函数(一切函数，用这俩就够了)
```

**对有返回值的函数进行装饰** 

```python
def set_func(func):
    def call_func(*ars, **kwargs):
        print("---这是权限验证1----")
        print("---这是权限验证2----")
        return func(*ars, **kwargs)     # [1]

    return call_func

@set_func
def test1(num, *args, **kwargs):
    print("-----test1----%d" % num)
    print("-----test1----", args)
    print("-----test1----", kwargs)
    return "ok!"

ret = test1(100)
print(ret)

# 以上是通用装饰器写法
# [1]处需要写return，否则set_func无法取到func的返回值，所以return也是通用装饰器的写法

```



**多个装饰器对同一个函数进行装饰：** 

```python
def add_qx(func):
	print("---开始进行装饰权限1的功能---")
	def call_func(*args, **kwargs):
		print("---这是权限验证1----")
		return func(*args, **kwargs)
	return call_func


def add_xx(func):
	print("---开始进行装饰xxx的功能---")
	def call_func(*args, **kwargs):
		print("---这是xxx的功能----")
		return func(*args, **kwargs)
	return call_func


@add_qx
@add_xx
def test1():
	print("------test1------")

test1()

# 执行结果：
# ---开始进行装饰xxx的功能---
# ---开始进行装饰权限1的功能---
# ---这是权限验证1----
# ---这是xxx的功能----
# ------test1------

# 可见最后的效果是先装饰写在后面的装饰器，执行的时候却是写在前面的装饰器先执行，追后再调用原函数
# 以上对于两个以上的装饰器装饰同一个函数仍然成立.
```

**demo:** 

```python
def set_func_1(func):
	def call_func():
		# "<h1>haha</h1>"
		return "<h1>" + func() + "</h1>"
	return call_func

def set_func_2(func):
	def call_func():
		return "<td>" + func() + "</td>"
	return call_func


@set_func_1
@set_func_2
def get_str():
	return "haha"

print(get_str())

# 结果： <h1><td>haha</td></h1>
# 这里注意装饰器中<h1>等标签需要写在return内部，否则显然达不到目的.

```

**使用类作为装饰器** 

```python
class Test(object):
	def __init__(self, func):
		self.func = func

	def __call__(self):
		print("这里是装饰器添加的功能.....")
		return self.func()


@Test  # 相当于get_str = Test(get_str)，创建了一个实例方法，get_str作为参数传给__init__中func
def get_str():
	return "haha"

print(get_str())

# 输出：
# 这里是装饰器添加的功能.....
# haha

# 了解一下即可，实际运用可能不多.
```









## 06 元类

**python中万物皆对象，这里对于对象的定义是：**

1. **你可以将它赋值给一个变量**
2. **你可以拷贝它**
3. **你可以为它增加属性**
4. **你可以将它作为函数参数进行传递**

   **python中类也是对象**

   

​        **python解释器在运行起来时会默认加载内建模块，可以直接使用的print函数，input函数等就在其中，可以用`print(globals())` 来显示当前的全局变量，其中的\_\_builtin\_\_就是内建模块** 

​         **ipython中内嵌了sqlite数据库(sqlite不需要服务器，直接使用软件操纵数据库)** 



​        **当定义一个函数，类，全局变量时，其实就是创建了一个"对象"，然后在globals获取的这个字典中添加一个名字让这个名字指向刚刚创建的对象而已**  

​        **元类是python中的万物之母，创造一切.**      

​        **元类创建类，类创建实例对象，**

​         **type除了可以得到一个对象的类型以外，还可以动态的创建类，即接受一个类的描述作为参数，然后返回一个类：`type(类名，由父类名称组成的元组(针对继承的情况，可以为空)，包含属性的字典(名称和值))`,  e.g.  **

```python
class test2()
    num = 100
    num2 = 200
# 等价于：
test2 = type("test2",(),{"num":100,"num2":200})
# 这里等号左边的test2只是名称而已可以随意更改，但是一般将等号左右两边的变量名设置为相同

class test22(test2):
    pass
# 等价于：
test22 = ype("test22",(test2,),{})
# 注意这里第二个参数是tuple,逗号不要丢，第三个参数是字典，即使为空也要写上空字典

# 用元类定义实例方法：
def test_2:(self):
    print("实例方法")
@classmethod
def test_3(cls):
    print("类方法")
@staticmethod
def test_4():
    print("静态方法")   
Test = type("Test",(),{"test_2":test_2,"test_3":test_3,"test_4":test_4})

```

plus一个细节：

```python
a = {}
a[1] = 1
a[2] = 2
print(a)
# 结果：
{1: 1, 2: 5}
# 但是对列表这么用会报错
```

==元类的使用极少，了解一下即可== 