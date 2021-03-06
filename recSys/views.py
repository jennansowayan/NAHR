from django.shortcuts import render
from mlxtend.frequent_patterns import apriori, association_rules
from mlxtend.preprocessing import TransactionEncoder
import pandas as pd
from .models import rules
from django.http import HttpResponse
from accounts.models import intrest
from courses import views, models
from itertools import chain

# Create your views here.


def generate_rules(self):
    records = [  # 2
        ['prog', 'ai'],
        ['prog', 'ai'],
        ['prog', 'ai'],
        ['prog', 'ai'],
        ['prog', 'ai'],
        ['prog', 'ai'],
        ['prog', 'ai'],
        ['prog', 'ai'],
        ['prog', 'cyber'],
        ['prog', 'cyber'],
        ['prog', 'cyber'],
        ['prog', 'cyber'],
        ['prog', 'cyber'],
        ['prog', 'cyber'],
        ['prog', 'cyber'],
        ['prog', 'cyber'],
        ['prog', 'phy'],
        ['prog', 'phy'],
        ['prog', 'phy'],
        ['prog', 'math'],
        ['prog', 'math'],
        ['prog', 'math'],
        ['prog', 'math'],
        ['prog', 'math'],
        ['prog', 'math'],
        ['prog', 'math'],
        ['prog', 'math'],
        ['prog', 'math'],
        ['prog', 'math'],
        ['prog', 'math'],
        ['prog', 'math'],
        ['prog', 'pm'],
        ['prog', 'pm'],
        ['prog', 'pm'],
        ['prog', 'da'],
        ['prog', 'da'],
        ['prog', 'da'],
        # end prog 2
        ['ai', 'prog'],
        ['ai', 'prog'],
        ['ai', 'prog'],
        ['ai', 'prog'],
        ['ai', 'prog'],
        ['ai', 'prog'],
        ['ai', 'prog'],
        ['ai', 'prog'],
        ['ai', 'cyber'],
        ['ai', 'cyber'],
        ['ai', 'cyber'],
        ['ai', 'cyber'],
        ['ai', 'phy'],
        ['ai', 'phy'],
        ['ai', 'math'],
        ['ai', 'math'],
        ['ai', 'math'],
        ['ai', 'math'],
        ['ai', 'math'],
        ['ai', 'pm'],
        ['ai', 'pm'],
        ['ai', 'da'],
        ['ai', 'da'],
        # end ai 2
        ['cyber', 'prog'],
        ['cyber', 'prog'],
        ['cyber', 'prog'],
        ['cyber', 'prog'],
        ['cyber', 'prog'],
        ['cyber', 'prog'],
        ['cyber', 'prog'],
        ['cyber', 'prog'],
        ['cyber', 'prog'],
        ['cyber', 'ai'],
        ['cyber', 'ai'],
        ['cyber', 'ai'],
        ['cyber', 'ai'],
        ['cyber', 'phy'],
        ['cyber', 'math'],
        ['cyber', 'math'],
        ['cyber', 'math'],
        ['cyber', 'math'],
        ['cyber', 'pm'],
        ['cyber', 'da'],
        # end cyber 2
        ['chem', 'math'],
        ['chem', 'math'],
        ['chem', 'math'],
        ['chem', 'phy'],
        ['chem', 'phy'],
        ['chem', 'phy'],
        ['chem', 'phy'],
        ['chem', 'phy'],
        ['chem', 'bio'],
        ['chem', 'bio'],
        ['chem', 'bio'],
        ['chem', 'bio'],
        ['chem', 'bio'],
        # end chem 2
        ['phy', 'prog'],
        ['phy', 'prog'],
        ['phy', 'prog'],
        ['phy', 'ai'],
        ['phy', 'ai'],
        ['phy', 'cyber'],
        ['phy', 'chem'],
        ['phy', 'chem'],
        ['phy', 'chem'],
        ['phy', 'chem'],
        ['phy', 'chem'],
        ['phy', 'bio'],
        ['phy', 'bio'],
        ['phy', 'bio'],
        ['phy', 'math'],
        ['phy', 'math'],
        ['phy', 'math'],
        ['phy', 'math'],
        ['phy', 'da'],
        ['phy', 'da'],
        # end phy 2
        ['bio', 'phy'],
        ['bio', 'phy'],
        ['bio', 'phy'],
        ['bio', 'chem'],
        ['bio', 'chem'],
        ['bio', 'chem'],
        ['bio', 'chem'],
        ['bio', 'chem'],
        ['bio', 'math'],
        ['bio', 'math'],
        # end bio 2
        ['math', 'prog'],
        ['math', 'prog'],
        ['math', 'prog'],
        ['math', 'prog'],
        ['math', 'prog'],
        ['math', 'prog'],
        ['math', 'prog'],
        ['math', 'prog'],
        ['math', 'prog'],
        ['math', 'prog'],
        ['math', 'prog'],
        ['math', 'prog'],
        ['math', 'ai'],
        ['math', 'ai'],
        ['math', 'ai'],
        ['math', 'ai'],
        ['math', 'ai'],
        ['math', 'cyber'],
        ['math', 'cyber'],
        ['math', 'cyber'],
        ['math', 'cyber'],
        ['math', 'chem'],
        ['math', 'chem'],
        ['math', 'chem'],
        ['math', 'phy'],
        ['math', 'phy'],
        ['math', 'phy'],
        ['math', 'phy'],
        ['math', 'bio'],
        ['math', 'bio'],
        ['math', 'acc'],
        ['math', 'acc'],
        ['math', 'acc'],
        ['math', 'acc'],
        ['math', 'acc'],
        ['math', 'acc'],
        ['math', 'acc'],
        ['math', 'acc'],
        ['math', 'acc'],
        ['math', 'acc'],
        ['math', 'da'],
        ['math', 'da'],
        # end math 2
        ['pm', 'prog'],
        ['pm', 'prog'],
        ['pm', 'prog'],
        ['pm', 'ai'],
        ['pm', 'ai'],
        ['pm', 'cyber'],
        ['pm', 'acc'],
        ['pm', 'acc'],
        ['pm', 'acc'],
        ['pm', 'acc'],
        ['pm', 'acc'],
        ['pm', 'mark'],
        ['pm', 'mark'],
        ['pm', 'mark'],
        ['pm', 'mark'],
        ['pm', 'mark'],
        ['pm', 'mark'],
        ['pm', 'fash'],
        ['pm', 'fash'],
        ['pm', 'fash'],
        ['pm', 'fash'],
        ['pm', 'music'],
        ['pm', 'music'],
        ['pm', 'music'],
        ['pm', 'da'],
        ['pm', 'da'],
        # end pm 2
        ['acc', 'math'],
        ['acc', 'math'],
        ['acc', 'math'],
        ['acc', 'math'],
        ['acc', 'math'],
        ['acc', 'math'],
        ['acc', 'math'],
        ['acc', 'math'],
        ['acc', 'math'],
        ['acc', 'math'],
        ['acc', 'pm'],
        ['acc', 'pm'],
        ['acc', 'pm'],
        ['acc', 'pm'],
        ['acc', 'pm'],
        ['acc', 'mark'],
        ['acc', 'mark'],
        # end acc 2
        ['mark', 'pm'],
        ['mark', 'pm'],
        ['mark', 'pm'],
        ['mark', 'pm'],
        ['mark', 'pm'],
        ['mark', 'pm'],
        ['mark', 'acc'],
        ['mark', 'acc'],
        ['mark', 'fash'],
        ['mark', 'fash'],
        ['mark', 'fash'],
        ['mark', 'fash'],
        ['mark', 'fash'],
        ['mark', 'music'],
        ['mark', 'music'],
        ['mark', 'music'],
        ['mark', 'music'],
        ['mark', 'music'],
        ['mark', 'da'],
        ['mark', 'da'],
        ['mark', 'da'],
        # end mark 2
        ['fash', 'pm'],
        ['fash', 'pm'],
        ['fash', 'pm'],
        ['fash', 'pm'],
        ['fash', 'mark'],
        ['fash', 'mark'],
        ['fash', 'mark'],
        ['fash', 'mark'],
        ['fash', 'mark'],
        ['fash', 'music'],
        ['fash', 'music'],
        ['fash', 'music'],
        ['fash', 'da'],
        ['fash', 'da'],
        ['fash', 'da'],
        ['fash', 'da'],
        ['fash', 'da'],
        ['fash', 'da'],
        # end fash 2
        ['music', 'pm'],
        ['music', 'pm'],
        ['music', 'pm'],
        ['music', 'mark'],
        ['music', 'mark'],
        ['music', 'mark'],
        ['music', 'mark'],
        ['music', 'mark'],
        ['music', 'fash'],
        ['music', 'fash'],
        ['music', 'fash'],
        ['music', 'da'],
        ['music', 'da'],
        ['music', 'da'],
        # end music 2
        ['da', 'prog'],
        ['da', 'prog'],
        ['da', 'prog'],
        ['da', 'ai'],
        ['da', 'ai'],
        ['da', 'cyber'],
        ['da', 'phy'],
        ['da', 'phy'],
        ['da', 'math'],
        ['da', 'math'],
        ['da', 'pm'],
        ['da', 'pm'],
        ['da', 'mark'],
        ['da', 'mark'],
        ['da', 'mark'],
        ['da', 'fash'],
        ['da', 'fash'],
        ['da', 'fash'],
        ['da', 'fash'],
        ['da', 'fash'],
        ['da', 'fash'],
        ['da', 'music'],
        ['da', 'music'],
        ['da', 'music'],
        # end da 2
        ###################################
        # 3
        ['prog', 'ai', 'cyber'],
        ['prog', 'ai', 'cyber'],
        ['prog', 'ai', 'cyber'],
        ['prog', 'ai', 'cyber'],
        ['prog', 'ai', 'cyber'],
        ['prog', 'ai', 'phy'],
        ['prog', 'ai', 'phy'],
        ['prog', 'ai', 'phy'],
        ['prog', 'ai', 'phy'],
        ['prog', 'ai', 'math'],
        ['prog', 'ai', 'math'],
        ['prog', 'ai', 'math'],
        ['prog', 'ai', 'math'],
        ['prog', 'ai', 'pm'],
        ['prog', 'ai', 'pm'],
        ['prog', 'ai', 'pm'],
        ['prog', 'ai', 'da'],
        ['prog', 'ai', 'da'],
        # end prog ai
        ['prog', 'cyber', 'ai'],
        ['prog', 'cyber', 'ai'],
        ['prog', 'cyber', 'ai'],
        ['prog', 'cyber', 'ai'],
        ['prog', 'cyber', 'ai'],
        ['prog', 'cyber', 'phy'],
        ['prog', 'cyber', 'phy'],
        ['prog', 'cyber', 'math'],
        ['prog', 'cyber', 'math'],
        ['prog', 'cyber', 'math'],
        ['prog', 'cyber', 'math'],
        ['prog', 'cyber', 'da'],
        ['prog', 'cyber', 'da'],
        ['prog', 'cyber', 'pm'],
        ['prog', 'cyber', 'pm'],
        # end prog cyber
        ['prog', 'phy', 'ai'],
        ['prog', 'phy', 'ai'],
        ['prog', 'phy', 'cyber'],
        ['prog', 'phy', 'cyber'],
        ['prog', 'phy', 'math'],
        ['prog', 'phy', 'math'],
        ['prog', 'phy', 'math'],
        ['prog', 'phy', 'da'],
        # end prog phy
        ['prog', 'math', 'ai'],
        ['prog', 'math', 'ai'],
        ['prog', 'math', 'ai'],
        ['prog', 'math', 'ai'],
        ['prog', 'math', 'cyber'],
        ['prog', 'math', 'cyber'],
        ['prog', 'math', 'cyber'],
        ['prog', 'math', 'cyber'],
        ['prog', 'math', 'phy'],
        ['prog', 'math', 'phy'],
        ['prog', 'math', 'phy'],
        ['prog', 'math', 'da'],
        # end prog math
        ['prog', 'pm', 'ai'],
        ['prog', 'pm', 'ai'],
        ['prog', 'pm', 'ai'],
        ['prog', 'pm', 'cyber'],
        ['prog', 'pm', 'cyber'],
        ['prog', 'pm', 'da'],
        # end prog pm
        ['prog', 'da', 'ai'],
        ['prog', 'da', 'ai'],
        ['prog', 'da', 'cyber'],
        ['prog', 'da', 'cyber'],
        ['prog', 'da', 'phy'],
        ['prog', 'da', 'phy'],
        ['prog', 'da', 'math'],
        ['prog', 'da', 'math'],
        ['prog', 'da', 'math'],
        ['prog', 'da', 'pm'],
        ['prog', 'da', 'pm'],
        # end prog da
        # end prog 3
        ['ai', 'prog', 'cyber'],
        ['ai', 'prog', 'cyber'],
        ['ai', 'prog', 'cyber'],
        ['ai', 'prog', 'cyber'],
        ['ai', 'prog', 'cyber'],
        ['ai', 'prog', 'phy'],
        ['ai', 'prog', 'phy'],
        ['ai', 'prog', 'phy'],
        ['ai', 'prog', 'phy'],
        ['ai', 'prog', 'math'],
        ['ai', 'prog', 'math'],
        ['ai', 'prog', 'math'],
        ['ai', 'prog', 'math'],
        ['ai', 'prog', 'pm'],
        ['ai', 'prog', 'pm'],
        ['ai', 'prog', 'pm'],
        ['ai', 'prog', 'da'],
        ['ai', 'prog', 'da'],
        # end ai prog
        ['ai', 'cyber', 'prog'],
        ['ai', 'cyber', 'prog'],
        ['ai', 'cyber', 'prog'],
        ['ai', 'cyber', 'prog'],
        ['ai', 'cyber', 'prog'],
        ['ai', 'cyber', 'phy'],
        ['ai', 'cyber', 'math'],
        ['ai', 'cyber', 'da'],
        # end ai cyber
        ['ai', 'phy', 'prog'],
        ['ai', 'phy', 'cyber'],
        ['ai', 'phy', 'math'],
        ['ai', 'phy', 'da'],
        # end ai phy
        ['ai', 'math', 'prog'],
        ['ai', 'math', 'cyber'],
        ['ai', 'math', 'phy'],
        ['ai', 'math', 'da'],
        # end ai math
        ['ai', 'pm', 'prog'],
        ['ai', 'pm', 'cyber'],
        ['ai', 'pm', 'da'],
        # end ai pm
        ['ai', 'da', 'prog'],
        ['ai', 'da', 'cyber'],
        ['ai', 'da', 'phy'],
        ['ai', 'da', 'math'],
        ['ai', 'da', 'pm'],
        # end ai da
        ['cyber', 'prog', 'ai'],
        ['cyber', 'prog', 'phy'],
        ['cyber', 'prog', 'math'],
        ['cyber', 'prog', 'pm'],
        ['cyber', 'prog', 'da'],
        # end cyber prog
        ['cyber', 'ai', 'prog'],
        ['cyber', 'ai', 'phy'],
        ['cyber', 'ai', 'math'],
        ['cyber', 'ai', 'pm'],
        ['cyber', 'ai', 'da'],
        # end cyber ai
        ['cyber', 'phy', 'prog'],
        ['cyber', 'phy', 'ai'],
        ['cyber', 'phy', 'math'],
        ['cyber', 'phy', 'da'],
        # end cyber phy
        ['cyber', 'math', 'prog'],
        ['cyber', 'math', 'ai'],
        ['cyber', 'math', 'phy'],
        ['cyber', 'math', 'da'],
        # end cyber math
        ['cyber', 'pm', 'prog'],
        ['cyber', 'pm', 'ai'],
        ['cyber', 'pm', 'da'],
        # end cyber pm
        ['cyber', 'da', 'prog'],
        ['cyber', 'da', 'ai'],
        ['cyber', 'da', 'phy'],
        ['cyber', 'da', 'math'],
        ['cyber', 'da', 'pm'],
        # end cyber da
        # end cyber 3
        ['chem', 'phy', 'bio'],
        ['chem', 'phy', 'math'],
        # end chem phy
        ['chem', 'bio', 'phy'],
        ['chem', 'bio', 'math'],
        # end chem bio
        ['chem', 'math', 'phy'],
        ['chem', 'math', 'bio'],
        # end chem math
        # end chem 3
        ['phy', 'prog', 'ai'],
        ['phy', 'prog', 'cyber'],
        ['phy', 'prog', 'math'],
        ['phy', 'prog', 'da'],
        # end phy prog
        ['phy', 'ai', 'prog'],
        ['phy', 'ai', 'cyber'],
        ['phy', 'ai', 'math'],
        ['phy', 'ai', 'prog'],
        ['phy', 'ai', 'da'],
        # end phy ai
        ['phy', 'cyber', 'prog'],
        ['phy', 'cyber', 'ai'],
        ['phy', 'cyber', 'matb'],
        ['phy', 'cyber', 'da'],
        # end phy cyber
        ['phy', 'chem', 'bio'],
        ['phy', 'chem', 'math'],
        # end phy chem
        ['phy', 'bio', 'chem'],
        ['phy', 'bio', 'math'],
        # end phy bio
        ['phy', 'math', 'prog'],
        ['phy', 'math', 'ai'],
        ['phy', 'math', 'cyber'],
        ['phy', 'math', 'chem'],
        ['phy', 'math', 'bio'],
        ['phy', 'math', 'da'],
        # end phy math
        ['phy', 'da', 'prog'],
        ['phy', 'da', 'ai'],
        ['phy', 'da', 'cyber'],
        ['phy', 'da', 'math'],
        # end phy da
        # end phy 3
        ['bio', 'chem', 'phy'],
        ['bio', 'chem', 'math'],
        # end bio chem
        ['bio', 'phy', 'chem'],
        ['bio', 'phy', 'math'],
        # end bio phy
        ['bio', 'math', 'chem'],
        ['bio', 'math', 'phy'],
        # end bio math
        # end bio 3
        ['math', 'prog', 'ai'],
        ['math', 'prog', 'cyber'],
        ['math', 'prog', 'phy'],
        ['math', 'prog', 'da'],
        # end math prog
        ['math', 'ai', 'prog'],
        ['math', 'ai', 'cyber'],
        ['math', 'ai', 'phy'],
        ['math', 'ai', 'da'],
        # end math ai
        ['math', 'cyber', 'prog'],
        ['math', 'cyber', 'ai'],
        ['math', 'cyber', 'phy'],
        ['math', 'cyber', 'da'],
        # end math cyber
        ['math', 'chem', 'phy'],
        ['math', 'chem', 'bio'],
        # end math chem
        ['math', 'phy', 'prog'],
        ['math', 'phy', 'ai'],
        ['math', 'phy', 'cyber'],
        ['math', 'phy', 'chem'],
        ['math', 'phy', 'bio'],
        ['math', 'phy', 'da'],
        # end math phy
        ['math', 'bio', 'chem'],
        ['math', 'bio', 'phy'],
        # end math bio
        ['math', 'da', 'prog'],
        ['math', 'da', 'ai'],
        ['math', 'da', 'cyber'],
        ['math', 'da', 'phy'],
        # end math da
        # end math 3
        ['pm', 'prog', 'ai'],
        ['pm', 'prog', 'cyber'],
        ['pm', 'prog', 'da'],
        # end pm prog
        ['pm', 'ai', 'prog'],
        ['pm', 'ai', 'cyber'],
        ['pm', 'ai', 'da'],
        # end pm ai
        ['pm', 'cyber', 'prog'],
        ['pm', 'cyber', 'ai'],
        ['pm', 'cyber', 'da'],
        # end pm cyber
        ['pm', 'acc', 'mark'],
        # end pm acc
        ['pm', 'mark', 'fash'],
        ['pm', 'mark', 'music'],
        ['pm', 'mark', 'da'],
        # end pm mark
        ['pm', 'fash', 'mark'],
        ['pm', 'fash', 'music'],
        ['pm', 'fash', 'da'],
        # end pm fash
        ['pm', 'music', 'mark'],
        ['pm', 'music', 'fash'],
        ['pm', 'music', 'da'],
        # end pm music
        ['pm', 'da', 'prog'],
        ['pm', 'da', 'ai'],
        ['pm', 'da', 'cyber'],
        ['pm', 'da', 'mark'],
        ['pm', 'da', 'fash'],
        ['pm', 'da', 'music'],
        # end pm da
        # end pm 3
        ['acc', 'pm', 'mark'],
        # end acc pm
        ['acc', 'mark', 'pm'],
        # end acc mark
        # end acc 3
        ['mark', 'pm', 'acc'],
        ['mark', 'pm', 'fash'],
        ['mark', 'pm', 'music'],
        ['mark', 'pm', 'da'],
        # end mark pm
        ['mark', 'acc', 'pm'],
        # end mark acc
        ['mark', 'fash', 'pm'],
        ['mark', 'fash', 'music'],
        ['mark', 'fash', 'da'],
        # end mark fash
        ['mark', 'music', 'pm'],
        ['mark', 'music', 'fash'],
        ['mark', 'music', 'da'],
        # end mark music
        ['mark', 'da', 'pm'],
        ['mark', 'da', 'fash'],
        ['mark', 'da', 'music'],
        # end mark da
        ['fash', 'pm', 'mark'],
        ['fash', 'pm', 'music'],
        ['fash', 'pm', 'da'],
        # end fash pm
        ['fash', 'mark', 'pm'],
        ['fash', 'mark', 'music'],
        ['fash', 'mark', 'da'],
        # end fash mark
        ['fash', 'music', 'pm'],
        ['fash', 'music', 'music'],
        ['fash', 'music', 'da'],
        # end fash music
        ['fash', 'da', 'pm'],
        ['fash', 'da', 'mark'],
        ['fash', 'da', 'music'],
        # end fash da
        ['music', 'pm', 'fash'],
        ['music', 'pm', 'music'],
        ['music', 'pm', 'da'],
        # end music pm
        ['music', 'mark', 'pm'],
        ['music', 'mark', 'fash'],
        ['music', 'mark', 'da'],
        # end music mark
        ['music', 'fash', 'pm'],
        ['music', 'fash', 'mark'],
        ['music', 'fash', 'da'],
        # end music fash
        ['music', 'da', 'pm'],
        ['music', 'da', 'mark'],
        ['music', 'da', 'fash'],
        # end music da
        # end music 3
        ['da', 'prog', 'ai'],
        ['da', 'prog', 'cyber'],
        ['da', 'prog', 'phy'],
        ['da', 'prog', 'math'],
        ['da', 'prog', 'pm'],
        # end da prog
        ['da', 'ai', 'prog'],
        ['da', 'ai', 'cyber'],
        ['da', 'ai', 'phy'],
        ['da', 'ai', 'math'],
        ['da', 'ai', 'pm'],
        # end da ai
        ['da', 'cyber', 'prog'],
        ['da', 'cyber', 'ai'],
        ['da', 'cyber', 'phy'],
        ['da', 'cyber', 'math'],
        ['da', 'cyber', 'pm'],
        # end da cyber
        ['da', 'phy', 'prog'],
        ['da', 'phy', 'ai'],
        ['da', 'phy', 'cyber'],
        ['da', 'phy', 'math'],
        # end da phy
        ['da', 'math', 'prog'],
        ['da', 'math', 'ai'],
        ['da', 'math', 'cyber'],
        ['da', 'math', 'phy'],
        # end da math
        ['da', 'pm', 'prog'],
        ['da', 'pm', 'ai'],
        ['da', 'pm', 'cyber'],
        ['da', 'pm', 'mark'],
        ['da', 'pm', 'fash'],
        ['da', 'pm', 'music'],
        # end da pm
        ['da', 'mark', 'pm'],
        ['da', 'mark', 'fash'],
        ['da', 'mark', 'music'],
        # end da mark
        ['da', 'fash', 'pm'],
        ['da', 'fash', 'mark'],
        ['da', 'fash', 'music'],
        # end da fash
        ['da', 'music', 'pm'],
        ['da', 'music', 'mark'],
        ['da', 'music', 'fash']]

    te = TransactionEncoder()
    te_ary = te.fit(records).transform(records)
    df = pd.DataFrame(te_ary, columns=te.columns_)

    frequent_itemsets = apriori(df, min_support=0.01, use_colnames=True)

    print(frequent_itemsets)

    rule = association_rules(
        frequent_itemsets, metric="lift", min_threshold=1.5)

    rule["antecedents"] = rule["antecedents"].apply(
        lambda x: ', '.join(list(x))).astype("unicode")
    rule["consequents"] = rule["consequents"].apply(
        lambda x: ', '.join(list(x))).astype("unicode")

    for ind in rule.index:
        ant = rule['antecedents'][ind]
        con = rule['consequents'][ind]
        r = rules(antecedents=ant, consequents=con)
        r.save()

    return HttpResponse("success")


