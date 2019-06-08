import pandas as pd

train_loss = []
train_auc = []

valid_loss = []
valid_auc = []

with open("results.txt") as f:
    l = f.readline()
    while l:
        l = f.readline()
        train_loss.append(float(l.split(":")[1]))
        l = f.readline()
        train_auc.append(float(l.split(":")[1]))
        l = f.readline()
        valid_loss.append(float(l.split(":")[1]))
        l = f.readline()
        valid_auc.append(float(l.split(":")[1]))
        l = f.readline()

pd.DataFrame({
    "train_loss": train_loss,
    "train_auc": train_auc,
    "valid_loss": valid_loss,
    "valid_auc": valid_auc
}).to_csv("first_results.csv")
