from django.http import Http404
from .models import Blog, CommentModel
from .forms import SearchForm, CommentForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required


def BlogListView(request):
    dataset = Blog.objects.all()
    context = {'dataset': dataset, }
    return render(request, 'blog/listview.html', context)


@login_required
def BlogDetailView(request, _id):
    try:
        data = Blog.objects.get(id=_id)
        data.views = data.views + 1
        data.save()
        comments = CommentModel.objects.filter(blog=data)
    except Blog.DoesNotExist:
        raise Http404('Data does not exist')

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            Comment = CommentModel(com_cont=form.cleaned_data['com_cont'],
                                   blog=data)
            Comment.save()
            return redirect(f'/blog/{_id}')
    else:
        form = CommentForm()

    context = {
        'data': data,

        'form': form,
        'comments': comments,
    }
    return render(request, 'blog/detailview.html', context)

# Create your views here.
