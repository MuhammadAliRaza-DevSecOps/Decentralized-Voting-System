from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.models import User
from .models import Candidate, Voter, Vote, VoteReceipt
from .blockchain import blockchain
from django.utils import timezone
from django.template.loader import get_template
from django.http import HttpResponse, JsonResponse
from collections import Counter
import matplotlib.pyplot as plt
import io, base64, qrcode
from xhtml2pdf import pisa


def home(request):
    return render(request, 'vote/home.html')


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            Voter.objects.create(user=user)
            login(request, user)
            return redirect('vote')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})


@login_required
def vote_view(request):
    voter = Voter.objects.get(user=request.user)
    candidates = Candidate.objects.all()

    if voter.has_voted:
        return render(request, 'vote/already_voted.html')

    if request.method == 'POST':
        candidate_id = request.POST['candidate']
        candidate = Candidate.objects.get(id=candidate_id)

        Vote.objects.create(voter=voter, candidate=candidate)
        voter.has_voted = True
        voter.save()

        vote_data = f"{request.user.username} voted for {candidate.name}"
        prev_hash = blockchain.get_previous_block()['hash']
        blockchain.create_block(vote_data, prev_hash)

        timestamp = timezone.now()
        VoteReceipt.objects.create(
            voter=request.user,
            candidate=candidate,
            timestamp=timestamp,
            block_hash=blockchain.get_previous_block()['hash'],
            receipt_text=vote_data
        )

        return redirect('vote_receipt', candidate_id=candidate.id)

    return render(request, 'vote/vote.html', {'candidates': candidates})


@login_required
def vote_receipt(request, candidate_id):
    voter = request.user
    candidate = Candidate.objects.get(id=candidate_id)
    timestamp = timezone.now()
    block = blockchain.get_previous_block()

    vote_info = f"{voter.username} voted for {candidate.name} at {timestamp}"

    qr = qrcode.make(vote_info)
    buffer = io.BytesIO()
    qr.save(buffer, format="PNG")
    qr_img = base64.b64encode(buffer.getvalue()).decode("utf-8")

    return render(request, "vote/vote_receipt.html", {
        "voter": voter,
        "candidate": candidate,
        "timestamp": timestamp,
        "block_hash": block['hash'],
        "qr_code": qr_img,
    })


@login_required
def generate_pdf_receipt(request, candidate_id):
    voter = request.user
    candidate = Candidate.objects.get(id=candidate_id)
    timestamp = timezone.now()
    block = blockchain.get_previous_block()

    template = get_template('vote/pdf_receipt.html')
    html = template.render({
        'voter': voter,
        'candidate': candidate,
        'timestamp': timestamp,
        'block_hash': block['hash']
    })

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="vote_receipt.pdf"'
    pisa.CreatePDF(io.BytesIO(html.encode("UTF-8")), dest=response)
    return response


@login_required
def my_receipts(request):
    receipts = VoteReceipt.objects.filter(voter=request.user).order_by('-timestamp')
    return render(request, 'vote/my_receipts.html', {'receipts': receipts})


@login_required
def live_results(request):
    return render(request, 'vote/live_results.html')


@login_required
def api_live_data(request):
    candidates = Candidate.objects.all()
    votes = Vote.objects.values_list('candidate_id', flat=True)
    vote_count = Counter(votes)

    names = []
    vote_numbers = []

    for candidate in candidates:
        names.append(candidate.name)
        vote_numbers.append(vote_count.get(candidate.id, 0))

    return JsonResponse({'names': names, 'votes': vote_numbers})


@login_required
def blockchain_viewer(request):
    chain = blockchain.get_chain()
    return render(request, 'vote/blockchain_viewer.html', {'chain': chain})
