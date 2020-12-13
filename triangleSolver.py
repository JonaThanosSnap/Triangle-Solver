########################################
#  Title: Triangle Solver              #
#  Date: 24 February 2020              #
#  Course: ICS3UI                      #
#  Description: Triangle Creator lets  #
# the user input the 3 sides of any    #
# triangle and then calculates the     #
# value of each angle which is         #
# displayed on a drawing made using    #
# Tkinter.                             #
########################################

from tkinter import *

from math import *

myInterface = Tk()

screen = Canvas( myInterface, width=800, height=800, background = "white" )

screen.pack()

#arrays so that the user has more freedom for what they write

acute = ["acute","Acute","a","A","ac","Ac","Acu","acu"]

obtuse = ["obtuse","Obtuse","O","o","ob","Ob","Obt","obt"]

right = ["right","Right","r","R","ri","Ri","Rit","rit","rite","Rite"]

scalene = ["scalene","Scalene","S","s","Sc","sc","Scal","scal"]

iso = ["isosceles","Isosceles","I","i","Iso","iso","isoc","isoc"]

equil = ["equilateral","Equilateral","E","e","Equil","equil","Eq","eq"]

#instead of typing screen.create_shape all the time, we can replace it with a variable 

l = screen.create_line

t = screen.create_text

p = screen.create_polygon

#there are some things that the user should know when using this code. As such, it is defined in a function so that we don't have to write the complete thing every time a tkinter drawing is made

def notes():
    
    t(350,50,text = "Note: The triangles are not meant to be drawn to scale and are simply a way of visualizing data.",font = "Arial 12")

    t(350,80,text = "Also, if your triangle includes negative angles,",font = "Arial 12")

    t(350,100,text = "this means the triangle you are trying to make does not exist",font = "Arial 12")

    #the notes are on different lines so the user can read them easier. 

def space():

    print(" ")

    #another function that adds spaces in between lines so the user has an easier time reading and the code looks cleaner
  
#asks the user for their name    

name = str(input("What is your name? "))

space() #use of the function

#welcomes the user

print("Hello "+name+", welcome to Triangle Creator!")

space()

#a bunch of asterisks to separate the introduction and the beginning of the actual code

print("*****************************************")

space()

#asks the user what type of triangle (by angle)they want to make (acute, right, obtuse)

tri = str(input("What type of triangle would you like to make? (by angle) "))

space()

#asks for the triangle by side (scalene, equilateral, isosceles)

tri2 = str(input("What type of triangle would you like to make? (by side) "))

space()

#always remember units!

units = str(input("What units are you using? "))

space()

