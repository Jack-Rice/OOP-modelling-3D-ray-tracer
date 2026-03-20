"""
A module for creating optical elements that propagate rays through themselves.
"""

class OpticalElement:
    """
    A base class for different optical elements.
    """
    
    def propagate_ray(self, ray):
        """Propagate a ray through the optical element."""
        raise NotImplementedError()
