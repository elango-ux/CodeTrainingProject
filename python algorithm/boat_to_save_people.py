def boat(people): 
    left = 0
    right = len(people)-1
    boat = 0
    
    limit = 5
    print(people[right])
    while people[left] < people[right] :
        if (people[left] + people[right] <= limit):
            left += 1
            right -= 1
            boat += 1
        print(boat)
        if people[left] == people[right]:
            boat += 1
    
    
people = [3, 4, 5, 6]
print(boat(people))