#Decorators take a function as a argument and enhances the behaviour of the passed function

# def my_decorator(fun):
#     def wrapper():
#         print("Before function  runs")
#         fun()
#         print("After Function runs")
#     return wrapper

# def say_hello():
#     print("hello")

# say_hello=my_decorator(say_hello)
# say_hello()

def my_decorator(func):
    def wrapper():
        print("Before function runs")
        func()
        print("After function runs")
    return wrapper

@my_decorator
def say_hello():
    print("Hello")

say_hello()

    
