#Shrish Kushwaha
#Date: 10/20/2025
#Compound Interest Calculator
#Extra:
import turtleGraphic
import turtle
t = turtle.Turtle()
t.speed(0)

screen = turtle.Screen()
screen.setup(width = 800 , height = 800)
offset = 100

principalAmount = float(input("How much money are currently investing?"))
timesCompoundedPerYear = float(input("How many times is this investment getting compounded per year?"))
yearsInvested = float(input("How many years will this investment be invested?"))
interestRate = float(input("What is the annual interest rate?(Type decimal form)"))
interest = 0


futureValue = principalAmount*(1+ interestRate/timesCompoundedPerYear)**(timesCompoundedPerYear*yearsInvested)
interest = futureValue-principalAmount
print(f'\033[91mThe future value of your investment is:{futureValue :,.2f}$\nThe interest/profit gained is: {interest: ,.2f}$\033[0m')


turtleGraphic.drawCordPlane(yearsInvested//2,futureValue//5, t)
turtleGraphic.plotPoints(yearsInvested,futureValue, yearsInvested//2,futureValue//5, t)

turtle.done()

