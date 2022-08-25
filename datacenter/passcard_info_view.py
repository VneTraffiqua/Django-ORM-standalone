from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from . import helper_script


def passcard_info_view(request, passcode):
    passcard = get_object_or_404(Passcard, passcode=passcode)
    visits = Visit.objects.filter(passcard=passcard)
    all_visits = []
    for visit in visits:
        duration = visit.get_duration()
        visit_duration = helper_script.format_duration(duration)

        this_passcard_visits = {
                'entered_at': timezone.localtime(visit.entered_at),
                'duration': visit_duration,
                'is_strange': visit.is_visit_long()
            }
        all_visits.insert(0, this_passcard_visits)
    context = {
        'passcard': passcard,
        'this_passcard_visits': all_visits
    }

    return render(request, 'passcard_info.html', context)
