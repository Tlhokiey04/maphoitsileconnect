from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Issue
from .forms import IssueForm, RegisterForm

# ── AUTH VIEWS ──────────────────────────────────────────────────

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, f'Welcome to MaphoitsileConnect, {user.first_name}!')
            return redirect('dashboard')
    else:
        form = RegisterForm()
    return render(request, 'accounts/register.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user     = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'accounts/login.html')


def user_logout(request):
    logout(request)
    return redirect('login')


@login_required
def dashboard(request):
    issues = Issue.objects.filter(user=request.user)
    context = {
        'issues':         issues,
        'total_count':    issues.count(),
        'pending_count':  issues.filter(status='pending').count(),
        'progress_count': issues.filter(status='in_progress').count(),
        'resolved_count': issues.filter(status='resolved').count(),
        'latest':         issues.first(),
    }
    return render(request, 'accounts/dashboard.html', context)


# ── REPORT VIEWS ────────────────────────────────────────────────

@login_required
def issue_list(request):
    status_filter = request.GET.get('status', '')
    issues        = Issue.objects.filter(user=request.user)
    if status_filter:
        issues = issues.filter(status=status_filter)
    context = {
        'issues':         issues,
        'status_filter':  status_filter,
        'pending_count':  Issue.objects.filter(user=request.user, status='pending').count(),
        'progress_count': Issue.objects.filter(user=request.user, status='in_progress').count(),
        'resolved_count': Issue.objects.filter(user=request.user, status='resolved').count(),
    }
    return render(request, 'reports/issue_list.html', context)


@login_required
def report_issue(request):
    if request.method == 'POST':
        form = IssueForm(request.POST, request.FILES)
        if form.is_valid():
            issue      = form.save(commit=False)
            issue.user = request.user
            issue.save()
            return redirect('issue_success', pk=issue.pk)
    else:
        form = IssueForm()
    return render(request, 'reports/report_form.html', {'form': form})


@login_required
def issue_success(request, pk):
    issue = get_object_or_404(Issue, pk=pk, user=request.user)
    return render(request, 'reports/success.html', {'issue': issue})


@login_required
def issue_detail(request, pk):
    issue = get_object_or_404(Issue, pk=pk, user=request.user)
    return render(request, 'reports/issue_detail.html', {'issue': issue})