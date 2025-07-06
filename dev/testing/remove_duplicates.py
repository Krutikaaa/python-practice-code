def remove_dups(lst):
    seen = set()
    for x in lst:
        if x not in seen:
            seen.add(x)
    # return [x for x in lst if not (x in seen or seen.add(x))]
    
    print(seen)


lst = [1, 2, 3, 1, 2, 3]
obj = remove_dups(lst)