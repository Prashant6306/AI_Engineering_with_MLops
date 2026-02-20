# import geo_utils

# r = 7.5
# area = geo_utils.circle_area(r)
# print(f"Area = {area:.2f}")

# dist = geo_utils.km_to_miles(100)
# print(f"100 km = {dist:.1f} miles")

# vol = geo_utils.sphere_volume(5)
# print(f"Vol = {vol:.2f} cu-units")


#from module import name

# from geo_utils import circle_area,km_to_miles,sphere_volume

# r = 7.5
# area = circle_area(r)
# print(f"Area = {area:.2f}")

# from geo_utils import *
# r = 7.5
# area = circle_area(r)
# print(f"Area = {area:.2f}")


# import geo_utils as gu

# r = 7.5
# area = gu.circle_area(r)
# print(f"Area = {area:.2f}")

from geo_utils import circle_area as ca

r = 7.5
area = ca(r)
print(f"Area = {area:.2f}")