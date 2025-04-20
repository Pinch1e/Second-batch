import json

x = '{"name": "Papi", "age":35, "city": "Frankfurt"}'

y = json.loads(x)

print(y["city"])

