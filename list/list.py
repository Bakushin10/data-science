top_male_names = []
male_name_counts = {}

for row in legislators:
    gender = row[3]
    year = row[7]
    if  gender == 'M' and year > 1940:
        name =  row[1]
        if name in male_name_counts:
            male_name_counts[name] = male_name_counts[name] + 1
        else:
            male_name_counts[name] = 1

highest_male_count = 0
for name, count in male_name_counts.items():
    if count > highest_male_count:
        highest_male_count = count

for name,count in male_name_counts.items():
    if count == highest_male_count:
        top_male_names.append(name)

##############################

values = [None, 10, 20, 30, None, 50]
checks = []
checks = [ num is not None and num > 30 for num in values]
