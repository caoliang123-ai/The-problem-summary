'''
num1=int(input())
num2=int(input())
if num1>num2:
    print(num1)
elif num1==num2:
    print('num1\nnum2')
else:
    print(num2)
#关于两个整数比较大小？

a=int(input())
if a//1000:
    if a//10000:
        print('wu weishuyishang ')
    else:
        print('siweishu')
elif a//10:
    if a//100:
        print('sanweishu')
    else :
        print('liangweishu')
else :
    print('yiweishu ')

#输入一个5位数以内的数字，判断这个数是几位数？

"循环——for语句"
'''
'''
message='hello python word!'
print(message)
'''
'''
cars=('audi','bmw','subaru','toyota')
for car in cars:
    if car=='bwmn':
        print(car.upper())
    else:
        print(car.title())
'''       '''
jihe=[1,2,3,4,5,6]
for i in jihe:
      if i==3:
        print('shuyush')
      else:
          print('shuchu12456')
'''
'''
element=['a','b','c','d','e','f']
print(element)
element=[1,2,3,4,5,6,7,8,9,10,11,12]
print(element)
names=['caohaiyun', 'caoyi', 'caohaihui']
message=f'i love :{names[0]}'
print(message)
element.append(0)
print(element)
names=[]
names.append(0)
names.append("1")
names.append(2)
print(names)
names=['caojing','caohaiyun','caowenqiang']
print(len(names))

  #del语句删除列表元素（验证是否可以找回）
names=[1,2,3,4,5]
del names[1]#指定的位置，是一个指令，无法指定给变量
print(names)
names=['caojing','caohaiyun','caowenqiang']
names.reverse()
print(names)
names=['caojing','laodu','bili']
print(sorted(names))
print(names)
names=['caojing','caohaiyun','caoxiansheng','caonvshi']
names.remove('caojing')
print(names)
names=['caojing','caohaiyun','caoguosheng']
names_1=names.pop(0)#names.pop()代表的是一个值，不是一个指令因此可以找回
print(names)
print(names_1)

-=
city=['shanghai','beijing','zhen','jiujiang']
print(city)
city_1=sorted(city)
print(city_1)
print(city)
city.reverse()
print(city)
city.reverse()
print(city)
city.sort()
print(city)
city.sort(reverse=True)
print(city)
print(len(city))

#对列表做一个集合，用到所有的功能
citys=['jiangxi','zhejiang','fujian','aomen','beijing ','xianggang','wenchuan']
#访问列表元素
print(citys[0])
#使用列表元素
citys_1=f'hello,{citys[0]}'
print(citys_1)
#t修改列表元素不可反回
citys[0]='wuhu'
print(citys)
#添加
#默认末尾添加添加江西
citys.append('jiangxi_1')
print(citys)
#指定位置和值添加鹰潭
citys.insert(0,'yingtan')
print(citys)
#删减第一个数
city_3=citys.pop(0)
print(citys)#不可返回
#找出删除的数
print(city_3)
#用del语句删除最后一个元素
del citys[0]
print(citys)
#按值删除列表的元素
citys.remove('aomen')
print(citys)#不可返回
#永久按字母排序
citys.sort()
print(citys)
citys.sort(reverse=True)
print(citys)#不可反回
#临时排序
print(sorted(citys))
print(citys)
#倒着打印
citys.reverse()
print(citys)
#打印列表的长度
print(len(citys))
#第二章的内容
message='    i love\'s \n\tyou    '
print(message)
information=message.title()
print(information)
information=message.upper()
print(information)
information=message.lower()
print(information)
print(message.strip())
print(message.rstrip())#右边空格删除
print(message.lstrip())
#第二章、第三章
#第二章内容
#什么是变量？变量只是一个标签，也可以表示变量指向某个特定的值。
#变量可以是由字母、数字、下划线组成的。但只能以字母和下划线开头。字符串不能留空白，例如：names、names_1
a=1
name='   cao jing   '
message='i love caohaiyun'
print(f'{a},{message},{name}')
messages=f'hello,my name\'s caojing:\n\t{a} {name} {message}'
print(messages)
b=2
print(a+b)
print(a**b)
print(a//b)
print(a/b)
print(a%b)
print(a-b)
print(a*b)
print(name.title())
print(name.upper())
print(name.lower())
print(name.strip())
print(name.rstrip())
print(name.lstrip())

#第三章，列表简介
#什么是列表，是指一系列特定顺序的元素集合，用中括号【】表示，元素可以是字母、数字、字符串
#列表的排列顺序是：0开始算。反着算-1开始。计算列表长度lenght从一开始算。
elements=[1,2,3,4,5,6]
names=['caojing','caohaiyun','caoguosheng']
citys=['jiangxi','beijing','tianjing']
#两个列表不能用format字符串传一起。
#访问列表的元素,列表的元素可以format
print(f'{elements[0]},{names[0]},{citys[0]}')
#使用列表的元素
print(f'my like\'s digital{elements[5]},\nmy name\'s {names[0]},\n\t i comeform {citys[0]}')
#替换（修改）
names[0]='caoxiansheng'
print(names)
#添加元素(默认末尾添加)
names.append('caonvshi')
print(names)
#添加（指定位置，和元素）
names.insert(0,'caoguniang')
print(names)
#删除元素del语句,不可返回
del names[0]
print(names)
#pop方法,不指定位置，默认删除最后一个
names_1=names.pop(0)
print(names)
print(names_1)
#指定列表元素删除。
names.remove('caohaiyun')
print(names)
#列表元素排序(永久排序)
elements.sort()
print(elements)
elements.sort(reverse=True)
print(elements)
#临时排序
print(sorted(elements))
print(elements)
#倒序
names.reverse()
print(names)
#计算长度lenght
print(len(names))
print(len(elements))
print(len(citys))


#第二章内容：变量和数据类型
#什么是变量（标识符）？变量可以说是指定某个特定的值，可以说成是一个标签。（由字母、数字、下划线组成）但是只能以字母和下划线开头。变量不能赋值给变量。
#什么是字符串？字符串是一系列的字符组成，表示某个特定的东西，在python编程中，只要加了单双引号的都可以是字符串。
#什么是数？数有整数和浮点数，是表示一个特定的值。
#运算符号有哪些？怎么用？
#注释怎么用？在pythonz中怎么运用？
digits=1
number=2
names='   caojing   '
messages='hello,python!'
print(f'{digits},{names},{messages}')#format,字符串
information=f'{digits+number},\n\t{names},\n\t{messages}'
print(information)
names_1=names.title()
names_2=names.upper()
names_3=names.lower()
print(f'{names_1},{names_2},{names_3}')
names_4=names.strip()
names_5=names.rstrip()
names_6=names.lstrip()
print(f'{names_4},{names_5},{names_6}')
multiply=digits*number
print(multiply)
division=digits/number
add=division+multiply
less=division-multiply
print(add,less,division)
#写一个if循环语句
a=int(input())
b=int(input())
if b>=a:
    if b>a:
        print(b)
    elif b==a:
        print(a+b)
else:
    print(a)
    
#x写一个for循环语句  
names=['caohaiyun' 'caojianghui' 'caojing']
for i in names:
    if i==names:
        print('i love you!')
    else :
        print('i hate you!')
        
#列表简介
#什么是列表？列表是一系列特殊顺序的元素组成，它可以是由字母、数字、字符串组成list,用【】号表示
#制作一个城市的列表
citys=['beijing','jiangxijiujiang''shanghai','nanchang']
print(citys)
#访问第一个城市
citys_1=citys[0]
print(citys_1)
#并且使用这个城市说一段话
messages=f'hello!\n\ti love{citys_1}'
print(messages)
#列表元素的替换
citys[0]='fuzhou'
print(citys)
#list element的添加，（指定位置添加）用了方法：append.insert
print(citys)
citys.append('beijing')#默认末尾添加。
print(citys)
#指定位置和元素添加
print(citys)
citys.insert(0,'aomen')
print(citys)
#删除列表元素，del语句删除后不可返回(是必须指定位置)，pop方法（可指定位置可默认位置）,可以retrun.
print(citys)
del citys[0]
print(citys)
citys_1=citys.pop(0)
print(citys)
print(citys_1)
print(citys)
#指定元素删除：remove
print(citys)
citys.remove('beijing')
print(citys)
#list的排序：永久排序sort,temp,sorted
print(citys)
citys.sort()
print(citys)
citys.sort(reverse=True)
print(citys)
print(sorted(citys))
print(citys)
#danxu,只是倒着打印，但是不涉及字母倒叙
print(citys)
citys.reverse()
print(citys)
citys.reverse()
print(citys)
#测长度lenght,从1开始算：

print(len(citys))

#第四章“操作列表
#4.1遍历整个列表
names=['daivi','sydi','poao','weilian']
for name in names:
    print('以下是我的自我介绍：')
#循环打印一个句子，给每个人问个好：
    print(f'hello,{name.title()}how are you!')
print("我的自我介绍结束了，谢谢大家！")#因为是没有缩进indenttation,因此执行完最后再打印最后一行，上面是一个块block

pizzas=['mydl','kendeji','zunbaopisa']
for pizza in pizzas:
    print(pizza)
    print(f'i like {pizza} pizza\n')
print('i really love pizza')
'''
'''
#4.2创建数值列表1(数值For循环
for digits in range(0 ,10):
    print(digits)

 #  创建数值表方法2 要用范围list(range())函数)
numbers=list(range(0,10))#打印从0-9的数，不包含10
print(numbers)
numberss=list(range(0,10,2))#打印从0开始，加2的数，不超过10，【0，2，4，6，8】
print(numberss)

#创建数值表3
digits=[]
for digit in range(0,3):
    x=digit**2
    digits.append(x)
print(digits)
#创建数值表
digits=[]
for x in range(0,8):
    digits.append(x/2)
print(digits)
#4.3列表解析
digits=[x*2 for x in range(0,3)]
print(digits)
#对列表数值进行简单的统计计算
digits=[1,2,3,4,5,6,7,8]
print(min(digits))
print(max(digits))
print(sum(digits))
#4.4列表切片(需要给定列表)
digits=[1,2,3,4,5,6]
print(digits[0:3])#打印前三个位置的数，0号位置，1号位置，2号位置，
print(digits[1:])#因为i没有最后的位置确定，则默认，打印1号位置往后打印
print(digits[-2:])
#遍历切片
names=['caojing','caohaiyun','caolaowu ','zhubajie']
for name in names[0:3]:
    print(name.title())
#复制列表
my_citys=['beijing','shanghai','jiangxi']
friends_citys=my_citys[:]
print(my_citys)
print(friends_citys)
#练习题目1
names=['caojing','caohaiyun','caolaowu ','caoming','caoxinzheng']
for name in names:
    print(name.title())
print('the frist three items in the list are:')
names_1=names[0:3]
print(names_1)
print('three items from the middle of the list are: ')
names_2=names[1:4]
print(names_2)
print('the last three items in the list are:')
names_3=names[-3:]
print(names_3)
#练习题2
my_pizzas=['zunbao','mingzi ','kendeji','piaoliang']
friend_pizzas=my_pizzas[:]
my_pizzas.append('zhu')
friend_pizzas.append('jiba')
print(my_pizzas)
print(friend_pizzas)
print('my favorite pizzas are:')
for a in my_pizzas:
    print(a)
print('\nmy favorite\'s  pizzas are:')
for b in friend_pizzas:
    print(b)
#练习3
foods=['shucai','roulei','xiangchang','pingguo','orgrang']
foods_py=foods[:]
foods.append('jibabi')
print(foods)
foods_py.append('shiguande')
print(foods_py)
for foods_py1 in foods_py:
    print(f'\n{foods_py1}')
for foods_py2 in foods:
    print(foods_py2)
#元组
#元组是一系列不可更改的值。可以访问但是不可以改变(不能删除、不能排序、不能有任何变化只能访问)，元组的表现形式是（），可以是数字，字符串，连个元素之间必须要，号隔开
a=(1,2,3,4,5,6)
print(a[1])
for b in a:
    print(b)
zizhucan=('dangao','shucai','ishi','jirou','pingguo')
for zhuzhu in zizhucan:
    print(zhuzhu)
zizhucan=('ishi','jirou','pingguo')
for zhuzhu in zizhucan:
    print(f'\n\t{zhuzhu}')

b=[]
c=list(range(1,9))
for a in c:
    e=a*2
    b.append(e)
print(b)

print("第四章，操作列表")
names=['davi','caojing','caoliangliang','cydn','mingming']
print('#第一部分是：遍历整个列表，并使用列表元素')
for name in names:
    print(name)
    print(f'hello,{name.title()}')
print('\n结束')
print('#第二部分是：range()函数创建数值列表')
print('\t#list(lange())函数使用')
a=list(range(0,10))
print(a)
b=list(range(0,10,2))
print(b)
print('\t#for语句与range函数创建数值列表')
c=[]
for d in range(0,10):
    z=d*2
    c.append(z)
print(c)
print('\n#第三部分是：数值列表简单计算')
print(max(c))
print(min(c))
print(sum(c))
print('\n#第四部分是：切片（列表某一片段数据')
print('\t#切片')
print(names[:])
print(names[0:2])
print(names[:3])
print(names[1:])
print('\t#遍历切片')
for a in names[0:4]:
    print(a)
    print('\t#复制数值列表')
names_1=names[:]
print(names_1)
print('\n#第五部分是：元组')
print('\t#什么是元组，元组是一些不可修改的列表，包括元素不能改变，列表形式不能修改用（）表示')
names_2=('daivi','caoming ','zhuzhu','bishi')
for y in names_2:#遍历取值
    print(y)
print(names[0])#直接访问

print('\n#第六部分是：程序的格式')
print('空行，代码模块block与block直接空行隔开')
print('每一行代码，最好是79个字符')
print('空格，每一个语句块与语句块最好空格4')
print('最好是严格按照PEP 8的格式书写代码')
a='love'

print(a.title())

a=[]
y=[]
n=[]
for i in range(1,20):
    c=i*2
    a.append(c)
print(a)
a_1=a[0:5]
print(a_1)
for i_1 in a_1[0:3]:
    y.append(i_1)
print(y)
for x in y:
    print(f'hello,my fovarited digits\'s {x}')
print('come over')
print(max(y))
print(min(y))
print(sum(y))
e=('a','b','c')
print(e[0])
e=('a','b','c')
print(e)
for m in a:
    n.append(m)
print(n)    
#第五章if语句。
names=['caojing','wenqiang','mingming','liangliang']
for name in names:
    if name != 'liangliang':
        print(name)
    else :
        print(name)
#if语句中的条件用法及意思：==，<=,>=,>,< ,and（和） ,or ,not in（不在） ,in（在）,!=(不等于)      
#第五章作业
car='subaru'
if car == 'subaru':
    print('true')
    print('is car ==\'subaru\',i predict ture')
else:
    print('false')
cars=['subaru','andi','fengtian','xiaopeng']
for car in cars:
    if car != 'xiaopeng':
        if car =='subaru':
            print(car)
        elif car=='andi':
            print(car)
        else:
            print('zhiyoufengtian!')
print('zzhisheng xia xiaopeng!')
    
a=int(input())
b=int(input())
if a == b :
    print(a+b)
elif a > 10 and b > 5:
    print('这么简单么？哈哈')
elif a > 10 or b > 5:
    print('我猜a和b ，a>10,b<5,要不就是a<10, b>5')
else:
    print('您好，您输入有误！')
messages=['caojing','wenqiang']
for message in messages:
    if message not in names:
        print('我真牛逼！')
    else :
        print('zaide l ')
        '''
