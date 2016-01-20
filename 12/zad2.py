def binarne_rek(L, left, right, y):
    zm = ((right - left) / len(L)) + left
    if (zm == len(L)) or (right is left):
        return False
    elif L[zm] is y:
        return zm
    elif L[zm] < y:
        return binarne_rek(L, zm + 1, right, y)
    else:
        return binarne_rek(L, left, zm, y)
