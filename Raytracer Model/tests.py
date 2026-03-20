"""
A module testing the code (and clasees used) in the 'raytracer' module.
"""
#--------------------------Testing Ray Class:---------------------------------
import numpy as np
import ray

temp_ray1 = ray.Ray([1,2,3],[5,10,15])
#Type 'temp_ray1' in console for precise representation:
#Ray(init_plist=[1, 2, 3], init_klist=[5, 10, 15], vertslist=[[1,2,3]])
print(temp_ray1) #For casual representation.

#Want to make sure from precise representation can gain SAME value ray object:
temp_ray2 = ray.Ray(init_plist=[1, 2, 3], init_klist=[5, 10, 15],
                    vertslist=[[1,2,3]])
print(temp_ray2) #For casual representation.

#Testing access methods:
#Remember nested list.
temp_ray3 = ray.Ray([1,2,3],[5,10,15],[[-9,-18,-27],[-4,-8,-12]])
print(f'\nRay 3: {temp_ray3}')
print(f'The current position of ray 3: {temp_ray3.p()}')
print(f'The current direction of ray 3: {temp_ray3.k()}')
print(f'The points travelled by ray 3: {temp_ray3.vertices()}')

#Testing modifier method(s):
temp_ray4 = ray.Ray([30,31,32],[4,5,6],[[26,26,26]])
print(f"\nRay 4: {temp_ray4}")
temp_ray4.ray_append([34,35,38],[8,10,12])
print(f"Appended Ray 4: {temp_ray4}")
print(f'The current position of ray 4: {temp_ray4.p()}')
print(f'The current direction of ray 4: {temp_ray4.k()}')
print(f'The points travelled by ray 4: {temp_ray4.vertices()}')

temp_ray5 = ray.Ray([10,20,30],[1,2,3],[[9,18,27]])
print(f"\nRay 5: {temp_ray5}")
print(f'The current direction of ray 5: {temp_ray5.k()}')
temp_ray5.set_k([1,1,1])
print(f"\nThe new ray 5: {temp_ray5}")
print(f'The current direction of ray 5: {temp_ray5.k()}')

temp_ray6 = temp_ray5.copy()
print(f'\nRay 6, a copy of ray 5: {temp_ray6}')
print(f'Is ray 6 stored as ray 5: {temp_ray6 is temp_ray5}.')
#%%---------------------------------------------------------------------------
#-------------------Testing SphericalRefracton Class:-------------------------
from spherical_refraction import SphericalRefraction

temp_spher_lens1 = SphericalRefraction([-5,2,0], 0.1, 1, 0.4, 5)
#Type 'temp_spher_lens1' in console for precise representation:
#SphericalRefraction(z0_list=[-5, 2, 0], curv=0.1, n1=1, n2=0.4, aper_rad=5)
print(f'\ntemp_spher_lens1: {temp_spher_lens1}') #For casual representation.

#Testing interception of rays:
#Positive curavature, dist < aperture radius, suitable ray direc. and pos.:
temp_spher_lens2 = SphericalRefraction([0.0 ,0.0 ,4.0], 0.5, 1.0, 1.0, 2.0)
print(f'\ntemp_spher_lens2: {temp_spher_lens2}')
temp_ray7 = ray.Ray([0.0, 0.0, 2.0], [3.0, 0.0, 10.0])
print(f'Ray 7: {temp_ray7}')
intercept = temp_spher_lens2.intercept(temp_ray7)
print(f'The intercept of ray 7 wtih spherical lens 2: {intercept}')
#Correct.

#Positive curavature, dist = aperture radius, suitable ray direc. and pos.:
temp_spher_lens3 = SphericalRefraction([0.0 ,0.0 ,4.0], 0.5, 1.0, 1.0,
                                       0.6306053)
print(f'\ntemp_spher_lens3: {temp_spher_lens3}')
intercept = temp_spher_lens3.intercept(temp_ray7)
print(f'The intercept of ray 7 wtih spherical lens 3: {intercept}')
#Correct.

#Positive curavature, dist > aperture radius, suitable ray direc. and pos.:
temp_spher_lens4 = SphericalRefraction([0.0 ,0.0 ,4.0], 0.5, 1.0, 1.0,
                                       0.1)
print(f'\ntemp_spher_lens4: {temp_spher_lens4}')
intercept = temp_spher_lens4.intercept(temp_ray7)
print(f'The intercept of ray 7 wtih spherical lens 4: {intercept}')
#Correct.

