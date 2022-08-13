from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render, get_object_or_404
from django.utils import timezone

def passcard_info_view(request, passcode):
    passcard = get_object_or_404(Passcard, passcode=passcode)
    # Программируем здесь
    visits = Visit.objects.filter(passcard=passcard)
    all_visits = []
    for visit in visits:
        duration = Visit.get_duration(visit)
        visit_duration = Visit.format_duration(duration)

        this_passcard_visits = {
                'entered_at': timezone.localtime(visit.entered_at),
                'duration': visit_duration,
                'is_strange': Visit.is_visit_long(visit)
            }
        all_visits.append(this_passcard_visits)
    all_visits.reverse()
    context = {
        'passcard': passcard,
        'this_passcard_visits': all_visits
    }

    return render(request, 'passcard_info.html', context)
