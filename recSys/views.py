from django.shortcuts import render
import apriory

# Create your views here.


class recommend(View):
    def post(self, request):
        interests = request.POST.get()
        #store intrests
       
    def get(self, request)   
        #compaire intrests with antecedents 
        #get all relevent consequents store in recs

        return recs
        

