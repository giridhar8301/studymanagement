from django.shortcuts import render, redirect, get_object_or_404
from .models import Study
from .forms import StudyForm
from django.db.models import Q
import logging

# Set up logging
logger = logging.getLogger(__name__)

def study_list(request):
    studies = Study.objects.all()
    return render(request, 'study/study_list.html', {'studies': studies})

def add_study(request):
    if request.method == 'POST':
        form = StudyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('study_list')
    else:
        form = StudyForm()
    return render(request, 'study/add_study.html', {'form': form})

def view_study(request, id):
    study = get_object_or_404(Study, id=id)
    return render(request, 'study/view_study.html', {'study': study})

def edit_study(request, id):
    study = get_object_or_404(Study, id=id)
    if request.method == 'POST':
        form = StudyForm(request.POST, instance=study)
        if form.is_valid():
            form.save()
            return redirect('study_list')
    else:
        form = StudyForm(instance=study)
    return render(request, 'study/edit_study.html', {'form': form, 'study': study})

def delete_study(request, id):
    study = get_object_or_404(Study, id=id)
    if request.method == 'POST':
        study.delete()
        return redirect('study_list')
    return render(request, 'study/delete_study.html', {'study': study})
