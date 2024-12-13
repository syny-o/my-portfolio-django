from django.shortcuts import render
from django.http import JsonResponse

from .models import Contact
from .api.serializers import ContactSerializer


# only for DEBUG MODE
from django.views.decorators.csrf import csrf_exempt
@csrf_exempt
def receive_contact_from_api(request):

    all_contacts = Contact.objects.all()

    if request.method == 'GET':
        return JsonResponse({'contacts': list(all_contacts.values())}, safe=False)


    if request.method == 'POST':

        print('TEST' + str(request.POST))

        serializer = ContactSerializer(data=request.POST)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        
        return JsonResponse(serializer.errors, status=400)
