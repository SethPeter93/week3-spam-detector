# Week 3 Spam Detector Analysis Report


## 1. Features

My spam detector uses six features:

1. Word count
2. Number of exclamation marks
3. Money-related words
4. All-capital words
5. Urgency words
6. Suspicious links

I used urgency word since scam emails want instant action, so you dont think and are more likely to fall for the scam. 
For real emails people dont need instant action they want you to think. 

I also added suspicious links since a lot of people dont know bad from good links, so they can very easliy click a bad one and get their computer taken over. 
Most of the time emails often dont have links, so filtering out emails with links for further review felt like a good choice to me.

## 2. Split

The split is needed since it allows us to see how well the  model can identify new spam emails. Instead of just memorizing the emails it was trained on.

## 3. Percision, and Recall

Percision means how many emails were marked as spam that were actually spam. While Recall means how many spam emails the model caught.

## 4. Worse

I would rather my filter put a spam email in my inbox since missing a job email could cause you to lose that job. While a spam email in the inbox is just annoying.
To combate this I would add more features to my model to make sure important emails are not incorrectly marked spam.

## 5. Data

Now for Percision, Accuracy, and Recall the program said all were 100%. On my matrix I tested 4 of the 12 emails and it got both the spam, and none spam ones right for a total of 2 real, and 2 spam emails.
After looking over the test and training sheet I can forsure say that the 100% is way to high since the test emails were close to a few of the training ones. Which I feel gave a false 100 score of 100% I feel that in reality the score would be closer to 75. Also our data sheet is very small, and with more data the number would probably go down even if the close emails had no effect.
The feature with the most weight was the money word one which I felt would be the top. Since a most real emails dont talk about free 1000 dollars or free money. Most of the time it is spam emails that use those words, and thats why the reasult did not shock me.

## 6. Attack

To futher test my program I used 3 more tricky emails to see if my bot would detect them or not. 
 "Hi! You have been selected for a FREE cash reward. Have a great day!",

Hello, congratulations on your gift. 

You can receive your money through our website.

URGENT! PLEASE REVIEW THE MEETING NOTES TODAY! The school meeting has moved to 10 AM.

The result for this were ok the first two I wanted the bot to detect the first 2 as spam, and it did so I was happy. Sadly it got the last one wrong, this happened because of the use of the word urgent. The bot saw this as oh this must be spam since the email wants instant action. When in reailty it was for a meeting changing times.
For that reason I would not use this bot without some more work because I would not want to miss a meeting.

 
