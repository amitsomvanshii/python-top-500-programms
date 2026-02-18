# print("welcome to brand name generatot")
#  # take inputs
# city = input("enter your city name: ")
# domain = input("enter your domain name: ")
# brand_name = city + " " + domain
# print(brand_name)

import random
print("welcome to brand name generator")

names = ["carrer", "hub", "work", "sonnet", "weekday", "workday", "perday", "advanced"]
domain = ["tech", "sales", "IT", "computer", "my", "data"]
brand_name = random.choice(names)+ " " + random.choice(domain)
print(brand_name)