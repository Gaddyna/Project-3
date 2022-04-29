from graphics import*
import random
#Initial Element, create window
win = GraphWin("Discount Program", 500, 500)
#Font size and color and question
t = Text(Point(250,100), 'What is the total of the items?')
t.setSize(30)
t.setTextColor('pink')
t.draw(win)

e = Entry(Point(250,200), 15)
e.draw(win)

m = win.getMouse()
user_choice = e.getText()

#Change Display tot he next question
t.undraw()
e.undraw()

t2 = Text(Point(250,100), 'What is the discount percentage?')
t2.setSize(30)
t2.setTextColor('pink')
t2.draw(win)
#win.getMouse()

p = Entry(Point(250,200), 15)
p.draw(win)
m = win.getMouse()
user_choice = p.getText()

#Change display again

t2.undraw()
p.undraw()
#Begin the math needed to do the discount and display the final price
t3 = Text(Point(250,100), "The discounted Price is $" + (e.getText()/100 * p.getText()))
t3.setSize(30)
t3.setTextColor('pink')
t3.draw(win)


win.getMouse()
win.close()