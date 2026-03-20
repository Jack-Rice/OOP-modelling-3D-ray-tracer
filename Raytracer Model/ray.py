"""
A module for making and using optical rays (used in geometric optics).
"""
import numpy as np

class Ray():
    """
    A class of optical rays (used in geometric optics).
    """
    def __init__(self, init_plist = [0, 0, 0], init_klist = [0, 0, 0],
                 vertslist = []):
        if len(init_plist) != 3:
            raise Exception("Ray parameter init_plist has incorrect size.")
        elif len(init_klist) != 3:
            raise Exception("Ray parameter init_dlist has incorrect size.")
        else:
            #Setting vertices list:
            if init_plist in vertslist:
                self._vertslist = vertslist
            else:
                new_vertslist = vertslist.copy()
                new_vertslist.append(init_plist)
                self._vertslist = new_vertslist
            #Setting initial pos. data attributes as arrays:
            self._init_plist = init_plist
            init_p = np.array(init_plist)
            self._init_p = init_p
            #Setting initial dir. data attributes as arrays:
            self._init_klist = init_klist
            init_k = np.array(init_klist)
            self._init_k = init_k
    
    def __repr__(self):
        return f"Ray(init_plist={self._init_plist}, " \
               f"init_klist={self._init_klist}, " \
               f"vertslist={self._vertslist})"
    
    def __str__(self):
        return f"({self._init_p}, {self._init_k}, {self._vertslist})"
    
#                  ------Ray Class Access Mehtods:------  
    def p(self):
        """Returns CURRENT point/position (p) of the ray."""
        curr_p_array = np.array(self._vertslist[-1])
        return curr_p_array
                                                            
    def k(self):
        """Returns CURRENT direction (k) of the ray."""
        return self._init_k
    
    def vertices(self):
        """Returns ALL the points travelled by the ray."""
        return self._vertslist

#               ------Ray Class Modifier Mehtod(s):------  
    def ray_append(self, p, k): #Both as lists. (Can't call 'append()'.)
        """APPEND new position and CHANGE CURRENT direction of ray."""
        if len(p) != 3:
            raise Exception("ray_append parameter p has incorrect size.")
        elif len(k) != 3:
            raise Exception("ray_append parameter k has incorrect size.")
        else:
            temp = self._vertslist
            temp.append(p)
            self._vertslist = temp
            self._init_k = np.array(k)
            self._init_klist = k
        
    def set_k(self, new_k): #Takes k as a list.
        """Sets a NEW direction of the ray."""
        if len(new_k) != 3:
            raise Exception("Ray parameter k has incorrect size.")
        else:
            self._init_klist = new_k
            self._init_k = np.array(new_k)
                                                             
    def copy(self):
        """Returns a copy of the inputted ray."""
        return Ray(self._init_plist, self._init_klist, self._vertslist)
    
    
    


    
    
    
    
    
    
    
    