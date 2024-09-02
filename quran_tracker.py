import json
from setup_db import setup_db

chapters_length = json.load(open("chapters_length.json"))
# load the user's data
user_scores, user_scores_dates = setup_db(chapters_length)
# now let's display the UI and start doing the logic

print("Hello, ye worthy preserver of Al-Furqaan!")

# so if the person hasn't done anything today
