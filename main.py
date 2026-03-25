def clean_heartrate_data(data: list) -> tuple:
    """
    """
    pass


def average(data: list) -> float:
    """
    Calculate average of a list of integers using a for-loop. Assumes data is clean.
    """
    pass


def median(data: list) -> float:
    """
    """
    pass


def range(data: list) -> float:
    """
    """
    pass


def rolling_avg(data: list, k: int) -> float:
    """
    CHALLENGE FUNCTION (Optional)
    """
    pass


def run(file: str):
    """
    Process heart rate data from the a file by cleaning and
    calculating summary statistics. Print out final values.

    Args:
        filename (str): The path to the data file (e.g., 'data/phase0.txt').

    Returns:
        float, float, float: You will return the average, median, and range.
    """
    data = []
    

    # open file using file I/O and read it into the `data` list
    file_object = open(file)
    for line in file_object:
        print(line)
    
    with open(file, 'r') as file_object:
        for line in file_object:
            data.append(line.strip())

    # Use `clean_heartrate_data` to clean the data and remove invalid entries
    def clean_heartrate_data(data):
        #Step 1: Remove invalid entries
        filtered = [x for x in data if not None and x != 'NO DATA' and x 1= ""]

        #Step 2: Convert to integers
    cleaned = []
    for x in filter: 
        try:
            cleaned.append(int(x))
        except ValueError:
            continue #skip anything that can't be converted

    return cleaned     

cleaned_data = clean_heartrate_data(data)    

        


    # calculate the average, median, and range of this file using the functions you've wrote
    
def average(data):
    return sum(data) / len(data)

def median(data):
    sorted_data = sorted(data)
    n = len(sorted_data) 
    if n % 2 == 0:
        return(sorted_data[n//2-1] + sorted_data[n//2]) /2
    else:
        return sorted_data[n//2]

def data_range(data):
    return max(data) - min(data)


    # print out your data quality measure to the console
total_entries = len(data)
valid_entries = len(cleaned_data)
invalid_entries = total_entries - valid_entries 

    # print out your descriptive statistics to the console
print('--Data Quality--')
print(f'Total entries: {total_entries}')
print(f'Valid entries: {valid_entries}')
print(f'Invalid entries removed: {invalid_entries}')

print('\n-- Descriptive Statistics --')
print(f'Average: {average(cleaned_data):.2f}')
print(f'Median: {median(cleaned_data)}')
print(f'Range: {data_range(cleaned_data)}')



if __name__ == "__main__":
    run("data/phase0.txt")
    run("data/phase1.txt")
    run("data/phase2.txt")
    run("data/phase3.txt")
