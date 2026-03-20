"""
A module for output plane elements that propagates ray to plane where no
refraction takes place.
"""
from optical_element import OpticalElement
from ray import Ray
import numpy as np

class OutputPlane(OpticalElement):
    """
    A derived class (of OpticalElement) that creates an output plane.
    """
    def __init__(self, z_value):
        self._z_value = z_value
        
    def __repr__(self):
        return f"OutputPlane(z_value={self._z_value})"
    
    def __str__(self):
        return f"z_value = {self._z_value}"
    
    def intercept(self, ray):
        """
        RETURNS any valid intercept of a ray with the output plane.
        """
        ray_obj = ray
        k_hat = ray_obj._init_k/(np.linalg.norm(ray_obj._init_k))
        if k_hat[2] == 0:
            return None
        L_sol = (self._z_value - ray_obj._vertslist[-1][2]) / k_hat[2]
        intercept = np.array(ray_obj._vertslist[-1]) + (L_sol * k_hat)
        return intercept
        
    def propagate_ray(self, ray):
        """
        Propagate a ray from the spherical, optical element.
        RETURNS intercepted ray.
        """
        ray_obj = ray
        #Calculate intercept:
        intercept = OutputPlane.intercept(self, ray_obj)
        if intercept is None:
            return None
        Ray.ray_append(ray_obj, list(intercept), list(ray_obj._init_klist))
        intercepted_ray = ray_obj
        return intercepted_ray
        
        