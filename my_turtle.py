import turtle

# 创建Screen(窗体)对象
screen = turtle.Screen()
# 使用Screen 的 setup() 方法设置窗体的大小，宽度为500像素，高为400像素
screen.setup(500, 400)
# 创建turtle(海龟)对象
myTurtle = turtle.Turtle()

# 向前移动海龟150个像素
myTurtle.forward(150)
# 向左移动海龟90个像素
myTurtle.left(90)
# 向前移动海龟75个像素
myTurtle.forward(75)

# 退出
screen.exitonclick()