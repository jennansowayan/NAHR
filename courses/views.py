from django.shortcuts import render
from django.shortcuts import render_to_response
from .models import{
    Course
}
# Create your views here.

# TO DO: 
#import aproiry records of the subcategories which we write
#convert the records into a list
#use aproiry func with support=0.005 and confidance=0.2 and lift=3 <- generated association rules about which subcats. are related 
# quiz view and get quiz response



# courses view 
# + analize response => get related subcats from the rules
# + apply recommendations    

def quiz(request):
  if request.method == 'POST':  #submits the quiz
		form = quizForm(request.POST) #?
		if form.is_valid():
			intrest = form.save()
			# if intrest.objects.all().count() % 10 == 0: 
			# 	generate_new_rules()
				
			# return redirect(recommned)

	else:
		form = quizForm()
	return render_to_response('courses_page.html', locals(), context_instance=RequestContext(request)) #pass the response?

def recommned(request):
	