from django.utils import timezone

from datacenter.models import Visit
from django.shortcuts import render



def storage_information_view(request):
    non_closed_visits = Visit.objects.filter(leaved_at=None)
    all_non_closed_visits = []
    for visit in non_closed_visits:
        visit_info = {
            'who_entered': visit.passcard,
            'entered_at': timezone.localtime(visit.entered_at),
            'duration': Visit.format_duration(visit.get_duration()),
            'is_strange': Visit.is_visit_long(visit),
        }
        all_non_closed_visits.append(visit_info)
    context = {
        'non_closed_visits': all_non_closed_visits,
    }
    return render(request, 'storage_information.html', context)
