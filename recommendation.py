import json
with open('yelp_training_set_business.json') as f:
    business = [json.loads(line) for line in f]
with open('yelp_training_set_review.json') as f:
    review = [json.loads(line) for line in f]

for i in range(len(business)):
   # if business[i]["state"] != "AZ":
    print(business[i]["full_address"][-5:])

