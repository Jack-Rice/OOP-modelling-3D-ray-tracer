"""
OOP code for a simple 3-D optical ray tracer that models the behaviour of some
simple optical systems (using geometric optics).
"""
from ray import Ray
from spherical_refraction import SphericalRefraction
from output_plane import OutputPlane
import numpy as np
import matplotlib.pyplot as plt
#-----------------------------------------------------------------------------
#%%----------------Spherical Aberration Demonstration:------------------------
#Spherical lens:
spher_lens_t9 = SphericalRefraction([0, 0, 100], 0.03, 1.0, 1.5, 1/0.03)
#Output plane:
out_plane_t9 = OutputPlane(250)    

#Tested rays:
#Near optical axis and no angle to optical axis:
ray1_t9 = Ray([0.1, 0.0, 0.0], [0.0, 0.0, 1.0]) #+ve close to optical axis
ray2_t9 = Ray([0.0, 0.0, 0.0], [0.0, 0.0, 1.0]) #On optical axis
ray3_t9 = Ray([-0.3, 0.0, 0.0], [0.0, 0.0, 1.0]) #-ve far from optical axis
ray4_t9 = Ray([-0.1, 0.0, 0.0], [0.025, 0.0, 100]) #-ve near OA, small angle
ray5_t9 = Ray([0.4, 0.0, 0.0], [-0.05, 0.0, 100]) #+ve far OA, large angle


#Refracting and propagating ray 1 to output plane:
ray1_t9_refracted = spher_lens_t9.propagate_ray(ray1_t9) 
ray1_t9_out_plane = out_plane_t9.propagate_ray(ray1_t9_refracted)
ray1_t9_lists = ray1_t9_out_plane._vertslist
ray1_t9_z_vals_list = []
ray1_t9_x_vals_list = []
for list_obj in ray1_t9_lists:
    z_val = list_obj[2]
    ray1_t9_z_vals_list.append(z_val)
    x_val = list_obj[0]
    ray1_t9_x_vals_list.append(x_val)
ray1_t9_z_vals_array = np.array(ray1_t9_z_vals_list)
ray1_t9_x_vals_array = np.array(ray1_t9_x_vals_list)

#Refracting and propagating ray 2 to output plane:
ray2_t9_refracted = spher_lens_t9.propagate_ray(ray2_t9) 
ray2_t9_out_plane = out_plane_t9.propagate_ray(ray2_t9_refracted)
ray2_t9_lists = ray2_t9_out_plane._vertslist
ray2_t9_z_vals_list = []
ray2_t9_x_vals_list = []
for list_obj in ray2_t9_lists:
    z_val = list_obj[2]
    ray2_t9_z_vals_list.append(z_val)
    x_val = list_obj[0]
    ray2_t9_x_vals_list.append(x_val)
ray2_t9_z_vals_array = np.array(ray2_t9_z_vals_list)
ray2_t9_x_vals_array = np.array(ray2_t9_x_vals_list)

#Refracting and propagating ray 3 to output plane:
ray3_t9_refracted = spher_lens_t9.propagate_ray(ray3_t9) 
ray3_t9_out_plane = out_plane_t9.propagate_ray(ray3_t9_refracted)
ray3_t9_lists = ray3_t9_out_plane._vertslist
ray3_t9_z_vals_list = []
ray3_t9_x_vals_list = []
for list_obj in ray3_t9_lists:
    z_val = list_obj[2]
    ray3_t9_z_vals_list.append(z_val)
    x_val = list_obj[0]
    ray3_t9_x_vals_list.append(x_val)
ray3_t9_z_vals_array = np.array(ray3_t9_z_vals_list)
ray3_t9_x_vals_array = np.array(ray3_t9_x_vals_list)

#Refracting and propagating ray 4 to output plane:
ray4_t9_refracted = spher_lens_t9.propagate_ray(ray4_t9) 
ray4_t9_out_plane = out_plane_t9.propagate_ray(ray4_t9_refracted)
ray4_t9_lists = ray4_t9_out_plane._vertslist
ray4_t9_z_vals_list = []
ray4_t9_x_vals_list = []
for list_obj in ray4_t9_lists:
    z_val = list_obj[2]
    ray4_t9_z_vals_list.append(z_val)
    x_val = list_obj[0]
    ray4_t9_x_vals_list.append(x_val)
