# # שאלה 1
# def start(func):
#     def wrapper():
#         print("Start function")
#         func()
#         print("End function")
#     return wrapper
    
# @start
# def stop():
#    print("in progrees") 
# stop()

# # שאלה 2
# import time

# def start(func):
#     def wrapper():
#         start = time.time()
#         func()
#         end = time.time()
#         print("The time it took for the function to execute:", end - start)
#     return wrapper
    
# @start
# def stop():
#    print("in progrees") 
# stop()

# # שאלה 3
# def arguments(func):
#     def wrapper(*argu):
#         func()
#         print(*argu)
#     return wrapper

# @arguments
# def start_arguments():
#     print("The arguments:")

# start_arguments("a", 1, "ass")

# שאלה 4
def conversion(func):
    def wrapper(string:str):
        func()
        print(string.upper())
        # return func
    return wrapper

@conversion
def srart_conversion():
    pass

srart_conversion("ariel")

# # שאלה 5
# def counter_readings(func):
#     count = 0
#     def wrapper():
#         nonlocal count
#         count += 1
#         func()
#         print(count)בלד
#     return wrapper

# @counter_readings
# def start_counter_readings():
#     pass

# start_counter_readings()