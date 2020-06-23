#!/usr/bin/python3


def outlierCleaner(predictions, ages, net_worths):
    """
        clean away the 10% of points that have the largest
        residual errors (different between the prediction
        and the actual net worth)

        return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error)
    """
    
    cleaned_data = []
    error = []
    error2 = []
    for i in range(len(predictions)):
        error.append(abs(net_worths[i] - predictions[i]))
        error2.append((net_worths[i] - predictions[i]))
    error.sort()
    split = int(len(error)*0.1)
    errcut = error[len(error)-split]
    checker = error[len(error)-split : len(error)]

    ### your code goes here
    for i in range(len(error2)):
        if abs(error2[i]) in checker:
            continue
        else:
            cleaned_data.append((ages[i], net_worths[i], error2[i]))
    return cleaned_data

