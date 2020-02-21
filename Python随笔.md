##                                                                                     Python随笔[^1] 



### 类对象、实例对象、类属性、实例属性、静态方法

```python
class Province(object):
    #类属性
    country = "中国"
    
    def __init__(self, name):
    #实例属性
    self.name = name
    
# 创建一个实例对象
obj = Province("山东省")
# 通过实例对象访问实例属性
print(obj.name)
# 通过类对象访问类属性
Province.country

```





​                        ![1582204270961](C:\Users\ton\AppData\Local\Temp\1582204270961.png) 

一个类在实例化的时候实际上做了两件事：

1 \__new__ ()方法 ：创建对象，通俗点说：产生一个存放实例对象的空间(在实例化的时候默认执行，不用写)

2 \__init__ ()方法 ： 对刚刚申请的空间，进行初始化 （实例化之后立即运行，运行时间在\_\_new__()之后）

**二者合在一起完成了构造方法的功能**

 

> ​        类对象只有一个，可以以类对象为模板产生n个实例对象；实例对象的存储空间中存储着\__class__()方法，它可以返回创建该对象的类，通过这个指向让二者的内存产生关联，从而可以访问到存储在类对象中的类属性(图中的country属性).  

**对于类属性 类对象和实例对象都可以访问**      

**对于实例属性 实例对象可以访问 类对象无法访问**

**显然， 通常将公有的属性作为类属性，私有的属性作为实例属性** 



> 以上面为例，通过实例对象改变类属性.     1. obj.country="美国"  这种写法会产生一个新的实例变量，而此实例变量和类变量并无交集，所以无法改变.   2. obj.\__class__().country = "美国"   这样当然会改变类属性 



```python
class Foo(object):
    def __init__(self, name):
        self.name = name
    
    #实例方法
    def ord_func(self):
        print("实例方法")
        
    #类方法
    @classmethod
    def class_func(cls):            # 有classmethod就要有cls参数(类参数)，二者捆绑的        
        print("类方法")            
        
    @staticmethod
    def static_func():
        print("静态方法")
        
f = Foo("中国)

f.ord_func()

Foo.class_func()
        
Foo.static_func()
        
```



- **类方法可以被类对象调用，可以被实例对象调用(和类属性类似，类属性也是可以被实例对象调用)**

- **类方法的定义中要用cls参数才行，类似于实例变量的定义中要有self** 

- **静态方法可以被类对象调用，也可以被实例对象调用, 但是当然无法直接调用(直接写static_func())**

- **在类对象的定义中，一个函数不接受任何参数而且没设置成静态方法，那么它将形同虚设，没有意义.**

- **可见实例方法可以调用类定义中的一切方法(前提是方法的定义合法)**

  ​

  ​

  ​

###                                              property属性

```python
class Goods(object):
    
    def __init__(self):
        self.original_price = 100
        self.discount = 0.8
        
    @property
    def price(self):
        new_price = self.original_price * self.discount
        return new_price
        
    @price.setter                      # @property下的函数名.setter 
    def price(self, value)
        self.original_price = value
        
    @price.deleter
    def price(self):
        del self.original_price
        
obj = Goods()
obj.price      #触发第一个函数
obj.price = 200   #触发第二个函数
del obj.price    #触发第三个函数
```

-  property属性可以让实例方法像实例属性一样被调用，不用加括号. 
-  obj.price = 200 触发第二个函数，200被传递给value
-  del obj.price触发第三个函数， obj.price会被删除
-  注意@property下的函数为price,  所以这里要写为price.setter     price.deleter  





**创建property属性的方法一共有两种，一种是上述的装饰器方法，另一种是用类属性的方法创建property属性**



property方法中有四个参数

- 第一个参数是方法名，调用 对象.属性 时自动触发执行方法
- 第二个参数是方法名， 调用 对象.属性 = XXX 时自动触发执行方法
- 第三个参数是方法名， 调用 del 对象.属性 时自动触发执行方法
- 第四个参数是字符串， 调用  对象.属性.\__doc__     此参数是该属性的描述信息



```python
class Foo(object):
    def get_bar(self):
        print("getter...")
        return 'laowang'
        
    def set_bar(self, value):
        print("setter ...")
        return 'set value' + value
        
    def del_bar(self):
        print("deleter...")
        return 'laowang'
        
    BAR = property(get_bar, set_bar, del_bar, "description...")
    
obj = Foo()

obj.BAR                              #自动调用get_bar
obj.BAR = "alex"                     #自动调用set_bar
desc = Foo.BAR.__doc__               #获取第四个参数的值
print(desc)    
del obj.BAR                          #自动调用del_bar
```







