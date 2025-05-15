# Programming Exercise 3-13

def calculateCost(weight):
    # Calculate the shipping charge.
    if weight > 10:
        shippingCost = 4.75
    elif weight > 6:
        shippingCost = 4.00
    elif weight > 2:
        shippingCost = 3.00
    else:
        shippingCost = 1.50
    return shippingCost
