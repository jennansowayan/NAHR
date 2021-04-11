from django.shortcuts import render
from mlxtend.frequent_patterns import apriori, association_rules


# Create your views here.


def recommend(request):

    


    records = []

    e = TransactionEncoder()
    te_ary = te.fit(records).transform(records)
    df = pd.DataFrame(te_ary, columns=te.columns_)
    frequent_itemsets = apriori(df, min_support=0.01, use_colnames=True)

    print(frequent_itemsets)


    rules = association_rules(frequent_itemsets, metric="lift", min_threshold=1.5)

    for item in rules:
        rule(antecedents = item["antecedents"], consequents = item["consequents"])


    # def post(self, request):
    #     interests = request.POST.get()
    #     #store intrests
       
    # def get(self, request)   
    #     #compaire intrests with antecedents 
    #     #get all relevent consequents store in recs

    #     return recs
        

