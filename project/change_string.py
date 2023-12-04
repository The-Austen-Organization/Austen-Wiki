def change_string(string, old, new):
    while string.find(old) != -1:
        index = string.find(old)
        if index == 0:
            string = new + string[1:]
        elif index == len(string)-1:
            string = string[0:-1] + new
        else:
            string = string[0:index] + new + string[index+1:]
    return string