#Negative curavature, dist < aperture radius, suitable ray direc. and pos.:
temp_spher_lens5 = SphericalRefraction([0.0 ,0.0 ,8.0], -0.5, 1.0, 1.0, 2.0)
print(f'\ntemp_spher_lens5: {temp_spher_lens5}')
intercept = temp_spher_lens5.intercept(temp_ray7)
print(f'The intercept of ray 7 wtih spherical lens 5: {intercept}')
#Correct.

#Negative curavature, dist = aperture radius, suitable ray direc. and pos.:
aper_rad_temp = intercept[0]
temp_spher_lens6 = SphericalRefraction([0.0 ,0.0 ,8.0], -0.5, 1.0, 1.0,
                                       aper_rad_temp)
print(f'\ntemp_spher_lens6: {temp_spher_lens6}')
intercept = temp_spher_lens6.intercept(temp_ray7)
print(f'The intercept of ray 7 wtih spherical lens 6: {intercept}')
#Correct.

#Negative curavature, dist > aperture radius, suitable ray direc. and pos.:
temp_spher_lens7 = SphericalRefraction([0.0 ,0.0 ,8.0], -0.5, 1.0, 1.0,
                                       aper_rad_temp-1)
print(f'\ntemp_spher_lens7: {temp_spher_lens7}')
intercept = temp_spher_lens7.intercept(temp_ray7)
print(f'The intercept of ray 7 wtih spherical lens 7: {intercept}')
#Correct.

#Positive curavature, dist < aperture radius, suitable ray direc. and pos.:
temp_spher_lens8 = SphericalRefraction([0.0 ,0.0 ,4.0], 0.5, 1.0, 1.0, 2.0)
print(f'\ntemp_spher_lens8: {temp_spher_lens8}')
temp_ray8 = ray.Ray([0.0, 0.0, 0.0], [0.0, 1.0, 3.0])
print(f'Ray 8: {temp_ray8}')
intercept = temp_spher_lens8.intercept(temp_ray8)
print(f'The intercept of ray 8 wtih spherical lens 8: {intercept}')
#Correct.

#Positive curavature, dist < aperture radius, suitable ray direc. and pos.:
#One intercept:
temp_spher_lens9 = SphericalRefraction([0.0 ,0.0 ,4.0], 0.5, 1.0, 1.0, 2.0)
print(f'\ntemp_spher_lens9: {temp_spher_lens9}')
temp_ray9 = ray.Ray([0.0, 0.0, 0.0], [0.0, np.sqrt(2), 4.0])
print(f'Ray 9: {temp_ray9}')
intercept = temp_spher_lens9.intercept(temp_ray9)
print(f'The intercept of ray 9 wtih spherical lens 9: {intercept}')
#Correct.

#Positive curavature, dist ? aperture radius, suitable ray direc. and pos.:
#No intercept:
print(f'\ntemp_spher_lens10: {temp_spher_lens9}')
temp_ray10 = ray.Ray([0.0, 0.0, 0.0], [0.0, 2*np.sqrt(2), 4.0])
print(f'Ray 10: {temp_ray10}')
intercept = temp_spher_lens9.intercept(temp_ray10)
print(f'The intercept of ray 10 wtih spherical lens 9: {intercept}')
#Correct.

#No curvature, dis < aperture radius, suitable ray direc. and pos.:
temp_spher_lens11 = SphericalRefraction([0.0 ,0.0 ,6.0], 0, 1.0, 1.0, 2.0)
print(f'\ntemp_spher_lens11: {temp_spher_lens11}')
temp_ray11 = ray.Ray([0.0, 0.0, 0.0], [1.0, 0.0, 6.0])
print(f'Ray 11: {temp_ray11}')
intercept = temp_spher_lens11.intercept(temp_ray11)
print(f'The intercept of ray 11 wtih spherical lens 11: {intercept}')
#Correct.

#No curvature, dis = aperture radius, suitable ray direc. and pos.:
temp_spher_lens12 = SphericalRefraction([0.0 ,0.0 ,6.0], 0, 1.0, 1.0, 1.0)
print(f'\ntemp_spher_lens12: {temp_spher_lens12}')
temp_ray11 = ray.Ray([0.0, 0.0, 0.0], [1.0, 0.0, 6.0])
print(f'Ray 11: {temp_ray11}')
intercept = temp_spher_lens12.intercept(temp_ray11)
print(f'The intercept of ray 11 wtih spherical lens 12: {intercept}')
#Correct.

