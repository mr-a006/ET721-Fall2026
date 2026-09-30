def addnumbers(a=0,b=0):
    return a+b

def subtractingnumbers(a=0, b=0):
    return a-b

def multiplynumbers(a=1, b=1):
    return a*b

def dividenumbers(a,b):
    try:
        return a/b
    except ZeroDivisionError:
        print("Error! can't divide by zero")
    except ValueError:
        print("Error! not a numerical value")
    except:
        print("ERROR!")