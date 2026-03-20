"""
A module for creating spherical refraction elements that propagates and
refracts rays that pass through the element.
"""
from optical_element import OpticalElement
from ray import Ray
import numpy as np

def refract_ray(k1_hat_array, n_hat_array, n1, n2):
    """RETURNS the refracted ray unit direction vector."""
    #Def terms:
    R = n1 / n2
    C = -1 * np.dot(k1_hat_array, n_hat_array)
    if C < 0:
        n_hat_array = -1 * n_hat_array
        C = -1 * np.dot(k1_hat_array, n_hat_array)
    term1 = R * k1_hat_array
    term2 = R * C
    term3 = (R*R) * (1 - (C*C))
    #Check if ray is subject to total internal reflection:
    if n2 < n1:
        n2_hat_sin_theta1_opps = np.cross(k1_hat_array, n_hat_array)
        sin_theta1_opps = np.linalg.norm(n2_hat_sin_theta1_opps)
        if sin_theta1_opps > (n2 / n1):
            if np.abs(sin_theta1_opps - (n2/n1)) > np.finfo(float).eps:
                return None
    #Calculating refracted ray unit vector:
    k2_hat_array = term1 + (n_hat_array * (term2 - np.sqrt(1 - term3)))
    return k2_hat_array

class SphericalRefraction(OpticalElement):
    """
    A derived class (of OpticalElement) that creates spherical,
    refracting surfaces.
    """
    def __init__(self, z0_list, curv, n1, n2, aper_rad):
        if len(z0_list) != 3:
            raise Exception("Spherical Refraction parameter z0_list "\
                            "has incorrect size.")
        else:
            self._z0_list = z0_list
        self._z0 = np.array(self._z0_list)
        self._curv = curv #Can be positive or negative.
        if self._curv == 0:
            self._curv_rad = 0
        else:
            self._curv_rad = np.abs(1/(curv))
        self._n1 = n1
        self._n2 = n2
        self._aper_rad = aper_rad

    def __repr__(self):
        return f"SphericalRefraction(z0_list={self._z0_list}, " \
               f"curv={self._curv}, n1={self._n1}, n2={self._n2}, " \
               f"aper_rad={self._aper_rad})"
    
    def __str__(self):
        return f"({self._z0}, {self._curv}, {self._n1}, {self._n2}, "\
               f"{self._aper_rad})" 
        
    def intercept(self, ray):
        """
        RETURNS first valid intercept of a ray with the spherical surface.
        """
        ray_obj = ray
        k_hat = ray_obj._init_k/(np.linalg.norm(ray_obj._init_k))
        
        if self._curv >= 0:
            self._cen_curv = self._z0 + np.array([0, 0, self._curv_rad])
        elif self._curv < 0:
            self._cen_curv = self._z0 - np.array([0, 0, self._curv_rad])
        
        r = ray._init_p - self._cen_curv
        term1 = np.dot(r, k_hat)
        term2 = (np.linalg.norm(r) * np.linalg.norm(r))
        term2 -= (self._curv_rad * self._curv_rad)
        if ((term1 * term1) - term2 < 0) and (self._curv != 0):
            return None
        if self._curv != 0:
            L_plus = (-term1) + np.sqrt((term1 * term1) - term2)
            L_minus = (-term1) - np.sqrt((term1 * term1) - term2)       
        if self._curv == 0:
            L_sol = (self._cen_curv[2] - ray._init_p[2]) / k_hat[2]
        elif self._curv > 0:  
            L_sol = min([L_plus, L_minus])
        elif self._curv < 0:
            L_sol = max([L_plus, L_minus])
            
        intercept = ray_obj._init_p + (L_sol * k_hat)
        #Determining distance from intersectin to z-axis:
        if self._curv != 0:
            cen_inter_vec = intercept - self._cen_curv
            cen_z0_vec = self._z0 - self._cen_curv
            numerator = np.linalg.norm(np.cross(cen_inter_vec, cen_z0_vec))
            denominator = np.linalg.norm(cen_z0_vec)
            dist = numerator / denominator
        elif self._curv == 0:
            x_y_inter_vec = np.array([intercept[0], intercept[1]])
            dist = np.linalg.norm(x_y_inter_vec)
        if dist > self._aper_rad:
            return None
        elif dist <= self._aper_rad:
            return intercept

    def propagate_ray(self, ray):
        """
        Propagate a ray through the spherical, optical element.
        RETURNS ray (intercept appended and new refracted ray direction).
        """
        ray_obj = ray
        init_k_hat = ray_obj._init_k/(np.linalg.norm(ray_obj._init_k))
        #Calculate intercept:
        intercept = SphericalRefraction.intercept(self, ray_obj)
        if intercept is None:
            return None
        if self._curv == 0:
            lens_n_hat_array = np.array([0, 0, -1])
        if self._curv < 0:
            lens_n_array = self._cen_curv - intercept
            lens_n_hat_array = lens_n_array / (np.linalg.norm(lens_n_array))
        if self._curv > 0:
            lens_n_array = intercept - self._cen_curv
            lens_n_hat_array = lens_n_array / (np.linalg.norm(lens_n_array))
        refract_ray_hat_array = refract_ray(init_k_hat, lens_n_hat_array,
                                            self._n1, self._n2)
        if refract_ray_hat_array is None:
            return None
        Ray.ray_append(ray_obj, list(intercept), list(refract_ray_hat_array))
        refracted_ray = ray_obj
        return refracted_ray
        


