ray4_t9_z_vals_array = np.array(ray4_t9_z_vals_list)
ray4_t9_x_vals_array = np.array(ray4_t9_x_vals_list)

#Refracting and propagating ray 5 to output plane:
ray5_t9_refracted = spher_lens_t9.propagate_ray(ray5_t9) 
ray5_t9_out_plane = out_plane_t9.propagate_ray(ray5_t9_refracted)
ray5_t9_lists = ray5_t9_out_plane._vertslist
ray5_t9_z_vals_list = []
ray5_t9_x_vals_list = []
for list_obj in ray5_t9_lists:
    z_val = list_obj[2]
    ray5_t9_z_vals_list.append(z_val)
    x_val = list_obj[0]
    ray5_t9_x_vals_list.append(x_val)
ray5_t9_z_vals_array = np.array(ray5_t9_z_vals_list)
ray5_t9_x_vals_array = np.array(ray5_t9_x_vals_list)

#Plotting rays:
plt.plot(ray1_t9_z_vals_array, ray1_t9_x_vals_array, color='blue')
plt.plot(ray2_t9_z_vals_array, ray2_t9_x_vals_array, color='blue')
plt.plot(ray3_t9_z_vals_array, ray3_t9_x_vals_array, color='blue')
plt.plot(ray4_t9_z_vals_array, ray4_t9_x_vals_array, color='red')
plt.plot(ray5_t9_z_vals_array, ray5_t9_x_vals_array, color='red')
plt.grid(color='black', linestyle='-', linewidth=0.5)
plt.xlabel('z (mm)')
plt.ylabel('x (mm)')
plt.xticks(np.arange(0, 275+1, 25))
plt.yticks(np.arange(-0.5, 0.5+.01, 0.1))
plt.xlim(0,275)
plt.ylim(-0.5,0.5)
#plt.savefig("spherical_aberration_plot.png",dpi=300)
plt.show()
#-----------------------------------------------------------------------------
#%%---------------------------Parallel Rays:----------------------------------
#Spherical lens:
spher_lens_t9 = SphericalRefraction([0, 0, 100], 0.03, 1.0, 1.5, 1/0.03)
para_focus = (1.5 * (1/0.03)) / (1.5 - 1)
#Output plane:
out_plane_t9 = OutputPlane(100 + para_focus)    

#Tested rays:
#Near optical axis and no angle to optical axis:
ray1_t9 = Ray([0.1, 0.0, 0.0], [0.0, 0.0, 1.0]) 
ray2_t9 = Ray([-0.1, 0.0, 0.0], [0.0, 0.0, 1.0]) 
ray3_t9 = Ray([0.0, 0.0, 0.0], [0.0, 0.0, 1.0]) 
ray4_t9 = Ray([0.05, 0.0, 0.0], [0.0, 0.0, 1.0])
ray5_t9 = Ray([-0.05, 0.0, 0.0], [0.0, 0.0, 1.0]) 


#Refracting and propagating ray 1 to output plane:
ray1_t9_refracted = spher_lens_t9.propagate_ray(ray1_t9) 
ray1_t9_out_plane = out_plane_t9.propagate_ray(ray1_t9_refracted)
ray1_t9_lists = ray1_t9_out_plane._vertslist
ray1_t9_z_vals_list = []
ray1_t9_x_vals_list = []
for list_obj in ray1_t9_lists:
    z_val = list_obj[2]
    ray1_t9_z_vals_list.append(z_val)
    x_val = list_obj[0]
    ray1_t9_x_vals_list.append(x_val)
ray1_t9_z_vals_array = np.array(ray1_t9_z_vals_list)
ray1_t9_x_vals_array = np.array(ray1_t9_x_vals_list)

