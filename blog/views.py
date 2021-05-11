from django.http import Http404
from .models import Blog, CommentModel
from .forms import SearchForm, CommentForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
# from parse.parsing import reg_list, vb_list, mad_pl


def BlogListView(request):
    dataset = Blog.objects.all()
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            blog = Blog.objects.get(blog_title=title)
            return redirect(f'/blog/{blog.id}')
    else:
        form = SearchForm()
        context = {
            'dataset': dataset,
            'form': form,
            # "reg_list": reg_list,
            # "vb_list": vb_list,
            # "mad_pl": mad_pl,
        }
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
