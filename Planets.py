from collections import Counter


def getMinimumCost():
    
    test_case = int(input())
    
    for case in range(test_case):
        
        counter = 0
        planet_amount, cost = list(map(int, input().split()))
        planet_orbits = input().split()

        #count the No of planets in a given orbit and store it in a dict as orbit : planets 
        orbit_planet_map = Counter(planet_orbits)

        for orbit in orbit_planet_map:
            #if given cost > planets on a given orbit, choose the first machine
            if cost > orbit_planet_map[orbit]:
                counter += orbit_planet_map[orbit]
            # otherwise choose the second machine
            else:
                counter += cost
        
        print(counter)


getMinimumCost()
