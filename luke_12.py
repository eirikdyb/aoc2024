import time
def readfile():
    mem = []
    with open("test_input.txt",'r') as content:
        for line in content:
            temp_list = []
            for char in line.split()[0]:
                temp_list.append(char)
            mem.append(temp_list)
            
    return mem

def find_connected(letter,pos,visited,found):
    y = pos[0]
    x = pos[1]
    visited.append(pos)
    next_pos = [[y+1,x],[y-1,x],[y,x+1],[y,x-1]]
    for element in visited:
        if element in next_pos:
            next_pos.remove(element)
    if y<0 or y >= len(data):
        return
    elif x<0 or x >= len(data[0]):
        return
    if data[y][x] != letter:
        return
    if data[y][x] == letter and [y,x] not in found:
        found.append([y,x])
    if len(next_pos)>0:
        for possible in next_pos:
            find_connected(letter,possible,visited,found)
    return found
    
def perimeter(coord):
    tot = 0
    for pos in coord:
        per = 4
        y = pos[0]
        x = pos[1]
        next_pos = [[y+1,x],[y-1,x],[y,x+1],[y,x-1]]
        for neigh in next_pos:
            if neigh in coord:
                per -= 1
        tot += per
    return tot
    
start = time.time()
data = readfile()

all_regions = []
acc_for = []
for i in range(len(data)):
    for j in range(len(data[0])):
        if [i,j] not in acc_for:
            where = find_connected(data[i][j],[i,j],[],[])
            where = sorted(where, key=lambda x: x[0])
            where = sorted(where, key=lambda x: x[1])
            if where not in all_regions:
                all_regions.append(where)
                for points in where:
                    acc_for.append(points)

sol = 0
print(all_regions)
for i in range(len(all_regions)):
    sol += perimeter(all_regions[i])*len(all_regions[i])
print(sol)
end = time.time()
print("Det tok", end - start)
