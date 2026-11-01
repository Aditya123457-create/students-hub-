from django.shortcuts import render

def course_list(request):
    return render(request,'course_list.html')
def course_details(request,course_id):
    return render(request,'course_details.html')

