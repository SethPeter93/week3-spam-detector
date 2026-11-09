
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.metrics import precision_score, recall_score

# Load the email data
data = pd.read_csv("data/emails.csv")

# Select the features
X = data[
    [
        "word_count",
        "exclamations",
        "money_words",
        "all_caps",
        "urgency_words",
        "suspicious_links"
    ]
]

# Select the answers
y = data["label"]

# Split the data into training and testing groups
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42, stratify=y
)

# Create the spam detector
model = LogisticRegression(max_iter=1000)

# Train the model
model.fit(X_train, y_train)

# Test the model
predictions = model.predict(X_test)

# Calculate accuracy
accuracy = accuracy_score(y_test, predictions)

# Calculate precision and recall
precision = precision_score(y_test, predictions, zero_division=0)
recall = recall_score(y_test, predictions, zero_division=0)

print("SPAM DETECTOR RESULTS")
print("Accuracy:", accuracy)
print("Precision:", precision)
print("Recall:", recall)

# Create confusion matrix
matrix = confusion_matrix(y_test, predictions, labels=[0, 1])

# Get the four results
tn, fp, fn, tp = matrix.ravel()

print("\nCONFUSION MATRIX RESULTS")

print("Spam correctly caught:", tp)
print("Legitimate correctly passed:", tn)
print("Legitimate wrongly marked as spam:", fp)
print("Spam wrongly let through:", fn)

# Display confusion matrix
plt.imshow(matrix, cmap="Blues")
plt.title("Spam Detector Confusion Matrix")
plt.xlabel("Predicted Result")
plt.ylabel("Actual Result")

plt.xticks([0, 1], ["Legitimate", "Spam"])
plt.yticks([0, 1], ["Legitimate", "Spam"])

plt.colorbar()
plt.show()

# Display feature weights
print("\nFEATURE WEIGHTS")

features = X.columns
weights = model.coef_[0]

for i in range(len(features)):
    print(features[i], ":", round(weights[i], 3))

# Test three additional emails
test_emails = [
    "Hi! You have been selected for a FREE cash reward. Have a great day!",

    "Hello, congratulations on your gift. You can receive your money through our website.",

    "URGENT! PLEASE REVIEW THE MEETING NOTES TODAY! The school meeting has moved to 10 AM."
]

print("\nADDITIONAL EMAIL TESTS")

for email in test_emails:

    words = email.split()

    word_count = len(words)
    exclamations = email.count("!")

    money_words = 0
    all_caps = 0
    urgency_words = 0
    suspicious_links = 0

    for word in words:
        clean_word = word.lower().strip("!.,")
        
        if clean_word in [
            "money", "cash", "prize", "free",
            "reward", "bonus", "gift", "loan"
        ]:
            money_words += 1

        if clean_word in [
            "urgent", "now", "today", "claim",
            "immediately", "limited"
        ]:
            urgency_words += 1

        if len(word) > 1 and word.isupper():
            all_caps += 1

    if "http" in email.lower() or "www." in email.lower():
        suspicious_links = 1

    new_email = pd.DataFrame([[
        word_count, exclamations, money_words,
        all_caps, urgency_words, suspicious_links
    ]], columns=features)

    result = model.predict(new_email)

    if result[0] == 1:
        print("SPAM:", email)
    else:
        print("LEGITIMATE:", email)


