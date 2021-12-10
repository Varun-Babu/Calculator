from  clear_screen import screen_clear
def add(n1,n2):
    return n1 + n2
def substract(n1,n2):
    return n1 - n2
def multiply(n1,n2):
    return n1 * n2
def divide(n1,n2):
    return n1 / n2            

operations = {
            "+":add,
            "-":substract,
            "*":multiply,
            "/":divide,
            }
def calculator():
    n1 = float(input("enter first no"))
    for symbol in operations:
        print(symbol)   
    stop = False
    while not stop:
        op = input("choose which operation ")    
        n2 = float(input("enter next no"))  
        calculation_function = operations[op]
        answer = calculation_function(n1,n2)
        print(answer)
        choice = input("Type 'yes' to continue and 'no' to restart ").lower()
        if choice == "no":
            stop =True
            screen_clear()
            calculator()
        elif choice == "yes":
            n1 = answer
            pass
        else:
            print("invalid input")   
calculator()            