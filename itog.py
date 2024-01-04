
import numpy as np
import seaborn as sn
import matplotlib.pyplot as plt


N = 100
M = 100
nx, ny = 100, 100
X = [[0]*M for i in range(N)]
viv = [[0]*M for j in range(N)]
for i in range(100):
    for j in range(100):
        X[i][j] = np.random.randint(10, 66)
for i in range(100):
    X[i][5]=100
    X[i][6] = 100
    X[i][7] = 100
    X[i][8] = 100
    viv[i][5] = 100
    viv[i][6] = 100
    viv[i][7] = 100
    viv[i][8] = 100
for j in range(100):
    viv[5][j] = 100
    viv[6][j] = 100
    viv[7][j] = 100
    viv[8][j] = 100

def create_movement_list(ix,iy):
    global movement_list
    if ix == 0 and iy ==0:
        a1 = 0
        a2 = X[iy][ix+1]
        b1 = X[iy+1][ix]
        b2 = X[iy+1][ix+1]
        movement_list=[[a1,a2],[b1,b2]]
    elif ix == 99 and iy == 99:
        a1 = X[iy-1][ix-1]
        a2 = X[iy-1][ix]
        b1 = X[iy][ix-1]
        b2 = 0
        movement_list = [[a1, a2], [b1, b2]]
    elif ix == 99 and iy == 0:
        a1 = X[iy][ix-1]
        a2 = 0
        b1 = X[iy+1][ix-1]
        b2 = X[iy+1][ix]
        movement_list = [[a1, a2], [b1, b2]]
    elif ix == 0 and iy == 99:
        a1 = X[iy-1][ix]
        a2 = X[iy-1][ix+1]
        b1 = 0
        b2 = X[iy][ix+1]
        movement_list = [[a1, a2], [b1, b2]]
    elif ix == 0 and iy != 0 and iy!=99:
        a1 = X[iy-1][ix]
        a2 = X[iy-1][ix+1]
        b1 = 0
        b2 = X[iy][ix+1]
        c1 = X[iy+1][ix]
        c2 = X[iy+1][ix+1]
        movement_list = [[a1, a2], [b1, b2],[c1, c2]]
    elif ix != 0 and iy == 0 and ix!=99:
        a1 = X[iy][ix - 1]
        a2 = 0
        a3 = X[iy][ix + 1]
        b1 = X[iy + 1][ix - 1]
        b2 = X[iy + 1][ix]
        b3 = X[iy + 1][ix + 1]
        movement_list = [[a1, a2, a3], [b1, b2, b3]]
    elif ix == 99 and iy !=99:
        a1 = X[iy-1][ix-1]
        a2 = X[iy-1][ix]
        b1 = X[iy][ix-1]
        b2 = 0
        c1 = X[iy+1][ix-1]
        c2 = X[iy+1][ix]
        movement_list = [[a1, a2], [b1, b2], [c1, c2]]
    elif iy == 99 and ix !=99:
        a1 = X[iy-1][ix-1]
        a2 = X[iy-1][ix]
        a3 = X[iy-1][ix+1]
        b1 = X[iy][ix-1]
        b2 = 0
        b3 = X[iy][ix+1]
        movement_list = [[a1, a2, a3], [b1, b2, b3]]
    else:
        a1 = X[iy - 1][ix - 1]
        a2 = X[iy - 1][ix]
        a3 = X[iy - 1][ix + 1]
        b1 = X[iy][ix - 1]
        b2 = 0
        b3 = X[iy][ix + 1]
        c1 = X[iy + 1][ix - 1]
        c2 = X[iy + 1][ix]
        c3 = X[iy + 1][ix + 1]
        movement_list = [[a1, a2, a3], [b1, b2, b3], [c1, c2, c3]]
    return movement_list


