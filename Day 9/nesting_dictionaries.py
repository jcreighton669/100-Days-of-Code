# Nesting
capitals = {
    "France": "Paris",
    "Germany": "Berlin",
}

# Nesting a list in a Dictionary

travel_log = {
    "France": ["Paris", "Lille", "Dijon"],
    "Germany": ["Berlin", "Hamburg", "Stuttgart"],
}

# Nesting a dictionary in a dictionary
travel_log = {
    "France": {"Cities_Visited": ["Paris", "Lille", "Dijon"], "total_visits": 12},
    "Germany": {"Cities_visited": ["Berlin", "Hamburg", "Stuttgart"], "total_visits": 5},
}

# Nesting Dictionary in a List

travel_log_list = [
    {
        "country": "France",
        "Cities_Visited": ["Paris", "Lille", "Dijon"], 
        "total_visits": 12
    },
    {
        "country": "Germany",
        "Cities_Visited": ["Berlin", "Hamburg", "Stuttgart"], 
        "total_visits": 5
    },
]

for country in travel_log_list:
    print(country.keys())