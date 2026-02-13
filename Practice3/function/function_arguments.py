def my_function(fname):
    print(fname + " Refsnes")

my_function("Emil")
my_function("Tobias")
my_function("Linus")





def my_function(name): # name is a parameter
    print("Hello", name)
my_function("Emil") # "Emil" is an argument




def my_function(fname, lname):
    print(fname + " " + lname)
my_function("Emil", "Refsnes")





# def my_function(fname, lname):
    # print(fname + " " + lname)
# my_function("Emil")    -----> This function expects 2 arguments, but gets only 1




def my_function(name = "friend"):
    print("Hello", name)
my_function("Emil")
my_function("Tobias")
my_function() #If you do not put any argument to the function it takes defaul argument
my_function("Linus")


def my_function(country = "Norway"):
    print("I am from", country)
my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")