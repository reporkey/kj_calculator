def factorization(target, factors):
    if len(factors) == 1:
        t = target % factors[0]
        r = [target // factors[0]]
        if 0 < t:
            t -= factors[0]
            r[0] += 1
        return t, r
        

    if target % factors[0] == 0:
        return 0, [target // factors[0]] + [0] * len(factors[1:])
        
    if 0 < target < factors[0]:
        t, r = factorization(target, factors[1:])
        if t > target - factors[0]:
            return t, [0] + r
        else:
            return target - factors[0], [1] + [0] * len(factors[1:])
    else:
        t0, r0 = factorization(target % factors[0], factors[1:])
        r0 = [target // factors[0]] + r0
        for q in reversed(range(target // factors[0])):
            if q > 10:
                break
            t1, r1 = factorization(target - q * factors[0], factors[1:])
            if t1 > t0:
                t0 = t1
                r0 = [q] + r1
            if t0 == 0:
                break
        return t0 ,r0

def kj_calculator(target, elements):
    if elements is None or type(elements) is not list or len(elements) == 0:
        return "Please provide valid amount options."
    try: 
        if target != int(target) or int(target) <= 0:
            return("Please provide a positive interger number as amount.")
        target = int(target)
    except ValueError:
        return "Please provide avalid amount."
    
    elements = list(sorted(elements, reverse=True))
    remainder, result = factorization(target, elements)
    total = [f*n for f, n in zip(elements, result)]

    out = "Total: {}.\n".format(sum(total))
    out += "They are: "
    for f, n in zip(elements, result):
        if n != 0 and f != 0:
            out += "{} of {}, ".format(n, f)
    out = out[:-2] + "."
    return out

if __name__=="__main__":
    elements=[6, 12, 30, 68, 128, 328, 648, 1298, 998, 2998, 4998]
    out = kj_calculator(288, elements)
    print(out)