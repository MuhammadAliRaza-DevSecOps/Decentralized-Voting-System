from django.contrib import admin
from .models import Candidate, Voter, Vote

admin.site.register(Candidate)
admin.site.register(Voter)
admin.site.register(Vote)