#No curvature, dis > aperture radius, suitable ray direc. and pos.:
temp_spher_lens13 = SphericalRefraction([0.0 ,0.0 ,6.0], 0, 1.0, 1.0, 0.5)
print(f'\ntemp_spher_lens13: {temp_spher_lens13}')
temp_ray11 = ray.Ray([0.0, 0.0, 0.0], [1.0, 0.0, 6.0])
print(f'Ray 11: {temp_ray11}')
intercept = temp_spher_lens13.intercept(temp_ray11)
print(f'The intercept of ray 11 wtih spherical lens 13: {intercept}')
#Correct.

#No curvature, dis ? aperture radius, suitable ray direc. and pos.:
temp_spher_lens14 = SphericalRefraction([0.0 ,0.0 ,6.0], 0, 1.0, 1.0, 2.0)
print(f'\ntemp_spher_lens14: {temp_spher_lens14}')
temp_ray14 = ray.Ray([2.0, -2.0, 3.0], [-1.0, 3.0, 3.0])
print(f'Ray 14: {temp_ray14}')
intercept = temp_spher_lens14.intercept(temp_ray14)
print(f'The intercept of ray 14 wtih spherical lens 14: {intercept}')
#Correct.

#No curvature, dis = aperture radius, suitable ray direc. and pos.:
temp_spher_lens15 = SphericalRefraction([0.0 ,0.0 ,6.0], 0, 1.0, 1.0,
                                        np.sqrt(2))
print(f'\ntemp_spher_lens15: {temp_spher_lens15}')
temp_ray15 = ray.Ray([2.0, -2.0, 3.0], [-1.0, 3.0, 3.0])
print(f'Ray 15: {temp_ray15}')
intercept = temp_spher_lens15.intercept(temp_ray15)
print(f'The intercept of ray 15 wtih spherical lens 15: {intercept}')
#Correct.

#No curvature, dis > aperture radius, suitable ray direc. and pos.:
temp_spher_lens16 = SphericalRefraction([0.0 ,0.0 ,6.0], 0, 1.0, 1.0,
                                        np.sqrt(2) - 1)
print(f'\ntemp_spher_lens16: {temp_spher_lens16}')
temp_ray16 = ray.Ray([2.0, -2.0, 3.0], [-1.0, 3.0, 3.0])
print(f'Ray 16: {temp_ray16}')
intercept = temp_spher_lens16.intercept(temp_ray16)
print(f'The intercept of ray 16 wtih spherical lens 16: {intercept}')
#%%---------------------------------------------------------------------------
#----------------------Testing refract_ray Function:--------------------------
print('\n----------------Testing refract_ray Function:-----------------------')
from spherical_refraction import refract_ray
#Surface with normal of -ve unit z direction and crit angle used (1):
n_hat_array = np.array([0.0, 0.0, -1.0])
n1 = 1.5
n2 = 1.0
crit_angle = np.arcsin(n2 / n1)
k1_hat_array = np.array([np.abs(np.cos((np.pi/2) - crit_angle)), 0.0,
                         np.abs(np.sin((np.pi/2) - crit_angle))])

k2_hat_array = refract_ray(k1_hat_array, n_hat_array, n1, n2)
print(f'\nThe unit refracted ray direction (1): {k2_hat_array}')
#Correct; had to incorporate np.finfo(float).eps inequality.
#Check if in same plane:
dot_cross_prod = np.dot(k1_hat_array, np.cross(k2_hat_array, n_hat_array))
print(f'The vector dot-cross product value: {dot_cross_prod}')
#Refracted ray is in the same plane as the incident ray and the surface normal.

#Surface with normal of -ve unit z direction and n2 > n1 (2):
n_hat_array = np.array([0.0, 0.0, -1.0])
n1 = 1.0
n2 = 1.2
theta1 = np.arcsin(1.2 * np.sin(np.pi/4))
k1_hat_array = np.array([np.abs(np.cos((np.pi/2) - theta1)), 0.0,
                         np.abs(np.sin((np.pi/2) - theta1))])

k2_hat_array = refract_ray(k1_hat_array, n_hat_array, n1, n2)
print(f'\nThe unit refracted ray direction (2): {k2_hat_array}')
#Correct.
dot_cross_prod = np.dot(k1_hat_array, np.cross(k2_hat_array, n_hat_array))
print(f'The vector dot-cross product value: {dot_cross_prod}')
#Correct.

#Surface with normal of -ve unit z direction and n2 > n1 (3):
n_hat_array = np.array([0.0, 0.0, -1.0])
n1 = 1.0
n2 = 1.2
theta1 = np.arcsin(1.2 * np.sin(np.pi/4))
k1_hat_array = np.array([np.pi/4, 1.0, np.pi/4])

