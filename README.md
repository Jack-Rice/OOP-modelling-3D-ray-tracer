# OOP-modelling-3D-ray-tracer (Python)
## Project Overview
This project uses object-oriented programming (OOP) to model some optical systems involving bundles of rays
(both parallel and at an angle to the optical axis) and a spherical lens. My model was able to produce paraxial 
focuses that agreed with theoretical values, and through tracing the paths of ray objects, I was able to demonstrate spherical aberration present in the refraction of a uniform bundle of rays.
![Example plot of parallel rays refracted by a spherical lens and all intersecting at the focal point](Figures/parallel_rays_plot.png)
![Example plot of a magnified and inverted image formed](Figures/magnification_inversion_plot.png)
![Example plot of angled rays refracted by a spherical lens and not intersecting at the focal point](Figures/spherical_aberration_plot.png)

## Objectives
- Create classes to initialise ray and optical elements objects.
- Model the refraction of rays at angles and parallel to the spherical lens.
- Demonstrate spherical aberration in the result image of refracted rays.

## Methods
### 1. Creation of Modules
Four different modules were made that each contained a class for initialising different objects: a Ray class,
an OpticalElement class, a SphericalRefraction class (a derived class of OpticalElement), and an OutputPlane class
(also a derived class of OpticalElement).

### 2. Refraction Function
Geometric optics was used to form an intercept function for the SphericalRefraction class 
that was dependent on the curvature of the spherical lens.

### 3. Initialising Bundles of Rays
Two different bundles of rays were initialised, one where the rays are parallel to the optical axis (red) and one where they are parallel to the optical axis (blue).
![Plot of bundle of rays, both parallel and angled, refracted by a spherical lens](Figures/both_bundles_refracted_plot.png)

### 4. Compare the Initial and Final Positions of Rays
I created two spot diagrams for each bundle: one at its initial position and one at its final position, after propagating and refracting through the lens.
More spherical aberration will be present if the spots are less precisely arranged about a single point.

Initial parallel bundle of rays positions:
![Spot diagram of initial positions for bundle of rays parallel to the optical axis](Figures/parallel_bundle_initial_spot_plot.png)
Final parallel bundle of rays positions:
![Spot diagram of final positions for bundle of rays parallel to the optical axis](Figures/parallel_bundle_final_spot_plot.png)

## Key Results
- The modelled paraxial focus position agrees with the theoretical values proposed using geometric optics
- Whilst spherical aberration is present for both bundles of rays, the angled bundle shows more spherical aberration. 

Initial angled bundle of rays positions:
![Spot diagram of initial positions for bundle of rays angled to the optical axis](Figures/angled_bundle_initial_spot_plot.png)
Final angled bundle of rays positions:
![Spot diagram of final positions for bundle of rays angled to the optical axis](Figures/angled_bundle_final_spot_plot.png)

## Tools & Technologies
- Python
- NumPy
- Matplotlib

## Key Techniques Demonstrated
- OOP through the creation of classes.
- Data visualisation
- Scientific model comparison

## How to Run the Model
1. Clone the repository:
github.com/Jack-Rice/OOP-modelling-3D-ray-tracer.git

2. Run the raytracer.py Python script.
