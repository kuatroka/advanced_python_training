from shapes import Paper, Triangle, Rectangle, Oval

paper = Paper()

rect1 = Rectangle()
rect1.set_color("blue")
rect1.set_width(200)
rect1.set_height(100)
rect1.set_x(100)
rect1.set_y(100)
rect1.draw()

rect2 = Rectangle()
rect2.set_color("red")
rect2.set_width(200)
rect2.set_height(100)
rect2.set_x(300)
rect2.set_y(100)
rect2.draw()

tria1 = Triangle(5, 5, 100, 5, 100, 200)
tria1.set_color("yellow")
# tria1.set_width(50)
tria1.set_x(300)
tria1.set_y(100)
tria1.draw()

oval1 = Oval()
oval1.randomize(50, 60)
oval1.draw()
paper.display()
