# # def greet(name,city):
# #     print(f"Hello,{name} from {city}")
# # greet("Yashika","Tiruppur")
# # greet("Chennai","Asha") 
# # # --------------------------------------------------------------------------
# # # 3. Keyword arguments - the name decides
# # # --------------------------------------------------------------------------
# # # You write slot=value. Now the order does not matter.
# # greet(city="Chennai", name="Asha")      # Hello Asha from Chennai

# # def power(base, exponent=2, show=False):
# #     result = base ** exponent
# #     if show:
# #         print(f"{base} to the power {exponent} is {result}")
# #     return result

# # print(power(5))                         # 25
# # print(power(5, 3))                      # 125
# # print(power(5,3, show=True))
# # print("a","b","c",end="")                    # a b c      (sep=" " is the default)
# # print("a", "b", "c", sep="-",end="")           # a-b-c
# # print("no new line", end="")         # end="\n" is the default
# # print("same line")

# def enrol(name, *subjects, fee=1000, **extra):
#     print("name    :", name)
#     print("subjects:",set(subjects))
#     print("fee     :", fee)
#     print("extra   :", extra)

# enrol("Asha", "Python", "SQL", fee=1500, city="Chennai", batch="A")


# def countdown(n):
#     if n == 0:                          # BASE CASE: stop here
#         print("Lift off!")
#         return
#     print(n)
#     countdown(n - 1)                    # RECURSIVE CASE: a smaller problem

# countdown(10)
# def forever(n):
#     print(n)
#     return forever(n + 1)               # never gets smaller, never stops

# try:
#     forever(1)
# except RecursionError:
#     print("Python stopped it: too many calls waiting")


# x=257
# y=257
# print(id(x))
# print(id(y))

def square(x):
    return x * x

square_short = lambda x: x * x

print(square(5))                        # 25
print(square_short(5)) 

add = lambda x, y: x + y
print(add(2, 3))                        # 5

always_ten = lambda: 10                 # no inputs is allowed
print(always_ten())                     # 10

with_default = lambda name,greeting="Hello": f"{greeting} {name}"
print(with_default("Good Morning!","Asha"))   