k2_hat_array = refract_ray(k1_hat_array, n_hat_array, n1, n2)
print(f'\nThe unit refracted ray direction (3): {k2_hat_array}')
dot_cross_prod = np.dot(k1_hat_array, np.cross(k2_hat_array, n_hat_array))
print(f'The vector dot-cross product value: {dot_cross_prod}')
#Correct.

#Surface with normal of +ve unit z direction and crit angle used (4):
n_hat_array = np.array([0.0, 0.0, 1.0])
n1 = 1.5
n2 = 1.0
crit_angle = np.arcsin(n2 / n1)
k1_hat_array = np.array([np.abs(np.cos((np.pi/2) - crit_angle)), 0.0,
                         np.abs(np.sin((np.pi/2) - crit_angle))])

k2_hat_array = refract_ray(k1_hat_array, n_hat_array, n1, n2)
print(f'\nThe unit refracted ray direction (4): {k2_hat_array}')
#Correct.
dot_cross_prod = np.dot(k1_hat_array, np.cross(k2_hat_array, n_hat_array))
print(f'The vector dot-cross product value: {dot_cross_prod}')
#Correct.

#Surface with normal of +ve unit z direction and n2 > n1 (5):
n_hat_array = np.array([0.0, 0.0, 1.0])
n1 = 1.0
n2 = 1.2
theta1 = np.arcsin(1.2 * np.sin(np.pi/4))
k1_hat_array = np.array([np.pi/4, 1.0, np.pi/4])

k2_hat_array = refract_ray(k1_hat_array, n_hat_array, n1, n2)
print(f'\nThe unit refracted ray direction (5): {k2_hat_array}')
dot_cross_prod = np.dot(k1_hat_array, np.cross(k2_hat_array, n_hat_array))
print(f'The vector dot-cross product value: {dot_cross_prod}')
#Correct.
#%%---------------------------------------------------------------------------
#---------------------Testing propagate_ray Function:-------------------------
print('\n--------------Testing propagate_ray Function:-----------------------')

#Positive curavature, dist < aperture radius, suitable ray direc. and pos.:
temp_spher_lens2 = SphericalRefraction([0.0 ,0.0 ,4.0], 0.5, 1.0, 1.1, 2.0)
print(f'\ntemp_spher_lens2: {temp_spher_lens2}')
temp_ray7 = ray.Ray([0.0, 0.0, 2.0], [3.0, 0.0, 10.0])
print(f'Ray 7 before intercept and refraction: {temp_ray7}')
intercept = temp_spher_lens2.intercept(temp_ray7)
print(f'The intercept of ray 7 wtih spherical lens 2: {intercept}')

temp_ray7_refracted = temp_spher_lens2.propagate_ray(temp_ray7)
print(f'\nRay 7 after intercept and refraction: {temp_ray7_refracted}')

#No curvature, dist < aperture radius, suitable ray direc. and pos.:
n1 = 1.5
n2 = 1.0
crit_angle = np.arcsin(n2 / n1)
k1_hat_array = np.array([np.abs(np.cos((np.pi/2) - crit_angle)), 0.0,
                         np.abs(np.sin((np.pi/2) - crit_angle))])

temp_spher_lens3 = SphericalRefraction([0.0 ,0.0 ,0.0], 0.0, 1.5, 1.0, 2.0)
print(f'\ntemp_spher_lens3: {temp_spher_lens3}')
temp_ray3 = ray.Ray(list(-1*k1_hat_array), list(k1_hat_array))
print(f'Ray 3 before intercept and refraction: {temp_ray3}')
intercept = temp_spher_lens3.intercept(temp_ray3)
print(f'The intercept of ray 3 wtih spherical lens 3: {intercept}')

temp_ray3_refracted = temp_spher_lens3.propagate_ray(temp_ray3)
print(f'\nRay 3 after intercept and refraction: {temp_ray3_refracted}')
#Correct.

#Negative curavature, dist < aperture radius, suitable ray direc. and pos.:
temp_spher_lens5 = SphericalRefraction([0.0 ,0.0 ,8.0], -0.5, 1.0, 1.0, 2.0)
print(f'\ntemp_spher_lens5: {temp_spher_lens5}')
temp_ray7 = ray.Ray([0.0, 0.0, 2.0], [3.0, 0.0, 10.0])
print(f'Ray 7 before intercept and refraction: {temp_ray7}')
intercept = temp_spher_lens5.intercept(temp_ray7)
print(f'The intercept of ray 7 wtih spherical lens 5: {intercept}')

