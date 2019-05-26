import pickle
import os
from view import Admin
from atm import ATM
import time
def main():
    #存储用户信息
    #allUsers = {}
    #管理员对象
    view = Admin()
    view.printAdminView()
    if view.adminOption() == -1:
        return -1
    
    filepath = os.path.join(os.getcwd(), 'allusers.txt')
    f = open(filepath, 'rb')
    allUsers = pickle.load(f)
    print(allUsers)
    atm = ATM(allUsers)



    
    while True:
        view.sysFunctionView()
        option = input('请输入操作:')
        if option == '1':
            print('开户')
            atm.createUser()
        elif option == '2':
            print('查询')
            atm.searchUserInfo()
        elif option == '3':
            print('取款')
            atm.getMoney()
        elif option == '4':
            print('存款')
            atm.saveMoney()
        elif option == '5':
            print('转账')
            atm.transferMoney()
        elif option == '6':
            print('改密')
            atm.changePasswd()
        elif option == '7':
            print('锁定')
            atm.lockUser()
        elif option == '8':
            print('解锁')
            atm.unlockUser()
        elif option == '9':
            print('补卡')
            atm.newCard()
        elif option == '0':
            print('销户')
            atm.killUser()
        elif option == 'a':
            print('退出')
            if not view.adminOption() == -1:
                   
                #将用户保存到文件中
                #filepath = os.path.join(os.getcwd(), '账户信息.txt')
                f = open(filepath, 'wb')
                pickle.dump(atm.allUsers, f)
                f.close()
                #print(filepath)
                return -1
        time.sleep(2)
            
            
    




if __name__ == '__main__':
    main()
