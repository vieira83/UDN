from django.http import HttpResponseRedirect
from django.shortcuts import render, render_to_response, get_object_or_404
from django.template import RequestContext
from udn.forms import ParticipantForm, ReviewForm
from udn.models import Participants


def participant_add(request):
    form = ParticipantForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            participant = form.save(commit=False)
            participant.save()
            return HttpResponseRedirect('results')
    return render(request, 'participants.html', {'form': form})


def participant_results(request):
    form = ReviewForm(request.POST or None)
    participants = Participants.objects.all()
    if request.method == 'POST':
        if form.is_valid():
            participant = get_object_or_404(participants, pk=request.POST.get('id'))
            participant.review = form.cleaned_data['review']
            participant.save()

    return render_to_response('results.html',
                          locals(),
                          context_instance=RequestContext(request))

