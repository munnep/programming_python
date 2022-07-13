with open('planet.txt', 'r') as planets_file: 
    planets = planets_file.readlines()
    for planet in reversed(planets): 
        print(planet.strip())