temp_ray7_refracted = temp_spher_lens5.propagate_ray(temp_ray7)
print(f'\nRay 7 after intercept and refraction: {temp_ray7_refracted}')
#Correct.

#Positive curavature, dist ? aperture radius, suitable ray direc. and pos.:
#No intercept:
temp_spher_lens10 = SphericalRefraction([0.0 ,0.0 ,4.0], 0.5, 1.0, 1.0, 2.0)
print(f'\ntemp_spher_lens10: {temp_spher_lens10}')
temp_ray10 = ray.Ray([0.0, 0.0, 0.0], [0.0, 2*np.sqrt(2), 4.0])
print(f'Ray 10: {temp_ray10}')
intercept = temp_spher_lens10.intercept(temp_ray10)
print(f'The intercept of ray 10 wtih spherical lens 10: {intercept}')

temp_ray10_refracted = temp_spher_lens10.propagate_ray(temp_ray10)
print(f'\nRay 10 after no intercept: {temp_ray10_refracted}')
#Made unrefracted ray None.

#No curvature, dis > aperture radius, suitable ray direc. and pos.:
temp_spher_lens13 = SphericalRefraction([0.0 ,0.0 ,6.0], 0, 1.0, 1.0, 0.5)
print(f'\ntemp_spher_lens13: {temp_spher_lens13}')
temp_ray11 = ray.Ray([0.0, 0.0, 0.0], [1.0, 0.0, 6.0])
print(f'Ray 11: {temp_ray11}')
intercept = temp_spher_lens13.intercept(temp_ray11)
print(f'The intercept of ray 11 wtih spherical lens 13: {intercept}')

temp_ray11_refracted = temp_spher_lens13.propagate_ray(temp_ray11)
print(f'\nRay 11 after no intercept: {temp_ray11_refracted}')

#No curvature, dist < aperture radius, suitable ray direc. and pos.:
#Total internal reflection:
n1 = 1.5
n2 = 1.0
crit_angle = np.arcsin(n2 / n1)
k1_hat_array = np.array([np.abs(np.cos((np.pi/2) - crit_angle)), 0.0,
                         np.abs(np.sin((np.pi/2) - crit_angle))])

temp_spher_lens3 = SphericalRefraction([0.0 ,0.0 ,0.0], 0.0, 1.7, 1.0, 2.0)
print(f'\ntemp_spher_lens3: {temp_spher_lens3}')
temp_ray3 = ray.Ray(list(-1*k1_hat_array), list(k1_hat_array))
print(f'Ray 3 before intercept and refraction: {temp_ray3}')
intercept = temp_spher_lens3.intercept(temp_ray3)
print(f'The intercept of ray 3 wtih spherical lens 3: {intercept}')

temp_ray3_refracted = temp_spher_lens3.propagate_ray(temp_ray3)
print(f'\nRay 3 after intercept and internally reflected:'
      f' {temp_ray3_refracted}')
#Retruned reflected ray as None.
#%%---------------------------------------------------------------------------
#------------------------Testing OutPlane Class:------------------------------
import output_plane

#----------------------Testing intercept Function:----------------------------
print('\n--------------Testing intercept Function:--------------------------')
#Ray with single nested list in vertslist that will intercept:
temp_ray1 = ray.Ray([2.0,0.0,0.0],[0.0,0.0,1.0])
output_plane1 = output_plane.OutputPlane(4)
intercept = output_plane1.intercept(temp_ray1)
print(f'{intercept}')
#Correct.

#Ray with single nested list in vertslist that will intercept:
temp_ray1 = ray.Ray([2.0,0.0,0.0],[7.0,5.0,1.0])
output_plane1 = output_plane.OutputPlane(4)
intercept = output_plane1.intercept(temp_ray1)
print(f'{intercept}')
#Correct.

#Ray with nested lists in vertslist that will intercept:
temp_ray1 = ray.Ray([2.0,0.0,0.0],[0.0,0.0,1.0], [[1,2,3],[4,5,6]])
output_plane1 = output_plane.OutputPlane(4)
intercept = output_plane1.intercept(temp_ray1)
print(f'{intercept}')
#Correct.

