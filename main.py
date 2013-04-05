#Imports other file(s)
from basic import gtorlt
from math import sin, cos, tan
from trig import csc, sec, cot

#First input that will act as a"guide" in a sense
mi1 = raw_input("Enter what calculation you want to do, or type help for more options: ")
mi2 = mi1.lower() #Supposed to make the main input lowercase
mi = str(mi1) #Supposed to make the main input into a string

#Takes in the x and y input
i1 = raw_input("Define your X value: ")
i2 = raw_input("Define your Y value: ")

#If block dealing with almost everything, will most likely be moved to another file that will deal with classes instead
def ifbm(mi, x, y):
    if mi == "help" or mi == "h":
        #Help Message
        return "Your choices are currently Greater than or Less than, Sine, Csc, Cosine, Sec, Tangent, and Cotangent"
    
    elif mi == "sin" or mi == "sine":
        #Does the sine calculation (Bad english, I know)
        return sin(x) 
    
    elif mi == "csc" or mi =="cosecant":
        #Does the csc calculation
        return csc(x)
    
    elif mi == "cos" or mi == "cosine":
        #Does the cosine calculation
        return cos(x)
    
    elif mi == "sec" or mi == "secant":
        #Does the sec calculation
        return sec(x)
    
    elif mi == "tan" or mi == "tangent":
        #Does the tangent calculation
        return tan(x)
    
    elif mi == "cot" or mi == "cotangent":
        return cot(x)
    
    elif mi == "gtorlt" or mi == "greater than or less than":
        return gtorlt(x, y)
    
    else:
        return "Something has gone horribly wrong, please restart the process"
    
#Creates the variable "output" which is basically another mediator between the top process and the print function
output = ifbm(mi, i1, i2)

#Simply prints the output
print output


