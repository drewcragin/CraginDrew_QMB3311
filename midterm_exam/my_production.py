def total_revenue(num_units, price: float) -> float:
    """ Calculates the revenue earned by a firm selling a product at
    a fix price using the formula price * units sold

    >>> total_revenue(10,15.50)
    155.00
    >>> total_revenue(8, 5.25)
    42.00
    """
    # needs 3 examples (-1)
    # needs either a precondition or checks to make sure that variables are not negative (-1)
    total = num_units * price

    return total


# Testing the function
total_revenue(10, 15.50)
# 155.0
total_revenue(8, 5.25)
# 42.0

def total_cost(num_units, fixed_costs: float, cost_coeff: float) -> float:
    """ Calculates total cost incurred to produce a product using the
    formula TC = a * quantity^2 + FC

    num_units - Number of units produced
    fixed_costs - total amount of fixed costs
    cost_coeff - constant that is multiplied by square of units produced

    >>> total_cost(400,4000.0,1.0)
    164,000.0
    >>> total_cost(50,1300.0,2.9)
    8550.0
    """
    # needs 3 examples (-1)
    # needs either a precondition or checks to make sure that variables are not negative (-1)
    total = cost_coeff * num_units ** 2 + fixed_costs

    return total


# Testing the function
total_cost(400, 4000.0, 1.0)
# 164,000.0
total_cost(50, 1300.0, 2.9)
# 8550.0
total_cost(130, 12000.0, 0.88)
# 26872.0

def total_profit(num_units, unit_price, multiplier, fixed_cost) -> float:
    """ Calculates profit earned by company

       num_units - Number of units produced
       unit_price - Price of units produced
       multiplier - Number units are being multiplied by
       fixed_costs - Fixed cost of product

    >>> total_profit(40,400,1,20)
    14380
    >>> total_profit(4,500,1,25)
    1959
    >>> total_profit(3,650,1,30)
    1911

    """
    revenue = num_units * unit_price

    cost = multiplier * num_units ** 2 + fixed_cost

    profit = revenue - cost

    return profit

# Testing the function
total_profit(40,400,1,20)
# 14380
total_profit(4,500,1,25)
# 1959
total_profit(3,650,1,30)
# 1911

def max_profit_calc(unit_price, multiplier, fixed_costs) -> float:
    """ Calculates optimal production level

         unit_price - Price of units produced (p)
         multiplier - Number units are being multiplied by (a)
         fixed_costs - Fixed cost of product (b)

    >>> max_profit_calc(4,4,1)
    0.5
    >>> max_profit_calc(9,3,12)
    1.5
    >>> max_profit_calc(13,8,13)
    0.8125
      """
    profit = (unit_price * multiplier) - fixed_costs

    if profit < 0:
        return 0
    if profit > 0:
       star = unit_price / (2 * multiplier)
       return star

# Testing the function
max_profit_calc(4,4,1)
# 0.5
max_profit_calc(9,3,12)
# 1.5
max_profit_calc(13,8,13)
# 0.8125

def profit_max_q(q_max, step, unit_price, multiplier, fixed_costs) -> float:

    i = 0

    maxp = (unit_price * multiplier) - fixed_costs

    while i != len(q_max) and q_max[i] != maxp:
        i = i + step

    if i == len(q_max):
        return -1
    else:
        return i
