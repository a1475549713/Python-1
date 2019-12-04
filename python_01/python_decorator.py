##python装饰器及常见的坑
# 本质上，装饰器可以理解为闭包函数


# 带参数的装饰器
def warpp(f):
    def inner(fun):
        def has(*args, **kwargs):
            # print(f)
            ret = fun(f, *args, **kwargs)
            return ret

        return has

    return inner


## 类装饰器
## 函数装饰器可以装饰函数与类的方法，类装饰器只能装饰函数

class log():
    def __init__(self, fun):
        self.fun = fun

    def __call__(self, *args, **kwargs):
        print(1)
        print('当前执行函数{}'.format(self.fun.__name__))
        self.fun(*args, **kwargs)


def warpper(a):
    # print(2)

    def meth(*args, **kwargs):
        print(3)
        return a(*args, **kwargs)

    return meth


class ret():
    def __init__(self, name):
        self.name = name

    @warpper
    @log
    def sayhi(self):
        print(4)
        print('hallo,i am{}'.format(self.name))


##此时会报错 TypeError: sayhi() missing 1 required positional argument: 'self'
## log 修饰后 调用sayhi实质上是调用log（fun(**) ,而fun.self属于ret
# 解决方法 一 写一个装饰器，call,所有self指向 warpper
## 此时运行 ret 等价于 warppr(log(ret.sayhi(**)))
# p = ret('zz')
# p.sayhi()
# 方法二
# 可以直接p.sayhi 调用，无法传参数 修改装饰器中 call方法为 get
##此时，syhai作为log类的属性被调用
class logs():
    def __init__(self, fun):
        self.fun = fun

    def __get__(self, a, b):
        print('当前执行函数{}'.format(self.fun.__name__))
        print('1', b)
        print('2', a)
        print('3', self.fun(a))
        return self.fun(a)


class hi():
    def __init__(self, naem):
        self.name = naem

    @logs
    def syahi(self):
        print('4')
        print('hallo,i am{}'.format(self.name))
        return 'hahh'




# p =hi('lulu')
# p.syahi


### 带参数的类装饰器
def warppers(a):
    print(2)
    def meth(*args, **kwargs):
        print(3)
        return a(*args, **kwargs)
    return meth
class logss():
    def __init__(self, s):
        self._s = s
        # print(self.s)
    def __call__(self, funs):
        print(self._s)
        self.fun = funs
        #  def call_fun(self):
        def hs(*args, **kwargs):
            print(1)
            print('当前执行函数{}'.format(self.fun.__name__))
            # print(self.s)
            self.fun(*args, **kwargs)
        return hs
    # return call_fun
class rets():
    def __init__(self, name):
        self.name = name
    @warppers
    @logss(s='hahah')
    def sayhi(self):
        print(4)
        print('hallo,i am{}'.format(self.name))


#p = rets('ho')
#p.sayhi()

## awrpp(f,ts(kk))
# ts('li', w='heh')
