# Travel Log
# Author: Powell A. Mims
# This practice program uses dictionaries to create a travel log.

def get_new_country(country, times, cities):
    new_country = {};
    new_country["country"] = country;
    new_country["visits"] = times;
    new_country["cities"] = cities;
    return new_country;

travel_log = [];

travel_log.append(get_new_country("France", 4, ["Paris", "Lille", "Dijon"]));
travel_log.append(get_new_country("Russia", 2, ["Moscow", "St. Petersburg"]));

for log in travel_log:
    print(log);
