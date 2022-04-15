def amazon(users):  # O(n)
    user_and_password = []
    user_in_system = []
    for i in users:
        if i[0] == 'r':  # register a user
            if user_and_password.__contains__(i[9:]):
                print("user exist")
            else:
                user_and_password.append(i[9:])
                print("register success")
        elif i[4] == 'n':  # login user
            if user_and_password.__contains__(i[6:]):
                user_in_system.append(i[6:])
                print("login success")
            else:
                print("login fail,you must register first")
        elif i[4] == 't':  # user logout
            if user_in_system.__contains__(i[6:]):
                user_in_system.remove(i[6:])
                print("logout success")
            else:
                print("logout fail, you must login first")


amazon_list = ['register david 123', 'login david 123', 'logout uou 125', 'logout david 123', 'logout david 123']
amazon(amazon_list)
