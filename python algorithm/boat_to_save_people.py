def boat_to_save(people, limit):
    print(limit)
    left = 0
    right = len(people)
    boatno = 0
    while left <= right:
        if left == right:
            boatno +=1
            break
        if people[left] + people[right] <= limit:
            left += 1
        right -=1
        boatno +=1
        return boatno

people = [2 , 3, 4, 5, 7, 10]
limit = 10
print(boat_to_save(people, limit))    