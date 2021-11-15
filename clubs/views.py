from django.shortcuts import render, get_object_or_404
from .models import Club


# Create your views here.
def all_clubs(request):
    """
    To return a list of clubs.
    """

    clubs = Club.objects.all()

    context = {
        'clubs': clubs,
    }
    return render(request, 'clubs/clubs.html', context)


def club_detail(request, club_id):
    """
    To return a veiw to see a single service details.
    """

    club = get_object_or_404(Club, pk=club_id)

    context = {
        'club': club,
    }
    return render(request, 'clubs/club_detail.html', context)
