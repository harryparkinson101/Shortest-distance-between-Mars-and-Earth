import math

def get_opposition_distance(a, e, v):
    return a * (1 - e**2) / (1 + e * math.cos(v))

# calculate the opposition distance for the Earth
earth_a = 149597871  # semi-major axis (km)
earth_e = 0.0167  # eccentricity
earth_v = math.radians(0)  # true anomaly (radians)
earth_opposition_distance = get_opposition_distance(earth_a, earth_e, earth_v)

# calculate the opposition distance for Mars
mars_a = 227939100  # semi-major axis (km)
mars_e = 0.0935  # eccentricity
mars_v = math.radians(0)  # true anomaly (radians)
mars_opposition_distance = get_opposition_distance(mars_a, mars_e, mars_v)

# determine the shortest distance between the Earth and Mars
shortest_distance = min(earth_opposition_distance, mars_opposition_distance)

print(shortest_distance)