def change_path_values(cleanliness, hurry, people_y_position, people_x_position, movement_list, start_x, end_x, start_y, end_y):
    global sum_of_movement
    sum_of_movement=0
    for i in range(len(movement_list)):
        for j in range(len(movement_list[i])):
            if movement_list[i][j]<cleanliness*100:
                movement_list[i][j] = movement_list[i][j] - movement_list[i][j]*cleanliness
    for i in range(len(movement_list)):
        for j in range(len(movement_list[i])):
            if start_x<end_x and start_y<end_y:
                if i > people_y_position and j > people_x_position and movement_list[i][j] != 0:
                    movement_list[i][j] += 150*hurry
                elif ((i > people_y_position and j == people_x_position) or (
                        i == people_y_position and j > people_y_position)) and movement_list[i][j] != 0:
                    movement_list[i][j] += 75*hurry
            elif start_x == end_x and start_y < end_y:
                if i > people_y_position and j == people_x_position and movement_list[i][j] != 0:
                    movement_list[i][j] += 300 * hurry
            elif start_x < end_x and start_y == end_y:
                if i == people_y_position and j > people_x_position and movement_list[i][j] != 0:
                    movement_list[i][j] += 300 * hurry
            elif start_x == end_x and start_y > end_y:
                if i < people_y_position and j == people_x_position and movement_list[i][j] != 0:
                    movement_list[i][j] += 300 * hurry
            elif start_x > end_x and start_y == end_y:
                if i == people_y_position and j < people_x_position and movement_list[i][j] != 0:
                    movement_list[i][j] += 300 * hurry
            elif start_x>end_x and start_y>end_y:
                if i < people_y_position and j < people_x_position and movement_list[i][j] != 0:
                    movement_list[i][j] += 150*hurry
                elif ((i < people_y_position and j == people_x_position) or (
                        i == people_y_position and j < people_y_position)) and movement_list[i][j] != 0:
                    movement_list[i][j] += 75*hurry
            else:
                movement_list[i][j] -= 50
            sum_of_movement += movement_list[i][j]
    return movement_list



for ix in range(90):
    for iy in range(90):
        for dx in range(ix+1, 90):
            for dy in range(iy+1, 90):
                X1 = X
                start_x = ix
                start_y = iy
                end_x = dx
                end_y = dy
                hod = 0
                cleanliness = np.random.random()
                hurry=0
                while hurry<0.5:
                    hurry = np.random.random()
                count_of_move = 0
                while (start_x != end_x or start_y != end_y) and count_of_move < 3000:
                        create_movement_list(start_x, start_y)
                        #for f in range(len(movement_list)):
                            #print(movement_list[f],0)
                        people_y_position = len(movement_list) - 2
                        people_x_position = len(movement_list[0]) - 2
                        change_path_values(cleanliness, hurry, people_y_position, people_x_position, movement_list, start_x, end_x, start_y, end_y)
                        #for f in range(len(movement_list)):
                            #print(movement_list[f],1)
                        #print(sum_of_movement, cleanliness, hurry)
                        coordinates = [0,0]
                        min = 0
                        for i in range(len(movement_list)):
                            for j in range(len(movement_list[i])):
                                if movement_list[i][j]>min and movement_list[i][j]!=0:
                                    min = movement_list[i][j]
                                    coordinates[0] = i
                                    coordinates[1] = j
                        if people_y_position==0:
                            start_y+=coordinates[0]
                        elif people_y_position==1:
                            start_y+=coordinates[0]-1
                        if people_x_position==0:
                            start_x+=coordinates[1]
                        elif people_x_position==1:
                            start_x+=coordinates[1]-1
                        if X[start_y][start_x]/100<(2/3):
                            X1[start_y][start_x] +=0.00005
                        viv[start_y][start_x] = 100
                        hod+=1
                        #print('fasafafaf', cleanliness, coordinates, [people_x_position, people_y_position], sum_of_movement, start_x, start_y, end_x, end_y)
                        count_of_move+=1
                print('PROCESS:', hod, ix, iy, dx, dy)


cmap = "binary"
# plotting the heatmap
hm = sn.heatmap(data=X1,
                cmap=cmap)

# displaying the plotted heatmap
plt.show()
