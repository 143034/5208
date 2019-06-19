from person import Person
from gun import Gun
from bullet import Bullet
bullet = Bullet(5)
gun = Gun(bullet)
per = Person(gun)
per.fire()
per.fire()
per.fire()
per.fire()
per.fire()
per.loadbullet(3)
per.fire()

