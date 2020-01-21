def get_the_top_n(sort_list, n, sort_argument, reverse):
    """Sorts the given list according to the sort argument, return the n top entries in a list

    Keyword arguments:
    sort_list       -- The unsorted list which has to be sorted
    n               -- The number of names in the display
    sort_argument   -- lambda argument with the info what key to sort
    reverse         -- True for descending False for ascending
    """

    sort_list = sorted(sort_list, key=sort_argument, reverse=reverse)
    top_sort_list = []

    counter = 0
    while counter < n:
        top_sort_list.append([sort_list[counter][0], str(sort_list[counter][1])])
        counter += 1

    return top_sort_list