#Refracting and propagating ray 2 to output plane:
ray2_t9_refracted = spher_lens_t9.propagate_ray(ray2_t9) 
ray2_t9_out_plane = out_plane_t9.propagate_ray(ray2_t9_refracted)
ray2_t9_lists = ray2_t9_out_plane._vertslist
ray2_t9_z_vals_list = []
ray2_t9_x_vals_list = []
for list_obj in ray2_t9_lists:
    z_val = list_obj[2]
    ray2_t9_z_vals_list.append(z_val)
    x_val = list_obj[0]
    ray2_t9_x_vals_list.append(x_val)
ray2_t9_z_vals_array = np.array(ray2_t9_z_vals_list)
ray2_t9_x_vals_array = np.array(ray2_t9_x_vals_list)

#Refracting and propagating ray 3 to output plane:
ray3_t9_refracted = spher_lens_t9.propagate_ray(ray3_t9) 
ray3_t9_out_plane = out_plane_t9.propagate_ray(ray3_t9_refracted)
ray3_t9_lists = ray3_t9_out_plane._vertslist
ray3_t9_z_vals_list = []
ray3_t9_x_vals_list = []
for list_obj in ray3_t9_lists:
    z_val = list_obj[2]
    ray3_t9_z_vals_list.append(z_val)
    x_val = list_obj[0]
    ray3_t9_x_vals_list.append(x_val)
ray3_t9_z_vals_array = np.array(ray3_t9_z_vals_list)
ray3_t9_x_vals_array = np.array(ray3_t9_x_vals_list)

#Refracting and propagating ray 4 to output plane:
ray4_t9_refracted = spher_lens_t9.propagate_ray(ray4_t9) 
ray4_t9_out_plane = out_plane_t9.propagate_ray(ray4_t9_refracted)
ray4_t9_lists = ray4_t9_out_plane._vertslist
ray4_t9_z_vals_list = []
ray4_t9_x_vals_list = []
for list_obj in ray4_t9_lists:
    z_val = list_obj[2]
    ray4_t9_z_vals_list.append(z_val)
    x_val = list_obj[0]
    ray4_t9_x_vals_list.append(x_val)
ray4_t9_z_vals_array = np.array(ray4_t9_z_vals_list)
ray4_t9_x_vals_array = np.array(ray4_t9_x_vals_list)

#Refracting and propagating ray 5 to output plane:
ray5_t9_refracted = spher_lens_t9.propagate_ray(ray5_t9) 
ray5_t9_out_plane = out_plane_t9.propagate_ray(ray5_t9_refracted)
ray5_t9_lists = ray5_t9_out_plane._vertslist
ray5_t9_z_vals_list = []
ray5_t9_x_vals_list = []
for list_obj in ray5_t9_lists:
    z_val = list_obj[2]
    ray5_t9_z_vals_list.append(z_val)
    x_val = list_obj[0]
    ray5_t9_x_vals_list.append(x_val)
ray5_t9_z_vals_array = np.array(ray5_t9_z_vals_list)
ray5_t9_x_vals_array = np.array(ray5_t9_x_vals_list)

#Plotting rays:
plt.plot(ray1_t9_z_vals_array, ray1_t9_x_vals_array, color='red')
plt.plot(ray2_t9_z_vals_array, ray2_t9_x_vals_array, color='red')
plt.plot(ray3_t9_z_vals_array, ray3_t9_x_vals_array, color='red')
plt.plot(ray4_t9_z_vals_array, ray4_t9_x_vals_array, color='red')
plt.plot(ray5_t9_z_vals_array, ray5_t9_x_vals_array, color='red')
plt.grid(color='black', linestyle='-', linewidth=0.5)
plt.xlabel('z (mm)')
plt.ylabel('x (mm)')
plt.xticks(np.arange(0, 225+1, 25))
plt.yticks(np.arange(-0.2, 0.2+.005, 0.05))
plt.xlim(0,225)
plt.ylim(-0.2,0.2)
#plt.savefig("parallel_rays_plot.png",dpi=300)
plt.show()
print(f'Paraxial focus: {para_focus} mm.')
#-----------------------------------------------------------------------------
#%%--------------------Magnification and Inversion:---------------------------
#Spherical lens:
spher_lens_t9 = SphericalRefraction([0, 0, 100], 0.03, 1.0, 1.5, 1/0.03)
para_focus = (1.5 * (1/0.03)) / (1.5 - 1)
#Output plane:
out_plane_t9 = OutputPlane(100 + para_focus +200)    

