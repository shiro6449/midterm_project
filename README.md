# midterm_project

<!-- MIDTERM PROJECT ABDUKADYROV KAMOLIDDIN MATH21 -->

Game of Life. Python. Tkinter

Project from scratch

Packages used in this project

<img width="201" alt="Снимок экрана 2022-04-02 в 23 18 49" src="https://user-images.githubusercontent.com/102587248/161394004-deb97689-fc34-4409-b6d8-1bdd0e723fa9.png">

If the game goes into a static state or loops, the program can detect this and offer to start the game again

<img width="598" alt="Снимок экрана 2022-04-02 в 23 24 57" src="https://user-images.githubusercontent.com/102587248/161394228-9720722d-1acb-4e34-97d8-fa6475d7698d.png">


The program saves the last 2 states of the board and checks it before each iteration with a new matrix.

<img width="641" alt="Снимок экрана 2022-04-02 в 23 22 45" src="https://user-images.githubusercontent.com/102587248/161394148-ced0b64b-f03a-4d37-99ff-c2953c7b0204.png">

All conditions are met for the project

Rules of the game

In an empty (dead) cell, next to which there are exactly three living cells, life is born;
if a living cell has two or three living neighbors, then this cell continues to live; otherwise, if there are fewer than two or more than three neighbors, the cell dies ("from loneliness" or "from overpopulation")