#Ray with nested lists in vertslist that will intercept:
temp_ray1 = ray.Ray([2.0,0.0,0.0],[0.0,0.0,1.0], [[1,2,3],[4,5,6],[2,0,0]])
output_plane1 = output_plane.OutputPlane(4)
intercept = output_plane1.intercept(temp_ray1)
print(f'{intercept}')
#Correct.

#Ray with nested lists in vertslist that will not intercept:
temp_ray1 = ray.Ray([2.0,0.0,0.0],[2.0,5.0,0.0], [[1,2,3],[4,5,6],[2,0,0]])
output_plane1 = output_plane.OutputPlane(4)
intercept = output_plane1.intercept(temp_ray1)
print(f'{intercept}')
#Correct.
#%%---------------------------------------------------------------------------
#---------------------Testing propagate_ray Function:-------------------------
print('\n--------------Testing propagate_ray Function:-----------------------')

#Ray with single nested list in vertslist that will intercept:
temp_ray1 = ray.Ray([2.0,0.0,0.0],[0.0,0.0,1.0])
print(f'\nRay:{temp_ray1}')
output_plane1 = output_plane.OutputPlane(4)
print(f'Output plane: {output_plane1}')
intercept = output_plane1.intercept(temp_ray1)
print(f'Intercept: {intercept}')
intercepted_ray = output_plane1.propagate_ray(temp_ray1)
print(f'Intercepted ray: {intercepted_ray}')
#Correct.

#Ray with single nested list in vertslist that will intercept:
temp_ray1 = ray.Ray([2.0,0.0,0.0],[7.0,5.0,1.0])
print(f'\nRay:{temp_ray1}')
output_plane1 = output_plane.OutputPlane(4.0)
print(f'Output plane: {output_plane1}')
intercept = output_plane1.intercept(temp_ray1)
print(f'Intercept: {intercept}')
intercepted_ray = output_plane1.propagate_ray(temp_ray1)
print(f'Intercepted ray: {intercepted_ray}')
#Correct.

#Ray with nested lists in vertslist that will intercept:
temp_ray1 = ray.Ray([2.0,0.0,0.0],[0.0,0.0,1.0], [[1,2,3],[4,5,6]])
print(f'\nRay:{temp_ray1}')
output_plane1 = output_plane.OutputPlane(4.0)
print(f'Output plane: {output_plane1}')
intercept = output_plane1.intercept(temp_ray1)
print(f'Intercept: {intercept}')
intercepted_ray = output_plane1.propagate_ray(temp_ray1)
print(f'Intercepted ray: {intercepted_ray}')
#Correct.

#Ray with nested lists in vertslist that will intercept:
temp_ray1 = ray.Ray([2.0,0.0,0.0],[0.0,0.0,1.0], [[1,2,3],[4,5,6],[2,0,0]])
print(f'\nRay:{temp_ray1}')
output_plane1 = output_plane.OutputPlane(4.0)
print(f'Output plane: {output_plane1}')
intercept = output_plane1.intercept(temp_ray1)
print(f'Intercept: {intercept}')
intercepted_ray = output_plane1.propagate_ray(temp_ray1)
print(f'Intercepted ray: {intercepted_ray}')
#Correct.

#Ray with nested lists in vertslist that will not intercept:
temp_ray1 = ray.Ray([2.0,0.0,0.0],[2.0,5.0,0.0], [[1,2,3],[4,5,6],[2,0,0]])
print(f'\nRay:{temp_ray1}')
output_plane1 = output_plane.OutputPlane(4.0)
print(f'Output plane: {output_plane1}')
intercept = output_plane1.intercept(temp_ray1)
print(f'Intercept: {intercept}')
intercepted_ray = output_plane1.propagate_ray(temp_ray1)
print(f'Intercepted ray: {intercepted_ray}')
#Correct.
#%%---------------------------------------------------------------------------
#--------------------------General Test Cell:---------------------------------
# a = np.array([1,2,3])
# b = np.array([5,12,7])
# print(np.dot(a,b))
# print(b-a)
# print(np.linalg.norm(b))
# print(b-np.array([0,0,5]))

# print(max([5, 7]))
# print(min([5, 7]))
# print(3*b)
# print(np.cross(a,b))
# print(np.linalg.norm(np.cross(a,b)))

# temp_ray8 = ray.Ray(init_plist=[0.0, 0.0, 1.0], init_klist=[7.0, 0.0, 20.0])
# print(f'\n{temp_ray8}')
# c = np.array([2,6])
# print(np.linalg.norm(c))

# d = [[1,2,3], [4,5], [6,7,8,9]]
# print(d[2][1])

# e = [[1,2,3]]
# print(e[-1])








