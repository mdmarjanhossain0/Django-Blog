from django.shortcuts import render
from django.core.paginator import EmptyPage,PageNotAnInteger,Paginator
from operator import attrgetter

from blog.models import BlogPost
from blog.views import get_blog_query_set

BLOG_POST_PER_PAGE = 1

def home_screen_view(request):
	print(request.headers)

	context={}

	query = ""
	if request.GET:
		query = request.GET.get("q", "")
		context['query'] = query

	blog_posts = sorted(get_blog_query_set(query), key=attrgetter('date_updated'), reverse=True)
	



	page = request.GET.get("page", 1)
	blog_post_paginator = Paginator(blog_posts, BLOG_POST_PER_PAGE)

	try:
		blog_posts = blog_post_paginator.page(page)

	except PageNotAnInteger:
		blog_posts = blog_post_paginator.page(BLOG_POST_PER_PAGE)
	except Emtypage:
		blog_posts = blog_post_paginator.page(blog_post_paginator.num_pages)

	context['blog_posts'] = blog_posts



	return render(request,"personal/home.html",context)
