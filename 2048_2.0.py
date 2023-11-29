import turtle
import random
boundary = turtle.Screen()
boundary.setup(430, 630, 500, 10)
boundary.bgcolor('gray')
boundary.title('2048')
boundary.register_shape('2.gif')
boundary.register_shape('4.gif')
boundary.register_shape('8.gif')
boundary.register_shape('16.gif')
boundary.register_shape('32.gif')
boundary.register_shape('64.gif')
boundary.register_shape('128.gif')
boundary.register_shape('256.gif')
boundary.register_shape('512.gif')
boundary.register_shape('1024.gif')
boundary.register_shape('2048.gif')
boundary.register_shape('4096.gif')
boundary.register_shape('8192.gif')
boundary.register_shape('bg.gif')
boundary.register_shape('title.gif')
boundary.register_shape('score.gif')
boundary.register_shape('top_score.gif')
boundary.tracer(0)


class Block(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.penup()

    def grow(self):
        num = random.choice([2, 2, 2, 2, 4])
        self.shape(f'{num}.gif')
        a = random.choice(allpos)
        self.goto(a)
        allpos.remove(a)
        block_list.append(self)
        boundary.update()

    def go_down(self):
        self.go(-150, -50, 50, 0, -100, True)

    def go_up(self):
        self.go(-50, -150, -250, 0, 100, True)

    def go_left(self):
        self.go(-50, 50, 150, -100, 0, False)

    def go_right(self):
        self.go(50, -50, -150, 100, 0, False)

    def go(self, b1, b2, b3, px, py, c):
        global move_time, z_bool
        move_time = 0
        block_1, block_2, block_3 = [], [], []
        for i in block_list:
            if c is True:
                if i.ycor() == b1:
                    block_1.append(i)
                elif i.ycor() == b2:
                    block_2.append(i)
                elif i.ycor() == b3:
                    block_3.append(i)
            else:
                if i.xcor() == b1:
                    block_1.append(i)
                elif i.xcor() == b2:
                    block_2.append(i)
                elif i.xcor() == b3:
                    block_3.append(i)
        for j in block_1:
            j.move(j.xcor()+px, j.ycor()+py)
        for j in block_2:
            for k in range(2):
                j.move(j.xcor()+px, j.ycor()+py)
        for j in block_3:
            for k in range(3):
                j.move(j.xcor()+px, j.ycor()+py)
        if move_time != 0:
            block = Block()
            block.grow()
        bc_score.show_score(score)
        bc_top_score.show_top_score(top_score)
        for k in block_list:
            if k.shape() == '2048.gif' and z_bool:
                win_lose.show_text('达成2048，继续请按回车键')
                z_bool = False
        if judge() is False:
            win_lose.show_text('游戏结束，重新开始请按空格键')

    def move(self, gox, goy):
        global move_time, score, z, top_score
        if (gox, goy) in allpos:
            allpos.append(self.pos())
            self.goto(gox, goy)
            allpos.remove((gox, goy))
            move_time += 1
        else:
            for i in block_list:
                if i.pos() == (gox, goy) and i.shape() == self.shape():
                    allpos.append(self.pos())
                    self.goto(gox, goy)
                    self.ht()
                    block_list.remove(self)
                    z = int(i.shape()[0:-4])
                    i.shape(f'{z*2}.gif')
                    move_time += 1
                    score = score + z
                else:
                    continue
        if score > top_score:
            top_score = score


class Background(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.penup()

    def show_text(self):
        self.color('white', 'white')
        self.goto(-215, 120)
        self.begin_fill()
        self.pd()
        self.goto(215, 120)
        self.goto(215, 110)
        self.goto(-215, 110)
        self.end_fill()
        self.pu()
        self.shape('title.gif')
        self.goto(-125, 210)
        self.stamp()
        self.shape('score.gif')
        self.goto(125, 245)
        self.stamp()
        self.shape('top_score.gif')
        self.goto(125, 170)
        self.stamp()

    def show_back(self):
        for i in allpos:
            self.shape('bg.gif')
            self.goto(i)
            self.stamp()

    def show_score(self, score):
        self.color('white')
        self.goto(125, 210)
        self.clear()
        self.write(f'{score}', align='center', font=("Arial", 20, "bold"))

    def show_top_score(self, top_score):
        self.color('white')
        self.goto(125, 135)
        self.clear()
        self.write(f'{top_score}', align='center', font=("Arial", 20, "bold"))


class WinLose(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.ht()
        self.color('blue')

    def show_text(self, text):
        self.write(f'{text}', align='center', font=("黑体", 20, "bold"))


def judge():
    judge_a = 0
    if allpos == []:
        for i in block_list:
            for j in block_list:
                if i.shape() == j.shape() and i.distance(j) == 100:
                    judge_a += 1
        if judge_a == 0:
            return False
        else:
            return True
    else:
        return True


def init():
    global z, z_bool, score, block_list, allpos
    z = 0
    z_bool = True
    score = 0
    allpos = [(-150, 50), (-50, 50), (50, 50), (150, 50),
              (-150, -50), (-50, -50), (50, -50), (150, -50),
              (-150, -150), (-50, -150), (50, -150), (150, -150),
              (-150, -250), (-50, -250), (50, -250), (150, -250)]
    for i in block_list:
        i.clear()
        i.ht()
    win_lose.clear()
    block_list = []
    block = Block()
    block.grow()


z = 0
z_bool = True
score = 0
top_score = 0
block_list = []
allpos = [(-150, 50), (-50, 50), (50, 50), (150, 50),
          (-150, -50), (-50, -50), (50, -50), (150, -50),
          (-150, -150), (-50, -150), (50, -150), (150, -150),
          (-150, -250), (-50, -250), (50, -250), (150, -250)]
bc_title = Background()
bc_score = Background()
bc_top_score = Background()
bc_title.show_text()
bc_title.show_back()
bc_score.ht()
bc_top_score.ht()
bc_score.show_score(score)
bc_top_score.show_top_score(top_score)
block = Block()
block.grow()
move_time = 0
win_lose = WinLose()

boundary.listen()
boundary.onkey(block.go_right, 'Right')
boundary.onkey(block.go_left, 'Left')
boundary.onkey(block.go_up, 'Up')
boundary.onkey(block.go_down, 'Down')
boundary.onkey(win_lose.clear, 'Return')
boundary.onkey(init, 'space')

boundary.mainloop()

