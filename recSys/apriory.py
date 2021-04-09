import pandas as pd
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori, fpmax, fpgrowth, association_rules
from django.db import models
from NAHR.recSys.models import rules


train_data = pd.read_csv( '/Users/shahadalmugrin/Desktop/venv2/nahrv1/train_data.csv', delim_whitespace=True, header=None)
data_len= len(train_data)


records = []
for i in range(0, data_len):
<<<<<<< HEAD
    records.append([str(train_data.values[i,j]) for j in range(1)])
print("hello")
association_rules = apriori(records, min_support=0.00001, min_confidence=0.8, min_lift=2, min_length=0)

association_results = list(association_rules)
print(records)
print(len(association_results))
=======
    records.append([str(train_data.values[i,j]) for j in range(2)])
>>>>>>> b0e15c1de2597e0d5c7cc99433829ecfe87f4ee2

print(records)
# print("hello")
# association_rules = apriori(records, min_support=0.001, min_confidence=0.01, min_lift=1, max_length=4)
# association_results = list(association_rules)
# print(len(association_results))

# print(association_results)
# #1-store fitting rules in db as dictionary 
# #2- write recommend function get response and retrive assosiated catigories from dictonary

# rules = {}

# for item in association_results:
#     print("hello")



#     # # first index of the inner list
#     # # Contains base item and add item
#     # pair = item[0] 
#     # items = [x for x in pair]
#     # print("Rule: " + items[0] + " -> " + items[1])

#     # #second index of the inner list
#     # print("Support: " + str(item[1]))

#     # #third index of the list located at 0th
#     # #of the third index of the inner list

#     # print("Confidence: " + str(item[2][0][2]))
#     # print("Lift: " + str(item[2][0][3]))
#     # print("=====================================")

dataset = [['Milk', 'Onion', 'Nutmeg', 'Kidney Beans', 'Eggs', 'Yogurt'],
           ['Dill', 'Onion', 'Nutmeg', 'Kidney Beans', 'Eggs', 'Yogurt'],
           ['Milk', 'Apple', 'Kidney Beans', 'Eggs'],
           ['Milk', 'Unicorn', 'Corn', 'Kidney Beans', 'Yogurt'],
           ['Corn', 'Onion', 'Onion', 'Kidney Beans', 'Ice cream', 'Eggs']]


te = TransactionEncoder()
te_ary = te.fit(records).transform(records)
df = pd.DataFrame(te_ary, columns=te.columns_)
# print(df)
frequent_itemsets = fpgrowth(df, min_support=0.006, use_colnames=True)
### alternatively:
# frequent_itemsets = apriori(df, min_support=0.01, use_colnames=True)
# frequent_itemsets = fpmax(df, min_support=0.6, use_colnames=True)

print(frequent_itemsets)


rules = association_rules(frequent_itemsets, metric="lift", min_threshold=1.5)

for item in rules:
    rule(antecedents = item["antecedents"], consequents = item["consequents"])

