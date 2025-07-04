# Added creativity: It identifies the largest life expectancy drop from one year to the next 
# for each country and displays the min, max, and average life expectancy when a country is specified.

file_path = '/Users/caroline/BYU-I/CSEPC 110 - Introduction to Programming/Project/life-expectancy.csv'

overall_min = float('inf')
overall_max = float('-inf')

min_country = ""
min_year = 0
max_country = ""
max_year = 0

data_by_year = {}
data_by_country = {}

with open(file_path, 'r') as file:
    next(file)
    for line in file:
        parts = line.strip().split(',')
        
        country = parts[0]
        year = int(parts[2])
        life_expectancy = float(parts[3])
        
        if life_expectancy < overall_min:
            overall_min = life_expectancy
            min_country = country
            min_year = year
        if life_expectancy > overall_max:
            overall_max = life_expectancy
            max_country = country
            max_year = year

        if year not in data_by_year:
            data_by_year[year] = []
        data_by_year[year].append(life_expectancy)
        
        if country not in data_by_country:
            data_by_country[country] = []
        data_by_country[country].append((year, life_expectancy))

print(f"The overall max life expectancy is: {overall_max} from {max_country} in {max_year}")
print(f"The overall min life expectancy is: {overall_min} from {min_country} in {min_year}")

user_year = int(input("Enter the year of interest: "))
if user_year in data_by_year:
    year_data = data_by_year[user_year]
    avg_life_exp = sum(year_data) / len(year_data)
    min_life_exp = min(year_data)
    max_life_exp = max(year_data)
    
    min_country_year = ""
    max_country_year = ""
    
    with open(file_path, 'r') as file:
        next(file)
        for line in file:
            parts = line.strip().split(',')
            country = parts[0]
            year = int(parts[2])
            life_expectancy = float(parts[3])
            
            if year == user_year:
                if life_expectancy == min_life_exp:
                    min_country_year = country
                if life_expectancy == max_life_exp:
                    max_country_year = country
    
    print(f"For the year {user_year}:")
    print(f"The average life expectancy across all countries was {avg_life_exp:.2f}")
    print(f"The max life expectancy was in {max_country_year} with {max_life_exp}")
    print(f"The min life expectancy was in {min_country_year} with {min_life_exp}")
else:
    print("Year not found in the dataset.")

user_country = input("Enter the country of interest (or leave blank to skip): ").strip()
if user_country in data_by_country:
    country_data = data_by_country[user_country]
    life_exps = [entry[1] for entry in country_data]
    avg_country_life_exp = sum(life_exps) / len(life_exps)
    min_country_life_exp = min(life_exps)
    max_country_life_exp = max(life_exps)
    
    print(f"In {user_country}:")
    print(f"Minimum life expectancy: {min_country_life_exp}")
    print(f"Maximum life expectancy: {max_country_life_exp}")
    print(f"Average life expectancy: {avg_country_life_exp:.2f}")
    
    largest_drop = 0
    drop_year = 0
    for i in range(1, len(country_data)):
        year_diff = country_data[i][1] - country_data[i-1][1]
        if year_diff < largest_drop:
            largest_drop = year_diff
            drop_year = country_data[i][0]
    
    print(f"The largest drop in life expectancy for {user_country} occurred in {drop_year} with a drop of {largest_drop:.2f}")
else:
    print("Country not found in the dataset.")
