accounts = {}
global name
name = None
balance = 0

def create_account():
    global name
    while True:
      name = input("please enter your account name:")
      if name in accounts:
         answer_1 = input("This account is already exists, please enter login or re-enter:")
         if answer_1 == "login":
             login()
             break
         elif answer_1 == "re-enter":
             continue
         else:
              print("Unable to understand the command, please re-enter")
              
     
      else:
          
          password = (input("please enter your passourd betwttn 8 to 16 digit: "))
          
          while True:
            if 8 <= len(password) <= 16:
                accounts[name] = {'password':password}
                
                print("hi,your account create successful")
                return  ##进入主程序
            else:
                print("this password is not allowed,please try again")
      break

def login():
    count = 0
    global name
    name = input("please enter your account name:")
    if name in accounts:
       while True:
         password = (input("please enter your password: "))
       
         if accounts[name]['password'] == password:
           print("password correct,welcome back")
           return  #进入主程序，删掉这个
           break  ##临时加上，待定
         else:
           print("your password is incorrect,please try again")
           count += 1
           if count == 3 :
               print("The number of entries reached the upper limit, and the program was locked")
               break
           else:
                 continue
    else:
        while True:
          answer_2 = input("we can't find this account,please enter try again or create account: ") #加上让用户选择重新输入或创建账号
          if answer_2 == "try again":
             login()
             break
          elif answer_2 == "create account":
               create_account()
               break
          else:
              print("Unable to understand the command, please re-enter")
            

def main():
    global name
    print(f"your account number is {name}") #use global name to define name
    
    global balance
    def check_balance():
        accounts[name] = {'balance':balance}
        print(f"your balance is {accounts[name]['balance']} pounds")
   
    
   
    def deposit():
        accounts[name] = {'balance':balance}
        amount = float(input("please enter deposit amount:"))
        if amount > 0:
            accounts[name]['balance'] += amount
            print(f" you successfully deposited {amount}pounds, now your balance is {accounts[name][balance]}pounds")
        else:
            while True:  
              answer_3 = input(" amount must > 0,please enter 'reenter' or 'return' :")
              if answer_3 == "reenter":
                    deposit()
                    break
              elif answer_3 == "return":
                  main()
                  break
              else:
                  print("Unable to understand the command, please re-enter")


    def withdraw_money():
        amount = float(input("Please enter the withdrawal amount:"))  #加上不是数字的情况
        if 0 < amount <= accounts[name]['balance']:
           print(f"withdraw {amount} pounds sucessful")
           accounts[name]['balance'] -= amount
        elif amount <= 0:
            print("Please enter a number greater than 0")
            withdraw_money()
        elif 1500 < amount <= accounts[name]['balance'] + 1500:  #提示透支金额
            while True:
              answer_4 = input(f"your balance is not enough,but you have 1500 pounds overdraft amount,this trading will overdraft {amount - 1500}pounds,weather to continue,please enter 'yes' or 'no' :")
              if answer_4 == "yes":
                 print(f"withdraw {amount} pounds sucessful")
                 accounts[name]['balance'] -= amount
                 return
              elif answer_4 == "no":
                  withdraw_money()
                  return
              else:
                  print("Unable to understand the command, please re-enter")
                  break
        else:
            amount > accounts[name]['balance'] + 1500
            print("your balance is not enough,please try again")
            withdraw_money()
    
    
    def transfer_money():
        account_name = input("please enter account name")
        
        if account_name not in accounts:
           print("This account not exist, please try again")
           transfer_money()
        else:
           amount = float(" please enter the withdraw amount:")              
           if 0 < amount <= accounts[name][balance]:
              print(f"transfer money to {account_name} sucessful")
              accounts[account_name]['balance'] += amount
           elif amount <= 0:
               print("Please enter a number greater than 0")
               transfer_money()
           
           elif 1500 < amount <= accounts[name]['balance'] + 1500:  #提示透支金额
               while True:
                 answer_5 = input(f"your balance is not enough,but you have 1500 pounds overdraft amount,this trading will overdraft {amount - 1500}pounds,weather to continue,please enter 'yes' or 'no' :")
                 if answer_5 == "yes":
                    print(f"transfer {amount} pounds to {account_name} sucessful")
                    accounts[name]['balance'] -= amount
                    accounts[account_name]['balance'] += amount
                    return
                 elif answer_5 == "no":
                     transfer_money()
                     return
                 else:
                     print("Unable to understand the command, please re-enter")
                     break   
           else:
               amount > accounts[name]['balance'] + 1500
               print("your balance is not enough,please try again")
               transfer_money()      
                
    while True:
     choose = input("please enter number to choose feature(1: Check balance, 2: Deposit, 3: Withdraw money, 4: Transfer money, 5: Exit):")
     if choose == "1":
        check_balance()
     elif choose == "2":
          deposit()
     elif choose == "3":
          withdraw_money()
     elif choose == "4":
          transfer_money()
     elif choose == "5":
          print("Thank you for using the bank system")
          break
     else:
             print("Unable to understand the command, please re-enter")
            
           
           
                

          
            
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    