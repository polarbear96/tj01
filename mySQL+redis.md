#                                                                 mySQL笔记



## 数据库的基本使用



## 01/02(言之无物，浪费时间)

 

**mySQL是一个关系型数据库管理系统，是开源的，支持多种操作系统，为多种语言提供API. 被oracle收购.** 

 

==**列>字段(如果能够唯一标记某个字段那么就是主键) 行>记录**==    

 

## 03 RDBMS(关系型数据库管理系统)

 

mySQL一般用来做网站

mongoDB一般用来做爬虫

(Oracle是做大型网站的，了解一下)

04-MySQL服务器、客户端安装及使用



## 04 MySQL服务器、客户端安装及使用

> 注意 服务器和客户端同时下载，MySQL有两种客户端：图形界面(Navicat) 和 命令行 
>
>  命令行默认连接本地服务器，所以省去了连接服务器的操作，直接输入数据库密码即可.
>
> 但是要知道数据库是可以通过ip和端口远程连接的。

  ==通过window+r，在弹窗中输入services.msc, 之后在弹出来的程序中找到以mysql开头的条目,将其启动，服务器便处于开启状态，之后才可以通过在命令行输入密码连接==  

```password
我的MySQL密码为science8863Vc
oracle的注册密码似乎也是这个.
```



## 05 Navicat操作数据库

**略** 



 

## 07数据库的操作

 

mySQL语句中中只要没加分号认定此句未结束，回车后不会弹出执行结果，一直到输入分号为止：



![1581753564743](C:\Users\ton\AppData\Local\Temp\1581753564743.png)

   

`select now(); 和select version();分别显示当前时间和mySQL的版本，了解一下即可` 

`show databases可以显示当前的数据库`     **注意只有此句database加了s, 并且注意此句databases后无括号**

`create database python01 charset=utf8;创建数据库`     **注意utf8不要写成utf-8，此外这里charset不写的话有可能导致中文字符的乱码** 

`drop database python01 删除python01数据库  ` 



## 08数据表的操作 

```mysql
输入 `mysql -uroot -p密码` 或`mysql -uroot -p` 回车后再输入密码
 # 通过DOS连接mySQL数据库    （进入DOS命令行模式，进入sql客户端的安装路径再输入上述指令）
 
use name;     # 进入某一数据库  name为数据库名称

select database();    # 查看当前使用的数据库

show tables;     #  查看当前数据库中的表单

create table ok(id int, name varchar(30)); # 建立一个名为ok的table,其中包含id和name字段，二者数据类型分别为int和varchar(30)

desc ok;   # 查看ok这个table的内容    注意和show tables的功能不要混淆

create table ok2(id int unsigned not null auto_increment primary key,name varchar(30),age tinyint unsigned default 0,gender enum("男","女", "中性","保密") default "保密");
# 创建一个名为ok2的列表,其中有id name age gender这几个字段，数据类型分别为int #unsigned,varchar(30),tinyint,enum ,  数据类型之后的词为 约束条件，比如这里id设为 非空 自动增长 主# 键 ； age默认值设为0 ；年龄默认值设为 “保密”  

exit;    # 退出客户端

**最后一个条目后面不能写逗号，这里保密的后面无逗号
**约束条件写的时候不分先后顺序
**注意 enum是枚举类，意味着这里的gender只能取其中的几个值 
**所有的逗号or分号都是英文状态下的，否则会出错。
```

关于数据类型和约束：

![1581773016775](C:\Users\ton\AppData\Local\Temp\1581773016775.png){:width="100px" height="100px"}







![1581773525843](C:\Users\ton\AppData\Local\Temp\1581773525843.png){:width="100px" height="100px"}  





## 09数据的增删查改

> 注意desc +列表名如` desc ok2` 打印的是列表的属性信息而非列表记录：
>
> ![1581766099398](C:\Users\ton\AppData\Local\Temp\1581766099398.png)
>
> select * from 列表名如`select * from ok2` 是打印列表中所有记录：
>
> ![1581766215077](C:\Users\ton\AppData\Local\Temp\1581766215077.png)
>
> 



> 了解一下， innodb 是数据库的操作引擎  支持事务处理/外键/行级锁 ... ... 

```mysql
# 修改表-添加字段
alter table 表名 add 字段名 类型；
alter table ok2 add birthday datatime;

# 修改表-修改字段：不重命名版
alter table 表名 modify 字段名 类型及约束;
alter table ok2 modify birthday date default "1990";

# 修改表-修改字段：重命名版
alter table 表名 change 原字段名 新字段名 类型及约束;
alter table ok2 change birthday  birth  date default "1990";

--修改表-删除字段
alter table 表名 drop 列名；
alter table ok2 drop birthday;

**注意以上是对字段以及其属性的修改，并没有增减成员或修改成员的值。
```

> 以上并没有涉及到数据的增删改查, 仅是修改表的结构

#### 数据的增删改查  ：

##### 1.数据的增加

```mysql
insert into ok2 value(0,19, "女"，"2002-10-1");   # 增加数据

insert into ok2 value(9,25,2,"1996-4-3");
# 注意这里的性别设置成了枚举类(enum)，增加数据时可以用序号来代替相应的类，e.g. enum("男"，"女"，"中性")，上面代码中的2就代表是女

insert into ok2 value(0,26,2,"1995-10-10"),(0,21,1,"2003-2-1");   
#  同时增加多个数据
#  由于这里的id设置了自动增长，第一个数字为0就相当于id取默认增长的值(等效于default).

insert into ok2 (id,age) value(0,26),(0,21);
# 增加数据时可以只写出部分的字段值，比如上面只写了id和age字段，其余的字段会被自动填充成null.对于设置了not null约束条件的一定要写出其字段值，否则会出错！

```



