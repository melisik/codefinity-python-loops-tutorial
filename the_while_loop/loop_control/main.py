# List of country names
countries = ['Wales', 'Denmark', 'Belgium', 'Japan', 'South Korea', 'South Africa', 'Indonesia', 'Singapore', 'Australia', 'India', 'Saudi Arabia', 'Mexico', 'Turkey', 'Greece', 'Netherlands', 'Finland', 'Monako', 'United Arab Emirates', 'Egypt', 'Morocco', 'Brazil', 'Argentina', 'Ireland', 'Portugal', 'Chile', 'Spain', 'Czech Republic', 'Sweden', 'Switzerland', 'Thailand', 'Luxemburg', 'New Zealand', 'France', 'Italy', 'Germany', 'China', 'Canada', 'Hungary', 'Scotland', 'Norway', 'Austria', 'Ukraine', 'Poland']

# List to hold selected countries
selected = []
while countries:
    if countries[0][0] == "S":
        selected.append(countries[0])
    countries.pop(0)
    if len(selected) == 3:
        break


# Testing
print('First three countries starting with "S":', selected)