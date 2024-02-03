from django.contrib import admin
from .models import Membership, Plan, Payment, Planfeature, Profile, Member




admin.site.register(Membership)
admin.site.register(Member)
admin.site.register(Plan)
admin.site.register(Planfeature)
admin.site.register(Payment)
admin.site.register(Profile)
