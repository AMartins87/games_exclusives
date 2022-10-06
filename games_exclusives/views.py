from django.shortcuts import render


def handler404(request, exception):
    """
    Handler for bad request 404
    """
    return render(request, "errors/404.html", status=404)
