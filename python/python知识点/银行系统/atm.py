import random
from card import Card
from user import User
class ATM(object):
    def __init__(self):
        self.allUsers = {}
    def createUser(self):
        #向用户字典中添加键值对(卡号:用户)
        name = input('请输入姓名:')
        idCard = input('输入身份证:')
        phone = input('请输入电话号码:')
        prestoreMoney = int(input('请输入金额:'))
        if prestoreMoney < 0:
            print('开户失败！')
            return -1
        onePasswd = input('请设置密码:')
        if not self.checkPasswd(onePasswd):
            print('密码输入错误,开户失败!')
            return 1
        #卡号
        cardStr = self.randomCardId()
        card = Card(cardStr, onePasswd, prestoreMoney)
        user = User(name,idCard,phone,card)
        self.allUsers[cardStr] = user
        print('开户成功!%s'% (cardStr))
        print(self.allUsers[cardStr])
    def searchUserInfo(self):
        cardNum = input('请输入您的卡号:')
        user = self.allUsers.get(cardNum)
        #判断是否存在
        if not user:
            print('该卡号不存在')
            return -1
        #判断锁定
        if user.card.cardLock:
           print('该卡已经被锁定,请解锁后再进行其他操作!')
           return -1
        #验证密码
        if not self.checkPasswd(user.card.cardPasswd):
            print('密码输入错误,查询失败，该卡已经被锁定,请解锁后再进行其他操作!')
            user.card.cardLock = True
            return -1
        print('账号:%s  余额:%d' %(user.card.cardId, user.card.cardMoney))
    def getMoney(self):
        pass
    def saveMoney(self):
        pass
    def transferMoney(money):
        pass
    def changePasswd(self):
        pass
    def lockUser(self):
        cardNum = input('请输入您的卡号:')
        user = self.allUsers.get(cardNum)
        #判断是否存在
        if not user:
            print('该卡号不存在!锁定失败!')
            return -1
        if user.card.cardLock:
            print('改卡已经被锁定,请解锁后使用其他功能')
            return -1
        if not self.checkPasswd(user.card.cardPasswd):
            print('密码输入错误,锁定失败!')
            return -1
        tempIdcard = input('请输入身份证号码:')
        if tempIdcard != user.idCard:
            print('密码输入错误,锁定失败!')
            return -1
        #锁定
        user.card.cardLock = True
        print('锁定成功!')
    def unlockUser(self):
        cardNum = input('请输入您的卡号:')
        user = self.allUsers.get(cardNum)
        #判断是否存在
        if not user:
            print('该卡号不存在!解锁失败!')
            return -1
        if not user.card.cardLock:
            print('该卡没有锁定,无需解锁!')
            return -1
        if not self.checkPasswd(user.card.cardPasswd):
            print('密码输入错误,解锁失败!')
            return -1
        tempIdcard = input('请输入身份证号码:')
        if tempIdcard != user.idCard:
            print('密码输入错误,解锁失败!')
            return -1
        user.card.cardLock = False
        print('解锁成功!')
    def newCard(self):
        pass
    def killUser(self):
        pass
    def checkPasswd(self, realPasswd):
        for i in range(3):
            tempPasswd = input('请重新输入密码:')
            if tempPasswd == realPasswd:
                return True
        return False
    #生成卡号
    def randomCardId(self):
        while True:
            str = ""
            for i in range(6):
                ch = chr(random.randrange(ord('0'), ord('9') + 1))
                str += ch
            #判断重复
            if not self.allUsers.get(str):
                return str