##### 2.数据的修改

```mysql
 update ok2 set gender=2,age=5 where id=5;
#对id=5的行进行修改，修改其gender和age的值,如果这里没有添加where的限制性条件 所有成员的gender和age都会被修改
```

##### 3.数据的删除

```mysql
drop database py01   #删除py01这个数据库

drop table ok   #删除ok这个列表

delete from ok where id=5;   #删除ok列表中id为5的记录

#  delete from ok 将删除所有成员    drop table ok直接将此table删除。
# 删除数据库 删除table 删除字段都是用drop 删除表单中的记录用delete

```

##### 4.数据的查询

```mysql
select * from ok2 where gender="男"  #"*" 代表的是所有字段  where后接限制性条件

select name,gender where gender = "男"  #"*"可以被具体的字段所代替

select id as 序号, gender as 性别, name as 姓名 from students;
# as可以让字段名以相应的字符显示，这里id gender name将分别以"序号" "性别" "姓名" 显示。
```



## 数据库的查询

## 01 略

## 02 数据准备、基本的查询

![1581778966471](C:\Users\ton\AppData\Local\Temp\1581778966471.png)

> 可以用distinct来去重 ` select distinct gender from ok2;`



## 03 /04 /05 条件查询 范围查询 排序

```mysql
 select * from students where age>18;   #不多说，都知道

 select name,gender from students where age=18;
 #注意，where条件里涉及的参数可以不在select后面出现，select只是选择显示的字段而已.
 # 此外注意一个细节，MySQL中等号不写成双“=” .
 
 select * from students where age>18 and age<30;
 # and 的运用，将两个条件判断连接起来不能直接打逗号.   
 
 select * from students where age>18 or gender=2;  #or 的运用，毋庸赘述
 
 select * from students where not age>18 and gender=2;
 #注意not的使用，MYSQL会将上一句解析成对age>18的否定，若写为not (age>18 and gender=2)则是对整体的否定 (这和正常逻辑是符合的)
 # 注意not是写在条件之前的，不要写成注入 where age not = 18.
 
 select * from students where name like "小%";
 select * from students where name like "小_";
 #这种属于模糊的查询，%可以代表任何长度的任意字符，_代表一个长度的任意字符
 
 select * from students where name rlike "RE";
 #用relike代替like,""内填正则表达式. 
 
 select * from students where age in (18,15);
 select * from students where not age between 18 and 34;
 #以上两个语句为范围查询，in 用于不连续的范围，between用于连续的范围 
 
 select * from students where not age is null;
 # null指空值 
  
 select * from students where age between 18 and 30 and gender=1 order by age desc;
 select * from students where age between 18 and 30 order by age desc,id desc;
  以上两个语句为排序的使用，MySQL返回的数据默认按主键从小到大排列，这里order by age默认将搜到的结果按age值从小到大排列，+ desc将反向排列(从大到小)，   第二个句子有两个排序条件，在第一个不满足的情况下启用第二个.   desc就是之前查询表格属性的单词，在这里表示反向排序

  # > < >= <= = != like rlike in between    is null
  # 两个排序之间用逗号隔开,显然不可用and.
```



## 06 聚合、分组

```mysql
聚合函数：

select count(*) from students where gender=1; 
select max(age) as ok from students where gender=1;
select sum(age) as ok from students where gender=1;
select avg(age) as ok from students where gender=1;

# 显然即使不分组也可以使用聚合函数(相当于一个组)，但是分组了就只能显示分组所使用的字段以及相应的聚合函数 e.g. select gender, max(heigth),sum(age) from xiaomi group by gender; 如果写select * from xiaomi group by gender会出错，原因不赘述.
# 显然即使不分组也可以使用having, 相当于每条记录都是一个组(后面会说到)。

#以上的函数属于聚合函数，会返回一个名称和一个属性值，e.g:
+---------+
| ok      |
+---------+
| 28.0000 |
+---------+
# 这里的as只是设置显示的时候不显示聚合函数名而显示为ok    count(*)可以返回条目的个数
#这里的逻辑：where这个条件判断得到的结果作为聚合函数作用的对象；以上四句分别返回gender值为1的成员中：数量 年龄最大的人 年龄总和 平均年龄.

select avg(age)/count(*) as ok from students where gender=1;
#聚合函数是可以进行加减乘除等运算的

select round(avg(age)/count(*),1) as ok from students where gender=2;
#round函数可以设置小数位，其接收的第二个参数即为设置的小数位数。


分组：
select gender from students group by gender;
结果：
+--------+
| gender |
+--------+
| 女     |
| 男     |
| 中性   |
+--------+
#group by gender将table按gender分组，select 后的属性必须是这个组成员里面独有的(常常就写分组时的属性)

select gender, avg(age) from students group by gender;
结果：
+--------+----------+
| gender | avg(age) |
+--------+----------+
| 女     |  29.4000 |
| 男     |  28.0000 |
| 中性   |  18.5000 |
+--------+----------+
#此聚合函数将分别对得到的三个组进行操作，返回三个值.

select gender, group_concat(name,age) from students group by gender;
结果：
+--------+-------------------------------------------------------------------------------+
| gender | group_concat(name,age)                                                        |
+--------+-------------------------------------------------------------------------------+
| 男     | 彭于晏29,陈坤27                                                               |
| 女     | 小明18,小月月18,刘德华59,黄蓉38,凤姐28,王祖贤18,周杰伦36,金星33,郭靖12,周杰34 |
| 中性   | 刘亦菲25,静香12                                                               |
+--------+-------------------------------------------------------------------------------+
group_concat这个聚合函数可以以一个条目的形式显示某一属性值,可以接受多个参数，这里接受了两个参数.但是它默认将这些属性值连接在一起，如这里彭于晏和29连在一起，如写group_concat(name," ",age)则二者之间会出现空格.

select gender, group_concat(name,"_",age) from students where gender=1 group by gender;
#分组的前面(group by ...）可以写条件语句，其逻辑是： 经过条件语句的过滤后的表格交给group去分组

select gender, group_concat(name) from students group by gender having avg(age)>30;
#分组的后面(group by ...）可以写having语句，其逻辑是：对分组所得到的组进一步过滤，剔除不满足条件的分组

# where group having的顺序不要乱
```



