Python 3.5.1 (v3.5.1:37a07cee5969, Dec  5 2015, 21:12:44) 
[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
Type "copyright", "credits" or "license()" for more information.
>>> WARNING: The version of Tcl/Tk (8.5.9) in use may be unstable.
Visit http://www.python.org/download/mac/tcltk/ for current information.

============ RESTART: /Users/isaaccallison/Documents/breakfasr.py ============
>>> make_omelette("bacon")
Mixing the ingredients
Greasing the frying pan
Pouring the mixture into a frying pan
Cooking the first side
Flipping it!
Cooking the other side
'a bacon tasty omelette'
>>> 
============ RESTART: /Users/isaaccallison/Documents/breakfasr.py ============
>>> make_omelette("bacon", "Cheese")
Mixing the ingredients
Greasing the frying pan
Pouring the mixture into a frying pan
Cooking the first side
Flipping it!
Cooking the other side
'a bacon tasty omelette'
>>> 
============ RESTART: /Users/isaaccallison/Documents/breakfasr.py ============
>>> fancy_omelette("cheese","bacon")
Mixing the ingredients
Greasing the frying pan
Pouring the mixture into a frying pan
Cooking the first side
Flipping it!
Cooking the other side
'a fancy omelette with 2 ingredinets'
>>> 
============ RESTART: /Users/isaaccallison/Documents/breakfasr.py ============
>>> make_omelette(cheese)
Mixing the ingredients
Greasing the frying pan
Pouring the mixture into a frying pan
Cooking the first side
Flipping it!
Cooking the other side
'a swiss tasty omelette'
>>> make_pancake(cheese)
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    make_pancake(cheese)
TypeError: make_pancake() takes 0 positional arguments but 1 was given
>>> 
============ RESTART: /Users/isaaccallison/Documents/breakfasr.py ============
>>> make_pancake(cheese)
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    make_pancake(cheese)
TypeError: make_pancake() takes 0 positional arguments but 1 was given
>>> make_pancake()
Mixing the ingredients
Greasing the frying pan
Pouring the mixture into a frying pan
Cooking the first side
Flipping it!
Cooking the other side
'a delicious provoline pancake'
>>> make_omelette()
Mixing the ingredients
Greasing the frying pan
Pouring the mixture into a frying pan
Cooking the first side
Flipping it!
Cooking the other side
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    make_omelette()
  File "/Users/isaaccallison/Documents/breakfasr.py", line 15, in make_omelette
    omelette = 'a {} tasty omelette'.format(*args)
IndexError: tuple index out of range
>>> make_omelette(cheese)
Mixing the ingredients
Greasing the frying pan
Pouring the mixture into a frying pan
Cooking the first side
Flipping it!
Cooking the other side
'a provoline tasty omelette'
>>> cheese
'provoline'
>>> 
============ RESTART: /Users/isaaccallison/Documents/breakfasr.py ============
>>> cheese
'swiss'
>>> make_pancake()
Mixing the ingredients
Greasing the frying pan
Pouring the mixture into a frying pan
Cooking the first side
Flipping it!
Cooking the other side
'a delicious provoline pancake'
>>> cheese
'provoline'
>>> 
>>> 
>>> "shirt"
'shirt'
>>> type("shirt")
<class 'str'>
>>> dir('shirt')
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
>>> x = 'shirt'
>>> x.
SyntaxError: invalid syntax
>>> x.capitalize
<built-in method capitalize of str object at 0x105613308>
>>> x
'shirt'
>>> x.capitalize()
'Shirt'
>>> id('Shirt')
4390786640
>>> id('shirt')
4385223432
>>> 
============ RESTART: /Users/isaaccallison/Documents/breakfasr.py ============
>>> my_jeans = jeans(36,30,"blue")
>>> my_jeans
<__main__.jeans object at 0x105a4de10>
>>> dir(my_jeans)
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'color', 'length', 'put_on', 'take_off', 'waist', 'wearing']
>>> my_jeans.put_on()
Putting on 36x30 blue jeans
>>> my_jeans.wearing
True
>>> my_jeans.take_off()
Taking off 36x30 blue jeans
>>> 
============ RESTART: /Users/isaaccallison/Documents/breakfasr.py ============
>>> auto = vehicle()
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    auto = vehicle()
TypeError: __init__() missing 2 required positional arguments: 'color' and 'manuf'
>>> auto = vehicle("Blue", "Toyota")
>>> auto
<__main__.vehicle object at 0x105b58198>
>>> auto.drive
<bound method vehicle.drive of <__main__.vehicle object at 0x105b58198>>
>>> auto.drive()
the Blue Toyota goes vroom
>>> newAuto = car()
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    newAuto = car()
TypeError: __init__() missing 2 required positional arguments: 'color' and 'manuf'
>>> newAuto = car("red", "Honda")
>>> newAuto.drive()
the red Honda goes vroom
>>> n = newAuto.drive()
the red Honda goes vroom
>>> n
>>> 
>>> newAuto.drive
<bound method vehicle.drive of <__main__.car object at 0x105b58940>>
>>> newAuto.drive()
the red Honda goes vroom
>>> newAuto.drive()
the red Honda goes vroom
>>> newAuto.drive()
The red Honda sputters out of gas
>>> newAuto.radio()
Rockin tunes
>>> newAuto.w
Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    newAuto.w
AttributeError: 'car' object has no attribute 'w'
>>> newAuto.window()
fresh air
>>> m = motorcycle()
Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    m = motorcycle()
TypeError: __init__() missing 2 required positional arguments: 'color' and 'manuf'
>>> 
>>> 
>>> 
>>> clear
Traceback (most recent call last):
  File "<pyshell#55>", line 1, in <module>
    clear
NameError: name 'clear' is not defined
>>> ec = Ecar()
Traceback (most recent call last):
  File "<pyshell#56>", line 1, in <module>
    ec = Ecar()
NameError: name 'Ecar' is not defined
>>> 
