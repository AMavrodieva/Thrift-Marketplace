import logging
from django.shortcuts import render


class RedirectToIndexMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, *args, **kwargs):
        return self._middleware(*args, **kwargs)

    def _middleware(self, request, *args, **kwargs):

        response = self.get_response(request, *args, **kwargs)

        if response.status_code == 500:
            return render(request, '404.html')

        return response
