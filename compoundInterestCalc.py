#Shrish Kushwaha
#Date: 10/20/2025
#Compound Interest Calculator
#Extra: Used turtle graphics to plot the growth of investment over time

#Importing turtleGraphic module
import turtleGraphic
import turtle
t = turtle.Turtle()
t.speed(0)
#Setting up the turtle screen
screen = turtle.Screen()
screen.setup(width = 800 , height = 800)
#Variables
offset = 100
futureValue = []
#User Inputs

principalAmount = float(input("How much money are currently investing?"))
principalAmountCOPY = principalAmount
timesCompoundedPerYear = float(input("How many times is this investment getting compounded per year?"))
yearsInvested = int(input("How many years will this investment be invested?"))
interestRate = float(input("What is the annual interest rate?(Type decimal form)"))
interestMade = 0
#Calculations

for i in range(yearsInvested):
    principalAmount = principalAmount * (1 + (interestRate / timesCompoundedPerYear))**(timesCompoundedPerYear*yearsInvested)
    futureValue.append(principalAmount)
interestMade = futureValue[0] - principalAmountCOPY

#Output
print(f'\033[91mThe future value of your investment is:{futureValue[0] :,.2f}$\nThe interest/profit gained is:{interestMade: ,.2f}$\033[0m')

#Plotting the graph using turtle graphics
print(f'\033[91mThe future value of your investment is:{futureValue[0] :,.2f}$\nThe interest/profit gained is:{interestMade: ,.2f}$\033[0m')

turtleGraphic.drawCordPlane(yearsInvested//2,futureValue[0]//5, t)
for i in range(yearsInvested):
    turtleGraphic.plotPoints(yearsInvested*(i+1),futureValue[i], yearsInvested//2,futureValue[0]//5, t)
turtle.done()

