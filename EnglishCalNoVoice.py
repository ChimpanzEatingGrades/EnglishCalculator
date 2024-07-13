import re
from time import sleep

def calculation():
    global result
    sleep(1)
    print("Calculating...")
    print()
    sleep(1)
    new_output = "Put in a number newoutput."
    result = "unavailable. Make sure you ask me to solve a coherent equation"
    new_output = re.findall('\d*\.?\d+',userin) ;s=0
    if any(x in userin.lower() for x in ["add", "addition", "plus", "+", "combine", "sum"]):
        result = 0
        for i in new_output:
            result = float(i)+result
    elif any(x in userin.lower() for x in ["time", "multipl", "x", "*"]):
            result = 1
            for i in new_output:
                result = float(i) * result
    elif any(x in userin.lower() for x in ["divi", "/", "over", "fraction"]):
        if len(new_output) > 2:
            if any(x in userin.lower() for x in ["from"]):
                result = 0
                result = float(new_output[-1]) / (float(new_output[0]) + float(new_output[-2]))
            else:
                result = "unavailable. Make sure you ask me to solve a coherent equation"
        else: 
            if any(x in userin.lower() for x in ["from", "how many"]):
                result = 0
                result = float(new_output[-1]) / float(new_output[0])
            else:
                result = 0
                result = float(new_output[0]) / float(new_output[-1])
    elif any(x in userin.lower() for x in ["power", "^", "exponent", "square", "cube"]):
        if any(x in userin.lower() for x in ["square"]):
            result = 0
            for i in new_output: 
                result = float(i) ** 2
        elif any(x in userin.lower() for x in ["cube"]):
            result = 0
            for i in new_output: 
                result = float(i) ** 3
        else: 
            result = 0
            var1, var2 = new_output
            result = float(var1) ** float(var2)
    elif any(x in userin.lower() for x in ["minus", "subtract", "subtraction", "-", "take", "lessen"]):
        if len(new_output) > 2:
            if any(x in userin.lower() for x in ["from"]):
                result = 0
                result = float(new_output[-1]) - (float(new_output[0]) + float(new_output[-2]))
            else:
                result = "unavailable. Make sure you ask me to solve a coherent equation"
        else: 
            if any(x in userin.lower() for x in ["from"]):
                result = 0
                result = float(new_output[-1]) - float(new_output[0])
            else:
                result = 0
                result = float(new_output[0]) - float(new_output[-1])


print("Hi! I am the magic calculator.")
print("I can do addition, subtraction, multiplication, and division.")
print("Your wish is my command!")
print()
while True:
    sleep(1)
    userin=input("What would you like me to do? ")
    print()
    if any(x in userin.lower() for x in ["stop", "end", "die", "terminate", "no", "quit", "done"]): 
        print("Very well. Shutting off...")
        print()
        sleep(1)
        print("XC")
        break
    else:
        try:
            calculation()
            print("Your answer is " + str(result) + ".")
            print()
        except:
            print("Ask me to solve a valid equation.")
            print()

 
