"""SR Education Group Application."""


def sum_multiples_3_5(max_range):
    """Sum of all multiples of 3 or 5 less than 1000."""
    threes = 3
    fives = 5
    multiples = set()
    while threes < max_range:
        multiples.add(threes)
        if fives < max_range:
            multiples.add(fives)
        threes += 3
        fives += 5
    return sum(multiples)

sum_multiples_3_5(1000)