'''
#动手试一试
alien_color='green'
color=['green','yellow','red']
if alien_color in color:
    if alien_color == 'green':
        print('恭喜您，获得5分奖励！')
    else :
        print('你猜的肯定是yellow or red,恭喜您获得10分')
else:
    print('对不起，你选的颜色不在列表color里')
age=int(input())
if 2 <= age < 4:
    print('这个人是幼儿')
elif 4 <= age < 13:
    print('这个人是儿童')
elif 13 <= age < 20:
    print('这个人是青少年')
elif 20 <= age < 65:
    print('这个人是成年人')
else:
    print('这个人是老年人')


x='mmmm'
favorite_fruits=['ap','or','bana','xigua']
if x  not in favorite_fruits :
    print('您好，您要的水果不在这个列表里！')
else:
    if x == 'bana':
        print('bana在')
    elif x == 'xigua':
        print('xigua在')
    elif x == 'or':
        print('or在')
    elif x=='ap':
        print('ap在')
digits=[1,2,3,4,5,6,7,8,9]
number=[1,3,4,10]
for i in number:
    if i in digits:
        print(i)
names=['caojing','caohaiyun','caoming','caowenqiang']
age=int(input())
for name in names:
         if name=='caojing' :
               print('恭喜您，获得5分奖励')
         elif name=='caohaiyun' :
               print('恭喜您，获得10分奖励')
         else :
               print('恭喜您，获得15分奖励')
if  0<=age<13 :
         if  2<=age<4 :
              print('你好，您是个幼儿') 
         elif  4<=age<13:
              print('你好，您是个儿童')   
         else:
             print('你好，您是个婴儿')
elif 13<=age<65:
         if   age<20 :     
             print('你好，您是个青少年') 
         else:  
             print('你好，您是个成年人了')
else:
    print('您好，您的年纪已经超过/等于65岁了，所以您是老年人了')

#continuey语句（跳出.....继续）

for i in range(10):
     if  i%2:
        continue
     print(i)
#计算1000以内的被7整除的前20个数(break语句（退出的意思）)
count=0
for i in range(0,1000,7):
    print(i)
    count+=1
    if count>=20:
        break
#whlie 语句

#第六章：字典（dict）
#访问字典中的值。
dict={'names':'caojing','age':29,'xingbie':'男'}
message=dict['names']
print(message)
#使用字典的值
print(f'我的所有组合都在这里：\n\t{message}')
#添加键值对
dict['x']=30#字典中添加键值对，已添加'x':30
dict['y']=25#字典中添加键值对，已添加'y':25
print(dict)
x={}
x['names']='caojing'
x['age']= 25
print(x)
#修改字典中的值
dict['names']='caohaiyun'
print(dict)
#删除键值对(del语句)
del dict['names']
print(dict)
#类似对象组成字典
favorite_languages={
     'caojing':'python',
     'caoliangliang':'java',
     'caoming':'c',
     'caoyi':'php'}
print(f"Caojing like {favorite_languages['caojing'].title()}")

#因为没有这个值因此，需要使用方法get()来设置一下
x=favorite_languages.get('points','no point value assigned')
print(x)
#遍历字典方法items包含键值循环遍历
names={'y':1,'x':2,'z':2}
for ky,vlue in names.items():
     print(f"\n{ky}:{vlue}")
     print(ky)
     print(vlue)
#遍历所有的键，用方法：keys()
for m in names.keys():
     print(m)
#遍历字典所有的值，用方法：values()
for n in names.values():
     print(n)
#按特定顺序遍历字典的键或值：
for m in sorted(names.keys()):
     print(m)
for n in sorted(names.values()):
     print(n)
#如果提取字典的值中有相同的，因此我们无法得出大概有有几类值，使用方法set（）可以解决这一点
for n in set(names.values()):
     print(n)
 

#练习
message={'first_name':'cao','last_name':'jing','age':29,'city':'shenzhen'}
print(message)
for x,y in message.items():
     print(f"{x}:{y}")
favorite_digits={'caojing':2,'caohaiyun':4,'caoyi':5,'zhubajie':10,'xinxin':13}

x=favorite_digits['caojing']
print(f"hello,caojing，are you favorite number {x}?")
y=favorite_digits['caohaiyun']
print(f"hello,caohaiyun,are you favorite number {y}?")
z=favorite_digits['caoyi']
print(f"hello,caoyi,are you favorite number {z}?")
u=favorite_digits['zhubajie']
print(f"hello,zhubajie,are you favorite number {u}?")
v=favorite_digits['xinxin']
print(f"hello,xinxin,are you favorite number{v}?" )
for x,y in favorite_digits.items():
     print(f"\n,{x}:{y}")
names={'name':'coajing','name1':'caohaiyun','name3':'zhubajie','name4':'caoming'}
for x in names.values():
     print(x)
print('thank you very much!')
print('请还未参加的同学尽快参加调查！')

#嵌套
#字典和列表
names={'names1':'caojing','names2':'caohaiyun','names3':'caowenqiang'}
next={'number1':1,'number2':2,'number3':3,'number4':4}
integrated=[names,next]
for y in integrated:
     print(y)

c=0
d=[]
for x in range(0,1000,7):
    print(x)
    c+=1
    d.append(x)
    if c >=20:
         break
print(d)
print(f'{sum(d)},{max(d)},{min(d)}')

#在字典中存储列表：
message={'names':['caojing','caohaiyun','caowenqiang'],
         'age':[23,24,25,27,29],
         '性别':['男','女'],
         'cype':['婴儿','少年','青年','成年','老年']}
for x in message['names']:
     print(f'\t{x}')
#在字典中存储字典。
    
#练习：
names={'names2':'caojing','names1':'caohaiyun','names3':'caowenqiang'}
age={'agea':1,'age2':2,'age3':3,'age4':4}
message=[names,age]
for x in message:
     print(x)

message={'number':12,'digit':14,'shuzi':18}
print(message['number'])
print(f"my favorite number is {message['number']}")
a={}
a['x']=65
a['y']=33
print(a)
del a['x']
print(a)
message={'caojing':'python','caohaiyun':'c','caolaozhu':'java'}
x=message['caojing'].title()
print(f"my favorite languages {x}")
names={'names':'caojing','names2':'caoming','names3':'caolaozhu'}
x=names.get('x','对不起您访问的没有这一行')
print(x)

favorite_language={'first':'python','next':'c','last':'java'}
for keys,values in favorite_language.items():
     print(f"{keys}:{values}")
for keys in favorite_language.keys():
       print(keys)
for values in favorite_language.values():
       print(values)
       
favorite_languages={'caojing':'python','baoming':'c','daohaiyun':'java'}
for x in sorted(favorite_languages.keys()):
       print(x)
for values in set(favorite_languages.values()):
     print(values)
favorite_languages={'caojing':'python','baoming':'c','daohaiyun':'java'}
for x in sorted(favorite_languages.values()):
       print(x)
a={'b':[1,2,3,4],
   'names':'caojing',
   'languages':['python','c','java']}
print(a['languages'])

a={
   'b':[1,2,3,4],
   'names':'caojing',
   'languages':['python','c','java']
   }
print(a['languages'])
for x,z in a.items():
       print(f"{x.title()},is name")
       for z1 in z:
            print(f"\t ,{z1}")

a={
     'names':{
          'names1':'caojing',
          'names2':'caohaiyun',
          'names3':'caoxing'
          },
     'number':{
          'number1':1,
          'numeber2':2,
          'number3':3
          },
     }
y=a['names']
print(y)
z=a['number']
print(z)
for x,z in a.items():
     print(f"\t{x}")
     for m in z.values():
          print(m)

#第六章练习
#第一块内容：字典的访问以及使用删除添加等
names_messages={
     'caojing':'shuaiqi',
     'caohaiyun':'buti',
     'caoliangliang':'angr',
     }
x=names_messages['caojing']
print(x)
print(f"caojing,{x}")
names_messages['caowenqiang']='chou'
print(names_messages)
del names_messages['caoliangliang']
print(names_messages)
#第二块内容：遍历字典，及使用
for z,y in names_messages.items():
     print(f"{z}:{y}")
     print(z)
     print(y)
for z in names_messages.keys():
     print(z)
for y in names_messages.values():
     print(y)
     #按特定顺序遍历所有的键和值：sorted(names_message.keys())其他同理
#第三块内容：嵌套：列表中有字典，字典中有列表，字典和字典，
favorite_numbers={
     'frist':1,
     'next':22,
     'last':44,
     }
integrated=[names_messages,favorite_numbers]
for h in integrated:
     print(h)
dictss={
     'favorite_numbers':[1,2,3,5,6,7],
     'names':['caojing','caohaiyun','caowenqiang'],
     'languages':['python','c','java'],
     }    
for f in dictss['favorite_numbers']:
     print(f)
for namess in dictss['names']:
     print(namess)
message={
     'choude':{
          'laji':'caoming',
          'xingge':'caolaowu',
          'zhu':'caoliangliang',
          },
     'numbers':{
          'caoyi':1,
          'caojing':2,
          'caohaiyun':4,
          },
     }
print(message['choude'])
print(message['numbers'])
for x,y in message['choude'].items():
     print(f"{x}:{y}")
for k,l in message.items():
     print(k)
     for n in l.keys():
          print(n)
     for g in l.values():
          print(g)
         
#第二章的内容
names='hello'
x=names.title()
print(x)
print(names.upper())
print(names.lower())
y=f'我们要勇敢的说:{x},或者：{names.upper()}'
print(y)
x='    caojing   '
print(x.strip())
print(x.rstrip())
print(x.lstrip())
message='不管怎么样，我都要学会python.\n\t_caojing'
print(message)
a=1
b=2
print(a+b)
a=2+3
print(a)
c=4/2
print(c)
number=14_0000_00000
print(number)
c,d,f=3,4,5
print(c+d)

#第三章内容
#列表简介
names=['caojing','caohaiyun','daci','edencao']
x=names[0]
print(x)
print(f'hello!{x},how are you ?')
names[1]='caohaihui'
print(names)
names.append('caohaiyun')
print(names)
names.insert(0,'caoyi')
print(names)
del names[4]
print(names)
dele=names.pop(3)
print(dele)
print(names)
names.remove('caojing')
print(names)
names.sort()
print(names)
print(len(names))
names.reverse()
print(names)
names.reverse()
print(names)
#第四章 操作列表
print(names)
for i in names:
     print(i)
     print(f'这些人都是我的亲人，比如：{i.title()}')
print('\n以上都是我的挚爱！')
#创建数值列表
x=[]
a=0
for c in range(20):
     y=c*2
     x.insert(0,y)
     a+=1
     if a>=5:
          break
print(x)
f=0
for t in range(0,27,2):
     f+=1
     print(t)
     if f>=5:
          break
g=list(range(0,20,5))
print(g)
print(len(g))
d=g[0:2]
print(d)
for o in g[0:]:
     print(o)
print(max(x))
print(min(x))
print(sum(x))
a=(1,2,3,4,5)
print(a[0])
#第五章（if语句）
age=int(input())
if 4>=age:
     print('您是个小孩')
elif 20>age>4:
     print('您是个青少年')
elif 20<=age<65:
     print('您是个成年人')
else:
     print('您是个老年人')
l=['caojing','caohaiyun','caoweni','lizhi']
for b in l:
     if b=='caohaiyun':
          print(f'hi,{b.title()}')
     elif b=='caojing':
          print(f'hi,{b.title()}')
     else:
          print(f'只有caoweni,和lizhi')
print('结束')
k=['caojing','caohaiyun']
for l1 in l:
     if l1 in k:
          print(l1)
     else:
          print(l1)
         
#第六章：
message={
     'names':'caojing',
     'age':29,
     'love':'caohaiyun',
     }
#访问，使用、修改、添加、删减
print(message['names'])
print(f"my names is {message['names'].title()}")
message['names']='caohaihui'
print(message)
message['身高']='180cm'
print(message)
del message['age']
print(message)
#遍历字典的键值对、键、值。
for i,x in message.items():
     print(f"{i}:{x}")
for i in message.keys():
     print(f'\t\n{i}')
for x in message.values():
     print(x)
#for x in set(message.values()))  :加上set()函数表示是查看有几个信息，去除掉相同的。
for i in sorted(message.keys()):#排序
     print(i)
#嵌套

#第七章内容（用户输入和while循环）
#input()函数
message=input('你的名字：')
print(message)
messages=' i like you.'
messages+='\nyou know?:'
a=input(messages)
print(f'hello,{a}')

#int（）函数获取数值
age=input("how old are you?")
print(age)
if int(age)>=2:
     print('你不是个婴儿')
else:
     print('你不过是个1岁的或者1岁不到的婴儿')
     
information="您好，您真的很好看："
information+='\n\t我并没有说谎，哈哈哈！'
x=input(information)
print(f'是么？{x}')
 
age=input("favorite number's")
age=int(age)
if 65>age>=20:
     print('你是个成年人！')
else:
     print('你是个老年人或者婴儿!')
print(age)
x=4&2
print(x)
#while+条件：循环
a=1
while a in range(45):
     print(a)
     a+=1
    
#练习
message='请问您要租赁什么样的汽车？'
message+='是哪国产的车？'
a=''
while a!='quit':
     a=input(message)
     if a!='quit':
         print(a)

a=[]
for i in range(12):
     i+=1
     if i%2==0:
          continue
     a.append(i)
print(a)
c=[]
x=0
while x<20:
     x+=1
     if x%2==0:
          continue
     c.append(x)
print(c)

#练习
message='请问有多少人吃饭?'
message=input(message)
message=int(message)
if message>8:
     print('没有空余的桌位')
else :
     print('有空桌')

digits=int(input())
if digits % 10 ==0 and digits!=0 :
     print('该数是10的整数')
else:
     
     print('该数不是10的倍数')
   
 
y='请问有多少人吃饭:'
x=''
while x != True:
     x=input(y)
     x=int(x)
     if x % 10==0 and x!=0:
          print('这个数是10的倍数')
     else:
          print('这个数不是10的倍数')
          continue
          ''
message='请输入你需要的披萨配料:'
cypes=""
while cypes!='quit':
     cypes=input(message)
     print(f'您好，我们会帮您加{cypes}')
     if cypes =='quit':
          print('x谢谢，祝您用餐愉快')

message='how old are you ?:'
while True:
     age=input(message)
     age=int(age)
     if age<3:
          print('need 免费')
     elif 3<=age<12:
          print('need 10美元')
     else:
          print('need 15美元')
        
#
message='how old are you ?:'
active=True
while active:
     age=input(message)
     age=int(age)
     if age<3:
          print('need 免费')         
     elif 3<=age<=12:
          print('need 10美元')
     elif 12<age<120:
          print('need 15美元')
     elif age>120:
          active=False
     elif age=='quit':
          break
print('结束')

#
while True:
     print('laodushishabi ')
     
#
a=1
while a<100000000:
     print(a)
     a+=1

message='看一看我们喜欢的是数字是什么类型'
message+='你喜欢奇数还是偶数？：'
variables=True
while variables:
     y=input(message)
     if y=='quit':
          variables=False
     else:
          print(f'我猜就知道你喜欢{y}')
         
message='看一看我们喜欢的是数字是什么类型'
message+='你喜欢奇数还是偶数？：'
while True:
     y=input(message)
     if y=='quit':
          break
     else:
          print(y)
          
#打印1-100的偶数
a=0
while a<100:
     a+=1
     if a%2==0:
          continue
     else:
          print(a)

#第八章内容函数
#8.1定义函数
def x():
     """简单的一句问候语"""
     print('good morning!')
x()
#打印一条信息
def message(zhu):
     """跟大家说对不起"""
     x='尊敬的各位嘉宾，各位来宾，欢迎大家来参加我的婚礼谢谢'
     print (f'hello,{x}{zhu}')
message('ngoushi ')#调用函数
def display_message():
     """打印你本章所学的内容"""
     print('本章学习的是第八张函数，谢谢！')
display_message()#调用函数
display_message()#调用函数
a=1
while True:
     display_message()
     a+=1
     if a>=10:
          break
def favorite_book(title):
     """喜欢的图书"""
     print(f'one of my favorite books is {title}')
favorite_book('Alice in wonderland')#调用函数
#8.2练习
def make_shirt(chima,languages):
     """T恤"""
     print(f'我喜欢的这个T恤，尺码是{chima}？')
     print(f'这个尺码的字样是{languages}。')
make_shirt('36.4','中文')
def make_shirt(chima,languages='ilove python'):
     """大号T恤"""
     print(f'我喜欢的这个T恤，尺码是{chima}？')
     print(f'这个尺码的字样是{languages}。')
make_shirt('大号')
def city(ciy,country="中国"):
     """城市的位置"""
     print(f'我来自{ciy}是x的一个城市')
     print(f'x是{country}的一个大省。')
city('reyjavik')
city('九江')
city('南昌')
city('伦敦','英')
 #8.3返回值

def x(y,z):
    """名字"""
    print(f'{y.title()}{z.title()}')
x('cao','jing')
x('cao','haiyun')

def cmp(x, y):
    if x < y:
        return -1
    if x == y:
        return 1
z=cmp(3,4)
print(z)
def make_shirt(chima,languages):
     """T恤"""
     x=f'我喜欢的这个T恤，尺码是{chima}？'
     x+=f'这个尺码的字样是{languages}。'
     return x
     
y=make_shirt('36.4','中文')
print(y)

def y(z,v,e=''):
     if e:
          x=f'{z}{v}{e}'
     else:
          x=f'{z}{v}'
     return x.title()
while True:
     print("\nplease tell me your name:" )
     names1=input('z')
     names2=input('v')
     names3=input('e')
     h=y(names1,names2,names3)

#复习第二章到第章的内容
#第二章
#第一个内容，运行hello python
print('hello python')
message='  hello python   '
print(message)
names=message.title()
print(names)
print(message.upper())
print(message.lower())
print(message.strip())
print(message.rstrip())
print(message.lstrip())
information=f"我真的喜欢python,我甚至想跟它打个招呼:\n\t\t\t\t\t{names.strip()}"
print(information) 
messagesss='laodu nishige shabi wotama de rini laomu '
print(messagesss)
messagesss='laodu nizheige shabi '
print(messagesss)
#字符串凡是只要只要带单双引号的都可以是字符串
#names_case.py
names1='eric'
names2=f'hello{names},would you like to learn some Python today？'
print(names2)
print(names1.title())
print(names1.upper())
print(names1.lower())
print(names1.strip())
print(names1.rstrip())
print(names1.lstrip())
print('Albert Einstein once said,"A person who never made a made mistaek never tried anything new"')
names='famous_person'
message=f'{names} said,"A person who never made a made mistaek never tried anything new"'
print(message)
#数
s=2
b=2
print(s+b)
print(s-b)
print('')
print(s*b)
print(s/b)
print(s//b)
print(s%b)
print(s**b)
print('整数和整数相除，以及与任何浮点数运算都是浮点数,数的大小可以用下划线隔开这样好看一点')
print(5+3)
print(4+4)
print(2+6)
print('多变量被赋值')
q,we,r,t,y=1,2,3,4,5
print(t+y)
digit=34
digit='我最喜欢的数是：34'
print(digit)
print('第三章的内容是列表简介')
names=['caojing','caohaiyun','duyucheng','tielin']
#访问列表的0位置的数
names0=names[0].title()
print(names0)
print(f'like{names0.upper()}')
for namess in names:
     print(namess.title())
     print(f'hello,{namess.upper()}')
print('创建自己喜欢的出行方式')
bicycles=['自行车','汽车','火车','subwey']
print('列表的修改添加、删减，排序，长度len')
names=['caojing','caohaiyun','wenqina','hubajie']
number=[1,3,5,6,8,9]
print('修改列列表的元素')
names[0]='nihao'
print(names[0])
print("添加涉及的放法，.append(),insert(0,'x')")
x=[]
x.append('caojing')
x.insert(1,'aohui')
x.append('zhuduiyou')
print(x)
print('列表的删减用法，涉及一个del语句,pop方法，按置删减的remove')
del x[1]
print(x)
m=x.pop()
print(x)
x.remove('caojing')
print(x)
print(m)
print('列表的排序是必须要拿下的')
number.sort()
print(number)
print('练习题开始了')
police=[]
police.append('caowenqiang')
police.insert(0,'luode ')
police.append('jiandong')
police.append('qiping')
print(police)
for x in police:
     print(f'我想邀请您来和我一起共进晚餐，{x}')
print(f'您好，我用另一种方式来请你吃饭{police[1]}')
print(f'刚好得知{police[2]}，没有办法来来赴约，因此我要来换一个人')
police[2]='zhubajie'
print(police)
for y in police:
     print(f'因为换了一个人，所以我们重新邀请，{y},好么?')
print('我已经找出一个更大的餐桌了，因此，我想多请三个人')
police.append('caohua')
police.append('caoxiaoxiao')
police.insert(0,'caohaihui ')
print(police)
police.insert(0,'caohaiyun')
police.insert(4,'caojing')
police.append('x')
print(police)
for c in police:
     print(f'您好，{c},请您来和我一起吃饭')
print("i'm sorry ,because 桌子没有到，因此只能邀请两位为好友吃饭")
v=police.pop(0)
print(f'对不起，{v}')
z=police.pop(1)
print(f'对不起，{z}')
b=police.pop(2)
print(f'对不起，{b}')
n=police.pop(3)
print(f'对不起，{n}')
l=police.pop(4)
print(f'对不起，{l}')
print(police)
for z in police:
     print(f'您好，您依然是被邀请范围之列{z}')
del police[0]
del police[1]
print(police)
police.remove('x')
print(police)
police.append(z)
police.append(v)
print(police)
h=[]
while police :
     y=police.pop()
     h.append(y)
print(h)
print(police)
h.sort()
print(h)
print(sorted(h))    
print(h)     
h.reverse()
print(h)
h.reverse()
print(h)
print(len(h))
like=[]
like.append('h梦幻巴黎')
like.append('t埃及金字塔')
like.append('f中国北京')
like.append('d死海')
like.append('a新疆')
print(like)
print(sorted(like))
print(like)
print(sorted(like))
print(like)
like.reverse()

a=[]
a.append('z中国')
a.append('a艾萨克斯坦')
a.append('w乌鲁木齐')
a.append('s死海')
a.insert(1,'caohaiyun')
print(a)
a[1]='美国'
a.sort()
print(a)
a.remove('美国')
del a[0]
print(a)
a.pop()
print(a)

print('亲爱的朋友们，我要开始第四章复习了，第四章的内容是操作列表')
favorite_languages=[]
favorite_languages.append('python')
favorite_languages.append('c')
favorite_languages.append('java')
favorite_languages.insert(0,'c++')
print(favorite_languages)
information=[]
for favorites in favorite_languages:
     print(favorites)
     print(f'我真的新欢这个语言：{favorites}')
     information.append(favorites)
print(information)
pizza=[]
pizza.append('zunmu')
pizza.append('kendiji')
pizza.append('hualaishi')
print(pizza)
for x in pizza:
     print(f'{x}真的难吃')
print('这辈子真的不能离开披萨')
dongwu=[]
dongwu.append('mao')
dongwu.append('dog')
dongwu.append('tuzi')
for f in dongwu:
     print(f)
     print('动物中我最喜欢的还是{f}')
print('谁不喜欢动物')
numbers=list(range(0,30))
print(numbers)
numbers=list(range(1,30,2))
print(numbers)
for digits in range(0,30):
     print(digits)
for digits in range(0,30,2):
     print(digits)
digit=[]
for x in range(1,30,2):
     digit.append(x)
print(digit)
x=[y**3 for y in range(0,20)]
print(x)
x=[y*1 for y in range(1,21)]
print(x)
for y in range(1,21):
     print(y)
x=[]
for digit in range(1,1000000):
     x.append(digit)
print(max(x))
print(min(x))
print(sum(x))
for f in range(1,20,2):
     print(f)
for x in range(3,30,3):
     print(x)
for v in range(1,11):
     x=v**3
     print(x)
m=[x**3 for x in range(1,11)]
print(m)
for c in m[3:]:
     print(c)
x=list(m[0:2])
print(x)
print('打印这个消息，如下为列表的三个元素')
v=list(m[0:3])
print(v)
print('再打印中间的三个元素')
v=list(m[4:7])
print(v)
v=list(m[-3:])
print(v)
pizza=[]
pizza.append('zunmu')
pizza.append('kendiji')
pizza.append('hualaishi')
print(pizza)
friend_pizza=pizza
pizza.append('zhuzhu')
friend_pizza.append('shi')
print(pizza)
print(friend_pizza)
print('哥要开始第五章的内容复习了，第五章if语句')
names=['caojing','caohaiyun','caowenqin','zhuzhu']
x=['caojing','caohai']
for v in x:
     if v in names:
          print(f'{v},表格间相同项')
     else :
          print(f'{v},x列表中不同项')
alien_color=['green','yellow','red']
x='green'
if x =='green':
     print('恭喜您获得了5分')
elif x=='yellow':
     print('恭喜您获得了10分')
else :
     print('恭喜您获得了15分')
age=int(input())
if  age<2:
     print('这个人是个婴儿')
elif 2<=age<4:
     print('这个人是个幼儿')
elif 4<=age<13:
     print('这个人是个儿童')
elif 13<=age<20:
     print('这个人是个青少年')
elif 20<=age<65:
     print('这个人是个成年人')
else:
     print('这个人是个老年人')

if age>=65:
     print('这是个老年人')
elif age<65:
     if age>=20:
          print('这是个成年人')
     elif age<20:
          if age>13:
               print('这是个青少年')
          elif 4<age<13:
               print('这是个儿童')
          else :
               print('这是个幼儿')
          
print('用if语句处理列表事宜')
names=['caojing','caohaiyun','caolaoqu','admin']

for x in names:
     if x=='caojing':
          print(f'woxihuannia,{x}')
     elif x=='caohaiyun':
          print(f'shige meilide nvzi {x}')
     else:
          print(f'nikendingshi ge wushigu l {x}')

for x in names:

     print(f'{x}是个优秀的人')
          
     if names:
          if x=='admin':
               print('nitama shigeshazi ')
          else:
               print('shagou ,zheishiyige putnyode xinxi ')
  
print('hahah...,我要开始第六章的复习了第六章是字典的学习')
 
a={}
a['names1']='caojing'
a['names2']='caojiabing'
a['names3']='caohaiyun'
a['names4']='caowenqiang'
print(a)
print(a['names1'])
print(f"说我是喜欢{a['names1'].title()}")
a['names2']='caojiche'
print(f"{a['names2'].title()}")
del a['names2']
print(a)
x={}
x['xingming']='caojing'
x['city']='bejiing'
x['languages']='chinaes'
x['age']=28
print(x)
y={}
y['names1']=1
y['names2']=2
y['names3']=3
y['names4']=4
y['names5']=5
print(y)
for keys,values in x.items():
     print(f"{keys}:\n{values}\n")
for x in y.keys():
     print(x)
for x in y.values():
     print(x)
d={}
d['names']='caojing'
d['age']='beijing'
d['city']='beijing'
for x in sorted(d.keys()):
     print(x)
for x in sorted(d.values()):
     print(x)
for x in set(sorted(d.values())):
     print(f'\n\n\n\n{x}')
message={}
message['黄河']='中国'
message['尼罗河']='非洲'
message['流沙河']='流沙'
for x,y in message.items():
     print(f"The {x.title()} run through {y.title()}")
for cx  in message.keys():
     print(cx.title())
for cy in message.values():
     print(cy.title())
x={}
y=['caojing','caihaiyun','caowenqiang','caolaowu','zhuzhu','caoyi','bishi','jiba']
x['names1']='caojing'
x['names2']='caihaiyun'
x['names3']='caolaowu'
print(x)
for z in y :
     if z in x.values():
          print(f"感谢您参与了调查{z.title()}")
     else:
          print(f"邀请您参与调查{z.title()}")
print(message)
print(x)
a=[]
for x in range(30):
     a.append(message)
for g in a[:5]:
     if g['黄河']=='中国':
          g['黄河']='bajie '
          g['尼罗河']='zhuzhu '
          g['流沙河']='jiba '
for v in a[:10]:
     print(f"{v}\nn")
print('hahahah  ,我已经开始第7章的复习了，用户输入和while循环')
#message=input('你属猪么？')
#print(f"no ,{message}")
message=input('请问您要租赁什么样的汽车？：')
print(f"我需要一辆{message.title()}")
digits=input('请问还有多少空位？')
y=int(digits)
if y >8 :
    print(f"对不起现在没有空位了。")
else :
    x=8-y
    print(f"现在还有位置,目前剩余位置是{x}")

x=1
while x<5:
    print("老杜是沙雕")
    x+=1

message='如果时间可以重来，你愿意回到过去么，为什么？'
message+='时间的长河从未因为人类的堕落而停滞不前。'
#x=True
#while x :
#   input(message)
#x=''
#while x != '停止':
#   messages=input(message)
#    if messages=='停止':
#       x='停止'
#  else :
#       print('谢谢，我知道你的答案了。')
y=[]
z=[]
x=-1
while x<100 :
    x+=1
    if x%2==0 :
        y.append(x)
    else:
        z.append(x)
print(f'100以内的奇数集合是：\n\n{z}')
print(f'\n\n\n100以内的偶数集合是：\n\n{y}')
y=True    
while y:
    message=input('请输入您需要的披萨配料：')
    if message=='quit':
        break
    else:
        print('尊敬的客户您好，我会为您添加配料{message}的，谢谢！')
        y=True

#y=True
#while y:
   # x=input('您好，请问您的年龄有多大？')
    #age=int(x)
    #if age in range(3,12):
       # print('如果您要购买电影票请投入10美元\n\n')
    #elif age>12:
        #print('如果您要购买电影票请投入15美元\n\n')
    #elif age<3:
        #print('\n\n您好，您是免费的！\n\n')
    #else:
       # break
       
#列表元素移动
names=['caojing','caohaiyun']
x=[]
while names:
    y=names.pop()
    x.append(y)
print(x)
    
#创建字典
message={}
t=True
while t :
    name=input('请问您的名字是：')
    information=input('您的年龄是:')
    message[name]=information
    v=input('是否还需要参与调查？yes/no')
    if v=='no':
        t=False
    else:
        t=True
print(message)
    


sandwich_orders=[]
sandwich_orders.append('三明治1')
sandwich_orders.append('三明治2')
sandwich_orders.append('三明治3')
finished_sandwiches=[]
for c in sandwich_orders:
    print(f'i made your tuna sandwich{c}')
while sandwich_orders:
    x=sandwich_orders.pop()
    finished_sandwiches.append(x)
print(finished_sandwiches)    
finished_sandwiches.append('pastrami')
finished_sandwiches.insert(1,'pastrami')
finished_sandwiches.insert(3,'pastrami')
print(finished_sandwiches)
while 'pastrasmi' in finished_sandwiches:
     finished_sandwhiches.remove('pastrasmi')
print(finished_sandwiches)
#第八章函数：
#第一节，定义函数
def message():
    print(f'我不知道未来会怎么样，但我会用我的方式去努力')
message()#函数调用
#向函数传递参数
def message(title):
    print(f'nishishenme {title}')
message('caojing')
#第二节，传递实参
def message(x,y):
    print(f'{x+y}，就是你要传递的参数之和')
message(2,3)
message(4,5)#多次调用
message(y=5,x=20)#只要赋值指定，顺序的付参就没有问题了。
#默认值
def message(x,y,z=20):
    print(f'{x+y+z}')
message(14,10,10)#默认值形参，只要你调用的时候需要就不写，如果需要，赋值的实参就是你要调用的
#第三节返回值：
def message(x,y,z=''):
    c=x+y
    d=c+z
    return d#填写了return返回则函数后面的就不会执行
    return c
r=message(1,1,1)
print(r)#因此返回的是d
#练习，利用函数收集名字
def names(names1,names2,names3=''):
    if names3:
        x=f'{names1}{names2}{names3}'
    else:
        x=f'{names1}{names2}'
    return x
while True:
    names1=input('您的姓:')
    names2=input('您的名:')
    names3=input('您的第二个名:')
    t=names(names1,names2,names3)
    print(f'你好：{t.title()}')
    b=input('是否还要继续调查：yes/no')
    if b=='no':
        break
    else:
        print('您已调查成功！')
#返回字典
def message(names,names1):
    x={names:names1,names1:names}
    return x
c=message('名字','内容')
print(c)
#换一种方式：
def message(names,names1):
    a={}
    a[names]=names1
    return a
y=message('cao','jing')
print(y)
#第4节，传毒列表
def message(names):
    for name in names:
        print(name)
y=[1,2,3,4,5]
message(y)#不能直接在实参上填写12345，因为实参要对应形参只能填写相对应数量的形参
def message(name):
    names=['caojing','zhzhu','bajie']
    if name in names:
        print('您好，您不是在邀请行里之内')        
    else:
        print('您好您是邀请行列!')
message('caojing')
message('nihao')
#第五节船传递任意数量的实参：
def peiliao(*jizhong):
    print(jizhong)
peiliao('lajiao','yan','jiangyou','cu')
#import 模块（文件名）
#文件名.函数（参数）#调用
#from 模块 import 函数（）：
#from 模块  import *    表示是八模块里面的函数全部导入

#第二章内容：
#变量
message='  hello,python  '
print(message)
s=message.title()
print(s)
y=message.upper()
c=message.lower()
v=(message.title()).strip()#k可以用括号给分隔开做两次方法
print(v)
#字符串
information="hello,python,i love you!"
print(information)
speak=f"{message} \n\t\t\t{information}"
print(speak)
print(f"{message.title()} \n{information.title()}")
#第三章列表简介
names=[]
names.append('caojing')#末尾添加元素
names.append('lixiaohong')
names.append('caohaiyun')
names.insert(0,'caohaiyun')#指定元素指定位置添加
print(names)
message=names[0]
print(f'{message.title()},i love you')#使用元素
names.remove('lixiaohong')#指定元素删除
print(names)
del names[0]#指定位置删除（永久）
v=names.pop()#末尾删除，也可指定位置，删除后可找回
print(names)
names.append('caohaihui')
names.append('haiyun')
names.insert(2,'zixia')
names.sort()#永久排序
print(names)
print(len(names))#计算列表长度
print(sorted(names))#临时排序
print(names)
names.reverse()#倒叙
print(names)
#第四章内容操作列表
#1、遍历列表2、创建数值列表3、数值列表的简单计算4、切片5、元组6、书写规范
for name in names:
    print(name)
number=[]
for digits in range(2,30):
    x=digits+2
    number.append(x)
print(number)
digits=list(range(30))
print(digits)
digits=list(range(0,30,2))#0，0+2，0+2+2，0+2+2+2.。。。不能超过30，不要忘记了
print(digits)
#range函数里面的（0，20，2）指的是从0开始加2一直加到不能超过20
y=[]
z=[]
for x in range(0,100):#第一种方法
    if x%2:
        continue
    else:
        y.append(x)
print(y)
for x in range(0,100,2):#第二种方法
    x+=1
    y.append(x)
print(y)    
number=list(range(2,101,2))#第三种方法
for x in number:
     x-=1
     z.append(x)
print(z)
x=max(z)
y=min(z)
c=sum(z)
print(max(z))
print(min(z))
print(sum(z))
for digits in z[0:20]:
    print(digits)
h=list(z[0:10])
print(h)
y=z[1:20]
print(y)
f=[]
for g in range(1,100,2):#第四种方法
    f.append(g)    
h=f[0:20]
print(h)
#第五章if语句
print(z)
x=f[1:10]
print(x)
r=[]
for i in x:#第一种方式查询不同的地方
    if i in z:
        r.append(i)
print(r)
x1=[]
x2=[]
message=['caojing','caoming','caowenqiang','caolianghua']#第二种放方法完美
names=['caohuaqiang','caowen ','caojing','caowenqiang']
for x in message:
    if x in names:
        x1.append(x)       
    else:
        x2.append(x)
print(f'\nmessage与names相比相同是：{x1}\n')
print(f'message与names相比不同是：{x2}')
age=input('您今年几岁了？')
age=int(age)
if age>20:
    print('您已成年了，请支付20万美元')
elif age<=20:
    print('您还未成年，可免费观看电影哦')
if None:
    print('您好')
else:
    print('哎，这一天简直太糟糕了！')
    
    
#第六章内容
message={}
message['名字']='caojing'
message['年龄']=29
message['性别']='男'
message['爱好']='喜欢唱歌'
print(message)
message['names']='caowenqiang'
print(message)
age=message['年龄']
print(age)
del message['names']
x=[]
y=[]
for key in message.keys():
    x.append(key)#如果遍历获得的数想放在一起就一定要用列表装起来
print(f'{x}\n')
for value in message.values():
    y.append(value)
print(y)
for key1,value1 in message.items():
    print(f'{key1}键的值是：{value1}')
message['名字']='jing'
#要使得值是独一无二的就要加一个set
for key1 in set(message.keys()):
    print(key1)
for value1 in set(message.values()):
    print(value1)
for key1,value1 in set(message.items()):
    print(f"\n{key1}:{value1}")
for key1 in sorted(set(message.keys())):
    print(f"hello,{key1}")
#q嵌套
print(message)
person={}
person['性格1']='red'
person['性格2']='black'
person['性格3']='blue'
person['性格4']='gree'
print(person)
list1=[]
list1.append(message)
list1.append(person)
for x in list1:
    print(x)
print(list1)
#字典嵌套在字典里面就是通过的获取他的键值对来定义这个
people={
    'color':{
        '性格1': 'red',
        '性格2': 'black',
        '性格3': 'blue',
        '性格4': 'gree'
        },
    'person':{
        '名字': 'jing',
        '年龄': 29,
        '性别': '男',
        '爱好': '喜欢唱歌'
        }
    }
for values1 in people.values():
    for values2 in values1.values():
        print(values2)
y=people['color']#字典的值一定是一个定值不能是一个变量，看到变量就是赋值，如这行
for x in y.values():
    print(x)
#字典里面加了字典真的非常好用，怎么取都没有问题
#简单完美
#同样字典里面有列表也是非常简单的
#访问值之后就直接遍历直接获得，列表字典你想要获得数组还是列表还是字典简单
#例子
information={
    'color':['red','blue','gree','black'],
    'message':['caojing','29岁','喜欢打球']
    }
neirong=information['message']
for x in neirong:
    print(x)
print(neirong[2])
#什么是王者，我就是i王者简单的要死

#第七章用户输入和while循环
#for与while的区别在于前者是之作用于集合，针对一个范围的集合去进行循环，而后者是可
#满足条件可以一直循环》
#第一个内容：y用户输入

message1=input('你是老杜么？yes/no')
while True:
    if message1 == 'yes':
        print('老杜是傻逼！')
    elif message1=='no':
        print('不是老杜就一边呆着去！')
        break
    else:
        print('瞎了你的狗眼了看清楚只填yes/no,瞎几把乱填，你是傻子么？')
        break
#a=0
#while a<100:#第五种
#    a+=1
    if a%2:
#        print(a)        
 #   else:        
#        continue

#第八章内容
#1、定义函数2、加参数、3、返回值4、列表、5、元组和字典、6、导入模块的函数
def names(names1):
    """对名字打印一个问候语"""
    print(f"Hello,{names1.title()}nice to meet you!")
#调用函数：
names('cao jing')
#例子一奇数列表
def name(names1):
    """求列表的所有奇数"""
    number_jishu=[]
    for digits in names1:
        if digits%2:
           number_jishu.append(digits)
        else:
            continue
    return number_jishu
#调用函数
numbers=list(range(0,33))
x=name(numbers)
print(x)
#获得名字例子
def names (names1,names2,names3=''):
    if names3:
        y=f'{names1.title()}{names2}{names3}'
    else:
        y=f'{names1.title()}{names2}'
    return y
#调用函数
name=names('cao','hai','yun')
namess=names('cao','jing')
print(name)
print(namess)
#元组和字典的表示方式
def message(name,*people):
    """美团收集点餐后的缺什么"""
    print(f'{name}同学，你剩余的配料如下：')
    for x in people:
        print(f'\n{x}')
#调用函数：
message('caojing','筷子','辣椒','佐料')
#字典的方式
def dicts(first,names,**dictss):
    """打印一个字典"""
    dictss['first_names']=first
    dictss['last_names']=names
    return dictss
#调用函数
y=dicts('cao','jing',z='cao',k='feng')
print(y)
#d导入模块调取函数
#import pizza
#pizza.函数名（参数）
#直接取模块特定函数
#from 模块 import 函数名
#函数名（参数）
#取多个函数
#from 模块 import 函数名1，函数名2，函数名3
#函数名1（参数）
#取所有函数
#from 模块 import *
#函数（参数）
#给函数换名字
#from 模块 import 函数名 as 重新取得名字
#重新取得名字（参数）
#给模块换名字
#import 模块名 as 更新的名字
#更新的名字.函数名（参数）
#函数说实在的确实简单

#第八章的内容，函数，这次要用俩个小时去回顾函数
#函数的内容如下：
information='8.1节：1.定义函数'
x=input(information)

def function_names():
    """定义函数"""
    print(f"函数定义，\ndef 函数名（形参）：\n\t函数体\n调用函数:\n函数名（实参）")
#调用函数
function_names()
def function_names1():
    """打印一个问候语"""
    print(f'hello,Mrcao,nice to meet you !')
#调用函数
function_names1()
message='8.2节传递实参:\n\t\t8.2.1,添加函数形参'
print(message)
def function_names2(names1,names2):
    """跟上面的人问好"""
    print(f'您好，{names1}!,希望能和您成为朋友！')
    print(f'您好，{names2}!,很高兴认识您！')
#调用函数：
function_names2('曹静','靓仔')
def function_names3(a,b):
    """数值的简单计算"""
    c=a+b
    print(c)
print('调用函数:')
function_names3(2,3)
print('8.2.2小节：关键值实参')
def names(names2,names3):
    """例子：形参与实参关联"""
    print(f'{names2}{names3}')
print('调用函数')
names(names2='cao',names3='jing')
print('8.2.3节：默认值')
def function_names4(names5,names4=1):#系统默认值不能放在形参的最前面，不然会引起错误
    """默认值例子"""
    print(f'{names4}{names5}')
print('调用函数')
function_names4(names4='cao',names5='jing')#当重新赋值，则以新的值去运行
print('8.3节return返回值，3.1')
def names7(frist_name,last_name,namess=''):
    """获得名字"""
    if namess:
        names_1=f'{frist_name.title()}{last_name}{namess}'
    else:
        names_1=f'{frist_name.title()}{last_name}'
    return names_1
print('调用函数')
namesss=names7('cao','jing')
print(namesss)
namesss=names7('cao','hai','yun')
print(namesss)
print('8.3节，返回字典8.3.2')
def dict(names,age):
    """返回字典"""
    x={'names':names,'age':age}
    return x
y=True
while y:
    names=input('您的名字是：')
    age=input('您的年龄是：')
    #调用函数
    message=dict(names,age)
    print(message)
    h=input('请问您还继续调查么？yes/no')
    if h=='no':
        break
    else:
        True
#8.4利用函数传递列表
def list_1(names):
    """传递列表"""
    for names1 in names:
        print(names1.title())
#调用函数
names=['caojing','caoming','caohua ']
list_1(names)
#8.5传递任意数量的实参
def number(*dict):
    print(dict)
#调用函数
number(1,2,3,4,5,6,7)
#使用位置实参，以及任意数量的实参
def messagess(information,*neirong):
    print(f'第{information}次，打印下面的元组了')
    print(neirong)
messagess(12,'x','y','u','iu')
#制作字典
def ci_dian(names,age,**message):
    message['names']=names
    message['age']=age
    return message
x=ci_dian('caojing',29,xing_ge='leguan',xing_bie='nan')
print(x)

#获得奇数
def ji_shu(list):
    """获得一个范围内的奇数"""
    jihe=[]
    for jishu in list :
        if jishu%2 :
            jihe.append(jishu)
        else:
            continue
    return jihe
list=range(100)
y=ji_shu(list)
print(y)
#获得奇数
def jishu(list):
    jishu_jihe=[]
    lengt=len(list)
    number=1
    while number==1:
        for jishu in list:
            if jishu%2:
                jishu_jihe.append(jishu)
        number+=1   
    return jishu_jihe

list=list(range(0,55))
message=jishu(list)
print(message)
#利用函数可以做一些事
#用列表可以做一些事
x=['caojing','nihao','gude','meidi']
y=[]
while x :
    y1=x.pop()
    y.append(y1)
    print(f'yanzheng{y1}')
for x1 in y:
    print(x1)

z=['caojing']
for x in z:
    while x in y:
        y.remove(x)
print(y)    

while True:
    x=int(input('请输入你想要验证的数字：'))
    if x%2:
        print('您输入的数是奇数')       
    else:
        print('您输入的数是偶数')

#第八章函数的复习：
#第一节内容：定义函数
#例子：
def names():
    """复习第八章的内容"""
    print('你好，我在做第八章的第一节的内容实例')
#调用函数
names()
def message():
    """利用函数打印一个句子"""
    print('我想在复习的是：\n\t第八章第1节的内容')
#调用函数
message()
#第二节内容：传递实参
#传递多个参数
def number(a,b,c,d,f,e,r):
    print('您的手机电话号码前面的7位数是？')
    x=[a,b,c,d,f,e,r]
    print(x)
#调用函数
number(1,2,3,4,5,6,7)
#默认值和关键字实参
#例子
def names(x,y='c'):
    """关键字实参"""
    print(f'我的名字是{x}，我喜欢的字母是{y}')
#调用函数
names('caojing')
names('caojing',y='a')
#以上两种调用函数的方式，如果在形参里有默认值，则相对性的形参变量可填可不填看需求
#第三节内容：return返回值

在什么情况下需要用到return？
当你需要这个值的时候，需要用到return
return与print之间的区别？
1、return并不是直接打印，是需要把值再利用，因此在调用函数时需要设置一个接受变量。然后看需求是否打印
并且return还有一个功能是只调用return后面的值,并且程序运行到return就回退出函数。
2、print表示是直接打印结果
因为在调取函数的时候关系到是直接把结果给到用户看还是再利用加工就关系到你使用那个。

def sums(a,b,c):
    
    """总数计算"""

    x=b+c
    d=x+a
    y=[x,d]
    return y
#调用函数
jieshou=sums(1,2,3)
print(jieshou)
#return返回值只能返回一个变量的值，如果需要返回两个就需要建立一个集合
#让实参变成可选+加whil用户输入
def names(names1,names2,names3=''):
    """打印名字"""
    if names:
        name=f'{names1.title()},{names2},{names3}'
    else:
        name=f'{names1.title()},{names2}'
    return name
while True:
    frist_name=input('您的姓是：')
    last_name=input('您的名是：')
    three_name=input('您的名的第二个字是：')
    #调用函数
    quanming=names(frist_name,last_name,three_name)
    print(quanming)

#传递字典
def tedian(name,age):
    tediand={'names':name,'ages':age}
    return tediand
#调用函数
zidian=tedian('caojing',29)
print(zidian)
#第四节传递列表
def lists(shu):
    y=[]
    for x in shu:
        y.append(x)
    return y
#调用函数：
shu=[1,2,3,4,5,6]
jihe=list(shu)
print(jihe)
#第五节：传递任意数量的实参
def tubles(*jihe):
    for x in jihe:
        print(x)
#调用函数
tubles('caojing','caohaiyun','caoming','caowenqinag')
def tuble(langes,*jihe2):
    print(f'现在是第{langes}次打印名字')
    for namess in jihe2:
        print(namess)
#调用函数：
tuble(2,'caojing','caohaiyun')

def dicits(**z):
    z['名字']='caojing'
    z['nihao']='nihao'
    return z
#调用函数
zidianss=dicits(f='zhu',d='s')
print(zidianss)   
#d第6节的内容：导入模块
print(f'\n1、导入模块：\nimport 模块\n调用函数：\n模块.函数名（参数）')
print(f"\n2、导入模块的指定函数：\nfrom 模块 import 函数名1，函数名2....\n调用函数：\n函数名1、2(实参)")
print(f"\n3、导入模块的所有函数：\nfrom 模块 import *)\n调用函数：\n函数名（实参）")
print(f"\n5、给模块的函数换名：\nfrom 模块 import 函数名 as 更换的名字\n 调用函数 ：\n更改的名字（实参）")
print(f"\n6、给模块换名：\nimport 模块名 as 新的模块名，\n调用函数：\n新的模块名.函数名（实参)")

#第八章，函数def funcion（形参）
#内容第一节定义函数
def function():
    """打印一句话"""
    print('你好，我开始学习函数了')
#调用函数
function()
#内容第二节传递参数
#1、内容是：传递实参
def function_frist(name,names):
    """打印名字"""
    print(f'{name.title()},nice to meet you ')
    print(f'{names.title()},i love you!')
#调用函数
function_frist('cao jing','cao hai yun')
#2、内容是：关键字实参以及默认值。
def function_last(names1,names2='caohaiyun'):
    #在定义函数时不能将有默认值的参数放在没有默认值参数的前面。
    """打印名字"""
    print(f'{names1},{names2}')
#调用函数
function_last( names1='caojing')
function_last('caowenqiang','caohaiyun')
function_last('x')
#第三节 返回值
#普通实参返回
def names(names1,names2,names3=''):
    x=f'{names1}{names2}'
    return x
#调用函数
jieshou=names('caojing','caohaiyun')
print(jieshou)
#传递字典
def dicts(names1,names2):
    dictss={'names':names1,'name':names2}
    return dictss
#调用函数
dicits=dicts('cojing','caohaiyun')
print(dicits)
#让参数变成可选
def names(names1,names2,names3=''):
    if names3:
        x=f'{names1.title()},\t{names2.title()},\t{names3.upper()}'
    else:
        x=f'{names1.lower()},\t{names2.upper()}'
    return x
#调用函数
names11=names('caojing','caohaiyun')
print(names11)
#与while语句的使用
def namesss(names1,names2,names3=''):
    if names3:
        x=f'{names1.title()},\t{names2.upper()}.\t{names3.lower()}'
    else:
        x=f'{names1.title()},\t{names2.upper()}'
    return x
while True:
    names1=input('请输入您姓：')
    names2=input('请输入您名：')
    names3=input('请输入您名：')
    s=namesss(names1,names2,names3)
    lianxu=input('调查是否还需要继续(yes\no)：')
    if lianxu=='yes':
        print(f'您的名字是{s.title()}')
        continue
    else:
        print(f'您好您的名字是：{s}谢谢您的参与！')
        break
#第八章内容
#1、定义函数2、加参数、3、返回值4、列表、5、元组和字典、6、导入模块的函数
def names(names1):
    """对名字打印一个问候语"""
    print(f"Hello,{names1.title()}nice to meet you!")
#调用函数：
names('cao jing')
#例子一奇数列表
def name(names1):
    """求列表的所有奇数"""
    number_jishu=[]
    for digits in names1:
        if digits%2:
           number_jishu.append(digits)
        else:
            continue
    return number_jishu
#调用函数
numbers=list(range(0,33))
x=name(numbers)
print(x)
#获得名字例子
def names (names1,names2,names3=''):
    if names3:
        y=f'{names1.title()}{names2}{names3}'
    else:
        y=f'{names1.title()}{names2}'
    return y
#调用函数
name=names('cao','hai','yun')
namess=names('cao','jing')
print(name)
print(namess)
#元组和字典的表示方式
def message(name,*people):
    """美团收集点餐后的缺什么"""
    print(f'{name}同学，你剩余的配料如下：')
    for x in people:
        print(f'\n{x}')
#调用函数：
message('caojing','筷子','辣椒','佐料')
#字典的方式
def dicts(first,names,**dictss):
    """打印一个字典"""
    dictss['first_names']=first
    dictss['last_names']=names
    return dictss
#调用函数
y=dicts('cao','jing',z='cao',k='feng')
print(y)
#d导入模块调取函数
#import pizza
#pizza.函数名（参数）
#直接取模块特定函数
#from 模块 import 函数名
#函数名（参数）
#取多个函数
#from 模块 import 函数名1，函数名2，函数名3
#函数名1（参数）
#取所有函数
#from 模块 import *
#函数（参数）
#给函数换名字
#from 模块 import 函数名 as 重新取得名字
#重新取得名字（参数）
#给模块换名字
#import 模块名 as 更新的名字
#更新的名字.函数名（参数）
#函数说实在的确实简单

#第八章的内容，函数，这次要用俩个小时去回顾函数
#函数的内容如下：
information='8.1节：1.定义函数'
x=input(information)

def function_names():
    """定义函数"""
    print(f"函数定义，\ndef 函数名（形参）：\n\t函数体\n调用函数:\n函数名（实参）")
#调用函数
function_names()
def function_names1():
    """打印一个问候语"""
    print(f'hello,Mrcao,nice to meet you !')
#调用函数
function_names1()
message='8.2节传递实参:\n\t\t8.2.1,添加函数形参'
print(message)
def function_names2(names1,names2):
    """跟上面的人问好"""
    print(f'您好，{names1}!,希望能和您成为朋友！')
    print(f'您好，{names2}!,很高兴认识您！')
#调用函数：
function_names2('曹静','靓仔')
def function_names3(a,b):
    """数值的简单计算"""
    c=a+b
    print(c)
print('调用函数:')
function_names3(2,3)
print('8.2.2小节：关键值实参')
def names(names2,names3):
    """例子：形参与实参关联"""
    print(f'{names2}{names3}')
print('调用函数')
names(names2='cao',names3='jing')
print('8.2.3节：默认值')
def function_names4(names5,names4=1):#系统默认值不能放在形参的最前面，不然会引起错误
    """默认值例子"""
    print(f'{names4}{names5}')
print('调用函数')
function_names4(names4='cao',names5='jing')#当重新赋值，则以新的值去运行
print('8.3节return返回值，3.1')
def names7(frist_name,last_name,namess=''):
    """获得名字"""
    if namess:
        names_1=f'{frist_name.title()}{last_name}{namess}'
    else:
        names_1=f'{frist_name.title()}{last_name}'
    return names_1
print('调用函数')
namesss=names7('cao','jing')
print(namesss)
namesss=names7('cao','hai','yun')
print(namesss)
print('8.3节，返回字典8.3.2')
def dict(names,age):
    """返回字典"""
    x={'names':names,'age':age}
    return x
y=True
while y:
    names=input('您的名字是：')
    age=input('您的年龄是：')
    #调用函数
    message=dict(names,age)
    print(message)
    h=input('请问您还继续调查么？yes/no')
    if h=='no':
        break
    else:
        True
#8.4利用函数传递列表
def list_1(names):
    """传递列表"""
    for names1 in names:
        print(names1.title())
#调用函数
names=['caojing','caoming','caohua ']
list_1(names)
#8.5传递任意数量的实参
def number(*dict):
    print(dict)
#调用函数
number(1,2,3,4,5,6,7)
#使用位置实参，以及任意数量的实参
def messagess(information,*neirong):
    print(f'第{information}次，打印下面的元组了')
    print(neirong)
messagess(12,'x','y','u','iu')
#制作字典
def ci_dian(names,age,**message):
    message['names']=names
    message['age']=age
    return message
x=ci_dian('caojing',29,xing_ge='leguan',xing_bie='nan')
print(x)

#获得奇数
def ji_shu(list):
    """获得一个范围内的奇数"""
    jihe=[]
    for jishu in list :
        if jishu%2 :
            jihe.append(jishu)
        else:
            continue
    return jihe
list=range(100)
y=ji_shu(list)
print(y)
#获得奇数
def jishu(list):
    jishu_jihe=[]
    lengt=len(list)
    number=1
    while number==1:
        for jishu in list:
            if jishu%2:
                jishu_jihe.append(jishu)
        number+=1   
    return jishu_jihe

list=list(range(0,55))
message=jishu(list)
print(message)
#利用函数可以做一些事
#用列表可以做一些事
x=['caojing','nihao','gude','meidi']
y=[]
while x :
    y1=x.pop()
    y.append(y1)
    print(f'yanzheng{y1}')
for x1 in y:
    print(x1)

z=['caojing']
for x in z:
    while x in y:
        y.remove(x)
print(y)    

while True:
    x=int(input('请输入你想要验证的数字：'))
    if x%2:
        print('您输入的数是奇数')       
    else:
        print('您输入的数是偶数')

#第八章函数的复习：
#第一节内容：定义函数
#例子：
def names():
    """复习第八章的内容"""
    print('你好，我在做第八章的第一节的内容实例')
#调用函数
names()
def message():
    """利用函数打印一个句子"""
    print('我想在复习的是：\n\t第八章第1节的内容')
#调用函数
message()
#第二节内容：传递实参
#传递多个参数
def number(a,b,c,d,f,e,r):
    print('您的手机电话号码前面的7位数是？')
    x=[a,b,c,d,f,e,r]
    print(x)
#调用函数
number(1,2,3,4,5,6,7)
#默认值和关键字实参
#例子
def names(x,y='c'):
    """关键字实参"""
    print(f'我的名字是{x}，我喜欢的字母是{y}')
#调用函数
names('caojing')
names('caojing',y='a')
#以上两种调用函数的方式，如果在形参里有默认值，则相对性的形参变量可填可不填看需求
#第三节内容：return返回值

在什么情况下需要用到return？
当你需要这个值的时候，需要用到return
return与print之间的区别？
1、return并不是直接打印，是需要把值再利用，因此在调用函数时需要设置一个接受变量。然后看需求是否打印
并且return还有一个功能是只调用return后面的值,并且程序运行到return就回退出函数。
2、print表示是直接打印结果
因为在调取函数的时候关系到是直接把结果给到用户看还是再利用加工就关系到你使用那个。

def sums(a,b,c):
    
    """总数计算"""

    x=b+c
    d=x+a
    y=[x,d]
    return y
#调用函数
jieshou=sums(1,2,3)
print(jieshou)
#return返回值只能返回一个变量的值，如果需要返回两个就需要建立一个集合
#让实参变成可选+加whil用户输入
def names(names1,names2,names3=''):
    """打印名字"""
    if names:
        name=f'{names1.title()},{names2},{names3}'
    else:
        name=f'{names1.title()},{names2}'
    return name
while True:
    frist_name=input('您的姓是：')
    last_name=input('您的名是：')
    three_name=input('您的名的第二个字是：')
    #调用函数
    quanming=names(frist_name,last_name,three_name)
    print(quanming)

#传递字典
def tedian(name,age):
    tediand={'names':name,'ages':age}
    return tediand
#调用函数
zidian=tedian('caojing',29)
print(zidian)
#第四节传递列表
def lists(shu):
    y=[]
    for x in shu:
        y.append(x)
    return y
#调用函数：
shu=[1,2,3,4,5,6]
jihe=list(shu)
print(jihe)
#第五节：传递任意数量的实参
def tubles(*jihe):
    for x in jihe:
        print(x)
#调用函数
tubles('caojing','caohaiyun','caoming','caowenqinag')
def tuble(langes,*jihe2):
    print(f'现在是第{langes}次打印名字')
    for namess in jihe2:
        print(namess)
#调用函数：
tuble(2,'caojing','caohaiyun')

def dicits(**z):
    z['名字']='caojing'
    z['nihao']='nihao'
    return z
#调用函数
zidianss=dicits(f='zhu',d='s')
print(zidianss)   
#d第6节的内容：导入模块
print(f'\n1、导入模块：\nimport 模块\n调用函数：\n模块.函数名（参数）')
print(f"\n2、导入模块的指定函数：\nfrom 模块 import 函数名1，函数名2....\n调用函数：\n函数名1、2(实参)")
print(f"\n3、导入模块的所有函数：\nfrom 模块 import *)\n调用函数：\n函数名（实参）")
print(f"\n5、给模块的函数换名：\nfrom 模块 import 函数名 as 更换的名字\n 调用函数 ：\n更改的名字（实参）")
print(f"\n6、给模块换名：\nimport 模块名 as 新的模块名，\n调用函数：\n新的模块名.函数名（实参)")

#第八章，函数def funcion（形参）
#内容第一节定义函数
def function():
    """打印一句话"""
    print('你好，我开始学习函数了')
#调用函数
function()
#内容第二节传递参数
#1、内容是：传递实参
def function_frist(name,names):
    """打印名字"""
    print(f'{name.title()},nice to meet you ')
    print(f'{names.title()},i love you!')
#调用函数
function_frist('cao jing','cao hai yun')
#2、内容是：关键字实参以及默认值。
def function_last(names1,names2='caohaiyun'):
    #在定义函数时不能将有默认值的参数放在没有默认值参数的前面。
    """打印名字"""
    print(f'{names1},{names2}')
#调用函数
function_last( names1='caojing')
function_last('caowenqiang','caohaiyun')
function_last('x')
#第三节 返回值
#普通实参返回
def names(names1,names2,names3=''):
    x=f'{names1}{names2}'
    return x
#调用函数
jieshou=names('caojing','caohaiyun')
print(jieshou)
#传递字典
def dicts(names1,names2):
    dictss={'names':names1,'name':names2}
    return dictss
#调用函数
dicits=dicts('cojing','caohaiyun')
print(dicits)
#让参数变成可选
def names(names1,names2,names3=''):
    if names3:
        x=f'{names1.title()},\t{names2.title()},\t{names3.upper()}'
    else:
        x=f'{names1.lower()},\t{names2.upper()}'
    return x
#调用函数
names11=names('caojing','caohaiyun')
print(names11)
#与while语句的使用
def namesss(names1,names2,names3=''):
    if names3:
        x=f'{names1.title()},\t{names2.upper()}.\t{names3.lower()}'
    else:
        x=f'{names1.title()},\t{names2.upper()}'
    return x
while True:
    names1=input('请输入您姓：')
    names2=input('请输入您名：')
    names3=input('请输入您名：')
    s=namesss(names1,names2,names3)
    lianxu=input('调查是否还需要继续(yes\no)：')
    if lianxu=='yes':
        print(f'您的名字是{s.title()}')
        continue
    else:
        print(f'您好您的名字是：{s}谢谢您的参与！')
        break
        #第八章内容
#1、定义函数2、加参数、3、返回值4、列表、5、元组和字典、6、导入模块的函数
def names(names1):
    """对名字打印一个问候语"""
    print(f"Hello,{names1.title()}nice to meet you!")
#调用函数：
names('cao jing')
#例子一奇数列表
def name(names1):
    """求列表的所有奇数"""
    number_jishu=[]
    for digits in names1:
        if digits%2:
           number_jishu.append(digits)
        else:
            continue
    return number_jishu
#调用函数
numbers=list(range(0,33))
x=name(numbers)
print(x)
#获得名字例子
def names (names1,names2,names3=''):
    if names3:
        y=f'{names1.title()}{names2}{names3}'
    else:
        y=f'{names1.title()}{names2}'
    return y
#调用函数
name=names('cao','hai','yun')
namess=names('cao','jing')
print(name)
print(namess)
#元组和字典的表示方式
def message(name,*people):
    """美团收集点餐后的缺什么"""
    print(f'{name}同学，你剩余的配料如下：')
    for x in people:
        print(f'\n{x}')
#调用函数：
message('caojing','筷子','辣椒','佐料')
#字典的方式
def dicts(first,names,**dictss):
    """打印一个字典"""
    dictss['first_names']=first
    dictss['last_names']=names
    return dictss
#调用函数
y=dicts('cao','jing',z='cao',k='feng')
print(y)
#d导入模块调取函数
#import pizza
#pizza.函数名（参数）
#直接取模块特定函数
#from 模块 import 函数名
#函数名（参数）
#取多个函数
#from 模块 import 函数名1，函数名2，函数名3
#函数名1（参数）
#取所有函数
#from 模块 import *
#函数（参数）
#给函数换名字
#from 模块 import 函数名 as 重新取得名字
#重新取得名字（参数）
#给模块换名字
#import 模块名 as 更新的名字
#更新的名字.函数名（参数）
#函数说实在的确实简单

#第八章的内容，函数，这次要用俩个小时去回顾函数
#函数的内容如下：
information='8.1节：1.定义函数'
x=input(information)

def function_names():
    """定义函数"""
    print(f"函数定义，\ndef 函数名（形参）：\n\t函数体\n调用函数:\n函数名（实参）")
#调用函数
function_names()
def function_names1():
    """打印一个问候语"""
    print(f'hello,Mrcao,nice to meet you !')
#调用函数
function_names1()
message='8.2节传递实参:\n\t\t8.2.1,添加函数形参'
print(message)
def function_names2(names1,names2):
    """跟上面的人问好"""
    print(f'您好，{names1}!,希望能和您成为朋友！')
    print(f'您好，{names2}!,很高兴认识您！')
#调用函数：
function_names2('曹静','靓仔')
def function_names3(a,b):
    """数值的简单计算"""
    c=a+b
    print(c)
print('调用函数:')
function_names3(2,3)
print('8.2.2小节：关键值实参')
def names(names2,names3):
    """例子：形参与实参关联"""
    print(f'{names2}{names3}')
print('调用函数')
names(names2='cao',names3='jing')
print('8.2.3节：默认值')
def function_names4(names5,names4=1):#系统默认值不能放在形参的最前面，不然会引起错误
    """默认值例子"""
    print(f'{names4}{names5}')
print('调用函数')
function_names4(names4='cao',names5='jing')#当重新赋值，则以新的值去运行
print('8.3节return返回值，3.1')
def names7(frist_name,last_name,namess=''):
    """获得名字"""
    if namess:
        names_1=f'{frist_name.title()}{last_name}{namess}'
    else:
        names_1=f'{frist_name.title()}{last_name}'
    return names_1
print('调用函数')
namesss=names7('cao','jing')
print(namesss)
namesss=names7('cao','hai','yun')
print(namesss)
print('8.3节，返回字典8.3.2')
def dict(names,age):
    """返回字典"""
    x={'names':names,'age':age}
    return x
y=True
while y:
    names=input('您的名字是：')
    age=input('您的年龄是：')
    #调用函数
    message=dict(names,age)
    print(message)
    h=input('请问您还继续调查么？yes/no')
    if h=='no':
        break
    else:
        True
#8.4利用函数传递列表
def list_1(names):
    """传递列表"""
    for names1 in names:
        print(names1.title())
#调用函数
names=['caojing','caoming','caohua ']
list_1(names)
#8.5传递任意数量的实参
def number(*dict):
    print(dict)
#调用函数
number(1,2,3,4,5,6,7)
#使用位置实参，以及任意数量的实参
def messagess(information,*neirong):
    print(f'第{information}次，打印下面的元组了')
    print(neirong)
messagess(12,'x','y','u','iu')
#制作字典
def ci_dian(names,age,**message):
    message['names']=names
    message['age']=age
    return message
x=ci_dian('caojing',29,xing_ge='leguan',xing_bie='nan')
print(x)

#获得奇数
def ji_shu(list):
    """获得一个范围内的奇数"""
    jihe=[]
    for jishu in list :
        if jishu%2 :
            jihe.append(jishu)
        else:
            continue
    return jihe
list=range(100)
y=ji_shu(list)
print(y)
#获得奇数
def jishu(list):
    jishu_jihe=[]
    lengt=len(list)
    number=1
    while number==1:
        for jishu in list:
            if jishu%2:
                jishu_jihe.append(jishu)
        number+=1   
    return jishu_jihe

list=list(range(0,55))
message=jishu(list)
print(message)
#利用函数可以做一些事
#用列表可以做一些事
x=['caojing','nihao','gude','meidi']
y=[]
while x :
    y1=x.pop()
    y.append(y1)
    print(f'yanzheng{y1}')
for x1 in y:
    print(x1)

z=['caojing']
for x in z:
    while x in y:
        y.remove(x)
print(y)    

while True:
    x=int(input('请输入你想要验证的数字：'))
    if x%2:
        print('您输入的数是奇数')       
    else:
        print('您输入的数是偶数')

#第八章函数的复习：
#第一节内容：定义函数
#例子：
def names():
    """复习第八章的内容"""
    print('你好，我在做第八章的第一节的内容实例')
#调用函数
names()
def message():
    """利用函数打印一个句子"""
    print('我想在复习的是：\n\t第八章第1节的内容')
#调用函数
message()
#第二节内容：传递实参
#传递多个参数
def number(a,b,c,d,f,e,r):
    print('您的手机电话号码前面的7位数是？')
    x=[a,b,c,d,f,e,r]
    print(x)
#调用函数
number(1,2,3,4,5,6,7)
#默认值和关键字实参
#例子
def names(x,y='c'):
    """关键字实参"""
    print(f'我的名字是{x}，我喜欢的字母是{y}')
#调用函数
names('caojing')
names('caojing',y='a')
#以上两种调用函数的方式，如果在形参里有默认值，则相对性的形参变量可填可不填看需求
#第三节内容：return返回值

在什么情况下需要用到return？
当你需要这个值的时候，需要用到return
return与print之间的区别？
1、return并不是直接打印，是需要把值再利用，因此在调用函数时需要设置一个接受变量。然后看需求是否打印
并且return还有一个功能是只调用return后面的值,并且程序运行到return就回退出函数。
2、print表示是直接打印结果
因为在调取函数的时候关系到是直接把结果给到用户看还是再利用加工就关系到你使用那个。

def sums(a,b,c):
    
    """总数计算"""

    x=b+c
    d=x+a
    y=[x,d]
    return y
#调用函数
jieshou=sums(1,2,3)
print(jieshou)
#return返回值只能返回一个变量的值，如果需要返回两个就需要建立一个集合
#让实参变成可选+加whil用户输入
def names(names1,names2,names3=''):
    """打印名字"""
    if names:
        name=f'{names1.title()},{names2},{names3}'
    else:
        name=f'{names1.title()},{names2}'
    return name
while True:
    frist_name=input('您的姓是：')
    last_name=input('您的名是：')
    three_name=input('您的名的第二个字是：')
    #调用函数
    quanming=names(frist_name,last_name,three_name)
    print(quanming)

#传递字典
def tedian(name,age):
    tediand={'names':name,'ages':age}
    return tediand
#调用函数
zidian=tedian('caojing',29)
print(zidian)
#第四节传递列表
def lists(shu):
    y=[]
    for x in shu:
        y.append(x)
    return y
#调用函数：
shu=[1,2,3,4,5,6]
jihe=list(shu)
print(jihe)
#第五节：传递任意数量的实参
def tubles(*jihe):
    for x in jihe:
        print(x)
#调用函数
tubles('caojing','caohaiyun','caoming','caowenqinag')
def tuble(langes,*jihe2):
    print(f'现在是第{langes}次打印名字')
    for namess in jihe2:
        print(namess)
#调用函数：
tuble(2,'caojing','caohaiyun')

def dicits(**z):
    z['名字']='caojing'
    z['nihao']='nihao'
    return z
#调用函数
zidianss=dicits(f='zhu',d='s')
print(zidianss)   
#d第6节的内容：导入模块
print(f'\n1、导入模块：\nimport 模块\n调用函数：\n模块.函数名（参数）')
print(f"\n2、导入模块的指定函数：\nfrom 模块 import 函数名1，函数名2....\n调用函数：\n函数名1、2(实参)")
print(f"\n3、导入模块的所有函数：\nfrom 模块 import *)\n调用函数：\n函数名（实参）")
print(f"\n5、给模块的函数换名：\nfrom 模块 import 函数名 as 更换的名字\n 调用函数 ：\n更改的名字（实参）")
print(f"\n6、给模块换名：\nimport 模块名 as 新的模块名，\n调用函数：\n新的模块名.函数名（实参)")

#第八章，函数def funcion（形参）
#内容第一节定义函数
def function():
    """打印一句话"""
    print('你好，我开始学习函数了')
#调用函数
function()
#内容第二节传递参数
#1、内容是：传递实参
def function_frist(name,names):
    """打印名字"""
    print(f'{name.title()},nice to meet you ')
    print(f'{names.title()},i love you!')
#调用函数
function_frist('cao jing','cao hai yun')
#2、内容是：关键字实参以及默认值。
def function_last(names1,names2='caohaiyun'):
    #在定义函数时不能将有默认值的参数放在没有默认值参数的前面。
    """打印名字"""
    print(f'{names1},{names2}')
#调用函数
function_last( names1='caojing')
function_last('caowenqiang','caohaiyun')
function_last('x')
#第三节 返回值
#普通实参返回
def names(names1,names2,names3=''):
    x=f'{names1}{names2}'
    return x
#调用函数
jieshou=names('caojing','caohaiyun')
print(jieshou)
#传递字典
def dicts(names1,names2):
    dictss={'names':names1,'name':names2}
    return dictss
#调用函数
dicits=dicts('cojing','caohaiyun')
print(dicits)
#让参数变成可选
def names(names1,names2,names3=''):
    if names3:
        x=f'{names1.title()},\t{names2.title()},\t{names3.upper()}'
    else:
        x=f'{names1.lower()},\t{names2.upper()}'
    return x
#调用函数
names11=names('caojing','caohaiyun')
print(names11)
#与while语句的使用
def namesss(names1,names2,names3=''):
    if names3:
        x=f'{names1.title()},\t{names2.upper()}.\t{names3.lower()}'
    else:
        x=f'{names1.title()},\t{names2.upper()}'
    return x
while True:
    names1=input('请输入您姓：')
    names2=input('请输入您名：')
    names3=input('请输入您名：')
    s=namesss(names1,names2,names3)
    lianxu=input('调查是否还需要继续(yes\no)：')
    if lianxu=='yes':
        print(f'您的名字是{s.title()}')
        continue
    else:
        print(f'您好您的名字是：{s}谢谢您的参与！')
        break
#第四节传递列表
def lists(list1):
    for x in list1:
        print(x)
list12=[1,2,3,4,5]
lists(list12)
#第五节是传递任意数量实参
def yuanzu(*jihe):
    for x in jihe:
        print(x)
yuanzu('caojing','caowenqiang','caoming')
def didain(**x):
    x['names']='caoing'
    x['nihao']='caohaiyun'
    return x
y=didain(f='ni')
print(y)
#第四节传递列表
def lists(list1):
    for x in list1:
        print(x)
list12=[1,2,3,4,5]
lists(list12)
#第五节是传递任意数量实参
def yuanzu(*jihe):
    for x in jihe:
        print(x)
yuanzu('caojing','caowenqiang','caoming')
def didain(**x):
    x['names']='caoing'
    x['nihao']='caohaiyun'
    return x
y=didain(f='ni')
print(y)#第四节传递列表
def lists(list1):
    for x in list1:
        print(x)
list12=[1,2,3,4,5]
lists(list12)
#第五节是传递任意数量实参
def yuanzu(*jihe):
    for x in jihe:
        print(x)
yuanzu('caojing','caowenqiang','caoming')
def didain(**x):
    x['names']='caoing'
    x['nihao']='caohaiyun'
    return x
y=didain(f='ni')
print(y)
#第八章内容
#1、定义函数2、加参数、3、返回值4、列表、5、元组和字典、6、导入模块的函数
def names(names1):
    """对名字打印一个问候语"""
    print(f"Hello,{names1.title()}nice to meet you!")
#调用函数：
names('cao jing')
#例子一奇数列表
def name(names1):
    """求列表的所有奇数"""
    number_jishu=[]
    for digits in names1:
        if digits%2:
           number_jishu.append(digits)
        else:
            continue
    return number_jishu
#调用函数
numbers=list(range(0,33))
x=name(numbers)
print(x)
#获得名字例子
def names (names1,names2,names3=''):
    if names3:
        y=f'{names1.title()}{names2}{names3}'
    else:
        y=f'{names1.title()}{names2}'
    return y
#调用函数
name=names('cao','hai','yun')
namess=names('cao','jing')
print(name)
print(namess)
#元组和字典的表示方式
def message(name,*people):
    """美团收集点餐后的缺什么"""
    print(f'{name}同学，你剩余的配料如下：')
    for x in people:
        print(f'\n{x}')
#调用函数：
message('caojing','筷子','辣椒','佐料')
#字典的方式
def dicts(first,names,**dictss):
    """打印一个字典"""
    dictss['first_names']=first
    dictss['last_names']=names
    return dictss
#调用函数
y=dicts('cao','jing',z='cao',k='feng')
print(y)
#d导入模块调取函数
#import pizza
#pizza.函数名（参数）
#直接取模块特定函数
#from 模块 import 函数名
#函数名（参数）
#取多个函数
#from 模块 import 函数名1，函数名2，函数名3
#函数名1（参数）
#取所有函数
#from 模块 import *
#函数（参数）
#给函数换名字
#from 模块 import 函数名 as 重新取得名字
#重新取得名字（参数）
#给模块换名字
#import 模块名 as 更新的名字
#更新的名字.函数名（参数）
#函数说实在的确实简单

#第八章的内容，函数，这次要用俩个小时去回顾函数
#函数的内容如下：
information='8.1节：1.定义函数'
x=input(information)

def function_names():
    """定义函数"""
    print(f"函数定义，\ndef 函数名（形参）：\n\t函数体\n调用函数:\n函数名（实参）")
#调用函数
function_names()
def function_names1():
    """打印一个问候语"""
    print(f'hello,Mrcao,nice to meet you !')
#调用函数
function_names1()
message='8.2节传递实参:\n\t\t8.2.1,添加函数形参'
print(message)
def function_names2(names1,names2):
    """跟上面的人问好"""
    print(f'您好，{names1}!,希望能和您成为朋友！')
    print(f'您好，{names2}!,很高兴认识您！')
#调用函数：
function_names2('曹静','靓仔')
def function_names3(a,b):
    """数值的简单计算"""
    c=a+b
    print(c)
print('调用函数:')
function_names3(2,3)
print('8.2.2小节：关键值实参')
def names(names2,names3):
    """例子：形参与实参关联"""
    print(f'{names2}{names3}')
print('调用函数')
names(names2='cao',names3='jing')
print('8.2.3节：默认值')
def function_names4(names5,names4=1):#系统默认值不能放在形参的最前面，不然会引起错误
    """默认值例子"""
    print(f'{names4}{names5}')
print('调用函数')
function_names4(names4='cao',names5='jing')#当重新赋值，则以新的值去运行
print('8.3节return返回值，3.1')
def names7(frist_name,last_name,namess=''):
    """获得名字"""
    if namess:
        names_1=f'{frist_name.title()}{last_name}{namess}'
    else:
        names_1=f'{frist_name.title()}{last_name}'
    return names_1
print('调用函数')
namesss=names7('cao','jing')
print(namesss)
namesss=names7('cao','hai','yun')
print(namesss)
print('8.3节，返回字典8.3.2')
def dict(names,age):
    """返回字典"""
    x={'names':names,'age':age}
    return x
y=True
while y:
    names=input('您的名字是：')
    age=input('您的年龄是：')
    #调用函数
    message=dict(names,age)
    print(message)
    h=input('请问您还继续调查么？yes/no')
    if h=='no':
        break
    else:
        True
#8.4利用函数传递列表
def list_1(names):
    """传递列表"""
    for names1 in names:
        print(names1.title())
#调用函数
names=['caojing','caoming','caohua ']
list_1(names)
#8.5传递任意数量的实参
def number(*dict):
    print(dict)
#调用函数
number(1,2,3,4,5,6,7)
#使用位置实参，以及任意数量的实参
def messagess(information,*neirong):
    print(f'第{information}次，打印下面的元组了')
    print(neirong)
messagess(12,'x','y','u','iu')
#制作字典
def ci_dian(names,age,**message):
    message['names']=names
    message['age']=age
    return message
x=ci_dian('caojing',29,xing_ge='leguan',xing_bie='nan')
print(x)

#获得奇数
def ji_shu(list):
    """获得一个范围内的奇数"""
    jihe=[]
    for jishu in list :
        if jishu%2 :
            jihe.append(jishu)
        else:
            continue
    return jihe
list=range(100)
y=ji_shu(list)
print(y)
#获得奇数
def jishu(list):
    jishu_jihe=[]
    lengt=len(list)
    number=1
    while number==1:
        for jishu in list:
            if jishu%2:
                jishu_jihe.append(jishu)
        number+=1   
    return jishu_jihe

list=list(range(0,55))
message=jishu(list)
print(message)
#利用函数可以做一些事
#用列表可以做一些事
x=['caojing','nihao','gude','meidi']
y=[]
while x :
    y1=x.pop()
    y.append(y1)
    print(f'yanzheng{y1}')
for x1 in y:
    print(x1)

z=['caojing']
for x in z:
    while x in y:
        y.remove(x)
print(y)    

while True:
    x=int(input('请输入你想要验证的数字：'))
    if x%2:
        print('您输入的数是奇数')       
    else:
        print('您输入的数是偶数')

#第八章函数的复习：
#第一节内容：定义函数
#例子：
def names():
    """复习第八章的内容"""
    print('你好，我在做第八章的第一节的内容实例')
#调用函数
names()
def message():
    """利用函数打印一个句子"""
    print('我想在复习的是：\n\t第八章第1节的内容')
#调用函数
message()
#第二节内容：传递实参
#传递多个参数
def number(a,b,c,d,f,e,r):
    print('您的手机电话号码前面的7位数是？')
    x=[a,b,c,d,f,e,r]
    print(x)
#调用函数
number(1,2,3,4,5,6,7)
#默认值和关键字实参
#例子
def names(x,y='c'):
    """关键字实参"""
    print(f'我的名字是{x}，我喜欢的字母是{y}')
#调用函数
names('caojing')
names('caojing',y='a')
#以上两种调用函数的方式，如果在形参里有默认值，则相对性的形参变量可填可不填看需求
#第三节内容：return返回值

在什么情况下需要用到return？
当你需要这个值的时候，需要用到return
return与print之间的区别？
1、return并不是直接打印，是需要把值再利用，因此在调用函数时需要设置一个接受变量。然后看需求是否打印
并且return还有一个功能是只调用return后面的值,并且程序运行到return就回退出函数。
2、print表示是直接打印结果
因为在调取函数的时候关系到是直接把结果给到用户看还是再利用加工就关系到你使用那个。

def sums(a,b,c):
    
    """总数计算"""

    x=b+c
    d=x+a
    y=[x,d]
    return y
#调用函数
jieshou=sums(1,2,3)
print(jieshou)
#return返回值只能返回一个变量的值，如果需要返回两个就需要建立一个集合
#让实参变成可选+加whil用户输入
def names(names1,names2,names3=''):
    """打印名字"""
    if names:
        name=f'{names1.title()},{names2},{names3}'
    else:
        name=f'{names1.title()},{names2}'
    return name
while True:
    frist_name=input('您的姓是：')
    last_name=input('您的名是：')
    three_name=input('您的名的第二个字是：')
    #调用函数
    quanming=names(frist_name,last_name,three_name)
    print(quanming)

#传递字典
def tedian(name,age):
    tediand={'names':name,'ages':age}
    return tediand
#调用函数
zidian=tedian('caojing',29)
print(zidian)
#第四节传递列表
def lists(shu):
    y=[]
    for x in shu:
        y.append(x)
    return y
#调用函数：
shu=[1,2,3,4,5,6]
jihe=list(shu)
print(jihe)
#第五节：传递任意数量的实参
def tubles(*jihe):
    for x in jihe:
        print(x)
#调用函数
tubles('caojing','caohaiyun','caoming','caowenqinag')
def tuble(langes,*jihe2):
    print(f'现在是第{langes}次打印名字')
    for namess in jihe2:
        print(namess)
#调用函数：
tuble(2,'caojing','caohaiyun')

def dicits(**z):
    z['名字']='caojing'
    z['nihao']='nihao'
    return z
#调用函数
zidianss=dicits(f='zhu',d='s')
print(zidianss)   
#d第6节的内容：导入模块
print(f'\n1、导入模块：\nimport 模块\n调用函数：\n模块.函数名（参数）')
print(f"\n2、导入模块的指定函数：\nfrom 模块 import 函数名1，函数名2....\n调用函数：\n函数名1、2(实参)")
print(f"\n3、导入模块的所有函数：\nfrom 模块 import *)\n调用函数：\n函数名（实参）")
print(f"\n5、给模块的函数换名：\nfrom 模块 import 函数名 as 更换的名字\n 调用函数 ：\n更改的名字（实参）")
print(f"\n6、给模块换名：\nimport 模块名 as 新的模块名，\n调用函数：\n新的模块名.函数名（实参)")

#第八章，函数def funcion（形参）
#内容第一节定义函数
def function():
    """打印一句话"""
    print('你好，我开始学习函数了')
#调用函数
function()
#内容第二节传递参数
#1、内容是：传递实参
def function_frist(name,names):
    """打印名字"""
    print(f'{name.title()},nice to meet you ')
    print(f'{names.title()},i love you!')
#调用函数
function_frist('cao jing','cao hai yun')
#2、内容是：关键字实参以及默认值。
def function_last(names1,names2='caohaiyun'):
    #在定义函数时不能将有默认值的参数放在没有默认值参数的前面。
    """打印名字"""
    print(f'{names1},{names2}')
#调用函数
function_last( names1='caojing')
function_last('caowenqiang','caohaiyun')
function_last('x')
#第三节 返回值
#普通实参返回
def names(names1,names2,names3=''):
    x=f'{names1}{names2}'
    return x
#调用函数
jieshou=names('caojing','caohaiyun')
print(jieshou)
#传递字典
def dicts(names1,names2):
    dictss={'names':names1,'name':names2}
    return dictss
#调用函数
dicits=dicts('cojing','caohaiyun')
print(dicits)
#让参数变成可选
def names(names1,names2,names3=''):
    if names3:
        x=f'{names1.title()},\t{names2.title()},\t{names3.upper()}'
    else:
        x=f'{names1.lower()},\t{names2.upper()}'
    return x
#调用函数
names11=names('caojing','caohaiyun')
print(names11)
#与while语句的使用
def namesss(names1,names2,names3=''):
    if names3:
        x=f'{names1.title()},\t{names2.upper()}.\t{names3.lower()}'
    else:
        x=f'{names1.title()},\t{names2.upper()}'
    return x
while True:
    names1=input('请输入您姓：')
    names2=input('请输入您名：')
    names3=input('请输入您名：')
    s=namesss(names1,names2,names3)
    lianxu=input('调查是否还需要继续(yes\no)：')
    if lianxu=='yes':
        print(f'您的名字是{s.title()}')
        continue
    else:
        print(f'您好您的名字是：{s}谢谢您的参与！')
        break
#第四节传递列表
def lists(list1):
    for x in list1:
        print(x)
list12=[1,2,3,4,5]
lists(list12)
#第五节是传递任意数量实参
def yuanzu(*jihe):
    for x in jihe:
        print(x)
yuanzu('caojing','caowenqiang','caoming')
def didain(**x):
    x['names']='caoing'
    x['nihao']='caohaiyun'
    return x
y=didain(f='ni')
print(y)
#第八章内容
#1、定义函数2、加参数、3、返回值4、列表、5、元组和字典、6、导入模块的函数
def names(names1):
    """对名字打印一个问候语"""
    print(f"Hello,{names1.title()}nice to meet you!")
#调用函数：
names('cao jing')
#例子一奇数列表
def name(names1):
    """求列表的所有奇数"""
    number_jishu=[]
    for digits in names1:
        if digits%2:
           number_jishu.append(digits)
        else:
            continue
    return number_jishu
#调用函数
numbers=list(range(0,33))
x=name(numbers)
print(x)
#获得名字例子
def names (names1,names2,names3=''):
    if names3:
        y=f'{names1.title()}{names2}{names3}'
    else:
        y=f'{names1.title()}{names2}'
    return y
#调用函数
name=names('cao','hai','yun')
namess=names('cao','jing')
print(name)
print(namess)
#元组和字典的表示方式
def message(name,*people):
    """美团收集点餐后的缺什么"""
    print(f'{name}同学，你剩余的配料如下：')
    for x in people:
        print(f'\n{x}')
#调用函数：
message('caojing','筷子','辣椒','佐料')
#字典的方式
def dicts(first,names,**dictss):
    """打印一个字典"""
    dictss['first_names']=first
    dictss['last_names']=names
    return dictss
#调用函数
y=dicts('cao','jing',z='cao',k='feng')
print(y)
#d导入模块调取函数
#import pizza
#pizza.函数名（参数）
#直接取模块特定函数
#from 模块 import 函数名
#函数名（参数）
#取多个函数
#from 模块 import 函数名1，函数名2，函数名3
#函数名1（参数）
#取所有函数
#from 模块 import *
#函数（参数）
#给函数换名字
#from 模块 import 函数名 as 重新取得名字
#重新取得名字（参数）
#给模块换名字
#import 模块名 as 更新的名字
#更新的名字.函数名（参数）
#函数说实在的确实简单

#第八章的内容，函数，这次要用俩个小时去回顾函数
#函数的内容如下：
information='8.1节：1.定义函数'
x=input(information)

def function_names():
    """定义函数"""
    print(f"函数定义，\ndef 函数名（形参）：\n\t函数体\n调用函数:\n函数名（实参）")
#调用函数
function_names()
def function_names1():
    """打印一个问候语"""
    print(f'hello,Mrcao,nice to meet you !')
#调用函数
function_names1()
message='8.2节传递实参:\n\t\t8.2.1,添加函数形参'
print(message)
def function_names2(names1,names2):
    """跟上面的人问好"""
    print(f'您好，{names1}!,希望能和您成为朋友！')
    print(f'您好，{names2}!,很高兴认识您！')
#调用函数：
function_names2('曹静','靓仔')
def function_names3(a,b):
    """数值的简单计算"""
    c=a+b
    print(c)
print('调用函数:')
function_names3(2,3)
print('8.2.2小节：关键值实参')
def names(names2,names3):
    """例子：形参与实参关联"""
    print(f'{names2}{names3}')
print('调用函数')
names(names2='cao',names3='jing')
print('8.2.3节：默认值')
def function_names4(names5,names4=1):#系统默认值不能放在形参的最前面，不然会引起错误
    """默认值例子"""
    print(f'{names4}{names5}')
print('调用函数')
function_names4(names4='cao',names5='jing')#当重新赋值，则以新的值去运行
print('8.3节return返回值，3.1')
def names7(frist_name,last_name,namess=''):
    """获得名字"""
    if namess:
        names_1=f'{frist_name.title()}{last_name}{namess}'
    else:
        names_1=f'{frist_name.title()}{last_name}'
    return names_1
print('调用函数')
namesss=names7('cao','jing')
print(namesss)
namesss=names7('cao','hai','yun')
print(namesss)
print('8.3节，返回字典8.3.2')
def dict(names,age):
    """返回字典"""
    x={'names':names,'age':age}
    return x
y=True
while y:
    names=input('您的名字是：')
    age=input('您的年龄是：')
    #调用函数
    message=dict(names,age)
    print(message)
    h=input('请问您还继续调查么？yes/no')
    if h=='no':
        break
    else:
        True
        #第八章内容
#1、定义函数2、加参数、3、返回值4、列表、5、元组和字典、6、导入模块的函数
def names(names1):
    """对名字打印一个问候语"""
    print(f"Hello,{names1.title()}nice to meet you!")
#调用函数：
names('cao jing')
#例子一奇数列表
def name(names1):
    """求列表的所有奇数"""
    number_jishu=[]
    for digits in names1:
        if digits%2:
           number_jishu.append(digits)
        else:
            continue
    return number_jishu
#调用函数
numbers=list(range(0,33))
x=name(numbers)
print(x)
#获得名字例子
def names (names1,names2,names3=''):
    if names3:
        y=f'{names1.title()}{names2}{names3}'
    else:
        y=f'{names1.title()}{names2}'
    return y
#调用函数
name=names('cao','hai','yun')
namess=names('cao','jing')
print(name)
print(namess)
#元组和字典的表示方式
def message(name,*people):
    """美团收集点餐后的缺什么"""
    print(f'{name}同学，你剩余的配料如下：')
    for x in people:
        print(f'\n{x}')
#调用函数：
message('caojing','筷子','辣椒','佐料')
#字典的方式
def dicts(first,names,**dictss):
    """打印一个字典"""
    dictss['first_names']=first
    dictss['last_names']=names
    return dictss
#调用函数
y=dicts('cao','jing',z='cao',k='feng')
print(y)
#d导入模块调取函数
#import pizza
#pizza.函数名（参数）
#直接取模块特定函数
#from 模块 import 函数名
#函数名（参数）
#取多个函数
#from 模块 import 函数名1，函数名2，函数名3
#函数名1（参数）
#取所有函数
#from 模块 import *
#函数（参数）
#给函数换名字
#from 模块 import 函数名 as 重新取得名字
#重新取得名字（参数）
#给模块换名字
#import 模块名 as 更新的名字
#更新的名字.函数名（参数）
#函数说实在的确实简单

#第八章的内容，函数，这次要用俩个小时去回顾函数
#函数的内容如下：
information='8.1节：1.定义函数'
x=input(information)

def function_names():
    """定义函数"""
    print(f"函数定义，\ndef 函数名（形参）：\n\t函数体\n调用函数:\n函数名（实参）")
#调用函数
function_names()
def function_names1():
    """打印一个问候语"""
    print(f'hello,Mrcao,nice to meet you !')
#调用函数
function_names1()
message='8.2节传递实参:\n\t\t8.2.1,添加函数形参'
print(message)
def function_names2(names1,names2):
    """跟上面的人问好"""
    print(f'您好，{names1}!,希望能和您成为朋友！')
    print(f'您好，{names2}!,很高兴认识您！')
#调用函数：
function_names2('曹静','靓仔')
def function_names3(a,b):
    """数值的简单计算"""
    c=a+b
    print(c)
print('调用函数:')
function_names3(2,3)
print('8.2.2小节：关键值实参')
def names(names2,names3):
    """例子：形参与实参关联"""
    print(f'{names2}{names3}')
print('调用函数')
names(names2='cao',names3='jing')
print('8.2.3节：默认值')
def function_names4(names5,names4=1):#系统默认值不能放在形参的最前面，不然会引起错误
    """默认值例子"""
    print(f'{names4}{names5}')
print('调用函数')
function_names4(names4='cao',names5='jing')#当重新赋值，则以新的值去运行
print('8.3节return返回值，3.1')
def names7(frist_name,last_name,namess=''):
    """获得名字"""
    if namess:
        names_1=f'{frist_name.title()}{last_name}{namess}'
    else:
        names_1=f'{frist_name.title()}{last_name}'
    return names_1
print('调用函数')
namesss=names7('cao','jing')
print(namesss)
namesss=names7('cao','hai','yun')
print(namesss)
print('8.3节，返回字典8.3.2')
def dict(names,age):
    """返回字典"""
    x={'names':names,'age':age}
    return x
y=True
while y:
    names=input('您的名字是：')
    age=input('您的年龄是：')
    #调用函数
    message=dict(names,age)
    print(message)
    h=input('请问您还继续调查么？yes/no')
    if h=='no':
        break
    else:
        True
#8.4利用函数传递列表
def list_1(names):
    """传递列表"""
    for names1 in names:
        print(names1.title())
#调用函数
names=['caojing','caoming','caohua ']
list_1(names)
#8.5传递任意数量的实参
def number(*dict):
    print(dict)
#调用函数
number(1,2,3,4,5,6,7)
#使用位置实参，以及任意数量的实参
def messagess(information,*neirong):
    print(f'第{information}次，打印下面的元组了')
    print(neirong)
messagess(12,'x','y','u','iu')
#制作字典
def ci_dian(names,age,**message):
    message['names']=names
    message['age']=age
    return message
x=ci_dian('caojing',29,xing_ge='leguan',xing_bie='nan')
print(x)

#获得奇数
def ji_shu(list):
    """获得一个范围内的奇数"""
    jihe=[]
    for jishu in list :
        if jishu%2 :
            jihe.append(jishu)
        else:
            continue
    return jihe
list=range(100)
y=ji_shu(list)
print(y)
#获得奇数
def jishu(list):
    jishu_jihe=[]
    lengt=len(list)
    number=1
    while number==1:
        for jishu in list:
            if jishu%2:
                jishu_jihe.append(jishu)
        number+=1   
    return jishu_jihe

list=list(range(0,55))
message=jishu(list)
print(message)
#利用函数可以做一些事
#用列表可以做一些事
x=['caojing','nihao','gude','meidi']
y=[]
while x :
    y1=x.pop()
    y.append(y1)
    print(f'yanzheng{y1}')
for x1 in y:
    print(x1)

z=['caojing']
for x in z:
    while x in y:
        y.remove(x)
print(y)    

while True:
    x=int(input('请输入你想要验证的数字：'))
    if x%2:
        print('您输入的数是奇数')       
    else:
        print('您输入的数是偶数')

#第八章函数的复习：
#第一节内容：定义函数
#例子：
def names():
    """复习第八章的内容"""
    print('你好，我在做第八章的第一节的内容实例')
#调用函数
names()
def message():
    """利用函数打印一个句子"""
    print('我想在复习的是：\n\t第八章第1节的内容')
#调用函数
message()
#第二节内容：传递实参
#传递多个参数
def number(a,b,c,d,f,e,r):
    print('您的手机电话号码前面的7位数是？')
    x=[a,b,c,d,f,e,r]
    print(x)
#调用函数
number(1,2,3,4,5,6,7)
#默认值和关键字实参
#例子
def names(x,y='c'):
    """关键字实参"""
    print(f'我的名字是{x}，我喜欢的字母是{y}')
#调用函数
names('caojing')
names('caojing',y='a')
#以上两种调用函数的方式，如果在形参里有默认值，则相对性的形参变量可填可不填看需求
#第三节内容：return返回值

在什么情况下需要用到return？
当你需要这个值的时候，需要用到return
return与print之间的区别？
1、return并不是直接打印，是需要把值再利用，因此在调用函数时需要设置一个接受变量。然后看需求是否打印
并且return还有一个功能是只调用return后面的值,并且程序运行到return就回退出函数。
2、print表示是直接打印结果
因为在调取函数的时候关系到是直接把结果给到用户看还是再利用加工就关系到你使用那个。

def sums(a,b,c):
    
    """总数计算"""

    x=b+c
    d=x+a
    y=[x,d]
    return y
#调用函数
jieshou=sums(1,2,3)
print(jieshou)
#return返回值只能返回一个变量的值，如果需要返回两个就需要建立一个集合
#让实参变成可选+加whil用户输入
def names(names1,names2,names3=''):
    """打印名字"""
    if names:
        name=f'{names1.title()},{names2},{names3}'
    else:
        name=f'{names1.title()},{names2}'
    return name
while True:
    frist_name=input('您的姓是：')
    last_name=input('您的名是：')
    three_name=input('您的名的第二个字是：')
    #调用函数
    quanming=names(frist_name,last_name,three_name)
    print(quanming)

#传递字典
def tedian(name,age):
    tediand={'names':name,'ages':age}
    return tediand
#调用函数
zidian=tedian('caojing',29)
print(zidian)
#第四节传递列表
def lists(shu):
    y=[]
    for x in shu:
        y.append(x)
    return y
#调用函数：
shu=[1,2,3,4,5,6]
jihe=list(shu)
print(jihe)
#第五节：传递任意数量的实参
def tubles(*jihe):
    for x in jihe:
        print(x)
#调用函数
tubles('caojing','caohaiyun','caoming','caowenqinag')
def tuble(langes,*jihe2):
    print(f'现在是第{langes}次打印名字')
    for namess in jihe2:
        print(namess)
#调用函数：
tuble(2,'caojing','caohaiyun')

def dicits(**z):
    z['名字']='caojing'
    z['nihao']='nihao'
    return z
#调用函数
zidianss=dicits(f='zhu',d='s')
print(zidianss)   
#d第6节的内容：导入模块
print(f'\n1、导入模块：\nimport 模块\n调用函数：\n模块.函数名（参数）')
print(f"\n2、导入模块的指定函数：\nfrom 模块 import 函数名1，函数名2....\n调用函数：\n函数名1、2(实参)")
print(f"\n3、导入模块的所有函数：\nfrom 模块 import *)\n调用函数：\n函数名（实参）")
print(f"\n5、给模块的函数换名：\nfrom 模块 import 函数名 as 更换的名字\n 调用函数 ：\n更改的名字（实参）")
print(f"\n6、给模块换名：\nimport 模块名 as 新的模块名，\n调用函数：\n新的模块名.函数名（实参)")

#第八章，函数def funcion（形参）
#内容第一节定义函数
def function():
    """打印一句话"""
    print('你好，我开始学习函数了')
#调用函数
function()
#内容第二节传递参数
#1、内容是：传递实参
def function_frist(name,names):
    """打印名字"""
    print(f'{name.title()},nice to meet you ')
    print(f'{names.title()},i love you!')
#调用函数
function_frist('cao jing','cao hai yun')
#2、内容是：关键字实参以及默认值。
def function_last(names1,names2='caohaiyun'):
    #在定义函数时不能将有默认值的参数放在没有默认值参数的前面。
    """打印名字"""
    print(f'{names1},{names2}')
#调用函数
function_last( names1='caojing')
function_last('caowenqiang','caohaiyun')
function_last('x')
#第三节 返回值
#普通实参返回
def names(names1,names2,names3=''):
    x=f'{names1}{names2}'
    return x
#调用函数
jieshou=names('caojing','caohaiyun')
print(jieshou)
#传递字典
def dicts(names1,names2):
    dictss={'names':names1,'name':names2}
    return dictss
#调用函数
dicits=dicts('cojing','caohaiyun')
print(dicits)
#让参数变成可选
def names(names1,names2,names3=''):
    if names3:
        x=f'{names1.title()},\t{names2.title()},\t{names3.upper()}'
    else:
        x=f'{names1.lower()},\t{names2.upper()}'
    return x
#调用函数
names11=names('caojing','caohaiyun')
print(names11)
#与while语句的使用
def namesss(names1,names2,names3=''):
    if names3:
        x=f'{names1.title()},\t{names2.upper()}.\t{names3.lower()}'
    else:
        x=f'{names1.title()},\t{names2.upper()}'
    return x
while True:
    names1=input('请输入您姓：')
    names2=input('请输入您名：')
    names3=input('请输入您名：')
    s=namesss(names1,names2,names3)
    lianxu=input('调查是否还需要继续(yes\no)：')
    if lianxu=='yes':
        print(f'您的名字是{s.title()}')
        continue
    else:
        print(f'您好您的名字是：{s}谢谢您的参与！')
        break
#第四节传递列表
def lists(list1):
    for x in list1:
        print(x)
list12=[1,2,3,4,5]
lists(list12)
#第五节是传递任意数量实参
def yuanzu(*jihe):
    for x in jihe:
        print(x)
yuanzu('caojing','caowenqiang','caoming')
def didain(**x):
    x['names']='caoing'
    x['nihao']='caohaiyun'
    return x
y=didain(f='ni')
print(y)
#8.4利用函数传递列表
def list_1(names):
    """传递列表"""
    for names1 in names:
        print(names1.title())
#调用函数
names=['caojing','caoming','caohua ']
list_1(names)
#8.5传递任意数量的实参
def number(*dict):
    print(dict)
#调用函数
number(1,2,3,4,5,6,7)
#使用位置实参，以及任意数量的实参
def messagess(information,*neirong):
    print(f'第{information}次，打印下面的元组了')
    print(neirong)
messagess(12,'x','y','u','iu')
#制作字典
def ci_dian(names,age,**message):
    message['names']=names
    message['age']=age
    return message
x=ci_dian('caojing',29,xing_ge='leguan',xing_bie='nan')
print(x)

#获得奇数
def ji_shu(list):
    """获得一个范围内的奇数"""
    jihe=[]
    for jishu in list :
        if jishu%2 :
            jihe.append(jishu)
        else:
            continue
    return jihe
list=range(100)
y=ji_shu(list)
print(y)
#获得奇数
def jishu(list):
    jishu_jihe=[]
    lengt=len(list)
    number=1
    while number==1:
        for jishu in list:
            if jishu%2:
                jishu_jihe.append(jishu)
        number+=1   
    return jishu_jihe

list=list(range(0,55))
message=jishu(list)
print(message)
#利用函数可以做一些事
#用列表可以做一些事
x=['caojing','nihao','gude','meidi']
y=[]
while x :
    y1=x.pop()
    y.append(y1)
    print(f'yanzheng{y1}')
for x1 in y:
    print(x1)

z=['caojing']
for x in z:
    while x in y:
        y.remove(x)
print(y)    

while True:
    x=int(input('请输入你想要验证的数字：'))
    if x%2:
        print('您输入的数是奇数')       
    else:
        print('您输入的数是偶数')

#第八章函数的复习：
#第一节内容：定义函数
#例子：
def names():
    """复习第八章的内容"""
    print('你好，我在做第八章的第一节的内容实例')
#调用函数
names()
def message():
    """利用函数打印一个句子"""
    print('我想在复习的是：\n\t第八章第1节的内容')
#调用函数
message()
#第二节内容：传递实参
#传递多个参数
def number(a,b,c,d,f,e,r):
    print('您的手机电话号码前面的7位数是？')
    x=[a,b,c,d,f,e,r]
    print(x)
#调用函数
number(1,2,3,4,5,6,7)
#默认值和关键字实参
#例子
def names(x,y='c'):
    """关键字实参"""
    print(f'我的名字是{x}，我喜欢的字母是{y}')
#调用函数
names('caojing')
names('caojing',y='a')
#以上两种调用函数的方式，如果在形参里有默认值，则相对性的形参变量可填可不填看需求
#第三节内容：return返回值

在什么情况下需要用到return？
当你需要这个值的时候，需要用到return
return与print之间的区别？
1、return并不是直接打印，是需要把值再利用，因此在调用函数时需要设置一个接受变量。然后看需求是否打印
并且return还有一个功能是只调用return后面的值,并且程序运行到return就回退出函数。
2、print表示是直接打印结果
因为在调取函数的时候关系到是直接把结果给到用户看还是再利用加工就关系到你使用那个。

def sums(a,b,c):
    
    """总数计算"""

    x=b+c
    d=x+a
    y=[x,d]
    return y
#调用函数
jieshou=sums(1,2,3)
print(jieshou)
#return返回值只能返回一个变量的值，如果需要返回两个就需要建立一个集合
#让实参变成可选+加whil用户输入
def names(names1,names2,names3=''):
    """打印名字"""
    if names:
        name=f'{names1.title()},{names2},{names3}'
    else:
        name=f'{names1.title()},{names2}'
    return name
while True:
    frist_name=input('您的姓是：')
    last_name=input('您的名是：')
    three_name=input('您的名的第二个字是：')
    #调用函数
    quanming=names(frist_name,last_name,three_name)
    print(quanming)

#传递字典
def tedian(name,age):
    tediand={'names':name,'ages':age}
    return tediand
#调用函数
zidian=tedian('caojing',29)
print(zidian)
#第四节传递列表
def lists(shu):
    y=[]
    for x in shu:
        y.append(x)
    return y
#调用函数：
shu=[1,2,3,4,5,6]
jihe=list(shu)
print(jihe)
#第五节：传递任意数量的实参
def tubles(*jihe):
    for x in jihe:
        print(x)
#调用函数
tubles('caojing','caohaiyun','caoming','caowenqinag')
def tuble(langes,*jihe2):
    print(f'现在是第{langes}次打印名字')
    for namess in jihe2:
        print(namess)
#调用函数：
tuble(2,'caojing','caohaiyun')

def dicits(**z):
    z['名字']='caojing'
    z['nihao']='nihao'
    return z
#调用函数
zidianss=dicits(f='zhu',d='s')
print(zidianss)   
#d第6节的内容：导入模块
print(f'\n1、导入模块：\nimport 模块\n调用函数：\n模块.函数名（参数）')
print(f"\n2、导入模块的指定函数：\nfrom 模块 import 函数名1，函数名2....\n调用函数：\n函数名1、2(实参)")
print(f"\n3、导入模块的所有函数：\nfrom 模块 import *)\n调用函数：\n函数名（实参）")
print(f"\n5、给模块的函数换名：\nfrom 模块 import 函数名 as 更换的名字\n 调用函数 ：\n更改的名字（实参）")
print(f"\n6、给模块换名：\nimport 模块名 as 新的模块名，\n调用函数：\n新的模块名.函数名（实参)")

#第八章，函数def funcion（形参）
#内容第一节定义函数
def function():
    """打印一句话"""
    print('你好，我开始学习函数了')
#调用函数
function()
#内容第二节传递参数
#1、内容是：传递实参
def function_frist(name,names):
    """打印名字"""
    print(f'{name.title()},nice to meet you ')
    print(f'{names.title()},i love you!')
#调用函数
function_frist('cao jing','cao hai yun')
#2、内容是：关键字实参以及默认值。
def function_last(names1,names2='caohaiyun'):
    #在定义函数时不能将有默认值的参数放在没有默认值参数的前面。
    """打印名字"""
    print(f'{names1},{names2}')
#调用函数
function_last( names1='caojing')
function_last('caowenqiang','caohaiyun')
function_last('x')
#第三节 返回值
#普通实参返回
def names(names1,names2,names3=''):
    x=f'{names1}{names2}'
    return x
#调用函数
jieshou=names('caojing','caohaiyun')
print(jieshou)
#传递字典
def dicts(names1,names2):
    dictss={'names':names1,'name':names2}
    return dictss
#调用函数
dicits=dicts('cojing','caohaiyun')
print(dicits)
#让参数变成可选
def names(names1,names2,names3=''):
    if names3:
        x=f'{names1.title()},\t{names2.title()},\t{names3.upper()}'
    else:
        x=f'{names1.lower()},\t{names2.upper()}'
    return x
#调用函数
names11=names('caojing','caohaiyun')
print(names11)
#与while语句的使用
def namesss(names1,names2,names3=''):
    if names3:
        x=f'{names1.title()},\t{names2.upper()}.\t{names3.lower()}'
    else:
        x=f'{names1.title()},\t{names2.upper()}'
    return x
while True:
    names1=input('请输入您姓：')
    names2=input('请输入您名：')
    names3=input('请输入您名：')
    s=namesss(names1,names2,names3)
    lianxu=input('调查是否还需要继续(yes\no)：')
    if lianxu=='yes':
        print(f'您的名字是{s.title()}')
        continue
    else:
        print(f'您好您的名字是：{s}谢谢您的参与！')
        break
#第四节传递列表
def lists(list1):
    for x in list1:
        print(x)
list12=[1,2,3,4,5]
lists(list12)
#第五节是传递任意数量实参
def yuanzu(*jihe):
    for x in jihe:
        print(x)
yuanzu('caojing','caowenqiang','caoming')
def didain(**x):
    x['names']='caoing'
    x['nihao']='caohaiyun'
    return x
y=didain(f='ni')
print(y)
#第八章内容
#1、定义函数2、加参数、3、返回值4、列表、5、元组和字典、6、导入模块的函数
def names(names1):
    """对名字打印一个问候语"""
    print(f"Hello,{names1.title()}nice to meet you!")
#调用函数：
names('cao jing')
#例子一奇数列表
def name(names1):
    """求列表的所有奇数"""
    number_jishu=[]
    for digits in names1:
        if digits%2:
           number_jishu.append(digits)
        else:
            continue
    return number_jishu
#调用函数
numbers=list(range(0,33))
x=name(numbers)
print(x)
#获得名字例子
def names (names1,names2,names3=''):
    if names3:
        y=f'{names1.title()}{names2}{names3}'
    else:
        y=f'{names1.title()}{names2}'
    return y
#调用函数
name=names('cao','hai','yun')
namess=names('cao','jing')
print(name)
print(namess)
#元组和字典的表示方式
def message(name,*people):
    """美团收集点餐后的缺什么"""
    print(f'{name}同学，你剩余的配料如下：')
    for x in people:
        print(f'\n{x}')
#调用函数：
message('caojing','筷子','辣椒','佐料')
#字典的方式
def dicts(first,names,**dictss):
    """打印一个字典"""
    dictss['first_names']=first
    dictss['last_names']=names
    return dictss
#调用函数
y=dicts('cao','jing',z='cao',k='feng')
print(y)
#d导入模块调取函数
#import pizza
#pizza.函数名（参数）
#直接取模块特定函数
#from 模块 import 函数名
#函数名（参数）
#取多个函数
#from 模块 import 函数名1，函数名2，函数名3
#函数名1（参数）
#取所有函数
#from 模块 import *
#函数（参数）
#给函数换名字
#from 模块 import 函数名 as 重新取得名字
#重新取得名字（参数）
#给模块换名字
#import 模块名 as 更新的名字
#更新的名字.函数名（参数）
#函数说实在的确实简单

#第八章的内容，函数，这次要用俩个小时去回顾函数
#函数的内容如下：
information='8.1节：1.定义函数'
x=input(information)

def function_names():
    """定义函数"""
    print(f"函数定义，\ndef 函数名（形参）：\n\t函数体\n调用函数:\n函数名（实参）")
#调用函数
function_names()
def function_names1():
    """打印一个问候语"""
    print(f'hello,Mrcao,nice to meet you !')
#调用函数
function_names1()
message='8.2节传递实参:\n\t\t8.2.1,添加函数形参'
print(message)
def function_names2(names1,names2):
    """跟上面的人问好"""
    print(f'您好，{names1}!,希望能和您成为朋友！')
    print(f'您好，{names2}!,很高兴认识您！')
#调用函数：
function_names2('曹静','靓仔')
def function_names3(a,b):
    """数值的简单计算"""
    c=a+b
    print(c)
print('调用函数:')
function_names3(2,3)
print('8.2.2小节：关键值实参')
def names(names2,names3):
    """例子：形参与实参关联"""
    print(f'{names2}{names3}')
print('调用函数')
names(names2='cao',names3='jing')
print('8.2.3节：默认值')
def function_names4(names5,names4=1):#系统默认值不能放在形参的最前面，不然会引起错误
    """默认值例子"""
    print(f'{names4}{names5}')
print('调用函数')
function_names4(names4='cao',names5='jing')#当重新赋值，则以新的值去运行
print('8.3节return返回值，3.1')
def names7(frist_name,last_name,namess=''):
    """获得名字"""
    if namess:
        names_1=f'{frist_name.title()}{last_name}{namess}'
    else:
        names_1=f'{frist_name.title()}{last_name}'
    return names_1
print('调用函数')
namesss=names7('cao','jing')
print(namesss)
namesss=names7('cao','hai','yun')
print(namesss)
print('8.3节，返回字典8.3.2')
def dict(names,age):
    """返回字典"""
    x={'names':names,'age':age}
    return x
y=True
while y:
    names=input('您的名字是：')
    age=input('您的年龄是：')
    #调用函数
    message=dict(names,age)
    print(message)
    h=input('请问您还继续调查么？yes/no')
    if h=='no':
        break
    else:
        True
#8.4利用函数传递列表
def list_1(names):
    """传递列表"""
    for names1 in names:
        print(names1.title())
#调用函数
names=['caojing','caoming','caohua ']
list_1(names)
#8.5传递任意数量的实参
def number(*dict):
    print(dict)
#调用函数
number(1,2,3,4,5,6,7)
#使用位置实参，以及任意数量的实参
def messagess(information,*neirong):
    print(f'第{information}次，打印下面的元组了')
    print(neirong)
messagess(12,'x','y','u','iu')
#制作字典
def ci_dian(names,age,**message):
    message['names']=names
    message['age']=age
    return message
x=ci_dian('caojing',29,xing_ge='leguan',xing_bie='nan')
print(x)

#获得奇数
def ji_shu(list):
    """获得一个范围内的奇数"""
    jihe=[]
    for jishu in list :
        if jishu%2 :
            jihe.append(jishu)
        else:
            continue
    return jihe
list=range(100)
y=ji_shu(list)
print(y)
#获得奇数
def jishu(list):
    jishu_jihe=[]
    lengt=len(list)
    number=1
    while number==1:
        for jishu in list:
            if jishu%2:
                jishu_jihe.append(jishu)
        number+=1   
    return jishu_jihe

list=list(range(0,55))
message=jishu(list)
print(message)
#利用函数可以做一些事
#用列表可以做一些事
x=['caojing','nihao','gude','meidi']
y=[]
while x :
    y1=x.pop()
    y.append(y1)
    print(f'yanzheng{y1}')
for x1 in y:
    print(x1)

z=['caojing']
for x in z:
    while x in y:
        y.remove(x)
print(y)    

while True:
    x=int(input('请输入你想要验证的数字：'))
    if x%2:
        print('您输入的数是奇数')       
    else:
        print('您输入的数是偶数')

#第八章函数的复习：
#第一节内容：定义函数
#例子：
def names():
    """复习第八章的内容"""
    print('你好，我在做第八章的第一节的内容实例')
#调用函数
names()
def message():
    """利用函数打印一个句子"""
    print('我想在复习的是：\n\t第八章第1节的内容')
#调用函数
message()
#第二节内容：传递实参
#传递多个参数
def number(a,b,c,d,f,e,r):
    print('您的手机电话号码前面的7位数是？')
    x=[a,b,c,d,f,e,r]
    print(x)
#调用函数
number(1,2,3,4,5,6,7)
#默认值和关键字实参
#例子
def names(x,y='c'):
    """关键字实参"""
    print(f'我的名字是{x}，我喜欢的字母是{y}')
#调用函数
names('caojing')
names('caojing',y='a')
#以上两种调用函数的方式，如果在形参里有默认值，则相对性的形参变量可填可不填看需求
#第三节内容：return返回值

在什么情况下需要用到return？
当你需要这个值的时候，需要用到return
return与print之间的区别？
1、return并不是直接打印，是需要把值再利用，因此在调用函数时需要设置一个接受变量。然后看需求是否打印
并且return还有一个功能是只调用return后面的值,并且程序运行到return就回退出函数。
2、print表示是直接打印结果
因为在调取函数的时候关系到是直接把结果给到用户看还是再利用加工就关系到你使用那个。

def sums(a,b,c):
    
    """总数计算"""

    x=b+c
    d=x+a
    y=[x,d]
    return y
#调用函数
jieshou=sums(1,2,3)
print(jieshou)
#return返回值只能返回一个变量的值，如果需要返回两个就需要建立一个集合
#让实参变成可选+加whil用户输入
def names(names1,names2,names3=''):
    """打印名字"""
    if names:
        name=f'{names1.title()},{names2},{names3}'
    else:
        name=f'{names1.title()},{names2}'
    return name
while True:
    frist_name=input('您的姓是：')
    last_name=input('您的名是：')
    three_name=input('您的名的第二个字是：')
    #调用函数
    quanming=names(frist_name,last_name,three_name)
    print(quanming)

#传递字典
def tedian(name,age):
    tediand={'names':name,'ages':age}
    return tediand
#调用函数
zidian=tedian('caojing',29)
print(zidian)
#第四节传递列表
def lists(shu):
    y=[]
    for x in shu:
        y.append(x)
    return y
#调用函数：
shu=[1,2,3,4,5,6]
jihe=list(shu)
print(jihe)
#第五节：传递任意数量的实参
def tubles(*jihe):
    for x in jihe:
        print(x)
#调用函数
tubles('caojing','caohaiyun','caoming','caowenqinag')
def tuble(langes,*jihe2):
    print(f'现在是第{langes}次打印名字')
    for namess in jihe2:
        print(namess)
#调用函数：
tuble(2,'caojing','caohaiyun')

def dicits(**z):
    z['名字']='caojing'
    z['nihao']='nihao'
    return z
#调用函数
zidianss=dicits(f='zhu',d='s')
print(zidianss)   
#d第6节的内容：导入模块
print(f'\n1、导入模块：\nimport 模块\n调用函数：\n模块.函数名（参数）')
print(f"\n2、导入模块的指定函数：\nfrom 模块 import 函数名1，函数名2....\n调用函数：\n函数名1、2(实参)")
print(f"\n3、导入模块的所有函数：\nfrom 模块 import *)\n调用函数：\n函数名（实参）")
print(f"\n5、给模块的函数换名：\nfrom 模块 import 函数名 as 更换的名字\n 调用函数 ：\n更改的名字（实参）")
print(f"\n6、给模块换名：\nimport 模块名 as 新的模块名，\n调用函数：\n新的模块名.函数名（实参)")

#第六节内容
import 模块
模块.函数名（实参）
from 模块 import 函数名,函数名1，函数名2.。。
函数名（实参）
for 模块 import *

#结束第8章内容
#第7章内容复习：用户输入与while循环
#在列表中移动元素
list_1=[1,2,3,4.5,6]
list_2=[]
while list_1:
    y=list_1.pop()
    list_2.append(y)
print(list_2)
#用while语句在列表中删除指定元素
name=['caojing','caohaiyun','caowenqinag','caojing','caoxing']
while 'caojing'in name:
    name.remove('caojing')
print(name)

#第九章类
class Student:
    name='caojing'#类属性
    age=29
person=Student()#创建对象
print(person.name)#因为是在类里面，因此实用类对象就是一个空间，空间里面就有类的属性
person.name='caoming'#修改对象的属性
print(person.name)
Student.name='caohaiyun'#修改类属性
#类中方法
#种类：普通方法，类方法，静态方法，魔术方法
#普通方法：
#def 方法名（self[参数，参数]）：
            #方法体
class Phone:
    #类属性
    brand='xiaomi'
    price=4999
    type='mate 20'
    #类操作方法比如打电话
    def call(self):
        print('正在打电话.....')
        for x in self.phonelist:
            print(x.items())
        print(f'留言：{self.note}')

#创建一个phone1的具体对象（实例）        
phone1=Phone()
phone1.phonelist=[{'123':'caojing'},{'124':'caoming'}]
phone1.note='我是谁？'
phone1.call()#调用类方法 

#定义一个猫类
class Cat:
    type='猫'
    #创建类属性，特征。
    def _init_(self,nickname,age,color):
        self.nickname=nickname
        self.age=age
        self.color=color
    #串讲类方法
    def eat(self,)
    
class phone:
    x=3
cj_phone=phone()
print(cj_phone)
print(cj_phone.x)
print(cj_phone)

a=[1,2,3]
b=a*3
print(b)

a=[[100,200],100,300]
b=a*3
print(b)
a=[[100,200],100,300]
b=a*3
a[0][0]=1
a[1]=1
print(b)

import copy
c=[1,2,3,[23,"a"],23]
b=copy.deepcopy(c)
print(c[3] is b[3])

#定义类
class Cat:

    #类的属性
    
    def __init__(self,nickname,age,color):
        self.nickname=nickname
        self.age=age
        self.color=color
        
    #类方法
        
    def eat(self,food):
        print(f'给{self.nickname}吃了{food}。')
    def gongzuo(self,color,whicg):
        print(f'{self.nickname}抓了一只{whicg}kg的{color}的大老鼠')
    def sleep(self,time):
        if time>8:
            print('乖乖，赶紧去抓老鼠！')
        else:
            print('乖乖继续睡觉吧！')
    def zhanshi(self):
        print('这个猫的特点是：')
        print(f'\n\t{self.nickname},{self.age},{self.color}')
#用类创建对象
cat1=Cat('杜杜',10,'白色')
cat1.gongzuo('灰色','2')
cat1.eat('小金鱼')
cat1.sleep(9)
cat1.zhanshi()


#第九章类
#第一节：创建和使用类
#创建一个餐厅的类
class Restaurant:
    def __init__(self,r_name,r_type):
        self.name=r_name
        self.type=r_type
    def describe_restaurant(self):
        print(f'{self.name}的建筑比较古老')
    def open_restaurant(self,time):
        print(f'现在的时间是北京时间{time}点，现在的时间餐厅的营业状态是：')     
        if 9<time<22:
            print(f'{self.name}餐厅正在营业!')
        else:
            print(f'{self.name}餐厅已停止营业!')
#用类创建对象1
china_restaurant=Restaurant('猪脚饭','中餐餐厅')
#打印两个属性
print(f'这是一家{china_restaurant.type}，名字是{china_restaurant.name}')
#调用类的方法
china_restaurant.describe_restaurant()
china_restaurant.open_restaurant(10)
print('谢谢您的光临！！！')

#用类创建对象2
us_restaurant=Restaurant('尊宝披萨','西餐披萨')
print(f'\n这是一家{us_restaurant.type},餐厅的名字是{us_restaurant.name}')
us_restaurant.describe_restaurant()
us_restaurant.open_restaurant(23)
#用类串讲对象3
china2_restaurant=Restaurant('兰州拉面','面食类')
print(f'\n这是一家{china2_restaurant.type}的餐厅，名字是{china2_restaurant.name}')
china2_restaurant.describe_restaurant()
china2_restaurant.open_restaurant(18)
print(f'/n/n/n/n')
class User:
    def __init__(self,frist_name,last_name):
        self.name1=frist_name
        self.name2=last_name
    def describe_user(self,age):
        print(f'我今年{age}岁了!!')
        print('可以开始调查：')
        if age<=2:
            print(f'{self.name1}{self.name2}您还是个婴儿!')
        elif 2<age<=18:
            print(f'{self.name1}{self.name2}您是一个儿童或者是一个青少年!')
        elif 18<age<65:
            print(f'{self.name1}{self.name2}您是一个成年人了！！')
        else:
            print(f'{self.name1}{self.name2}您是一个老年人了！！')
    def greet_user(self):
        print(f'{self.name1}{self.name2} 感谢您参加我们的信息调查！')
#调用类创建对象，实例
user1=User('cao','jing')
print(f'大家好，我的姓名是{user1.name1}{user1.name2},很高兴认识大家！！！')
user1.describe_user(68)
user1.greet_user()
#第二节，使用类和实例对象
class Car:
    def __init__(self,make,year,model):
        self.leibie=make
        self.nianxian=year
        self.xinghao=model
        self.licheng=20
    def descritive_car(self):
        name=f'{self.leibie}\t{self.xinghao}\t{self.nianxian}'
        return name             
    def lichengs(self):
        print(f'您的车的真实里程数：{self.licheng}')
    def lichengshu(self,number):
        if number>=self.licheng:
            self.licheng=number
        else:
            print('您这个撒比，不能调表')
car1=Car('aodi','2020年','a4')
print(car1.descritive_car())
car1.lichengshu(18)
car1.lichengs()
#练习
class Restaurant:
    def __init__(self,r_name,r_type):
        self.name=r_name
        self.type=r_type
        self.number_served=0
    def describe_restaurant(self):
        print(f'{self.name}的建筑比较古老')
    def open_restaurant(self,time):
        print(f'现在的时间是北京时间{time}点，现在的时间餐厅的营业状态是：')     
        if 9<time<22:
            print(f'{self.name}餐厅正在营业!')
        else:
            print(f'{self.name}餐厅已停止营业!')
    def set1(self,number2):
        self.number_served=number2
        if self.number_served>30:
            print('目前已经没有位置')
        else:
            print('里面还有空位')
    def dicits(self,mile):
        self.number_served+=mile
restaurant1=Restaurant('腊肠盖饭店','中餐馆')
print(f'截至目前有{restaurant1.number_served}人在这里吃饭')
restaurant1.number_served=20
print(f'截至目前有{restaurant1.number_served}人在这里吃饭')
restaurant1.set1(31)        
print(f'截至目前有{restaurant1.number_served}人在这里吃饭')

'''

class User:
    def __init__(self,name1,name2,age_2,xingbie):
        self.name_1=name1
        self.name_2=name2
        self.age_1=age_2
        self.xb=xingbie
    def describe_user(self):
        print('打印用户信息:')
        print( f'姓名是：{self.name_1}{self.name_2.}\n年龄是：{self.age_1}.\n型别是:{self.xb}')
    def greet_user(self):
        print(f'{self.name_1}{self.name_2}你好，祝您生活美好，工作顺利！')

user1=User('曹','靖',29,'男')
user1.describe_user()


