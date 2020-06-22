import csv, io
from django.shortcuts import render
from django.contrib import messages
from .models import Profile
# Create your views here.
# one parameter named request
def profile_upload(request):
    # declaring template
    template = "profile_upload.html"
    data = Profile.objects.all()
# prompt is a context variable that can have different values      depending on their context
    prompt = {
        'order': '',
        'profiles': data
              }
    # GET request returns the value of the data with the specified key.
    if request.method == "GET":
        return render(request, template, prompt)
    csv_file = request.FILES['file']
    # let's check if it is a csv file
    if not csv_file.name.endswith('.csv'):
        messages.error(request, 'THIS IS NOT A CSV FILE')
    data_set = csv_file.read().decode('UTF-8')

    io_string = io.StringIO(data_set)
    next(io_string)
    for column in csv.reader(io_string, delimiter=',', quotechar="|"):
        created = Profile.objects.update_or_create(name=column[0],points=column[1])
    context ={}
    return render(request, template, context)


def get_points(request):
    pr = Profile.objects.order_by('-points')
    return render(request,'leaderboard.html', {'pr': pr})
