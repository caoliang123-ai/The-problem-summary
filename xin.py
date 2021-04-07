'''
#第九章内容的第1、2节，创建类和实例对象，使用类和对象
class User:
    def __init__(self,name1,name2,age_2,xingbie):
        self.name_1=name1
        self.name_2=name2
        self.age_1=age_2
        self.xb=xingbie
        self.toufa=10000
    def describe_user(self):
        print('打印用户信息:')
        print( f'姓名是：{self.name_1}{self.name_2}\n年龄是：{self.age_1}.\n型别是:{self.xb}')
    def greet_user(self):
        print(f'{self.name_1}{self.name_2}你好，祝您生活美好，工作顺利！')
    def helft_toufa(self,number):
        self.toufa=number
        if number>=10000:
            print('您毛发旺盛')
        elif 10000>number>=5000:
            print('您注意平时多爱惜头发')
        elif number<5000:
            print('您要秃顶了！！')
        print(f'您的头发是{self.toufa}根')
    def add1(self,x):
        self.toufa+=x
        print('治辽中...')
        print(f'第一期治疗您头发可增加至{self.toufa}，足足增加了{x}根')
name1=input('您的姓是：')
name2=input('您的名是：')
age_2=input('您的年龄：')
xingbie=input('您的性别:')
user1=User(name1,name2,age_2,xingbie)
user1.describe_user()
user1.greet_user()
user1.helft_toufa(5000)
print('定期治疗：')
user1.add1(10000)
user1.helft_toufa(10000)
#第三节，继承
class Car:
    #初始化类的属性（变化的属性）
    def __init__(self,make,year,model):
        self.make=make
        self.year=year
        self.model=model
        self.odometer_reading=0
    #类方法,类的动作
    def usage1(self,name):
        print(f'{name.title()},我们可以开车去拉萨')
    def jiayou(self,number):
        if number<50:
            print('您剩余油量已不足50升，请及时加油！！')
        elif number>200:
            print('油量充足，可继续前行')
    def odomenter(self,dicits):
        if dicits>=self.odometer_reading:
            self.odometer_reading=dicits
            print(self.odometer_reading)
        else :
            print('对不起您不能调低里程数，做人要讲诚信！！')
    def show(self):
        print(f'{self.make},{self.year},{self.model}')
#用类创建对象实例
user='如果您近期有旅游的打算，'
user+='您想自驾那款车去旅游？：'
user1=input(user)
car1=Car(user1,'2019','a4')
print('如果您想去拉萨旅游，又有奥迪车：')
car1.usage1('曹靖')
print('检查一下您的油量如何？')
car1.jiayou(54)
print('如果别人想调里程数，我们看看能不能调？')
car1.odomenter(-20)
car1.show()
#用类创建一个子类：比如电动车
#子类的编写方法class 子类名（父类）：
#1、子类必须在父类的后面
#2、如果子类里的方法跟父类不相同，那么它可以编写同样的方法名，当调用时，则以子类的为准》
#3、如果需要使用父类的方法和属性则需要
#：def __init__(self,参数)：并且需要在方法下面加一个：加一个方法:super().__init__(形参)这样
#如果在加一个没有继承关系的类怎么处理？
class Diandongche:
    def __init__(self,name,numbers):
        self.name=name
        self.numbers=numbers
    def jisuan(self):
        print(f'{self.name}开车跑{self.numbers},就会跑不动！！')

class Electric(Car):
    def __init__(self,make,year,model):
        super().__init__(make,year,model)#super方法是用来调父类的方法
        #用来是调用父类的所有方法，同时也包含类的属性
        self.lichengshu =34
        self.x=Diandongche('美国车','300公里')
    def qubie(self,chongdian):
        print(f'电动车是需要充电的，每充电{chongdian}小时能跑200公里')
#用子类创建对象
dd=Electric('比亚迪','2020年','biyadi3')
dd.show()
dd.qubie(3)   
dd.x.jisuan()

#创建餐饮类
class Can_yin:
    def __init__(self,type1,name,can_shu):
        self.type1=type1
        self.name=name
        self.can_shu=can_shu
    def show(self):
        print(f'我们是餐饮行业，我们的名字是{self.name}，属于{self.type1}类别，每人每天可以在我们这里消费{self.can_shu}次')
    def bi_jiao(self):
        if self.can_shu != 3:
            print('该餐馆属于其他小吃或饮料店')
        else:
            print('该餐馆属于是正餐类')
#再创建一个没有继承关系的类，并使用他(关于冰激零的品牌)
class Ice_zhong_lei:
    def __init__(self,pin_pai,jia_ge):
        self.pin_pai=pin_pai
        self.jia_ge=jia_ge
    def message(self):
        print(f'{self.pin_pai}品牌的冰激淋是很不错的，价格是{self.jia_ge}')
#创建子类（继承）
class IceCreamStand(Can_yin):
    """初始化继承父类的属性和方法或者添加属性和方法"""
    def __init__(self,type1,name,can_shu):
        super().__init__(type1,name,can_shu)
        self.ice_zhong_lei=Ice_zhong_lei('五羊冰激淋','5元')        
    def show(self):
        print(f'我们是餐饮行业，我们的名字是{self.name}，属于{self.type1}类别，每人每天可以在我们这里消费{self.can_shu}次及任意数量的消费')
    def wen_du(self,wei_dao):
        print(f'我们的食品温度是冷的，味道是{wei_dao}的，欢迎大家来品尝！')
#创建一个实例对象
shi_wu=IceCreamStand('甜点','冰激淋小店','n')
shi_wu.show()
shi_wu.bi_jiao()
shi_wu.ice_zhong_lei.message()
shi_wu.wen_du('甜')
#再创建一个实例对象
bingde=IceCreamStand('甜筒','肯德基甜筒','x')
bingde.show()
bingde.ice_zhong_lei.pin_pai='肯德基甜筒'
bingde.ice_zhong_lei.message()
bingde.wen_du('甜冰')
#第四节导入类是和导入函数的方式一样
#第五节
#在random模块中，利用函数randint()返回一个随机的数
from random import randint
print(randint(1,20))
#在random模块中，利用函数choice()返回列表中的任意一个元素
from random import choice
x=[1,2,3,4,5]
y=choice(x)
print(y)
'''
#第十章文件和异常 第一节：从文件中读取数据
with open('测试文档1.txt')as file_object:
    contents=file_object.read()
print(contents.rstrip())

#第二节，文件路径#读取与py文件同一界面的文件中的文件的小文件（相对路径）
with open('测试文件夹1\新建文件夹\测试文档2.txt','r',encoding='UTF-8')as file_object:
    print(file_object.read())
#绝对路径
path_1=(r'C:\Users\Administrator\Documents\WeChat Files\cao19035553551232654\FileStorage\File\2021-04\测试文件夹1\新建文件夹\测试文档2.txt')
with open(path_1,'r',encoding='UTF-8') as file_object:
    print(file_object.read())
#逐行读取
with open('测试文档1.txt')as file_object:
    for hang in file_object:
        print(hang.rstrip())



        

