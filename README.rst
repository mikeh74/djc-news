====
News
====

This is an example reusable app.

Quick start
-----------

1. Add "news" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'news',
    ]

2. Include the polls URLconf in your project urls.py like this::

    path('news/', include('news.urls')),

3. Run `python manage.py migrate` to create the news models.

4. Start the development server and visit http://127.0.0.1:8000/admin/
   to create a news item (you'll need the Admin app enabled).

5. Visit http://127.0.0.1:8000/news/ to view all news
