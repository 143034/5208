def func():
    for n in range(10)[1:]:
        for k in range(10)[1:]:
            if n<=k:
                num = n*k
                print('%d*%d=%d' %(n,k,num),end = '\t')
            if k==9:
                print('',end = '\n')
                
func()        
        

