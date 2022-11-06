import colorama 
from colorama  import Fore 
class Database: 
    def new_account(): 
        n=  str(input('enter your Name : '))
        m= int(input('enter your age : '))
        if  m in range(10, 99) : 
            print(' hi , ' ,  n  )
            num= [int(input('enter  your phone number : '))]            
            nx= int(input('enter you otp : '))
            if len(nx)==  6 : 
                    print('account varified : ')
                    
                    an=str(input('enter your password : '))
                    na= str(input('conframe your paswrod :'))
                    if an == na : 
                        print('  account created : ')
                    else: 
                        print( ' password does not matched : ')
            else : 
                    print('  code does not matched , we will like to  resend the otp : ')
                    nc = str(input('would we  resend the otp , y  for yes n for no: '))
                    if nc== 'yes'  or nc  == 'y': 
                        ni= int(input('enter your otp : '))
                        if len(ni)== 6 : 
                            print(' account varified : ')
                            
                        anx=str(input('enter your password : '))
                        nxa= str(input('conframe your paswrod :'))
                        if anx == nxa : 
                            print('  account created : ')
                        else: 
                            print( ' password does not matched : ')
            print('wrong number  , plz try another time : ')
                   