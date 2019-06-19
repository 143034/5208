'''
模块:
    引入模块:
        import
    自定义模块:
        from module import name1,name2....
        from module import *#全部导入
        from time import sleep
    __name__属性:
        模块是一个可执行的py文件，一个模块被领一个程序引入,我们不想模块的某些内容执行使用此方法.
        每一个py文件都有这个属性__name__,当其值等于'__main__'时,表明模块自身在执行.否则被引入了其他文件.     
        def main():
            pass
        if __name__ == '__main__'引入时这句话不会被执行
            main()
        
'''
'''
import sys
print(sys.argv)#路径
for i in sys.argv:
    print(i)
#name = sys.argv[1]
#age = sys.argv[2]
#查找所需模块路径的列表
print(sys.path)
'''
'''
包:
    为了解决模块命名冲突,引入按目录来组织模块的方法,成为包.
    引入包以后，只要顶层的包不与其他人冲突,模块都不会与别人的包冲突.
    要在各个包文件里面创建__init__.py的文件才被认为是一个包.文件中什么也不用写
    主要是为了避免一些滥竽充数的名字
    import a.包名
    import b.包名
    pip 下载包
    from PIL import Image
    im = Image.open('111.jpg')
    print(im.format, im.size, im.mode)#查看图片的信息
    im.thumbnail((150,100))#设置图片大小    元组
    im.save('222.jpg', 'JPEG')保存
'''
from PIL import Image
im = Image.open('111.jpg')
print(im.format, im.size, im.mode)
im.thumbnail((150,100))#设置图片大小    元组
im.save('222.jpg', 'JPEG')
