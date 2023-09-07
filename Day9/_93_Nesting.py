# Nesting lists and dictionaries
capitals = {
    "France": "Paris",
    "Germany": "Berlin",
}

travel_log = {
    "France": {"cities_visited": ["Paris","Lille","Dijon"], "total_visits":12},
    "Germany":{"cities_visited": ["Berlin","Hanburg","Stuttgart"], "total_visits": 10},

}

#Nesting Dictionary in a List
travel_log = [
    {
        "country": "France", 
        "cities_visited": ["Paris","Lille","Dijon"], 
        "total_visits":12
    },
    {
    "country": "Germany",
        "cities_visited": ["Berlin","Hanburg","Stuttgart"], 
        "total_visits": 10
        },
]