from apyori import apriori
import pandas as pd
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori, fpmax, fpgrowth, association_rules


train_data = pd.read_csv( '/Users/jennansowayan/Nahr/NAHR/train_data.csv', header=None)
data_len= len(train_data)


records = []
for i in range(0, data_len):
    records.append([str(train_data.values[i,j]) for j in range(2)])

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
print(rules)