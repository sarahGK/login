from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
# avoid having to hardcode a URL in the view function
from django.core.urlresolvers import reverse
# for static pages or listing pages,use generic views classes 
from django.views import generic

from .models import Spot,Reservation

# Create your views here.

def index(request):
  return HttpResponse("Welcome! Please Login first!")

class ResultsView(generic.DetailView):
  model = Reservation
  template_name = 'reservation/result.html'

'''
def results(request,id):

    reservation = get_object_or_404(Reservation, user_id=id) # search the current user's reservation and return the record or raise 404
    context = {'reservation':reservation}
    return render(request,'reservation/result.html',context)
'''
'''
def get_userid(request):
  # if this is a POST request we need to process the form data
  if request.method == 'POST':
      # create a form instance and populate it with data from the request:
      form = LoginForm(request.POST)
      # check whether it's valid:
      if form.is_valid():
          # process the data in form.cleaned_data as required
          # ...
          # redirect to a new URL:
          return HttpResponseRedirect('/thanks/')

  # if a GET (or any other method) we'll create a blank form
  else:
  #    form = LoginForm()

  return render(request, 'login.html', {'form': form})
'''
