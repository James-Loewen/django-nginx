from django.shortcuts import render
from django.http import JsonResponse


def hello_world(request):
    return render(request, "hello/index.html")


def get_client_ip(request):
    remote_addr = request.META.get("REMOTE_ADDR", None)
    x_forwarded_for = request.META.get("HTTP_X_FORWARDED_FOR", None)
    x_real_ip = request.META.get("HTTP_X_REAL_IP", None)
    return JsonResponse(
        {
            "remote_addr": remote_addr,
            "x_forwarded_for": x_forwarded_for,
            "x_real_ip": x_real_ip,
        }
    )