if tri in acute: #if the triangle (by angle) is acute

    if tri2 in scalene: #if it is an acute scalene triangle

        a = float(input("What is the length of the longest side? ")) #asking for longest side

        space()

        b = float(input("What is the length of the second side? ")) #asking for second longest

        space()

        c = float(input("What is the length of the shortest side? ")) #asking for shortest

        space()

        if (a + b) > c and (a + c) > b and (b+c) > a and a != b and b != c and c != a: #testing to see if the triangle exists; the sum of 2 sides must always be greater than the third and since the user chose scalene and acute, neither of the sides can equal

            A = round(((acos(((b**2)+(c**2)-(a**2))/(2*b*c)))*57.2957795),1) #cosine law
    
            #since Python calculates in radians, the '57.2957795' is to convert the value into degrees. 180°/π ≈ 57.2957795

            B = round(((asin((b*sin(A))/a))*57.2957795),1) #sine law

            C = round((180-(A+B)),1) #the sum of the angles in a triangle add up to 180

            p(400,300,300,425,475,475,fill="white",width=4,outline="black") #begin drawing a generic triangle in tkinter

            t(250,325,text = str(c)+(" ")+str(units),font = "Arial 15") #adding the inputted values onto the image

            t(525,375,text = str(a)+(" ")+str(units),font = "Arial 15")

            t(325,475,text = str(b)+(" ")+str(units),font = "Arial 15")

            t(450,450,text = "C",font = "Arial 10") #the location of each angle

            t(325,412.5,text = "A",font = "Arial 10")

            t(390,330,text = "B",font= "Arial 10")

            t(350,600,text = "A = "+str(A)+"°,"+"B = "+str(B)+"°, C = "+str(C)+"°",font="Arial 20") #prints all the angles neatly at the bottom of the page

            notes()

        else: #if the sides work out
            
            print("sorry, the triangle you're making doesn't exist") #if the sides don't follow the rule mentioned before, the triangle doesn't exist

            t(425,350,text = "¯\_(ツ)_/¯", font = "Arial 100" )

            t(425,500,text = "looks like the triangle doesn't exist")
        
    elif tri2 in iso: #acute isosceles triangle

        a = float(input("What is the length of the two equally long sides? ")) #since in an isosceles triangle, 2 sides are equal, we only need to ask the user once

        space()

        c = float(input("What is the length of the remaining side? "))

        b = a

        if (a + b) > c and (a + c) > b and (b+c) > a and a != c: #once again, testing to see if the sides make sense

            A = round(((acos(((b**2)+(c**2)-(a**2))/(2*b*c)))*57.2957795),1) #cosine law

            B = A

            C = round((180-(A+B)),1)

            p(400,225,275,475,525,475,fill="white",width=4,outline="black") #draw a generic acute isosceles triangle

            t(312,450,text ="A",font= "Arial 10")

            t(485,450,text = "B",font= "Arial 10")

            t(400,260,text = "C",font= "Arial 10")

            t(525,325,text = str(a)+(" ")+str(units),font = "Arial 15")

            t(225,325,text = str(b)+(" ")+str(units),font = "Arial 15")

            t(400,525,text = str(c)+(" ")+str(units),font = "Arial 15")

            t(350,600,text = "A = "+str(A)+"°,"+"B = "+str(B)+"°, C = "+str(C)+"°",font="Arial 20")

            notes()

        else: #if the sides don't make sense

            space()

            print("Sorry, the triangle you're trying to make doesn't exist")
            
            t(425,350,text = "¯\_(ツ)_/¯", font = "Arial 100" )

            t(425,500,text = "looks like the triangle doesn't exist")

    elif tri2 in equil: #acute equilateral triangle

        side = float(input("What are the lengths of the sides? ")) #since all 3 sides are equal, we only need to ask the user once

        p(400,262.5,275,475,525,475,fill="white",width=4,outline="black") #generic equilateral triangle

        t(400,300,text = "B",font = "Arial 10")

        t(485,450,text = "C",font = "Arial 10")

        t(312,450,text ="A",font="Arial 10")

        t(525,325,text = str(side)+(" ")+str(units),font = "Arial 15")

        t(250,325,text = str(side)+(" ")+str(units),font = "Arial 15")

        t(400,500,text = str(side)+(" ")+str(units),font = "Arial 15")

        t(350,600,text = "A = 60°, B = 60°, C = 60°",font="Arial 20") #rather than wasting time calculating, we know the angles are all 60°

        notes()

    else: #if the user types in something random, it won't understand

        space()

        print("Sorry, I’m afraid I don’t understand")
        
elif tri in right: #if the user wants to make a right triangle

    if tri2 in scalene: #right scalene triangle

        a = float(input("What is the length of the longest side? "))

        space()

        b = float(input("What is the length of the second side? "))

        space()

        c = float(input("What is the length of the shortest side? "))


        if (a + b) > c and (a + c) > b and (b+c) > a and a != b and b != c and c != a and round((a**2),1) == round((b**2+c**2),1): #once again testing for sides. Now, it also tests for pythagorean theorem since it's a right triangle

            A = 90

            B =round(((asin(b/a))*57.2957795),1) #cosine law

            C =round((180-(A+B)),1) #Angle sum triangle theorem (all 3 sides must equal 180)

            p(275,475,600,475,275,350,fill = "white",width = 4, outline="black")

            t(200,375,text = str(c)+(" ")+str(units),font = "Arial 15")

            t(475,512.5,text = str(b)+(" ")+str(units),font = "Arial 15")

            t(475,355,text = str(a)+(" ")+str(units),font = "Arial 15")

            t(300,450,text = "A",font = "Arial 10")

            t(290,375,text = "B", font = "Arial 10")

            t(525,462.5,text = "C",font = "Arial 10")

            t(350,600,text = "A = "+str(A)+"°,"+"B = "+str(B)+"°, C = "+str(C)+"°",font="Arial 20")

            notes()

        else: #non-existent triangles

            space()
            
            print("Sorry, the triangle you're trying to make doesn't exist")

            t(425,350,text = "¯\_(ツ)_/¯", font = "Arial 100" )

            t(425,500,text = "looks like the triangle doesn't exist")

    elif tri2 in iso: #right isosceles triangle

        a = float(input("What is the length of the two equally long sides? "))

        space()

        #b = a

        c = float(input("What is the length of the remaining side? "))

        C = 90

        A = 45

        B = 45

        #rights isosceles triangles only have one possible combination of angles (45, 45, 90)

        if round((c**2),1) == round((2*a**2),1): #using pythagorean theorem to make sure the triangle exists. Also, added rounding in because sometimes there is a huge number of decimals and it's impossible for the user to type all of them in

            p(275,475, 575,475,275,175,fill = "white",width = 4, outline="black")

            t(200,350,text = str(a)+(" ")+str(units),font = "Arial 15")

            t(425,500,text = str(a)+(" ")+str(units),font = "Arial 15")

            #side b = side a

            t(475,300,text = str(c)+(" ")+str(units),font = "Arial 15")

            t(300,450,text = "C",font = "Arial 10")

            t(290,225,text = "A",font = "Arial 10")

            t(525,460,text = "B",font = "Arial 10")

            t(350,600,text = "A = "+str(A)+"°,"+"B = "+str(B)+"°, C = "+str(C)+"°",font="Arial 20")

            notes()

        else: #triangle doesn't exist

            space()
            
            print("Sorry, the triangle you're trying to make doesn't exist.")

            t(425,350,text = "¯\_(ツ)_/¯", font = "Arial 100" )

            t(425,500,text = "looks like the triangle doesn't exist")

    elif tri2 in equil: #right equilateral triangles are not possible

        print("I’m afraid the triangle you’re trying to create doesn’t exist")

        t(425,350,text = "¯\_(ツ)_/¯", font = "Arial 100" )

        t(425,500,text = "looks like the triangle doesn't exist")

    else:

        space()

        print("Sorry, I’m afraid I don’t understand")

