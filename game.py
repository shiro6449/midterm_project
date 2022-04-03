import tkinter as tk
import random
from copy import deepcopy
from time import sleep
import tkinter.messagebox


class Field:
    def __init__(self, n, m, canvas, width, height):
        self.n = n
        self.m = m
        self.canvas = canvas
        self.width = width
        self.height = height
        self.__h = height / n
        self.__w = width / m

        self.flag = False

        self.__matrix = [[2 for i in range(m + 2)]]

        for i in range(n):
            row = [2]
            for j in range(m):
                row.append(random.choice([0, 1]))

            row.append(2)
            self.__matrix.append(row)

        self.__matrix.append([2 for i in range(m + 2)])

        self.validate_data()
        self.last_state = None
        self.pre_last_state = None
        self.draw_matrix()

    def show_matrix_console(self):
        for i in self.__matrix:
            print(i)

    def draw_matrix(self):
        y = 0
        self.canvas.delete('all')
        for i in range(1, self.n+1):
            x = 0
            for j in range(1, self.m+1):
                # print(x, y)
                self.canvas.create_rectangle(
                    x, y, x + self.__w, y + self.__h,
                    fill='#5effa4' if self.__matrix[i][j] == 1 else 'white',
                    outline=''
                )
                x += self.__w
            y += self.__h

        self.__tramp()
        self.__check_for_restart()
        if self.flag:
            return
        self.canvas.after(200, self.draw_matrix)

    def __tramp(self):
        mat_copy = deepcopy(self.__matrix)

        for i in range(1, self.n+1):
            for j in range(1, self.m+1):
                rm = 0

                if mat_copy[i-1][j] == 1:
                    rm += 1

                if mat_copy[i-1][j+1] == 1:
                    rm += 1

                if mat_copy[i][j+1] == 1:
                    rm += 1

                if mat_copy[i+1][j+1] == 1:
                    rm += 1

                if mat_copy[i+1][j] == 1:
                    rm += 1

                if mat_copy[i+1][j-1] == 1:
                    rm += 1

                if mat_copy[i][j-1] == 1:
                    rm += 1

                if mat_copy[i-1][j-1] == 1:
                    rm += 1

                if rm not in (2, 3):
                    self.__matrix[i][j] = 0
                elif rm == 3:
                    self.__matrix[i][j] = 1

        self.pre_last_state = deepcopy(self.last_state)
        self.last_state = deepcopy(mat_copy)

    def __check_for_restart(self):
        if self.last_state == self.__matrix or self.pre_last_state == self.__matrix:
            self.flag = True
            sleep(1)
            print('Game is over')
            tk.messagebox.showinfo(message='Game is over. Do you want to restart?')
            self.__init__(self.n, self.m, self.canvas, self.width, self.height)

    def validate_data(self):
        if type(self.canvas) != tk.Canvas:
            raise TypeError('The canvas should be an object of the class tk.Canvas')

        if type(self.n) != int:
            raise TypeError('n must be an integer')

        if type(self.m) != int:
            raise TypeError('m must be an integer')

        if self.n <= 0 or self.m <= 0:
            raise Exception('n and m can not be equal to a negative number')


b = tk.Tk()
b.geometry('640x640')

canvas = tk.Canvas(b, width=640, height=640)
canvas.pack()

a = Field(2, 1, canvas, 640, 640)

a.show_matrix_console()
# a.tramp()
print('------')

b.mainloop()
