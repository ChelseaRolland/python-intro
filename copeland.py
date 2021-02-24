def username_generator(first_name, last_name):
    username = ""
    if len(first_name) > 3 or len(last_name) > 4:
        username = first_name[0:3] + last_name[0:4]
    else:
        username = first_name + last_name
    return username

def password_generator(username):
    password = ""
    for i in range(0,len(username)):
        password += username[i - 1]
    return password