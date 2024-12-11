def readfile():
    with open("test_input.txt",'r') as content:
        for line in content:
            return line.split()

def blink(n,string):
    for j in range(n):
        new_list = []
        for elements in string:
            if elements == "0":
                new_list.append("1")
            elif len(elements) % 2 == 0:
                new_list.append(elements[:int(len(elements)/2)])
                new_list.append(elements[int(len(elements) / 2):])
                while new_list[-1][0] == "0" and len(new_list[-1]) >1:
                    new_list[-1] = new_list[-1][1:]
            else:
                new_list.append(str(int(elements)*2024))
        string = new_list
        print(string)
    return string

data = readfile()
res = blink(10,data)
print(len(res))