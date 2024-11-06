import math
import random
import datetime
import json


# de modulos.aritmetica importe suma
from modulos.aritmetica import suma

# importe modulos.aritmetica con alias aritmetica
import modulos.aritmetica as aritmetica

# de moduleos importe aritmetica con alias art
from modulos import aritmetica as art

print(suma(5,3))

print(aritmetica.suma(5,3))

print(art.suma(5,3))