#Tested rays:
#Near optical axis and angle to optical axis:
ray1_t9 = Ray([0.05, 0.0, 0.0], [0.0, 0.0, 1.0]) 
ray2_t9 = Ray([0.05, 0.0, 0.0], [-0.05, 0.0, 100.0]) 

#Refracting and propagating ray 1 to output plane:
ray1_t9_refracted = spher_lens_t9.propagate_ray(ray1_t9) 
ray1_t9_out_plane = out_plane_t9.propagate_ray(ray1_t9_refracted)
ray1_t9_lists = ray1_t9_out_plane._vertslist
ray1_t9_z_vals_list = []
ray1_t9_x_vals_list = []
for list_obj in ray1_t9_lists:
    z_val = list_obj[2]
    ray1_t9_z_vals_list.append(z_val)
    x_val = list_obj[0]
    ray1_t9_x_vals_list.append(x_val)
ray1_t9_z_vals_array = np.array(ray1_t9_z_vals_list)
ray1_t9_x_vals_array = np.array(ray1_t9_x_vals_list)

#Refracting and propagating ray 2 to output plane:
ray2_t9_refracted = spher_lens_t9.propagate_ray(ray2_t9) 
ray2_t9_out_plane = out_plane_t9.propagate_ray(ray2_t9_refracted)
ray2_t9_lists = ray2_t9_out_plane._vertslist
ray2_t9_z_vals_list = []
ray2_t9_x_vals_list = []
for list_obj in ray2_t9_lists:
    z_val = list_obj[2]
    ray2_t9_z_vals_list.append(z_val)
    x_val = list_obj[0]
    ray2_t9_x_vals_list.append(x_val)
ray2_t9_z_vals_array = np.array(ray2_t9_z_vals_list)
ray2_t9_x_vals_array = np.array(ray2_t9_x_vals_list)


#Plotting rays:
plt.plot(ray1_t9_z_vals_array, ray1_t9_x_vals_array, color='red')
plt.plot(ray2_t9_z_vals_array, ray2_t9_x_vals_array, color='red')
plt.grid(color='black', linestyle='-', linewidth=0.5)
plt.xlabel('z (mm)')
plt.ylabel('x (mm)')
plt.xticks(np.arange(0, 400+1, 25))
plt.yticks(np.arange(-0.5, 0.5+.01, 0.1))
plt.xlim(0,400)
plt.ylim(-0.5,0.5)
#plt.savefig("magnification_inversion_plot.png",dpi=300)
plt.show()
print(f'Paraxial focus: {para_focus} mm.')
#-----------------------------------------------------------------------------
#%%------------------------Bundles of Rays:-----------------------------------
#Spherical lens:
spher_lens_t12 = SphericalRefraction([0, 0, 100], 0.03, 1.0, 1.5, 1/0.03)
para_focus = (1.5 * (1/0.03)) / (1.5 - 1)
#Output plane:
out_plane_t12 = OutputPlane(100 + para_focus) 

#Forming bundles of rays:

#Uniform bundle of rays parallel to the optical axis (diameter of 5 mm):
#Gaining initial points for rays (bundle 1):
bundle1_center_list = [0, 0, 0]
bundle1_init_points_list = [bundle1_center_list]
circle1_num_points = 6
num_circles = 5
r = 2.5 / num_circles

start_angle_var = (2 * np.pi) / circle1_num_points
bundle_var_rad = r

#First 2 circles:
while bundle_var_rad <= 2 * r:
    angle_var = start_angle_var
    for i in np.arange(1, circle1_num_points+1):
        new_x_val = bundle_var_rad * np.cos(angle_var)
        new_y_val = bundle_var_rad * np.sin(angle_var)
        new_point_list = [new_x_val, new_y_val, 0]
        bundle1_init_points_list.append(new_point_list)
        angle_var += start_angle_var
    circle1_num_points = 2 * circle1_num_points
    bundle_var_rad += r
    start_angle_var = start_angle_var / 2
    