### 魔法属性

**\__doc__   表示类的描述信息**

**\__module__    表示当前操作的对象在哪个模块**

**\__class__          表示当前操作的对象的类是什么**

```python
from test import Person

obj =  Person()
print(obj.__module__)            # 输出test
print(obj.__class__)             # 输出test.Person

```



**\__init__略**    

**\__del__( 当对象在内存中被释放时，自动触发执行**

*注: 此方法一般无需定义，因为python是一门高级语言，程序员在使用时无需关心内部的分配和释放，因为此工作都是交给python解释器来执行，所以，\__del__的调用方法是==由解释器在进行垃圾回收时自动触发执行的==*

**\__call__                暂略**

**\__dict__                以字典形式返回类或对象中的所有属性**

**\__str__                  如果一个类中定义了\_\_str__ 方法，那么在打印对象或者获得对象的描述时，默认调用返回值**

e.g.

```python
class Foo:
    def __str__(self):
        return 'hello!'
        
obj = Foo()
print(obj)                        # 输出hello, world!
new_s = "%s world!" % obj         # new_s 将等价于 "hello! world!"
print(new_s)                      # 输出hello! world!
```

demo一看就懂，不赘述



----



### **关于GIL锁：** 

**1. GIL(全局解释器锁)和python没关系，仅仅是由于历史原因在Cpython解释器，难以移出GIL**

**2. 每个线程在执行时都需要获取GIL，保证同一时刻只有一个线程可以执行代码**

**3.  线程释放GIL锁的情况：在IO操作等可能引起阻塞的system call之前可以暂时释放GIL，并在执行结束后重新获取GIL，python3.x使用计时器(执行时间达到阈值后释放GIL)**

**4. python的多进程是可以真正利用CPU的多核资源的(并行)**

**5. jpython解释器则不存在GIL锁的问题，其多线程是并行，然而通常下载的Python默认用的是Cpython解释器(官网推荐)**

**6. 对于计算密集型代码用多线程并无优势，但对于IO密集型代码用多线程比较高效. 计算密集型：多进程；IO密集型：多线程(or 携程)**

**7. ** **如果想要让python的多线程称为真正的并行，除了更换解释器之外还可以在python代码中的线程中引入其它语言的代码(python中调用C C++ Java javascript等是没问题。**



### **关于浅拷贝和深拷贝：**

![img](file:///C:\Users\ton\AppData\Local\Temp\ksohtml9124\wps1.png) 

![img](file:///C:\Users\ton\AppData\Local\Temp\ksohtml9124\wps2.png) 

![img](file:///C:\Users\ton\AppData\Local\Temp\ksohtml9124\wps3.png) 

不赘述，看图。另外注意list的切片操作和字典的copy方法(如a.copy(),a为字典)都属于浅拷贝。

### **关于类和私有变量：**

![img](file:///C:\Users\ton\AppData\Local\Temp\ksohtml9124\wps4.jpg)   ![img](file:///C:\Users\ton\AppData\Local\Temp\ksohtml9124\wps5.jpg)

类定义中没用self的变量可以被类和实例访问到，用self声名的变量只能被实例访问，所以截图中第三个print语句会出错。   实际运用中若希望各个实例可以获得不同的属性值，那么用self声名，反之直接声名。

 

**用双下划线和但下划线命名的变量为私有变量**

_x : import a后欲用其中的变量或函数需要写a.xxx的形式，from a import *则可以让代码中免写模块名，相当于把a中所有对象都导入，然而并不能导入以下划线开头的变量(但是以其它形式导入是完全没问题的)  plus: *同样无法导入双下划线开头的变量：__x，__x__,**即只要是以下划线开头的变量都无法通过这种方法导入**，**但是注意若变量在类定义中，则是可以导入这个类，其使用也完全不受影响**。  **注意__x__并不是私有变量，在子类可以使用，也可以在类定义外通过 .__x__获取 （已测试）。** 

__x: 如图，__name经过了命名重整化，无法在类定义之外通过a.name获得，如果我们直接在外部写上对a.name(类定义中没提到的变量在其外部直接写是没问题的)的赋值语句就相当于增加了另一个变量，不会对它产生影响，但是我们可以通过其他方式获取到(如图中的__Test__name)

![img](file:///C:\Users\ton\AppData\Local\Temp\ksohtml9124\wps6.png) 

 

----

----





 



[^1]: **以上节选自 04-python高级语法v3.1**   其中04-方法解析顺序表MRO完全未看  06/04-with、上下文管理器未看 .