class Person(object):
    def __init__(self, gun):
        self.gun = gun
    def fire(self):
        self.gun.shoot()
    def loadbullet(self, count):
        self.gun.bullet.bulletCount = count
