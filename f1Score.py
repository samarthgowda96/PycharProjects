from sklearn.metrics import f1_score


def f1_scrore(actual, predicted):
    return 2 * ((precision * recall) / (precision + recall))

actual = [0,1,2,2,1,0,1,0,2]
predicted = [0,2,1,2,0,0,1,2,2]

print(f1_scrore(actual,predicted, average=None))

