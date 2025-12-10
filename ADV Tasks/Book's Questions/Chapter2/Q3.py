# ========== 3 =============
# Point Class with __slots__ :

class Point:
    __slots__ = ('x', 'y')
    
    def __init__(self, x, y):
        self.x = x
        self.y = y

p = Point(3, 4)
print(p.x, p.y)

p.z = 5  
# will return an error
# AttributeError: 'Point' object has no attribute 'z'
