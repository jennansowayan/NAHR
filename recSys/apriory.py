from apyori import apriori
import pandas as pd

train_data = pd.read_csv( '/Users/shahadalmugrin/Desktop/venv2/nahrv1/train_data.csv', delim_whitespace=True, header=None)
data_len= len(train_data)


records = []
for i in range(0, data_len):
    records.append([str(train_data.values[i,j]) for j in range(1)])
print("hello")
association_rules = apriori(records, min_support=0.00001, min_confidence=0.8, min_lift=2, min_length=0)

association_results = list(association_rules)
print(records)
print(len(association_results))


for item in association_results:
    print("hello")

    # first index of the inner list
    # Contains base item and add item
    pair = item[0] 
    items = [x for x in pair]
    print("Rule: " + items[0] + " -> " + items[1])

    #second index of the inner list
    print("Support: " + str(item[1]))

    #third index of the list located at 0th
    #of the third index of the inner list

    print("Confidence: " + str(item[2][0][2]))
    print("Lift: " + str(item[2][0][3]))
    print("=====================================")


