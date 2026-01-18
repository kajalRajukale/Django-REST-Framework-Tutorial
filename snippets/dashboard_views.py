from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from .models import Snippet
from .forms import SnippetForm

# Profile view for /accounts/profile/
from django.contrib.auth import get_user_model

def home(request):
    return render(request, 'snippets/home.html')


@login_required
def dashboard(request):
    snippets = Snippet.objects.all().order_by('-created')
    return render(request, 'snippets/dashboard.html', {'snippets': snippets})

@login_required
def snippet_add(request):
    if request.method == 'POST':
        form = SnippetForm(request.POST)
        if form.is_valid():
            snippet = form.save(commit=False)
            snippet.owner = request.user
            snippet.save()
            return redirect(reverse('snippets:dashboard'))
    else:
        form = SnippetForm()
    return render(request, 'snippets/snippet_form.html', {'form': form})

@login_required
def snippet_edit(request, pk):
    snippet = get_object_or_404(Snippet, pk=pk)
    if request.method == 'POST':
        form = SnippetForm(request.POST, instance=snippet)
        if form.is_valid():
            form.save()
            return redirect(reverse('snippets:dashboard'))
    else:
        form = SnippetForm(instance=snippet)
    return render(request, 'snippets/snippet_form.html', {'form': form, 'snippet': snippet})

@login_required
def snippet_delete(request, pk):
    snippet = get_object_or_404(Snippet, pk=pk)
    if request.method == 'POST':
        snippet.delete()
        return redirect(reverse('snippets:dashboard'))
    return render(request, 'snippets/snippet_confirm_delete.html', {'snippet': snippet})

@login_required
def snippet_preview(request, pk):
    snippet = get_object_or_404(Snippet, pk=pk)
    return render(request, 'snippets/snippet_preview.html', {'snippet': snippet})


# New profile view
@login_required
def profile(request):
    User = get_user_model()
    user = request.user
    return render(request, 'snippets/profile.html', {'user': user})