def recommend(request):
    l = []
    #i = intrest.objects.all()
    i = intrest.objects.last().intrests
    l.extend(i)
    r = rules.objects.all()

    for item in i:
        for rule in r:
            print(rule.antecedents)

            if item == rule.antecedents:
                l.extend([rule.consequents])
               # print(rule.antecedents)

    print(l)
    techlist = models.Technology.objects.all()
    artlist = models.Art.objects.all()
    businesslist = models.Business.objects.all()
    sciencelist = models.Science.objects.all()
    interestslist = i

    if 'mark' in l and 'music' in l and 'cyber' in l or 'mark' in l and 'da' in l and 'cyber' in l or 'mark' in l and 'fash' in l and 'cyber' in l or 'pm' in l and 'music' in l and 'cyber' in l or 'pm' in l and 'da' in l and 'cyber' in l or 'pm' in l and 'fash' in l and 'cyber' in l or 'acc' in l and 'music' in l and 'cyber' in l or 'acc' in l and 'da' in l and 'cyber' in l or 'acc' in l and 'fash' in l and 'cyber' in l:
        queryset = chain(businesslist, artlist, techlist)

    elif 'phy' in l and 'cyber' in l and 'music' in l or 'phy' in l and 'da' in l and 'cyber' in l or 'phy' in l and 'fash' in l and 'cyber' in l or 'chem' in l and 'music' in l and 'cyber' in l or 'chem' in l and 'da' in l and 'cyber' in l or 'chem' in l and 'fash' in l and 'cyber' in l or 'bio' in l and 'cyber' in l and 'music' in l or 'bio' in l and 'cyber' in l and 'da' in l or 'bio' in l and 'fash' in l and 'cyber' in l or 'phy' in l and 'prog' in l and 'music' in l or 'phy' in l and 'da' in l and 'prog' in l or 'phy' in l and 'fash' in l and 'prog' in l or 'chem' in l and 'music' in l and 'cyber' in l or 'chem' in l and 'da' in l and 'cyber' in l or 'chem' in l and 'fash' in l and 'cyber' in l or 'bio' in l and 'cyber' in l and 'music' in l or 'bio' in l and 'prog' in l and 'da' in l or 'bio' in l and 'fash' in l and 'prog' in l or 'phy' in l and 'ai' in l and 'music' in l or 'phy' in l and 'da' in l and 'ai' in l or 'phy' in l and 'fash' in l and 'ai' in l or 'chem' in l and 'music' in l and 'ai' in l or 'chem' in l and 'da' in l and 'ai' in l or 'chem' in l and 'fash' in l and 'ai' in l or 'bio' in l and 'ai' in l and 'music' in l in l or 'bio' in l and 'ai' in l and 'da' in l or 'bio' in l and 'fash' in l and 'ai' in l:
        queryset = chain(sciencelist, artlist, techlist)

    elif 'mark' in l and 'music' in l or 'mark' in l and 'da' in l or 'mark' in l and 'fash' in l or 'pm' in l and 'music' in l or 'pm' in l and 'da' in l or 'pm' in l and 'fash' in l or 'mark' in l and 'music' in l or 'acc' in l and 'da' in l or 'acc' in l and 'fash' in l:
        queryset = chain(businesslist, artlist)

    elif 'cyber' in l and 'music' in l or 'cyber' in l and 'da' in l or 'cyber' in l and 'fash' in l or 'prog' in l and 'music' in l or 'prog' in l and 'da' in l or 'prog' in l and 'fash' in l or 'ai' in l and 'music' in l or 'ai' in l and 'da' in l or 'ai' in l and 'fash' in l:
        queryset = chain(techlist, artlist)

    elif 'cyber' in l and 'acc' in l or 'cyber' in l and 'pm' in l or 'cyber' in l and 'mark' in l or 'prog' in l and 'pm' in l or 'prog' in l and 'acc' in l or 'prog' in l and 'mark' in l or 'ai' in l and 'acc' in l or 'ai' in l and 'pm' in l or 'ai' in l and 'mark' in l:
        queryset = chain(techlist, businesslist)

    elif 'phy' in l and 'music' in l or 'phy' in l and 'da' in l or 'phy' in l and 'fash' in l or 'chem' in l and 'music' in l or 'chem' in l and 'da' in l or 'chem' in l and 'fash' in l or 'bio' in l and 'music' in l or 'bio' in l and 'da' in l or 'bio' in l and 'fash' in l:
        queryset = chain(sciencelist, artlist)

    elif 'phy' in l and 'mark' in l or 'phy' in l and 'acc' in l or 'phy' in l and 'pm' in l or 'chem' in l and 'acc' in l or 'chem' in l and 'mark' in l or 'chem' in l and 'pm' in l or 'bio' in l and 'mark' in l or 'bio' in l and 'acc' in l or 'bio' in l and 'pm' in l:
        queryset = chain(sciencelist, businesslist)

    elif 'cyber' in l and 'math' in l or 'ai' in l and 'math' in l or 'prog' in l and 'math' in l or 'cyber' in l or 'ai' in l or 'prog' in l:
        queryset = techlist

    elif 'music' in l or 'da' in l or 'fash' in l:
        queryset = artlist

    elif 'mark' in l or 'acc' in l or 'pm' in l:
        queryset = businesslist

    elif 'bio' in l or 'chem' in l or 'phy' in l or 'math' in l:
        queryset = sciencelist

    else:
        queryset = chain(techlist, artlist, sciencelist, businesslist)
    context = {
        "course_list": queryset
    }

    return render(request, "courses.html", context)