## 7 分页

```mysql
 select * from students limit 2;
 结果：
 +----+--------+------+--------+--------+--------+----------------------+
| id | name   | age  | height | gender | cls_id | is_delete            |
+----+--------+------+--------+--------+--------+----------------------+
|  1 | 小明   |   18 | 180.00 | 女     |      1 | 0x00                 |
|  2 | 小月月 |   18 | 180.00 | 女     |      2 | 0x01                 |
+----+--------+------+--------+--------+--------+----------------------+
显示两个条目
select * from students limit 0,3;	
结果：
+----+--------+------+--------+--------+--------+----------------------+
| id | name   | age  | height | gender | cls_id | is_delete            |
+----+--------+------+--------+--------+--------+----------------------+
|  1 | 小明   |   18 | 180.00 | 女     |      1 | 0x00                 |
|  2 | 小月月 |   18 | 180.00 | 女     |      2 | 0x01                 |
|  3 | 彭于晏 |   29 | 185.00 | 男     |      1 | 0x00                 |
+----+--------+------+--------+--------+--------+----------------------+
从第一个开始，显示3个条目
select * from students limit 4,3;
结果：
+----+--------+------+--------+--------+--------+----------------------+
| id | name   | age  | height | gender | cls_id | is_delete            |
+----+--------+------+--------+--------+--------+----------------------+
|  5 | 黄蓉   |   38 | 167.00 | 女     |      3 | 0x00                 |
|  6 | 凤姐   |   28 | 139.00 | 女     |      4 | 0x01                 |
|  7 | 王祖贤 |   18 | 174.00 | 女     |      1 | 0x00                 |
+----+--------+------+--------+--------+--------+----------------------+
从第5个开始，显示3个条目

# 第一个数字代表起始位置的下标，第二个数字代表显示的个数，两个数字之间用逗号隔开；若只有一个数字那么该数字代表显示的个数(从第一个开始显示)
# limit放在语句的最后面.

```



## 8 链接查询

```mysql
# 链接分为三种---- 内链接 左链接 右链接 分别对应inner join ,left join, right join. 
# 链接出现的位置在两表格之间，     A inner/left/right join B on A.xx = B.xx    不要写错位置

#内连接 取交集（inner join on） ：
select * from students inner join classes;
#这种不设置限制性条件的inner join会产生 m * n 的效果(表A中有m个条目，表B中有n个条目)

select * from students inner join classes on students.cls_id=classes.id;
#这是添加了添加了条件的inner join(on后面接条件不要写成where!), 会在上述的m*n中剔出来满足要求的条目.

select s.name, c.name from students as s inner join classes as c on s.cls_id=c.id;
 #以上是显示学生和班级的姓名
 #注意select后面的属性要用逗号隔开.
 #as放在原名的后面. 
 #原名被改后所有地方都用不了原名
 #这个不会显示出s.name以及c.name的字样 而是显示name name,因为"."只是表明属性而已！！ 此外这里写成s.name as a, c.name as b是没问题的，表格和属性同时都有as并不影响.
 
 select s.name, c.name from students as s left join classes as c on s.cls_id=c.id ;
 #左链接用left join表示，左连接以left join字符左边的table为基准，以上面的语句为例，其和inner join的区别就是students列表中s.cls_id != c.id的会以null显示.
   e.g: students 列表的内容
   +----+--------+------+--------+--------+--------+----------------------+
| id | name   | age  | height | gender | cls_id | is_delete            |
+----+--------+------+--------+--------+--------+----------------------+
|  1 | 小明   |   18 | 180.00 | 女     |      1 | 0x00                 |
|  2 | 小月月 |   18 | 180.00 | 女     |      2 | 0x01                 |
|  3 | 彭于晏 |   29 | 185.00 | 男     |      1 | 0x00                 |
|  4 | 刘德华 |   59 | 155.00 | 女     |      2 | 0x01                 |
|  5 | 黄蓉   |   38 | 167.00 | 女     |      3 | 0x00                 |
|  6 | 凤姐   |   28 | 139.00 | 女     |      4 | 0x01                 |
|  7 | 王祖贤 |   18 | 174.00 | 女     |      1 | 0x00                 |
|  8 | 周杰伦 |   36 | 180.00 | 女     |      1 | 0x00                 |
|  9 | 陈坤   |   27 | 190.00 | 男     |      2 | 0x01                 |
| 10 | 刘亦菲 |   25 | 180.00 | 中性   |      2 | 0x01                 |
| 11 | 金星   |   33 | 180.00 | 女     |      4 | 0x00                 |
| 12 | 静香   |   12 | 170.00 | 中性   |      3 | 0x01                 |
| 13 | 郭靖   |   12 | 150.00 | 女     |      4 | 0x00                 |
| 14 | 周杰   |   34 | 182.00 | 女     |      5 | 0x00                 |
+----+--------+------+--------+--------+--------+----------------------+
classes列表的内容
+----+------------+
| id | name       |
+----+------------+
|  1 | python01期 |
|  2 | python02期 |
|  3 | python03期 |
+----+------------+
执行上面语句的结果：
+--------+------------+
| name   | name       |
+--------+------------+
| 小明   | python01期 |
| 彭于晏 | python01期 |
| 王祖贤 | python01期 |
| 周杰伦 | python01期 |
| 小月月 | python02期 |
| 刘德华 | python02期 |
| 陈坤   | python02期 |
| 刘亦菲 | python02期 |
| 黄蓉   | python03期 |
| 静香   | python03期 |
| 凤姐   | NULL       |
| 金星   | NULL       |
| 郭靖   | NULL       |
| 周杰   | NULL       |
+--------+------------+

   右链接和左连接的区别就是它是以右边为基准的，所以通常用调换左链接左右两边列表的位置来实现右链接的效果，而不用right join字样.
   
   select s.name, c.name from students as s left join classes as c on s.cls_id=c.id  having c.id is null; 
   这句话会运行出错，这里并没有group语句，having作用的结果是select s.name c.name之后的列表，而这个列表中并没有c.id这个信息，将这里的s.name ，c.name改成"*"就可以了.
  显然即使不分组也可以使用having, 相当于每条记录都是一个组。
```



