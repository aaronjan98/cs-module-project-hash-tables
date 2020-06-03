import math, random
lookup_table = {}
answer_table = {}


def slowfun_too_slow(x, y):
    v = math.pow(x, y)
    v = math.factorial(v)
    v //= (x + y)
    v %= 982451653

    return v

def find_answer(x, y):
    v = math.pow(x, y)

    if v not in answer_table:
        v_ans = math.factorial(v)
        v_ans //= (x + y)
        v_ans %= 982451653
        answer_table.update({v: v_ans})
        return v_ans
    return answer_table[v]

def slowfun(x, y):
    """
    Rewrite slowfun_too_slow() in here so that the program produces the same
    output, but completes quickly instead of taking ages to run.
    """
    # convert lookup_table to a list to iterate through it
    fun_list = list(lookup_table.items())

    # Loop through lookup_table
    for key in fun_list:
        # print('lookup_table:', lookup_table)
        # If v is not in lookup_table
        if (f'{x}, {y}') is key[0]:
            return key[1]
    # call slowfun_too_slow(x, y)
    # v = slowfun_too_slow(x, y)
    v = find_answer(x, y)
    # v //= (x + y)
    # v %= 982451653

    # else the value exists; return the value inside lookup_table
    lookup_table.update({f'{x}, {y}': v})
    return v


# Do not modify below this line!

# slowfun(2, 3)

for i in range(50000):
    x = random.randrange(2, 14)
    y = random.randrange(3, 6)
    print(f'{i}: {x},{y}: {slowfun(x, y)}')
