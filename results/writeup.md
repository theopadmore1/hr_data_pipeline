1) Which file appears to represent the most active period? Explain using at least two metrics. Consider that this is a 30 year old participant and compare your output to the column titled "Target HR Zone 50-85%" within this link: https://www.heart.org/en/healthy-living/fitness/fitness-basics/target-heart-rates

...

2) Which file had the **poorest** data quality? How do you know?


3) Suppose one heart-rate file contains the following cleaned values: `68, 70, 71, 72, 72, 73, 74, 75, 180`. The value 180 was recorded during a sensor glitch.

a) Calculate the range of this dataset.
heart rate = (max) - (min): 180 - 68 = 112
data = [68, 70, 71, 72, 72, 73, 74, 75, 180]

data_range = max(data) - min(data)

print(data_range)

b) Explain how the extreme value affects the range.
The 180 in the list is an extreme outlier that doesn't reflect the true range of the list. This is because apart from 180, the general differences in the values are between 1 and 2 and the reset of the values don't go above 80 which is very misleading.


c) Identify a different statistic that would better represent the typical variability of the dataset. Why would this measure be better?
One statistic I would do is simply remove the 180 from the list of values. This would give a more accurate range as all the other values are relatively close to each other. 
