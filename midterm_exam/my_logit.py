def CESutility(consumed_good1, consumed_good2, degree_complements: float) -> float:
    """ Calculates value of Constant Elasticity of Substitution utility function
    which measures degree of satisfaction a consumer gets from two goods with formula
   (x^r+y^r)^1/r

    consumed_good1 - Quantity of good 1 consumed
    consumed_good2 - Quantity of good 2 consumed
    degree_complements - Degree to which the goods are complements or substitutes

    >>> CESutility(40,55,0.7)
    127.38
    >>> CESutility(170,168,-0.35)
    23.323
    """
    # needs 3 examples (-1)
    # needs either a precondition or checks to make sure that variables are not negative (-1)
    total = round(
        (consumed_good1 ** degree_complements + consumed_good2 ** degree_complements) ** (1 / degree_complements), 3)

    return total


# Testing the function
CESutility(40, 55, 0.7)
# 127.38
CESutility(170, 168, -0.35)
# 23.323
CESutility(1030, 1600, 0.9)
# 2833.825

def CESutility_valid(consumed_good1, consumed_good2,
                     degree_complements: float) -> float:  # expected input for the goods? (-1)
    """ Calculates value of Constant Elasticity of Substitution utility function
   which measures degree of satisfaction a consumer gets from two goods with formula
  (x^r+y^r)^1/r while

   consumed_good1 - Quantity of good 1 consumed
   consumed_good2 - Quantity of good 2 consumed
   degree_complements - Degree to which the goods are complements or substitutes

   >>> CESutility_valid(5, 8, 3)
   8.604
   >>> CESutility_valid(-5, -8, 3)
   None
   >>> CESutility_valid(5, -8, 3)
   None
   >>> CESutility_valid(5, 8, -3)
   None
   """
    if consumed_good1 < 0:
        print("X Can not be a negative number")
        return None
    if consumed_good2 < 0:
        print("Y can not be a negative number")
        return None
    if degree_complements <= 0:
        print("r must be strictly positive")
        return None

    total = CESutility(consumed_good1, consumed_good2, degree_complements)

    return total

    def CESutility_in_budget(consumed_good1, consumed_good2, degree_complements: float, p_x, p_y,
                             w) -> float:  # unexpected indent (-1)
        """ Evaluates the CESutility_valid function when the consumer's choice of goods
        x and y are in budget, and returns None otherwise using the wealth formula
        w >= p_x*x + p_y*y

        consumed_good1 - Quantity of good one
        consumed_good2 - Quantity of good two
        r - Degree to which the goods are complements or substitutes
        p_x - Price of good one
        p_y - Price of good two
        w - Wealth

        >>> CESutility_in_budget(5, 3, 2, 2, 2, 20)
        5.831
        >>> CESutility_in_budget(5, 3, 2, 2, 2, 4)
        None
        >>> CESutility_in_budget(5, 3, -2, 2, 2, 20)
        None
        >>> CESutility_in_budget(5, 3, 2, -2, 2, 20)
        None
        """
        if p_x < 0:
            print("Price of X can not be negative")
            return None
        if p_y < 0:
            print("Price of Y can not be negative")
            return None

        if w < p_x * consumed_good1 + p_y * consumed_good2:
            print("Consumers basket of goods can not exceed wealth")
            return None

        return CESutility_valid(consumed_good1, consumed_good2, degree_complements)
import math
def max_logit(y, x, beta_0, beta_1):
    """
     y_i - Binary variable for if event occured
    x_i - Independent variable
    beta0 - Beta 0, the intercept
    beta1 - Beta 1, the slope

    """
    probability = logit(x, beta_0, beta_1)

    if y == 1:
        return math.log(probability)
    elif y == 0:
        return math.log(1 - probability)
    else:
        print("y must be 1 or 0")
        return None
