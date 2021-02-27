from django.shortcuts import render

from django.http import JsonResponse
from django.shortcuts import render
from dashboard.models import Sample_Information
from django.core import serializers
from .forms import SampleCodeForm
from .forms import UseSampleCodeForm
from dashboard.sample_controller import SampleController

sample_controller1 = SampleController()

def dashboard_with_pivot(request):
    return render(request, 'dashboard_with_pivot.html', {})


def pivot_data(request):
    dataset = Sample_Information.objects.all()
    data = serializers.serialize('json', dataset)
    return JsonResponse(data, safe=False)


def home_page(request):
    return render(request, 'home.html', {})


def get_sample_code(request):
    # if this is a POST request we need to process the form data
    sampleForm = SampleCodeForm(request.POST)
    useSampleForm = UseSampleCodeForm(request.POST)
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        # check whether it's valid:
        if useSampleForm.is_valid() and sampleForm.is_valid() and useSampleForm.cleaned_data['use_sample_code'] is not None:
            print('use enter')
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            sample_controller1.set_current(useSampleForm.cleaned_data['sample_code'])
            sample_controller1.use_sample(useSampleForm.cleaned_data['use_sample_code'])
            return render(request, 'use_a_sample.html', {'sampleForm': sampleForm, 'useSampleForm': useSampleForm,
                                                         'sample': sample_controller1})

        if sampleForm.is_valid():
            print('Sample form entered')
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            sample_controller1.set_current(sampleForm.cleaned_data['sample_code'])
            return render(request, 'use_a_sample.html', {'sampleForm': sampleForm, 'useSampleForm': useSampleForm,
                                                         'sample': sample_controller1})


    # if a GET (or any other method) we'll create a blank form
    else:
        sampleForm = SampleCodeForm()
        useSampleForm = UseSampleCodeForm()

    return render(request, 'use_a_sample.html', {'sampleForm': sampleForm, 'useSampleForm': useSampleForm,
                                                 'sample': sample_controller1})

