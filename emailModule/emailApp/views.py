from rest_framework.views import APIView
from rest_framework.response import Response

from emailApp.tasks import send_email_to_all

# Create your views here.

class SendMailView(APIView):
    
    def post(self, request, *args, **kwargs):
        '''
        For post email
        '''
        email_list = request.data.get('email_list')
        send_email_to_all.delay(email_list)
        return Response({'message': 'Ok'})