#Outer 3 circles:
circle3_num_points = 18
start_angle_var = (2*np.pi) / circle3_num_points 
bundle_var_rad = 3 * r
while bundle_var_rad <= 2.5:
    angle_var = start_angle_var
    for i in np.arange(1, circle3_num_points+1):
        new_x_val = bundle_var_rad * np.cos(angle_var)
        new_y_val = bundle_var_rad * np.sin(angle_var)
        new_point_list = [new_x_val, new_y_val, 0]
        bundle1_init_points_list.append(new_point_list)
        angle_var += start_angle_var
    circle3_num_points += 6
    bundle_var_rad += r
    numerator = (start_angle_var * (circle3_num_points - 6))
    denom = circle3_num_points
    start_angle_var = numerator / denom

#Plotting initial center points (bundle 1):
x_init_bundle1_vals_list = []
y_init_bundle1_vals_list = []

for init_point in bundle1_init_points_list:
    x_init_bundle1_vals_list.append(init_point[0])
    y_init_bundle1_vals_list.append(init_point[1])

x_init_bundle1_vals_array = np.array(x_init_bundle1_vals_list)
y_init_bundle1_vals_array = np.array(y_init_bundle1_vals_list)

#plt.title('Initial positions of bundle 1 (z=0)')
plt.xlabel('x (mm)')
plt.ylabel('y (mm)')
plt.xticks(np.arange(-3.0, 3.0+0.5, 0.5))
plt.yticks(np.arange(-3.0, 3.0+0.5, 0.5))
plt.xlim(-3.0,3.0)
plt.ylim(-3.0,3.0)
plt.plot(x_init_bundle1_vals_array, y_init_bundle1_vals_array, 'bo')
#plt.savefig("parallel_bundle_initial_spot_plot.png",dpi=300)
plt.show()

#Initialising rays (bundle 1):
bundle1_rays_list = []
for init_pos_list in bundle1_init_points_list:
    ray_obj = Ray(init_pos_list, [0, 0, 1])
    bundle1_rays_list.append(ray_obj)
#Intersecting, refracting, and intersecitng ray bundle (1):
for ray_obj in bundle1_rays_list:
    ray_refracted = spher_lens_t12.propagate_ray(ray_obj) 
    ray_out_plane = out_plane_t12.propagate_ray(ray_refracted)
    ray_lists = ray_out_plane._vertslist
    ray_z_vals_list = []
    ray_x_vals_list = []
    for list_obj in ray_lists:
        z_val = list_obj[2]
        ray_z_vals_list.append(z_val)
        x_val = list_obj[0]
        ray_x_vals_list.append(x_val)
    ray_z_vals_array = np.array(ray_z_vals_list)
    ray_x_vals_array = np.array(ray_x_vals_list)
    plt.plot(ray_z_vals_array, ray_x_vals_array, color='blue')
    
#Plotting bundle (1):
plt.grid(color='black', linestyle='-', linewidth=0.5)
plt.title('Refracting a bundle (1) of rays')
plt.xlabel('z (mm)')
plt.ylabel('x (mm)')
plt.xticks(np.arange(0, 225+1, 25))
plt.yticks(np.arange(-5.0, 5.0+1, 1))
plt.xlim(0,225)
plt.ylim(-5,5)
plt.show()

#Plotting spot diagram for bundle 1:
#Initialising rays (bundle 1):
bundle1_rays_list = []
for init_pos_list in bundle1_init_points_list:
    ray_obj = Ray(init_pos_list, [0, 0, 1])
    bundle1_rays_list.append(ray_obj)
#Intersecting, refracting, and intersecitng ray bundle (1):
for ray_obj in bundle1_rays_list:
    ray_refracted = spher_lens_t12.propagate_ray(ray_obj) 
    ray_out_plane = out_plane_t12.propagate_ray(ray_refracted)
    ray_lists = ray_out_plane._vertslist
    ray_focal_x_val = ray_lists[-1][0]
    ray_focal_y_val = ray_lists[-1][1]
    plt.plot(np.array(ray_focal_x_val), np.array(ray_focal_y_val), 'bo',
             markersize=3)
