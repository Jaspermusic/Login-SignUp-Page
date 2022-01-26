from Sign_up import input_user, input_pass
from Log_in import login_user, login_pass


l_s = input("Press S for Sign UP or L for Log In:")
if l_s == 's' or l_s == 'S':
    print("\n")
    print("Sign UP")
    input_user()
    input_pass()
    print("\n")
    print("Account has been created, please Log IN")
    print("\n")
    print("Log IN")
    user_no = login_user()
    login_pass(user_no)
elif l_s == 'l' or l_s == 'L':
    print("\n")
    print("Log IN")
    user_no = login_user()
    login_pass(user_no)
