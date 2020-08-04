#  引入turtle模块
import turtle
# 引入 os 模块
import os
# Windows 系统发声模块
#import winsound

# 创建一个 Screen 对象，并赋给变量 wn
wn = turtle.Screen()
# 设置程序窗口的标题为 Pong by @MatrixTech
wn.title("Pong by @MatrixTech")
# 设置程序窗体的背景颜色为黑色
wn.bgcolor("black")
# 设置程序窗口宽为 800 像素大小，高为 600 像素大小
wn.setup(width=800, height=600)
# tracer方法调用禁止动画显示
wn.tracer(0)


# 球拍 A （左边球拍）
# 通过 turtle 模块创建一个 Turtle 对象，并赋给变量 paddle_a
paddle_a = turtle.Turtle()
# 设置速度为0
paddle_a.speed(0)
# 设置形状为矩形
paddle_a.shape("square")
# 设置颜色为白色
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5,stretch_len=1)
# 画笔抬起 -- 移动时不画线
paddle_a.penup()
# 前往 x 坐标为 -350, y 坐标为 0 的位置
paddle_a.goto(-350,0)

# 球拍 B （右边球拍）
# 通过 turtle 模块创建一个 Turtle 对象，并赋给变量 paddle_b
paddle_b = turtle.Turtle()
# 设置速度为0
paddle_b.speed(0)
# 设置形状为矩形
paddle_b.shape("square")
# 设置颜色为白色
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5,stretch_len=1)
# 画笔抬起 -- 移动时不画线
paddle_b.penup()
# 前往 x 坐标为 350, y 坐标为 0 的位置
paddle_b.goto(350,0)

# 乒乓球
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0,0)
# 乒乓球的 x 坐标增量
ball.dx = 2
# 乒乓球的 y 坐标增量
ball.dy = -2

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
# 隐藏海龟，加快绘制速度
pen.hideturtle()
pen.goto(0,260)
pen.write("玩家 A: 0  玩家 B: 0", align="center", font=("Courier",24,"normal"))

# 得分
score_a = 0
score_b = 0

# 函数
# 向上移动球拍 A
def paddle_a_up():
  	# 获得 paddle_a 的y坐标数值，并赋给变量 y
    y = paddle_a.ycor()
    # 在原来的数值基础上，增加20个像素
    y += 20
    # 重新设置 paddle_a 的y坐标，使其向上移动20个像素的距离
    paddle_a.sety(y)

# 向下移动球拍 A
def paddle_a_down():
    # 获得 paddle_a 的y坐标数值，并赋给变量 y
    y = paddle_a.ycor()
    # 在原来的数值基础上，减少20个像素
    y -= 20
    # 重新设置 paddle_a 的y坐标，使其向下移动20个像素的距离
    paddle_a.sety(y)

# 向上移动球拍 B
def paddle_b_up():
  	# 获得 paddle_b 的y坐标数值，并赋给变量 y
    y = paddle_b.ycor()
    # 在原来的数值基础上，增加20个像素
    y += 20
    # 重新设置 paddle_b 的y坐标，使其向上移动20个像素的距离
    paddle_b.sety(y)

# 向下移动球拍 B
def paddle_b_down():
    # 获得 paddle_b 的y坐标数值，并赋给变量 y
    y = paddle_b.ycor()
    # 在原来的数值基础上，减少20个像素
    y -= 20
    # 重新设置 paddle_b 的y坐标，使其向下移动20个像素的距离
    paddle_b.sety(y)    

# 键盘事件绑定
# 事件监听
wn.listen()
# 键盘 w 键的按下事件与方法 paddle_a_up 绑定
wn.onkeypress(paddle_a_up,'w')
# 键盘 s 键的按下事件与方法 paddle_a_down 绑定
wn.onkeypress(paddle_a_down,'s')
# 键盘 ↑ 键的按下事件与方法 paddle_b_up 绑定
wn.onkeypress(paddle_b_up,'Up')
# 键盘 ↑ 键的按下事件与方法 paddle_b_down 绑定
wn.onkeypress(paddle_b_down,'Down')


# 游戏主循环
while True:
    # print("x: ",ball.xcor()," y: ",ball.ycor() )
    # 执行 TurtleScreen 刷新。在每帧绘制结束后调用update方法进行屏幕刷新，让绘制的图形一次性显示在窗口里。
    wn.update()
    # 移动乒乓球
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # 上边界检测
    if ball.ycor() > 290:# 当乒乓球的 y 坐标大于 290 像素时候
        # 设置乒乓球的 y 坐标设置为290
        ball.sety(290)
        # 把乒乓球 y 坐标的增量变成 -2
        ball.dy *= -1
        # MacOS 系统下播放 bounce.wav 音频文件
        os.system("afplay bounce.wav&")
        # Windows 系统下播放 bounce.wav 音频文件
        #winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)


    # 下边界检测
    if ball.ycor() < -290:# 当乒乓球的 y 坐标小于 290 像素时候
        # 设置乒乓球的 y 坐标设置为290
        ball.sety(-290)
        # 把乒乓球 y 坐标的增量变成 -2
        ball.dy *= -1
         # MacOS 系统下播放 bounce.wav 音频文件
        os.system("afplay bounce.wav&")
        # Windows 系统下播放 bounce.wav 音频文件
        #winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    # 左边界检测
    if ball.xcor() > 390: #当乒乓球的 y 坐标大于 390 像素时候 
        # 乒乓球恢复到原点坐标
        ball.goto(0,0)
        # 改变开球方向
        ball.dx *= -1
        # score_a 得 1 分
        score_a += 1 
        # 清除画笔的绘图
        pen.clear()
        # 重新生成新的绘图
        pen.write("玩家 A: {}  玩家 B: {}".format(score_a,score_b), align="center", font=("Courier",24,"normal"))

    # 右边界检测
    if ball.xcor() < -390: #当乒乓球的 y 坐标小于 -390 像素时候 
        # 乒乓球恢复到原点坐标
        ball.goto(0,0)
        # 改变开球方向
        ball.dx *= -1
        # 玩家 B 得 1 分
        score_b += 1
        # 清除画笔的绘图
        pen.clear()
        # 重新生成新的绘图
        pen.write("玩家 A: {}  玩家 B: {}".format(score_a,score_b), align="center", font=("Courier",24,"normal"))


    # 乒乓球与球拍 B 的碰撞检测
    if (ball.xcor() > 340 and ball.xcor() < 350)  and (ball.ycor() < paddle_b.ycor() + 50 and ball.ycor() > paddle_b.ycor() - 50 ):
        ball.setx(340)
        ball.dx *= -1
        # MacOS 系统下播放 bounce.wav 音频文件
        os.system("afplay bounce.wav&")
        # Windows 系统下播放 bounce.wav 音频文件
        #winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    # 乒乓球与球拍 A 的碰撞检测
    if (ball.xcor() < -340 and ball.xcor() > -350)  and (ball.ycor() < paddle_a.ycor() + 50 and ball.ycor() > paddle_a.ycor() - 50 ):
        ball.setx(-340)
        ball.dx *= -1
        # MacOS 系统下播放 bounce.wav 音频文件
        os.system("afplay bounce.wav&")
        # Windows 系统下播放 bounce.wav 音频文件
        #winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
