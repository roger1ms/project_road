import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation
from matplotlib import colors

neighbourhood = ((-1,-1), (-1,0), (-1,1), (0,-1), (0, 1), (1,-1), (1,0), (1,1))

nx, ny = 100, 100
X  = np.zeros((ny, nx))
X[1:ny-1, 1:nx-1] = np.random.randint(0, 100, size=(ny-2, nx-2))
for i in range(100):
    X[i][1]=100
for j in range(100):
    X[1][j]=100


def create_movement_list(ix,iy):
    global movement_list
    if ix == 0 and iy ==0:
        a1 = X[iy][ix]
        a2 = X[iy][ix+1]
        b1 = X[iy+1][ix]
        b2 = X[iy+1][ix+1]
        movement_list=[[a1,a2],[b1,b2]]
    elif ix == 0 and iy != 0:
        a1 = X[iy-1][ix]
        a2 = X[iy-1][ix+1]
        b1 = X[iy][ix]
        b2 = X[iy][ix+1]
        c1 = X[iy+1][ix]
        c2 = X[iy+1][ix+1]
        movement_list = [[a1, a2], [b1, b2],[c1, c2]]
    elif ix != 0 and iy == 0:
        a1 = X[iy][ix - 1]
        a2 = X[iy][ix]
        a3 = X[iy][ix + 1]
        b1 = X[iy + 1][ix - 1]
        b2 = X[iy + 1][ix]
        b3 = X[iy + 1][ix + 1]
        movement_list = [[a1, a2, a3], [b1, b2, b3]]
    else:
        a1 = X[iy - 1][ix - 1]
        a2 = X[iy - 1][ix]
        a3 = X[iy - 1][ix + 1]
        b1 = X[iy][ix - 1]
        b2 = X[iy][ix]
        b3 = X[iy][ix + 1]
        c1 = X[iy + 1][ix - 1]
        c2 = X[iy + 1][ix]
        c3 = X[iy + 1][ix + 1]
        movement_list = [[a1, a2, a3], [b1, b2, b3], [c1, c2, c3]]
    return movement_list


def update(X):
    X1 = X
    for ix in range(1, nx-1):
        for iy in range(1, ny-1):
            for dx in range(ix, nx-1):
                for dy in range(iy, ny-1):
                    start_x = ix
                    start_y = iy
                    end_x = dx
                    end_y = dy
                    direction = np.random.random()
                    while start_x != end_x and start_y != end_y:

                        create_movement_list(start_x, start_y)
                        sum_of_movement = 0
                        mid_y = len(movement_list) - 2
                        mid_x = len(movement_list[0]) - 2
                        for i in range(len(movement_list)):
                            for j in range(len(movement_list[i])):
                                if i > mid_y and j > mid_x and movement_list[i][j] != 0:
                                    movement_list[i][j] += 150
                                elif ((i > mid_y and j == mid_x) or (i == mid_y and j > mid_y)) and movement_list[i][j] != 0:
                                    movement_list[i][j] +=  75
                                sum_of_movement += movement_list[i][j]
                        min_difference = 1
                        coordinates = [0,0]
                        for i in range(len(movement_list)):
                            for j in range(len(movement_list[i])):
                                if direction > movement_list[i][j] / sum_of_movement:
                                    if direction - movement_list[i][j] < min_difference:
                                        min_difference = direction - movement_list[i][j]
                                        coordinates = [i - mid_y, j - mid_x]
                                    elif min_difference == direction - movement_list[i][j]:
                                        if np.random.random()>=0.5:
                                            min_difference = direction - movement_list[i][j]
                                            coordinates = [i - mid_y, j - mid_x]
                                elif direction <= movement_list[i][j]:
                                    if movement_list[i][j] - direction < min_difference:
                                        min_difference = movement_list[i][j] - direction
                                        coordinates = [i - mid_y, j - mid_x]
                                    elif min_difference == movement_list[i][j] - direction:
                                        if np.random.random()>=0.5:
                                            min_difference = movement_list[i][j] - direction
                                            coordinates = [i - mid_y, j - mid_x]
                        start_x += coordinates[1]
                        start_y += coordinates[0]
                        if X1[start_y][start_x]<(2/3):
                            X1[start_y][start_x] +=0.1
    X=X1
    mat.set_data(X)
    return [mat]

fig, ax = plt.subplots()
mat = ax.matshow(X)
ani = animation.FuncAnimation(fig, update, interval=40, save_count=1000)
plt.show()