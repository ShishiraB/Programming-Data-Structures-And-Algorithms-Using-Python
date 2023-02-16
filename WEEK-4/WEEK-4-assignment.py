def flatten(l):
    result = []
    for item in l:                              # loop over each item in the input list
        if type(item) == list:                  # if the current item is a list, recursively flatten it and add its elements to the result
            result.extend(flatten(item))
        else:                                   # if the current item is not a list, add it to the result
            result.append(item)
    return result


def rainaverage(l):
    city_rainfall = {}                                                                          # create an empty dictionary to keep track of the total rainfall for each city
    city_count = {}                                                                             # create an empty dictionary to keep track of the number of rainfall recordings for each city
    for city, rainfall in l:                                                                    # iterate over each element in the input list
        city_rainfall[city] = city_rainfall.get(city, 0) + rainfall                             # add the rainfall to the city's total rainfall
        city_count[city] = city_count.get(city, 0) + 1                                          # increment the city's number of rainfall recordings
    return sorted([(city, city_rainfall[city] / city_count[city]) for city in city_rainfall])   # create a list of pairs containing the city and the average rainfall for that city, sorted in ascending order of city name