#plt.title('Spot diagram of bundle 1 rays (z=200)')
plt.xlabel('x (mm)')
plt.ylabel('y (mm)')
plt.xticks(np.arange(-0.004, 0.004+0.001, 0.001))
plt.yticks(np.arange(-0.004, 0.004+0.001, 0.001))
plt.xlim(-0.004, 0.004)
plt.ylim(-0.004,0.004)
#plt.savefig("parallel_bundle_final_spot_plot.png",dpi=300, bbox_inches='tight')
plt.show()

#Uniform bundle of rays not parallel to the optical axis (diameter of 5 mm):
#Gaining initial points for rays (bundle 2):
bundle2_center_list = [-2, 0, 0]
bundle2_init_points_list = [bundle2_center_list]
circle1_num_points = 6
num_circles = 5
r = 2.5 / num_circles

start_angle_var = (2 * np.pi) / circle1_num_points
bundle_var_rad = r

#First 2 circles:
while bundle_var_rad <= 2 * r:
    angle_var = start_angle_var
    for i in np.arange(1, circle1_num_points+1):
        new_x_val = -2 + (bundle_var_rad * np.cos(angle_var))
        new_y_val = bundle_var_rad * np.sin(angle_var)
        new_point_list = [new_x_val, new_y_val, 0]
        bundle2_init_points_list.append(new_point_list)
        angle_var += start_angle_var
    circle1_num_points = 2 * circle1_num_points
    bundle_var_rad += r
    start_angle_var = start_angle_var / 2
    
#Outer 3 circles:
circle3_num_points = 18
start_angle_var = (2*np.pi) / circle3_num_points 
bundle_var_rad = 3 * r
while bundle_var_rad <= 2.5:
    angle_var = start_angle_var
    for i in np.arange(1, circle3_num_points+1):
        new_x_val = -2 + (bundle_var_rad * np.cos(angle_var))
        new_y_val = bundle_var_rad * np.sin(angle_var)
        new_point_list = [new_x_val, new_y_val, 0]
        bundle2_init_points_list.append(new_point_list)
        angle_var += start_angle_var
    circle3_num_points += 6
    bundle_var_rad += r
    numerator = (start_angle_var * (circle3_num_points - 6))
    denom = circle3_num_points
    start_angle_var = numerator / denom

#Plotting initial center points (bundle 2):
x_init_bundle2_vals_list = []
y_init_bundle2_vals_list = []

for init_point in bundle2_init_points_list:
    x_init_bundle2_vals_list.append(init_point[0])
    y_init_bundle2_vals_list.append(init_point[1])

x_init_bundle2_vals_array = np.array(x_init_bundle2_vals_list)
y_init_bundle2_vals_array = np.array(y_init_bundle2_vals_list)

#plt.title('Initial positions of bundle 2 (z=0)')
plt.xlabel('x (mm)')
plt.ylabel('y (mm)')
plt.xticks(np.arange(-5.0, 1.0+0.5, 0.5))
plt.yticks(np.arange(-3.0, 3.0+0.5, 0.5))
plt.xlim(-5.0,1.0)
plt.ylim(-3.0,3.0)
plt.plot(x_init_bundle2_vals_array, y_init_bundle2_vals_array, 'ro')
#plt.savefig("angled_bundle_initial_spot_plot.png",dpi=300)
plt.show()

#Initialising rays (bundle 2):
bundle2_rays_list = []
for init_pos_list in bundle2_init_points_list:
    ray_obj = Ray(init_pos_list, [1, 0, 100])
    bundle2_rays_list.append(ray_obj)
#Intersecting, refracting, and intersecitng ray bundle (2):
for ray_obj in bundle2_rays_list:
    ray_refracted = spher_lens_t12.propagate_ray(ray_obj) 
    ray_out_plane = out_plane_t12.propagate_ray(ray_refracted)
    ray_lists = ray_out_plane._vertslist
    ray_z_vals_list = []
    ray_x_vals_list = []
    for list_obj in ray_lists:
        z_val = list_obj[2]
        ray_z_vals_list.append(z_val)
        x_val = list_obj[0]
        ray_x_vals_list.append(x_val)
    ray_z_vals_array = np.array(ray_z_vals_list)
    ray_x_vals_array = np.array(ray_x_vals_list)
    plt.plot(ray_z_vals_array, ray_x_vals_array, color='red')
    
