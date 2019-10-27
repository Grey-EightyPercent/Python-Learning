def a_power(a, power):
    print(f"The {power} times of {a} is {a} ** {power}") # This is only a statement without computation!!!
    return a ** power # This line is to do the real computation and return the value.

def rate_of_increase(n, n_1):
    print(f"The YoY rate of increase is {n_1} / {n} * 100 %")
    return (n_1 / n) * 100

revenue_3 = a_power(2, 3) # assign the result of the function to the variable.
revenue_2 = a_power(2, 2)
growth_rate = rate_of_increase(revenue_2, revenue_3)

print(f"The 3rd-year revenue is {revenue_3}")
print(f"The 2nd-year revenue is {revenue_2}")
print(f"The YoY growth rate from 2nd year to 3rd year is {growth_rate} % .")


# Below is to breakdown the functions to formulas
# Helping you understand what is "inside out"

revenue_3_b = 2 ** 3
revenue_2_b = 2 ** 2
growth_rate_b = (revenue_3_b / revenue_2_b) * 100

print(f"The 3rd-year revenue is {revenue_3_b}")
print(f"The 2nd-year revenue is {revenue_2_b}")
print(f"The YoY growth rate from 2nd year to 3rd year is {growth_rate_b} % .")
