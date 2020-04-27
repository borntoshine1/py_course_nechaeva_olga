import pandas as pd

def mean():
    data = pd.read_csv("hw.csv", delimiter=',')
    height = data[' "Height(Inches)"'].mean() * 2.54
    weight = data[' "Weight(Pounds)"'].mean() * 0.45359

    return f"{height} / {weight}"
