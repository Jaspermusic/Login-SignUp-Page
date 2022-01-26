def input_user():
    user = input("UserName : ")
    f = open("User_Details.txt", "r")
    j = 0
    for i in f:
        j = j+1
        if j % 3 == 1 or j == 1:
            i_list = list(i)
            # print(i_list)
            # i_list.remove(' ')
            i_list.remove('\n')
            i = ""
            for str in i_list:
                i = i+str
            if i == user:
                print("User not available")
                return input_user()
    f.close()
    f = open("User_Details.txt", "a")
    f.write(user)
    f.write("\n")
    f.close()


def confirm_pass(Pass):
    Conf_Pass = input("Confirm Password : ")
    if Conf_Pass != Pass:
        print("Password not matched")
        return confirm_pass(Pass)
    else:
        pass


def input_pass():
    Pass = input("Password : ")
    if check_pass(Pass) == False:
        return input_pass()
    f = open("User_Details.txt", "a")
    confirm_pass(Pass)
    f.write(Pass)
    f.write("\n")
    f.write("\n")
    f.close()


def check_pass(a):
    s = list(a)
    man = 0
    for i in s:
        if i == '1' or i == '2' or i == '3' or i == '4' or i == '5' or i == '6' or i == '7' or i == '8' or i == '9' or i == '0':
            man = 1
    if(man == 0):
        print("Password should contain mix of numbers")
        return False
    else:
        return True
