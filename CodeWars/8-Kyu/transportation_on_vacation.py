def rental_car_cost(d):
    # your code
    return d * 40 - (d > 2) * 20 - (d > 6) * 30
