# adding new dictionary using a def function
travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]
def add_new_country(country, visits, cities):
    new_visits = {}
    new_visits["country"]= country
    new_visits["visits"]= visits
    new_visits["cities"]= cities
    travel_log.append(new_visits)

add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)