#Plotting bundle (2):
plt.grid(color='black', linestyle='-', linewidth=0.5)
plt.title('Refracting a bundle (2) of rays')
plt.xlabel('z (mm)')
plt.ylabel('x (mm)')
plt.xticks(np.arange(0, 225+1, 25))
plt.yticks(np.arange(-6.0, 3.0+1, 1))
plt.xlim(0,225)
plt.ylim(-6,3)
plt.show()    

#Plotting spot diagram for bundle 2:
#Initialising rays (bundle 2):
bundle2_rays_list = []
for init_pos_list in bundle2_init_points_list:
    ray_obj = Ray(init_pos_list, [1, 0, 100])
    bundle2_rays_list.append(ray_obj)
#Intersecting, refracting, and intersecitng ray bundle (2):
for ray_obj in bundle2_rays_list:
    ray_refracted = spher_lens_t12.propagate_ray(ray_obj) 
    ray_out_plane = out_plane_t12.propagate_ray(ray_refracted)
    ray_lists = ray_out_plane._vertslist
    ray_focal_x_val = ray_lists[-1][0]
    ray_focal_y_val = ray_lists[-1][1]
    plt.plot(np.array(ray_focal_x_val), np.array(ray_focal_y_val), 'ro',
             markersize=3)
#plt.title('Spot diagram of bundle 2 rays (z=200)')
plt.xlabel('x (mm)')
plt.ylabel('y (mm)')
plt.xticks(np.arange(0.665, 0.674+0.001, 0.001))
plt.yticks(np.arange(-0.004, 0.004+0.001, 0.001))
plt.xlim(0.665, 0.674)
plt.ylim(-0.004,0.004)
#plt.savefig("angled_bundle_final_spot_plot.png",dpi=300, bbox_inches='tight')
plt.show()    
#%%---------------------------------------------------------------------------  
#-----------------Plotting both bundles on the same graph:--------------------
spher_lens_t12 = SphericalRefraction([0, 0, 100], 0.03, 1.0, 1.5, 1/0.03)
para_focus = (1.5 * (1/0.03)) / (1.5 - 1)
#Output plane:
out_plane_t12 = OutputPlane(100 + para_focus) 

#Forming bundles of rays:

#Uniform bundle of rays parallel to the optical axis (diameter of 5 mm):
#Gaining initial points for rays (bundle 1):
bundle1_center_list = [0, 0, 0]
bundle1_init_points_list = [bundle1_center_list]
circle1_num_points = 6
num_circles = 5
r = 2.5 / num_circles

start_angle_var = (2 * np.pi) / circle1_num_points
bundle_var_rad = r

#First 2 circles:
while bundle_var_rad <= 2 * r:
    angle_var = start_angle_var
    for i in np.arange(1, circle1_num_points+1):
        new_x_val = bundle_var_rad * np.cos(angle_var)
        new_y_val = bundle_var_rad * np.sin(angle_var)
        new_point_list = [new_x_val, new_y_val, 0]
        bundle1_init_points_list.append(new_point_list)
        angle_var += start_angle_var
    circle1_num_points = 2 * circle1_num_points
    bundle_var_rad += r
    start_angle_var = start_angle_var / 2
    
#Outer 3 circles:
circle3_num_points = 18
start_angle_var = (2*np.pi) / circle3_num_points 
bundle_var_rad = 3 * r
while bundle_var_rad <= 2.5:
    angle_var = start_angle_var
    for i in np.arange(1, circle3_num_points+1):
        new_x_val = bundle_var_rad * np.cos(angle_var)
        new_y_val = bundle_var_rad * np.sin(angle_var)
        new_point_list = [new_x_val, new_y_val, 0]
        bundle1_init_points_list.append(new_point_list)
        angle_var += start_angle_var
    circle3_num_points += 6
    bundle_var_rad += r
    numerator = (start_angle_var * (circle3_num_points - 6))
    denom = circle3_num_points
    start_angle_var = numerator / denom

#Initialising rays (bundle 1):
bundle1_rays_list = []
for init_pos_list in bundle1_init_points_list:
    ray_obj = Ray(init_pos_list, [0, 0, 1])
    bundle1_rays_list.append(ray_obj)
