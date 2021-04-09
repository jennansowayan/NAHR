from django.shortcuts import render


# Create your views here.

# TO DO: 
#import aproiry records of the subcategories which we write
#convert the records into a list
#use aproiry func with support=0.005 and confidance=0.2 and lift=3 <- generated association rules about which subcats. are related 
# quiz view and get quiz response



# courses view 
def tech(request):
 return render(request, "tech_courses.html", {} )

def science(request):
 return render(request, "science_courses.html", {} )

def business(request):
 return render(request, "business_courses.html", {} )

def art(request):
 return render(request, "art_courses.html", {} )
# + analize response => get related subcats from the rules
# + apply recommendations    
def courses(request):
 return render(request,"courses.html",{})

def quiz(request):
  if request.method == 'POST':  #submits the quiz
       form = quizForm(request.POST) #?
       if form.is_valid():
            intrest = form.save()
			# if intrest.objects.all().count() % 10 == 0: 
			# 	generate_new_rules()
				
			# return redirect(recommned)


