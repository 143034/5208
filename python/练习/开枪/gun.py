class Gun(object):
    def __init__(self, bullet):
        self.bullet = bullet
    def shoot(self):
        if self.bullet.bulletCount == 0:
            print('没有子弹了')
        else:
            self.bullet.bulletCount -= 1
            if self.bullet.bulletCount == 0:
                print('没有子弹了')
            else:
                print('剩余:%d'%(self.bullet.bulletCount))