#Intersecting, refracting, and intersecitng ray bundle (1):
for ray_obj in bundle1_rays_list:
    ray_refracted = spher_lens_t12.propagate_ray(ray_obj) 
    ray_out_plane = out_plane_t12.propagate_ray(ray_refracted)
    ray_lists = ray_out_plane._vertslist
    ray_z_vals_list = []
    ray_x_vals_list = []
    for list_obj in ray_lists:
        z_val = list_obj[2]
        ray_z_vals_list.append(z_val)
        x_val = list_obj[0]
        ray_x_vals_list.append(x_val)
    ray_z_vals_array = np.array(ray_z_vals_list)
    ray_x_vals_array = np.array(ray_x_vals_list)
    plt.plot(ray_z_vals_array, ray_x_vals_array, color='blue')

#Uniform bundle of rays not parallel to the optical axis (diameter of 5 mm):
#Gaining initial points for rays (bundle 2):
bundle2_center_list = [-2, 0, 0]
bundle2_init_points_list = [bundle2_center_list]
circle1_num_points = 6
num_circles = 5
r = 2.5 / num_circles

start_angle_var = (2 * np.pi) / circle1_num_points
bundle_var_rad = r

#First 2 circles:
while bundle_var_rad <= 2 * r:
    angle_var = start_angle_var
    for i in np.arange(1, circle1_num_points+1):
        new_x_val = -2 + (bundle_var_rad * np.cos(angle_var))
        new_y_val = bundle_var_rad * np.sin(angle_var)
        new_point_list = [new_x_val, new_y_val, 0]
        bundle2_init_points_list.append(new_point_list)
        angle_var += start_angle_var
    circle1_num_points = 2 * circle1_num_points
    bundle_var_rad += r
    start_angle_var = start_angle_var / 2
    
#Outer 3 circles:
circle3_num_points = 18
start_angle_var = (2*np.pi) / circle3_num_points 
bundle_var_rad = 3 * r
while bundle_var_rad <= 2.5:
    angle_var = start_angle_var
    for i in np.arange(1, circle3_num_points+1):
        new_x_val = -2 + (bundle_var_rad * np.cos(angle_var))
        new_y_val = bundle_var_rad * np.sin(angle_var)
        new_point_list = [new_x_val, new_y_val, 0]
        bundle2_init_points_list.append(new_point_list)
        angle_var += start_angle_var
    circle3_num_points += 6
    bundle_var_rad += r
    numerator = (start_angle_var * (circle3_num_points - 6))
    denom = circle3_num_points
    start_angle_var = numerator / denom

#Initialising rays (bundle 2):
bundle2_rays_list = []
for init_pos_list in bundle2_init_points_list:
    ray_obj = Ray(init_pos_list, [1, 0, 100])
    bundle2_rays_list.append(ray_obj)
#Intersecting, refracting, and intersecitng ray bundle (2):
for ray_obj in bundle2_rays_list:
    ray_refracted = spher_lens_t12.propagate_ray(ray_obj) 
    ray_out_plane = out_plane_t12.propagate_ray(ray_refracted)
    ray_lists = ray_out_plane._vertslist
    ray_z_vals_list = []
    ray_x_vals_list = []
    for list_obj in ray_lists:
        z_val = list_obj[2]
        ray_z_vals_list.append(z_val)
        x_val = list_obj[0]
        ray_x_vals_list.append(x_val)
    ray_z_vals_array = np.array(ray_z_vals_list)
    ray_x_vals_array = np.array(ray_x_vals_list)
    plt.plot(ray_z_vals_array, ray_x_vals_array, color='red')

#Plotting bundles:
plt.grid(color='black', linestyle='-', linewidth=0.5)
#plt.title('Refracting bundles of rays')
plt.xlabel('z (mm)')
plt.ylabel('x (mm)')
plt.xticks(np.arange(0, 225+1, 25))
plt.yticks(np.arange(-5.0, 3.0+1, 1))
plt.xlim(0,225)
plt.ylim(-5,3)
#plt.savefig("both_bundles_refracted_plot.png",dpi=300)
plt.show()
