

import pandas as pd


emails = [
    ["You won free money! Claim your prize now!", 1],
    ["URGENT! You won a cash reward!", 1],
    ["Make money fast from home today!", 1],
    ["Claim your free gift immediately!", 1],
    ["WIN BIG! Your cash prize is waiting!", 1],
    ["Get a loan today with no questions!", 1],
    ["Limited offer! Claim your bonus now!", 1],
    ["You have won a free vacation!", 1],

    ["Are we still meeting for lunch tomorrow?", 0],
    ["The meeting starts at 2 PM today.", 0],
    ["Please return your library book Friday.", 0],
    ["Thanks for sending me the homework.", 0],
    ["The school office is closed Monday.", 0],
    ["Can you send me the pictures?", 0],
    ["Your appointment is Tuesday at 10 AM.", 0],
    ["Here is the recipe we discussed.", 0]
]


data = []

for email in emails:

    text = email[0]
    label = email[1]

    # Count words
    words = text.split()
    word_count = len(words)

    exclamations = text.count("!")


    money_words = 0

    for word in words:
        if word.lower().strip("!.,") in [
            "money", "cash", "prize", "free",
            "reward", "bonus", "gift", "loan"
        ]:
            money_words += 1

    all_caps = 0

    for word in words:
        if len(word) > 1 and word.isupper():
            all_caps += 1

   
    urgency_words = 0

    for word in words:
        if word.lower().strip("!.,") in [
            "urgent", "now", "today", "claim",
            "immediately", "limited"
        ]:
            urgency_words += 1

    
    suspicious_links = 0

    if "http" in text.lower() or "www." in text.lower():
        suspicious_links = 1

    data.append([
        text, label, word_count, exclamations,
        money_words, all_caps, urgency_words,
        suspicious_links
    ])

columns = [
    "email_text", "label", "word_count",
    "exclamations", "money_words", "all_caps",
    "urgency_words", "suspicious_links"
]

df = pd.DataFrame(data, columns=columns)


import os
os.makedirs("data", exist_ok=True)


df.to_csv("data/emails.csv", index=False)

print("Email dataset created successfully!")
print("Total emails:", len(df))
print("Spam emails:", sum(df["label"] == 1))
print("Legitimate emails:", sum(df["label"] == 0))

