list = []
with open('phone.txt') as f:

    for i in range(200):
        line_data = f.readline()
        list.append(line_data)
    print list




