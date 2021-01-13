names = []

planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus"]

print(planets)

planets.append("Neptune")
planets.append("*Pluto")

print(planets)
print(planets[-1])

print("----")

for planet in planets:
  print(planet)
  
print("----")

for num in range(len(planets)):
  print(planets[num])