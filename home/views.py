from django.shortcuts import render

from django.db.models import Q


def index(request):
    return render(
        request=request,
        context={},
        template_name="home/index.html",
    )


  
def search(request):
    search_param = request.GET["search_param"]
    print("search: ", search_param)
    context_dict = dict()
  
    return render(
        request=request,
        context=context_dict,
        template_name="home/index.html",
    )  
