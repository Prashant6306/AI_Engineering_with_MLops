import math

EARTH_RADIUS_KM = 6371

def circle_area(radius):
    """Area of a circle."""
    return math.pi * radius ** 2

def km_to_miles(km):
    """Convert km to miles."""
    return km * 0.621371

def sphere_volume(r):
    return (4 / 3) * math.pi * r ** 3