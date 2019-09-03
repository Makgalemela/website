from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Post
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin,  UserPassesTestMixin
from django.contrib.auth.models import User
def index(request):
	# context = {
	# 'posts' : Post.objects.all()
	# }
	return render(request , 'index/base.html')


class PostListView(ListView):
	model = Post;
	template_name = 'index/index.html'
	context_object_name ='posts'
	ordering = ['-date_posted']
	paginate_by = 5

class UserPostListView(ListView):
	model = Post;
	template_name = 'index/user_post.html'
	context_object_name ='posts'
	paginate_by = 5

	def get_query_set(self):
		user = get_object_or_404(User, username=self.kwargs.get('username'))
		# return Post.objects.filter(author=user).ordered_by('-date_posted')

class PostDetailView(DetailView):
	model = Post
	template_name = 'index/detail.html'

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin,DeleteView):
	model = Post
	success_url ='/'
	# def test_func(self):
	# 	post = self.get_object()
	# 	if self.request.user == post.author:
	# 		return True
	# 	return False
	def test_func(self):
		# post = self.get_object()
		# if self.request.user == post.author:
		if self.request.user.username == 'admin':
			return True
		return False

class PostCreateView(LoginRequiredMixin, UserPassesTestMixin,CreateView ):
	model = Post
	fields = ['title', 'content']
	# template_name = 'index/detail.html'
	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)

	def test_func(self):
		# post = self.get_object()
		# if self.request.user == post.author:
		if self.request.user.username == 'admin':
			return True
		return False

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView ):
	model = Post
	fields = ['title', 'content']

	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)
	def test_func(self):
		# post = self.get_object()
		# if self.request.user == post.author:
		if self.request.user.username == 'admin':
			return True
		return False
	

def about(request):
	return render(request , 'index/about.html', {'title' : 'About'})


def base(request):
	return render(request , 'index/base.html')
