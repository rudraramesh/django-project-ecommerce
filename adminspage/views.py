import django
from django.shortcuts import render
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from users.auth import admin_only


@login_required
@admin_only
def admin_home(request):
    return render(request,'admins/adminhome.html')

