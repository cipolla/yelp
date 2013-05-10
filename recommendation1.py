import json
with open('./yelp_training_set/yelp_training_set_business.json') as f:
    business = [json.loads(line) for line in f]
with open('./yelp_training_set/yelp_training_set_review.json') as f:
    review = [json.loads(line) for line in f]
with open('./yelp_training_set/yelp_training_set_user.json') as f:
    user = [json.loads(line) for line in f]
with open('./yelp_test_set/yelp_test_set_business.json') as f:
    businesst = [json.loads(line) for line in f]
with open('./yelp_test_set/yelp_test_set_review.json') as f:
    reviewt = [json.loads(line) for line in f]
with open('./yelp_test_set/yelp_test_set_user.json') as f:
    usert = [json.loads(line) for line in f]



business_id = []
for item in range(len(business)):
    business_id.append(business[item]["business_id"])

user_id = []
for item in range(len(user)):
    user_id.append(user[item]["user_id"])

business_id_review = []
user_id_review = []
for item in range(len(review)):
    business_id_review.append(review[item]["business_id"])
    user_id_review.append(review[item]["user_id"])

businesst_id = []
for item in range(len(businesst)):
    businesst_id.append(businesst[item]["business_id"])

usert_id = []
for item in range(len(usert)):
    usert_id.append(usert[item]["user_id"])

businesst_id_review = []
usert_id_review = []
for item in range(len(reviewt)):
    businesst_id_review.append(reviewt[item]["business_id"])
    usert_id_review.append(reviewt[item]["user_id"])



print(len(set(usert_id_review) & set(user_id_review)))
print(len(usert_id_review))
