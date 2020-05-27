from django.http import HttpResponseRedirect
from django.shortcuts import render # noqa imported unused

from group.forms import GroupCreateForm


def index(request):

    return render(request, 'index.html')


def create_group(request):

    if request.GET:
        form = GroupCreateForm(request.GET)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = GroupCreateForm(request.GET)

    context = {'create_form': form}

    return render(request, 'create_group.html', context=context)