## 9/10 自关联 子查询 

自关联的定义以及自关联表了解一下

```mysql
select * from areas as province inner join areas as city on city.pid=province.aid having provingce.atitle="山东省"
我们可以通过as将同一个列表起两个名字，这样就可以将其视为两个列表(as后接的名字当然得不同)来进行inner join操作.

我们也可以通过子查询来得到这个结果：
select * from areas where pid = (select aid from areas where atitle="山东省")
#这里子查询中(select aid ...)的返回值被赋值给pid.一看便知.
```



## 11 数据库设计 

> 经过研究和对使用中问题的总结，对于设计数据库提出了一些规范，这些规范被称为范式(Normal Form)

> 目前有迹可循的共有8种范式，一般需要遵守三范式即可

##### 第一范式 : 强调的是原子性，即列不能够再分成其他列

##### 第二范式：首先是1F，另外包含两部分内容，一是必须有一个主键，二是没有包含在主键内的列必须完全依赖主键，而不能只依赖于主键的一部分

e.g. 考虑一个订单明细表(OrderID, ProductID, UnitPrice, Discount,Quantity ，ProductName) 因为我们知道在一个订单中可以订购多种产品，所以单单一个OrderID是不足以成为主键的，主键应该是(OrderID, ProductID，二者合在一起才是主键),  可见Discount, Quantity , 完全依赖于(取决于)主键(OrderID, ProductID)，而UnitPrice, ProductName只依赖于ProductID.  所以此表格的设计不符合第二范式。  

可以将表拆成(OrderID, ProductID,Discount,Quantity  )和（ ProductID,UnitPrice,ProductName ）来解决此问题

** 这里的A取决于B可以理解为B确定了A就确定了下来.

##### 第三范式：首先是2NF，另外非主键必须直接依赖于主键，不能存在传递依赖，即不能存在：非主键列A依赖于非主键列B，非主键列B依赖于主键的情况

e.g.  考虑一个订单表【Order】

  (OrderID, OrderDate, CustomerID, CustomerName, CustomerAddr, CustomerCity), 主键是OrderID. 显然它是符合第二范式的，然而，其中CustomerName, CustomerAddr, CustomerCity 直接依赖的是CustomerID而非主键，它是通过传递才依赖于主键，所以不符合第三范式.



##### E-R模型

- E表示entry ,实体， 设计实体就像定义一个类一样，指定从哪些方面描述对象，一个实体转换为数据库中的一个表

- R表示relationship, 关系， 关系描述两个实体之间的对应规则，关系的类型包括一对一、一对多、多对多

- 关系也是一种数据，需要通过一个字段存储在表中

  ​

  - [x] 实体A对实体B为1对1，则在表A或者表B中创建一个字段，存储另一个表的主键值.
  - [x] 实体A对实体B为1对多，则在表B(多的那个表)中创建一个字段，存储A表的主键值.
  - [x] 实体A对实体B为多对多，新建一张表C, 这个表只有两个字段，一个用于存储表A的主键值 ,另一个用于存储表B的主键值.

  ​



## MySQL与python交互



## 01 数据的准备、基本查询

```mysql
# 获得价格大于平均价格的商品的信息
select * from goods where price>(select avg(price) from goods)；  
# 此为子查询 返回的聚合函数的结果被拿来和price比较   子查询中的子语句就是select开头的.

#查找每种商品类型中最贵的一种(如水果中最贵的，蔬菜中最贵的，...)
select * from goods inner join (select cata_name , max(price) as max_price  from goods group by cata_name) as goods_new_info on goods.cata_name=goods_new_info.cata_name and goods.price=goods_new_info.max_price;
#这里用到了链接查询和子查询，这里的子查询是将select的结果视为一个table,为表级子查询.


```



## 02/03 数据操作演练：拆为多个表



==此章节内容建议看视频，以下记录仅为说明语法，SQL语句之间并无联系== 

----



