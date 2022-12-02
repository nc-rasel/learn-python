li = [1,2,3,4,5,6,7,8]
key = 5
flag = False

for item in li:
    if key == item:
        # print('Found')
        flag = True
        break
# if flag is False:
#     print('Not found')

if flag:
    print('found')
else:
    print('Not found')
