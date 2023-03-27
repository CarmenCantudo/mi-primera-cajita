from django.shortcuts import render


def handler404(request, exception):
    """
    Error Handler 404 - Page Not Found
    from CI Project Ado
    """
    return render(request, "errors/404.html", status=404)