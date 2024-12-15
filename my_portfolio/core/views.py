from django.shortcuts import render
from django.http import JsonResponse
from django.core.mail import send_mail

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


        serializer = ContactSerializer(data=request.POST)
        if serializer.is_valid():
            serializer.save()
        
            # Extract concrete values from the serializer
            message = serializer.validated_data.get('message', 'No message provided')
            email = serializer.validated_data.get('email', 'No email provided')
            name = serializer.validated_data.get('name', 'Anonymous')

            # Send the email
            send_mail(
                subject=f'{name} sent you a message on your web portfolio',
                message=message,
                from_email=email,
                recipient_list=['synek.o@seznam.cz', 'synekjbc@gmail.com'],
            )

            return JsonResponse(serializer.data, status=201)
        
        return JsonResponse(serializer.errors, status=400)