```mysql
creat table if not exists goods_cates(... ...)
# 这里加的if not exists 其作用是在goods_cates不存在的时候创建此table,否则不创建

insert into goods_cates (name) select cata_name from goods group by cata_name;
# select语句的位置本来应该是value(...), 这里select语句执行后得到的结果充当了value的参数，但是注意这里不用写value.
# 可见select不仅可以用于子查询还可以用来代替插入数据的value部分.

update goods as g inner join goods_cates as c on g.cate_name=c.name set g.cate_name=c.id; 
# 这是update和inner join的连用，类比select和inner join的连用，前者可以设置join之后的表中的属性值，后者是可以显示join之后的表的属性值. 


alter table goods change cate_name cate_id int unsigned not null
# alter table 表名 change 原字段名 现字段名  数据类型 约束条件
# alter table 表名 modify 原字段名 数据类型 约束条件     （不重命名）


alter table goods add foreign key (cata_id) reference goods_catas(id);
# 建立外键   为goods的cata_id字段设置外键 ，外键链接的是goods_cates表中的id字段.
```



> 在实际开发中，很少会使用到外键约束，会极大的降低表更新的效率



- 取消外键： ==见视频03== 

​          

​                     











## 04 安装pymsql

可以通过python中的pymysql模块来操作MySQL:

![1581991705704](C:\Users\ton\AppData\Local\Temp\1581991705704.png) 



## 05 python操作sql:查询数据

```python
from  pymysql import *                # 导入模块
conn = connect( host="localhost",port=3306,user="root",password="science8863Vc",
               database="python_test",charset="utf8"); 
# 建立连接  localhost会连接本地的服务器，3306的端口是mysql的默认初始配置， 默认的用户名是root.
cs1 = conn.cursor()   # 获得cursor对象
count = cs1.execute("select * from students")  # 执行SQL语句 若执行成功将返回信息的条数
print(count)         #打印出来的是信息的条数
for i in range(5):
    a = cs1.fetchone()
    # fetchone fetchmany fetchall分别是取一个、多个、全部
    # 注意这里是cs1.fetchone不是count.fetchone
    print(a)    
cs1.close()   #关闭链接
conn.close()  #关闭游标

输出结果：
14
(1, '小明', 18, Decimal('180.00'), '女', 1, b'\x00')
(2, '小月月', 18, Decimal('180.00'), '女', 2, b'\x01')
(3, '彭于晏', 29, Decimal('185.00'), '男', 1, b'\x00')
(4, '刘德华', 59, Decimal('155.00'), '女', 2, b'\x01')
(5, '黄蓉', 38, Decimal('167.00'), '女', 3, b'\x00')

# 可见fetchone()每次取一条信息，一直往下取，就像游标一样，其次注意fetchone取出的是一个tuple若用fetchmany(n)则每次取出n条信息，形式是一个2维的tuple: e.g. :
#                    a = cs1.fetchmany(3)
#                    print(a)
                                                  
#                    results:  ((1, '小明', 18, Decimal('180.00'), '女', 1, b'\x00'), (2, '小月月', 18, Decimal('180.00'), '女', 2, b'\x01'), (3, '彭于晏', 29, Decimal('185.00'), '男', 1, b'\x00'))     若fetchmany()中未接受数值，那么默认取1条，但是返回的任然是二维tuple: ((...),)   
```



## 06 京东商城查询 



==**重要**==

```python
from pysql import connect

class JD(object):
    def __init__(self):
    #创建connect连接
    self.conn =  connect(host="localhost",port=3306,user="root",
                         password="science8863Vc",database="jing_dong",charset="utf-8");
    #获得cursor对象
    self.cursor = conn.cursor()
    
    def __del__(self):
        self.cursor.close()
        self.conn.close()
        
    def execute_sql(self,sql):
        self.cursor.execute(sql)
        for temp in self.cursor.fetchall():
            print(temp)
            
    def show_all_items(self):
       #显示所有商品
        sql = "select * from goods;"
        self.execute_sql(sql)
        
    def show_cates(self):
        sql = "select name from goods_cates;"
        self.execute_sql(sql)
        
    def show_brands(self):
        sql = "select name from goods_brands;"
        self.execute_sql(sql)
    @staticmethod
    def print_menu():
        print("-----京东-----")
        print("1：所有商品：")
        print("2: 所有商品的分类")
        print("3: 所有商品品牌分类")
        return input("请输入功能对应的序号：")
    
    def run(self):
        while True:
            num = self.print_menu()     # IO操作的函数进行封装
            if num == "1":
                self.show_all_items()
            if num == "1":
                self.show_cates()
            if num == "3":
                self.show_brands()
            else:
                print("输入有误，请重新输入")
             
     def main():
        jd = JD()
        jd.run()
if __name__ == "__main__":
    main()
```



