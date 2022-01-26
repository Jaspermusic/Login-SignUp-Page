def login_user():
    user = input("UserName : ")
    f = open("User_Details.txt", "r")
    j = 0
    h = 0
    l = 0
    for i in f:
        if h == 0:
            l = l+1
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
                h = 1
    # print(l)
    if h == 0:
        print("User not available")
        return login_user()
    f.close()
    return l


def login_pass(l):
    Pass = input("Password : ")
    f = open("User_Details.txt", "r")
    content = (f.readlines())
    cont_list = list(content[l])
    cont_list.remove("\n")
    i = ""
    for str in cont_list:
        i = i+str
    if i == Pass:
        print("Log IN Successful")
    else:
        print("Password does not match")
        return login_pass(l)
    f.close()
