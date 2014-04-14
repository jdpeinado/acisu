from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import Post

class IndexView(generic.ListView):
	template_name = 'posts/index.html'
	context_object_name = 'latest_posts_list'

	def get_queryset(self):
		latest_posts_list = Post.objects.order_by('-created')
		paginator = Paginator(latest_posts_list, 3)

		page = self.request.GET.get('page')
		try:
			latest_posts_list = paginator.page(page)
		except PageNotAnInteger:
			# If page is not an integer, deliver first page.
			latest_posts_list = paginator.page(1)
		except EmptyPage:
			# If page is out of range (e.g. 9999), deliver last page of results.
			latest_posts_list = paginator.page(paginator.num_pages)
		return latest_posts_list

class DetailView(generic.DetailView):
	model = Post
	template_name = 'posts/detail.html'

def about(request):
	return render(request, 'posts/about.html', None)

class TagView(generic.ListView):
	template_name = 'posts/tag.html'
	context_object_name = 'posts_list'

	def get_queryset(self):
		tag = self.kwargs['tag']
		posts_list = Post.objects.filter(tag=tag).order_by('-created')

		return posts_list