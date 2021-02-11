def majority(elements):
    element_to_count = {}
    for element in elements:
        if element not in element_to_count:
            element_to_count[element] = 0
        element_to_count[element] += 1
    # Find the element with most count
    return max(element_to_count, key=element_to_count.get)