elif tri in obtuse: #finally, obtuse triangles

    if tri2 in scalene: #obtuse scalene triangle 

        a = float(input("What is the length of the longest side? "))

        space()

        b = float(input("What is the length of the second side? "))

        space()

        c = float(input("What is the length of the shortest side? "))

        if (a + b) > c and (a + c) > b and (b+c) > a and a != b and b != c and c != a: #making sure the sides make sense

            A = round(((acos(((b**2)+(c**2)-(a**2))/(2*b*c)))*57.2957795),1) #cosine law

            B = round(((asin((b*sin(A))/a))*57.2957795),1) #sine law

            C = round((180-(A+B)),1)

            p(375,475,625,475,250,225,fill = "white",width = 4, outline="black") #drawing the triangle and adding text

            t(500,325,text = str(a)+(" ")+str(units),font = "Arial 15")

            t(500,500,text = str(c)+(" ")+str(units),font = "Arial 15")

            t(250,375,text = str(b)+(" ")+str(units),font = "Arial 15")

            t(390,450,text = "A",font = "Arial 10")

            t(285,270,text = "B",font = "Arial 10")

            t(575,460,text = "C",font = "Arial 10")

            t(350,600,text = "A = "+str(A)+"°,"+"B = "+str(B)+"°, C = "+str(C)+"°",font="Arial 20")

            notes()

        else: #if triangle doesn't exist

            space()
            
            print("Sorry, the triangle you're trying to make doesn't exist.")

            t(425,350,text = "¯\_(ツ)_/¯", font = "Arial 100" )

            t(425,500,text = "looks like the triangle doesn't exist")

    elif tri2 in iso: #obtuse isosceles triangle 

        a = float(input("What is the length of the two equally long sides? ")) #the 2 equally long sides

        space()

        b = a

        c = float(input("What is the length of the remaining side? "))

        if (a + b) > c and (a + c) > b and (b+c) > a and a != c:

            C = round(((acos(((b**2)+(a**2)-(c**2))/(2*b*a)))*57.2957795),1) #cosine law but since there are 2 identical sides, we only need to solve once

            A = round(((180-C)/2),1) #sum of all angles in a tringle is 180 degrees

            #B = A

            p(400,500,575,375,225,375,fill = "white",width = 4, outline="black")

            t(275,387.5,text = "B",font = "Arial 10")

            t(525,387.5,text = "A",font = "Arial 10")

            t(400,475,text = "C",font = "Arial 10")

            t(350,600,text = "A = "+str(A)+"°,"+"B = "+str(A)+"°, C = "+str(C)+"°",font="Arial 20") #since B = A, we can use A as B's value 

            notes()

        else: #if triangle doesn't exist

            space()
            
            print("Sorry, the triangle you're trying to make doesn't exist")

            t(425,350,text = "¯\_(ツ)_/¯", font = "Arial 100" )

            t(425,500,text = "looks like the triangle doesn't exist")


    elif tri2 in equil: #equilateral obtuse triangles are not possible

        space()

        print("I’m afraid the triangle you’re trying to create doesn’t exist")

        t(425,350,text = "¯\_(ツ)_/¯", font = "Arial 100" )

        t(425,500,text = "looks like the triangle doesn't exist")


    else:

        space()

        print("Sorry, I’m afraid I don’t understand")

        t(425,350,text = "¯\_(ツ)_/¯", font = "Arial 100" )

        t(425,500,text = "I don't understand.")
        
else: #if the user input for tri1 is not acute, right or obtuse, the program won't understand
    
    print("Sorry, I’m afraid I don’t understand")

    t(425,350,text = "¯\_(ツ)_/¯", font = "Arial 100" )

    t(425,500,text = "I don't understand.")
