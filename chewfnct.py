
def chew_up(list,conditional kwarg):
"""find condtional argument items in list"
    temp = b
    while len(temp)>0:
        last = len(temp) -1
        move_one = last - 1
        print(temp)
        if temp[last] - temp[move_one] == 1:
            del temp[-1]
        else:
            print (temp[last] - temp[move_one])
            del temp[-1]
