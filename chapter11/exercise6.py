

import string
# After doing a series of experiments, you have compiled a dictionary showing the probability of detecting certain kinds of subatomic particles. The particles’ names are the dictionary’s keys, and the probabilities are the values: {'neutron': 0.55, 'proton': 0.21, 'meson': 0.03, 'muon': 0.07, 'neutrino': 0.14}. Write a function that takes a single dictionary of this kind as input and returns the particle that is least likely to be observed. Given the dictionary shown earlier, for example, the function would return 'meson'.

def least_likely(particles):
    
    name_particle = ""
    number_particle = 1000
    
    for particle in particles:
        # print(particles[particle])

        if particles[particle] < number_particle:
            name_particle = particle
            number_particle = particles[particle]

    
    return print(name_particle)


particles = {'neutron': 0.55, 'proton': 0.21, 'meson': 0.03, 'muon': 0.07, 'neutrino': 0.14}

least_likely(particles)

