import random
import os
import csv
os.makedirs("data", exist_ok=True)
ages = list(range(10, 60))
genders = ["M", "F"]
budgets = list(range(10, 201, 10))
interests = ["gadgets", "books", "toys", "fashion", "sports", "music", "art"]
gift_history_samples = [
    "headphones, smart band",
    "novel, journal", "books", "jewellery", "chocolates",
    "action figure, puzzle",
    "smartwatch, scarf",
    "soccer ball, sneakers",
    "paint set, sketchbook",
    "earphones, charging cable",
    "jacket, handbag",
    "board game, video game",
    "music player, guitar picks"
]

data = []
for user_id in range(1, 101):
    age = random.choice(ages)
    gender = random.choice(genders)
    budget = random.choice(budgets)
    user_interests = random.sample(interests, k=random.randint(1, 3))
    gift_history = random.choice(gift_history_samples)

    data.append([
        user_id, age, gender, budget, ", ".join(user_interests), gift_history
    ])

csv_file = "data/gift_data.csv"
with open(csv_file, mode="w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["UserID", "Age", "Gender", "Budget",
                    "Interests", "GiftHistory"])
    writer.writerows(data)

print(f"Dataset created successfully: {csv_file}")
