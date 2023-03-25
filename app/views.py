from django.shortcuts import render
# Create your views here.
def bootstrap_cdn_r(request):
    return render(request,'bootstrap_cdn_r.html')
def bootstrap_cdn(request):
    return render(request,'bootstrap_cdn.html')

