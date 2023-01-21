import random
intervals = [50,100,500,1000,2000,3000,4000,5000,10000]
result ={}
for interval in intervals:
    circle_points = 0
    square_points = 0
    for i in range(interval**2):
        rand_x = random.uniform(-1, 1)
        rand_y = random.uniform(-1, 1)
        origin_dist = rand_x**2 + rand_y**2
        if origin_dist <= 1:
            circle_points += 1
        square_points += 1
        
        pi = 4 * circle_points / square_points
    result[interval] = pi
print(result) 