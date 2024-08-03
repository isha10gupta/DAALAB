#GALE SHAPELY- here we find the perfect match for each men and women 
#TC- O(n^2)
man = {}
women = {}
n = int(input("Enter the number of men and women: "))
# Input preferences for men
print("Enter preferences for men:")
for i in range(n):
        m = input(f"Enter the name of man {i + 1}: ")
        man[m] = [] #CREATE A TUPLE
        preferences = input(f"Enter the preferences of {man} (space-separated list of women): ").split() 
        man[m] = preferences
# Input preferences for women
print("Enter preferences for women:")
for i in range(n):
        w = input(f"Enter the name of woman {i + 1}: ")
        women[w] = [] #CREATE A TUPLE
        preferences = input(f"Enter the preferences of {women} (space-separated list of men): ").split()
        women[w] = preferences
# List of free men
free = [x for x in man.keys()]
# Dictionary to keep track of proposals made by each man
prop = {x: [] for x in man.keys()}

# Dictionary to keep track of engagements; 0 means not engaged
eng = {x: 0 for x in women.keys()}

def match(man, women):
    while free:
        # Pop a man from the free list
        m = free.pop()
        # Get his preferences
        mp = man[m]

        for w in mp:
            # If the man has not yet proposed to this woman
            if w not in prop[m]:
                # Add the woman to the list of proposals made by the man
                prop[m].append(w)

                # If the woman is not engaged
                if not eng[w]:
                    # Engage the woman with the man
                    eng[w] = m
                    break
                else:
                    # Woman's current partner
                    cp = eng[w]
                    # Woman's preferences
                    wp = women[w]

                    # If the woman prefers the new man over her current partner
                    if wp.index(cp) > wp.index(m):
                        # Engage the woman with the new man
                        eng[w] = m
                        # Add the old partner back to the free list
                        free.append(cp)
                        break
 # Print final engagements
    print(eng)

# Call the match function with the defined preferences
match(man, women)
