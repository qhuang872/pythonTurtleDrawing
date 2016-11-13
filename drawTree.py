import turtle
def tree(branchlen,t):
    if branchlen >5:
        t.forward(branchlen)
        t.right(30)
        tree(branchlen-15,t)
        t.left(30)
        tree(branchlen-15,t)
        t.left(30)
        tree(branchlen-15,t)
        t.right(30)
        t.backward(branchlen)

def main():
    t=turtle.Turtle()
    myWin=turtle.Screen()
    t.left(90)
    t.up()
    t.backward(100)
    t.down()
    t.color("green")
    tree(80,t)
    myWin.exitonclick()

main()
