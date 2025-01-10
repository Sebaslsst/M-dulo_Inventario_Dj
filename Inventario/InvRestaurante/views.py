from django.shortcuts import render

def Inventario(request):
    return render(request,template_name= 'Inventario.html')
def Principal(request):
    return render(request,template_name='Principal.html')