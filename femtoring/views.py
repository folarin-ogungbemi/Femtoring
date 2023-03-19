from django.shortcuts import render


def handler400(request, exception):
    """
    Renders the custom error 400 page.
    """
    return render(request, 'error_pages/400error.html', status=400)


def handler403(request, exception):
    """
    Renders the custom error 403 page.
    """
    return render(request, 'error_pages/403error.html', status=403)


def handler404(request, exception):
    """
    Renders the custom error 404 page.
    """
    return render(request, 'error_pages/404error.html', status=404)


def handler405(request, exception):
    """
    Renders the custom error 405 page.
    """
    return render(request, 'error_pages/405error.html', status=405)


def handler500(request):
    """
    Renders the custom error 500 page.
    """
    return render(request, 'error_pages/500error.html', status=500)