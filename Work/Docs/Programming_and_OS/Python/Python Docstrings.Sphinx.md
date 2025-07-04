---
tags: note/python
type: note
---

# Background
- Easy and traditional style. Created specifically for Python
- Sphinx uses the `keyword(reserved word)`; most of the programming language does. But it is explicitly called `role` in Sphinx. In the above code, Sphinx has the `param` as a role, and `type` is a role, which is the Sphinx data type for `param`. `type` role is optional, but `param` is mandatory. The return roles document the returned object. It is different from the param role. The return role is not dependent on the rtype and vice-versa. The rtype is the type of object returned from the given function.
# Usage
### Example
```python
class Vehicle(object):
    '''
    The Vehicle object contains lots of vehicles
    :param arg: The arg is used for ...
    :type arg: str
    :param `*args`: The variable arguments are used for ...
    :param `**kwargs`: The keyword arguments are used for ...
    :ivar arg: This is where we store arg
    :vartype arg: str
    '''


    def __init__(self, arg, *args, **kwargs):
        self.arg = arg

    def cars(self, distance, destination):
        '''We can't travel a certain distance in vehicles without fuels, so here's the fuels

        :param distance: The amount of distance traveled
        :type amount: int
        :param bool destinationReached: Should the fuels be refilled to cover required distance?
        :raises: :class:`RuntimeError`: Out of fuel

        :returns: A Car mileage
        :rtype: Cars
        '''  
        pass

```


