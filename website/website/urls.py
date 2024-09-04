from django.contrib import admin
from django.urls import path


from django.core.cache import cache
from django.http import HttpResponse


def factorial_with_cache(request, n):
    n = int(n)

    # Check if the result is already in the cache
    result = cache.get(f"factorial_{n}")

    if result is None:
        # If not in the cache, calculate the factorial
        result = 1
        for i in range(1, n + 1):
            result *= i
        cache.set(f"factorial_{n}", result, 60)  # Cache for 60 seconds

    return HttpResponse(f"Factorial of {n} is: {result}")


urlpatterns = [
    path("admin/", admin.site.urls),
    path("factorial/<int:n>/", factorial_with_cache, name="factorial_with_cache"),
]