- 这个代码很好的体现了封装的思想，在main函数中尽可能写的很少，这里main函数中只是创建了一个实例变量，之后调用了其run函数
- 在类定义的run函数中做集中的函数调用也体现出了这里的封装。 集中的函数调用中涉及IO操作的函数放在前面，其它函数放在后面(因为涉及IO操作的函数往往起着选择和控制程序走向的作用)   这里IO函数内容有点多所以被封装了起来
- 这里的\_\_init\_\_()方法和\_\_del\_\_()方法都是魔法属性，一个在实例化的时候立即执行，一个在类方法调用结束后立即关闭
- 这里的@staticmethod方法是静态方法，类和实例变量都可以访问到 (因为这里的print_menu函数用不到任何类变量，所以可以写成静态方法，但是写print_menu(self)也是可以的，区别就是类无法访问).
- 短链接和长连接，短链接接是每调用一次函数都会创立链接，调用结束之后就关闭链接，长链接是调用后不关闭，可以调用很多次，最后再关闭(不手动销毁实例对象，python执行完毕也会自动收回，所以\_\_del\_\_()一定会被执行）.
- 这里的方法和属性基本都加了self，相当于是一个炳，让别的函数可以“够得着”，e.g.   \_\_init\_\_() 中的conn和cursor不写self也是可以链接服务器并获取cursor对象，但是由于是函数内的local变量，在调用后即销毁，别的函数将无法使用他们， 同样函数中若没有self则run方法没有办法够得着它们.    ==仔细看看代码中self出现的位置,嵌套在类方法中的类方法前面是有"self."的==.



## 07 python操作sql: 添加、修改、删除数据



```python
from  pymysql import *

conn = connect(host="localhost",port=3306,user="root",password="science8863Vc",database="python_test          ")

cs1 = conn.cursor()
cs1.execute("""insert into students (name,gender) value("何1",2);""")
# """ """ 中包裹着""   注意python中存在"" '' 以及 ''' '''   """ """ 但是没有两个的(1 or 3)
此句将向数据库添加一个条目
conn.commit()
# 数据的增、删、改 必须要有这句才能真正提交到数据库 注意这是conn的方法不是cs1 .
```



```python
cs1.execute("""insert into students (name,gender) value("何1",2);""")
cs1.execute("""insert into students (name,gender) value("何2",2);""")
conn.rollback()   #回滚事件
cs1.execute("""insert into students (name,gender) value("胡2",2);""")

#若这里何1、何2的条目都写错了，应该是胡2，那么可以可以通过conn.rollback()将未提交的增、删、改全部撤销
# 被rollback的条目虽然没有被提交但是仍然消耗了主键，这里的  "胡2" 会跳过这两个ID
```

==注意rollback和commit并不是绑在游标上的== 



## 08 案例： 京东商城-添加，防止SQL注入



若为06中代码增加一个 可以往数据库中添加条目的函数：

```
def get_info_by_name(self):
    item_name = input("please input the name of the goods :")
    sql = """select * from goods where name = '%s' ;   """ % item_name
    self.execute_sql(sql)
```

若输入 '  or  1=1  or  '1 则相当于 传递了`select * from goods where name = '' or 1=1 or '1'` 这样这个where条件便恒成立    

==此即MySQL的注入== 



防止SQL注入：

```python
sql = "select * from goods where name = %s "
self.cursor.execute(sql, [item_name])

```



若这里sql = "...%s...%s...%s.." 中有很多%s则可以将[item_name] 写成 ：\[数值1，数值2，数值3...] 将其自动填到相应的位置.



## MySQL 高级 （这里的SQL语句不用记忆，即用即搜）



## 01 视图

对于复杂的查询，往往是有多个数据进行关联查询而得到，如果数据库因为需求等原因发生了改变，为了保证查询到的数据与之前的相同，则要在多个地方进行修改，维护起来非常麻烦

==视图：通俗的将，视图就是一条SELECT语句执行后返回的结果== ，所以我们在创建视图的时候，主要的工作就落在创建这条SQL语句中(前面的笔记中提到过select可以用于子查询，可以用于insert into语句中的value, 这几个地方可以串一下)

==视图是对若干张基本表的引用，一张虚表，查询语句的执行结果==，不存储具体的数据(==基本数据发生了改变，视图也会跟着改变(e.g. 表中小明的名字改成了小强，那么在作用在其上的视图中，小明也会变成小强)==)

方便操作，特别是查询操作，减少复杂的SQL语句，增强可读性

视图提高了重用性，就像一个函数，其存在同时也提高了安全性(大公司中可能将原表保存而只提供视图给员工操作)



`select g.*, c.name as cate_name, b.name as brand_name from goods as g left join goods_cates as c on g.cate_id left join goods_brands as b on g.brand_id=b.id;` 

​                                        :arrow_down:  

创建视图： `create view 图名 as select语句` 

creat view v_goods_info as + 上面的一大段  可以将上面的很长的select语句得到的结果创建成一个虚拟的图--视图，它可以和正常的table一样进行查询操作.(不能做其他操作，删除需要用`drop view 视图名` ，而drop table 视图名是删不掉的)



## 02 /03 事务

考虑一个场景：A转账给B 500元，那么银行后台需要将A的账户 -500，之后将B的账户 +500, 若银行后台出了问题

A的钱已经扣除而B未增加那就出事故了，而事务可以解决诸如此类问题

==所谓事务，它是一个操作序列，这些操作要么都执行，要么都不执行，它是一个不可分割的工作单位。== 

##### 事务四大特性：

- ##### 原子性   (Atomicity）

- ##### 一致性   (Consistency)

- ##### 隔离性   (Isolation)

- ##### 持久性   (Durability)

##### 即   ==ACID== 



```mysql
start transaction();    # 或 begain;
... ...
commit
```

​       以上就是开启事务的写法，commit和begain之间是对数据表的增删改之类的操作，在commit之后这些对列表的操作才会真正被提交到列表之中.    ==A,B链接同一个服务器，对同一个列表进行操作，分别在自己的MySQL客户端上执行SQL语句；A开启了事务(B未开启)，在未commit之前，他通过输入select查询语句所得到的列表是被改变了的，但这只是明面上的显示而已，真实的情况是修改并没有被添加进列表；此外在A未commit之前对列表做的增删改操作在B的客户端而言是看不到任何变化的，这点即为事务的隔离性（A commit之后B当然就可以看到变化了）；此外还要注意A如果在对列表中某个记录进行操作的话，那么同一时间内B无法对此记录进行操作(会阻塞住，阻塞一段时间会直接放弃执行),比较类似于python解释器中的GIL锁，在A commit之后B对此条记录的操作会立刻解阻塞== 

​     ==如果A B两人都开启了事务，A commit之后B并没有commit,那么显然此时在B的服务器上将仍然看不到变化，原因还是事务的隔离性，B未commit之前也是处于一个封闭的环境，外面的变化进不来.换言之就是开启了事务但未commit时，对于查询来说是内外隔绝的(外面变化进不来，里面变化外面观察不到)，但是注意这只是对于查询而言，真实的数据库已经被修改！== 

​    ==其实对于MySQL客户端，默认每一个命令单独成一个事务，也就是对于命令语句A,其实相当于python中的`begain;A;commit` 只是begain和commit客户端替我们写上了,我们可以通过人为将SQL语句包裹在begain和commit间来改变这种默认状态==   



##  04 /05 索引

​        **一般的应用对数据库的读写比例大概为10:1（平均读10次写1次），并且写入过程罕见出错，而较为复杂的查询语句有时会出错并且往往很耗时, 索引对于数据库尤为重要**

> 索引是一种特殊的文件(innoDB数据表上的索引是表空间的一个组成部分)，它们包含着对数据表里所有记录的引用指针，更通俗的的说，数据库索引好比是一本书前面的目录，能加快数据库的查询操作

e.g.

```mysql
#创建了一个有1000000个记录的列表，查询其最后一个记录是什么：
create table test_index(title varchar(10));
#从1到100000，共输入100000条记录
insert into test_index value("ha-1") 
#查找最后一个记录的信息，此语句较为耗时
select * from test_index where title="ha-99999"
#考虑创建索引：
# create index 索引名 on 表名(字段名称(长度))     这样便为title创建了索引
create index title_index on test_index(title(10))  
#此时查询所耗时间将大大减少
select * from test_index where title="ha-99999"


# 如果指定字段是字符串，那么需要指定长度，建议长度与定义字段时的长度一致
# 字段类型如果不是字符串，那么可以不写长度
```



```mysql
show index from 表名  #可以显示表的索引信息
drop index 索引名 on 表名    # 可以删除索引
```



   

==MySQL会自动给主键或者外键创建索引，所以对主键或外键进行搜索速度很快==    

==建立太多索引会影响更新和插入的速度，因为它需要同样更新每个索引文件。  对于一个经常需要更新和插入的表格，没必要为了一个很少使用的where字句建立索引      即内容很多并且字段很常用才考虑添加索引        建立索引会占用磁盘空间== 



## 06 账户管理(了解）

输入`show databases` :

+--------------------+
| Database           |
+--------------------+
| information_schema |
| mysql              |
| performance_schema |
| py                 |
| python_01          |
| python_test        |
| sakila             |
| sys                |
| world              |
+--------------------+

可以看到mysql这个database

输入`select user,host,authentication_string from user;`  :

![1582029129818](C:\Users\ton\AppData\Local\Temp\1582029129818.png)

显示 用户名、是否可以远程登录、密码(已经过)， `localhost` 代表不可以远程登录，`%` 代表可以远程登录.(实际上即使是”%“可能也难以登录)



```
grant 权限列表 on 数据库 to '用户名 ‘@’访问主机‘  identifie by '密码' ;    创建用户并授权 

grant select on students.*  to 'laowang'@'localhost' identified by '123456'
创建一个新用户laowang, 他不能远程登陆，他可以使用students这个数据库的所有列表，但是只有select权限(查询)，密码为123456
grant all privileges on students.*  to 'laowang'@'%' identified by '123456'
创建一个用户老李，他可以远程登录，他可以使用students这个数据库的所有列表，有一切操作权限，密码为123456.

更新密码：
update user set authentication_string=password("新密码")  where user="用户名"
flush privileges 刷新权限之后才起作用

```



##  07 MySQL主从

##### MySQL中主从同步配置

- 主从同步的定义：

>   主从同步使得数据可以从一个服务器复制到其他服务器上，在复制数据时，一个服务器充当主服务器(master),另一个充当从服务器(slave). 因为复制是异步进行的，所以从服务器一般不需要一直连着主服务器，从服务器甚至可以通过拨号连接断断续续地链接主服务器。通过配置文件，可以指定复制所有的数据库，某个数据库，甚至是某个数据库上的某个表.

- 主从同步的好处

1. 通过增加从服务器来提高数据库的性能，在主服务器上执行写入和更新，在从服务器上向外提供读功能，可以动态的调整从服务器的数量，从而调整整个数据库的性能
2. 提高数据安全，因为数据已经复制到从服务器，从服务器可以终止复制进程，所以，可以在服务器上备份而不破坏主服务器相应数据
3. 在主服务器上生成实时数据，而在从服务器上分析这些数据，从而提高主服务器的性能

### 略  暂时不看



#                                                                      redis数据库



## redis安装和配置

## 01 _redis_nosql和redis简介



**关系型数据库：mysql /oracle / sql server (具有统一的语言，sql语言)**

**nosql ** **：一类新出现的数据库(not only sql), 特点：**

- **不支持sql语法**
- **存储结构和传统的关系型数据库的那种关系表完全不同，nosql中存储是数据都是==KV==形式**
- **==NoSQL的数据库中没有一种通用的语言，每种nosql数据库都有自己的api和语法==，以及擅长的业务场景**
- **NoSQL的产品种类相当多：**
  - **==Mongodb==**
  - **==Redis==** 
  - **Hbase hadoop**
  - **cassandra hadoop**

**NoSQL和SQL数据库比较：**

- **使用场景不同，sql适合于关系特别复杂的数据查询场景，nosql反之**
- **“事务” 特性的支持：sql对事务的支持特别完善，而nosql基本不支持事务**



##### Redis简介 :   Redis是一个开源的用ANSI C语言编写的、支持网络亦可持久化的日志型、key-value数据库，并提供多种语言的API

##### Redis特性：

- ##### Redis与其它key-value缓存产品有以下三个特点

- ##### Redis支持数据的持久化，可以将内存中的数据保存在磁盘中，重启的时候可以再次加载进行使用

- ##### Redis不仅支持简单的key-value类型的数据，同时还提供list, set, zset, hash等数据结构的存储

- ##### Redis支持数据的备份，即master-slave模式的数据备份

**Redis优势：**

- **性能极高：读的速度为110000次/s，写的速度是81000次/s**
- **丰富的数据类型  Redis支持二进制案例的string， list， hash， sets等数据类型操作**
- **原子 - Redis的所有操作都是原子性的，同时redis还支持对几个操作全并后的原子性执行**
- **丰富的特性 Redis还支持publish/subscribe，通知，key过期等特性**

​               **==Redis主要用来做缓存(Redis是个内存数据库)，通常，查询一条数据 先去redis上查，若数据未失效那么直接返回 若数据失效，那么去mySQL上查，并且将查询到的值更新到redis,下次直接从redis查找==** 

 

## 02/03 Redis的安装和配置

##### 略  （这两节涉及到一点在linux上安装和配置软件的知识，有时间可以回看）



## 04 Redis启动服务端和客户端

##### 略   （此节涉及到一些linux中启动和关闭服务等知识， 有时间可以回看）

**plus：数据库没有名称，默认16个，通过0-15来标识，连接redis默认选择第一个数据库**

**select n 切换到到第n个数据库**



## redis数据类型及其操作



## 01 redis数据类型

- **redis是key-value的数据结构，每条数据都是一个键值对**
- **键的类型是字符串**
- **键不能重复** 
-  **五种数据类型**
  - **string **
  - **hash **
  - **list（list中元素只能是字符串） **
  - **set   （无序集合）** 
  - **zset（有序的集合，和set一样元素不能重复）** 

## 02 \_redis数据类型_string和键命令

- 字符串类型是redis中最为基础的数据存储类型，他在redis中的二进制安全的，该类型可以接受任何形式的数据，如JEPG图像数据或Json对象描述信息等. 在Redis中字符串类型的value最多可以容纳的数据长度是512M.



- 设置键值(若设置的键不存在则为添加，如果存在则为修改) 和取值

> set key value                         get key
>
> set name ton                        get ton

- 设置值及值过期时间，以秒为单位

> setex key seconds value
>
> setex ton 3 25     (3s后此键将失效)

- 设置多个键值

> mset key1 value1 key2 value2 key3 value3
>
> mset a1 c++ a2 python a3 java

- 向键值中追加信息

> append key value
>
> append a1 c    ==此时get a1会显示“c++c”，并不是“c++” “c”,即使输入append a1 "c"也是此结果== 

- 获取多个键值

> maget key1 key2 key3
>
> mget a1 a2 a3

- 其它

> keys * 显示所有键名
>
> EXISTS key判断键是否存在（存在返回1否则返回0） e.g.  EXISTS a1  ==注意不是EXIST==
>
> type key 显示键值的类型    e.g.   type a1     将显示string
>
> del key1 key2...     删除键
>
> expire key seconds  设置过期时间   （创立键时未设置过期时间则此键永久有效，除非删除之，通过expire可以设置其过期时间）

==操作不区分大小写，e.g. EXISTS可以写成exISTs, 但是键和值毫无疑问是区分的==

==set get mset mget /setex/append/type /exists/del/keys *==

   

## 03 hash命令

增加、修改

- 设置单个属性

  > hset key field value
  >
  > hset user name tj       # 设置ton的属性age为25

- 设置多个属性值

>  hmset key1 field1 value1  filed2  field 3 value3 ...
>
>  hmset u1 name tj  age 11  height 180

- 获取

> hkeys key 获取指定键所有属性  hkeys u1    
>
> 获取一个属性的值   hget key field       hget u1 name   
>
> hmget key field1 filed1      获取多个属性的值     hmget u1 name age   返回       1) "tj"    2) "18"
>
> hvals key 获取指定键的所有属性的值    hvals u1  返回   1) "tj"   2) "18"  3) "180"

