def unique_preserving_order(xs):
    # BUG: transformă în set și apoi list – ordinea se pierde!
    return list(set(xs))
