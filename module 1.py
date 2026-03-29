import statistics as stats

def average(data:list)-> float:
    return sum(data) / len(data)

def median(data:list)-> float:
    sorted_data = sorted(data)
    n = len(sorted_data) 
    if n % 2 == 0:
        return(sorted_data[n//2-1] + sorted_data[n//2]) /2
    else:
        return sorted_data[n//2]

def range(data:list)-> float:
    return max(data) - min(data)


