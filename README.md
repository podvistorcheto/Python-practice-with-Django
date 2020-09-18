Hello there, 

This is full-feature app for my history blog.

It is programmed as a self-study tutorial for Python3 with Django 3.1.1.

Enjoy exploring the code!

Python Django Tutorial: Full-Featured Web App Part 11 - Pagination

To code in the shell part type django shell if you use django-shortcuts or regular command python manage.py shell. The type:

In [1]: from django.core.paginator import Paginator

In [2]: posts = ['1','2','3','4','5']

In [3]: p = Paginator(posts,2)

In [4]: p.num_pages
Out[4]: 3

In [5]: for page in p.page_range:
   ...:     print(page)
   ...: 
1
2
3

In [6]: p1 = p.page(1)

In [7]: p1
Out[7]: <Page 1 of 3>

In [8]: p1.number
Out[8]: 1

In [9]: p1.object_list
Out[9]: ['1', '2']

In [10]: p1.has_previous()
Out[10]: False

In [11]: p1.has_next()
Out[11]: True

In [12]: p1.has.next_page_number()
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)
<ipython-input-12-2041b3b011bd> in <module>
----> 1 p1.has.next_page_number()

AttributeError: 'Page' object has no attribute 'has'

In [13]: p1.next_page_number()
Out[13]: 2

In [14]: exit()