- 删除

> del  & hdel     前者是将整个键删除，后者是删除部份属性：hdel u2 age将u2键的age属性删除

==hset hget hmset hmget/hkeys hvals/del hdel== 

==hkeys是获取指定键的所有属性，hvals是获取指定键的所有属性值==

==注意hash和string的操作的逻辑明显不是完全一一对应的的，细节要注意==



## set和zset命令

set ：

- 无序
- 元素为string
- 元素不可重复
- 对于集合没有修改操作



sadd key member1 member2  初始化成员

smembers key 返回所有元素

srem key  member删除指定元素



zset：

- 有序
- 元素为string
- 元素不可重复
- 每个元素都会关联一个double类型的score, 表示权重，通过权重将元素从小到大排列
- 对于集合没有修改操作



>  zadd key score1 member1 score2 member2... ..

zadd a4 1 zhangsan 2 lisi 3 wangwu    创建zset

>  zrange key start stop   (索引可以是负数)

zrange a4 0 -1		返回所有成员

>  zrangebyscore key min max（包括min max）  查看权值在多少之间的成员

zrangebyscore a4 2 3     返回权值在2-3(包括2，3)的成员



>  zscore key member 返回成员的score

>  zrem key member1 member2...      删除成员    

zrem a4 zhangsan lisi

>  zremrangebyscore key value1 value2

zremrangebyscore a4 0 3         删除a4中score为0-3的成员



----

----



==redis与python交互---redis集群(03-05）感觉redis对我无实际意义== 









[^1]: 
