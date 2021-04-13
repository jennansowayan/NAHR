from django.shortcuts import render
from .models import Technology
from .models import Business
from .models import Science
from .models import Art
# Create your views here.

# TO DO:
# import aproiry records of the subcategories which we write
# convert the records into a list
# use aproiry func with support=0.005 and confidance=0.2 and lift=3 <- generated association rules about which subcats. are related
# quiz view and get quiz response


# courses view
def tech(request):
    return render(request, "tech_courses.html", {})


def science(request):
    return render(request, "science_courses.html", {})


def business(request):
    return render(request, "business_courses.html", {})


def art(request):
    return render(request, "art_courses.html", {})
# + analize response => get related subcats from the rules
# + apply recommendations


def courses(request):
    return render(request, "courses.html", {})


def tech(request):
    queryset = Technology.objects.all()
    context = {
        "tech_list": queryset
    }
    return render(request, "tech_courses.html", context)


def business(request):
    queryset = Business.objects.all()
    context = {
        "business_list": queryset
    }
    return render(request, "business_courses.html", context)


def science(request):
    queryset = Science.objects.all()
    context = {
        "science_list": queryset
    }
    return render(request, "science_courses.html", context)


def art(request):
    queryset = Art.objects.all()
    context = {
        "art_list": queryset
    }
    return render(request, "art_courses.html", context)
    # if intrest.objects.all().count() % 10 == 0:
    # 	generate_new_rules()

    # return redirect(recommned)
