from rest_framework.request import Request
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from django.core.mail import send_mail
from django.conf import settings
from django.urls import reverse

from ....logic.referral.referral_logic import ReferralLogic
from ....api.serializer.Referral.referral_serializer import ReferralRequestSerializer
from ....models import User


class ReferralController(ViewSet):
    permission_classes = [IsAuthenticated]

    def __init__(self):
        super().__init__()
        self.referral_logic = ReferralLogic()

    def generate_referral_code(self, user):
        # Generate a unique referral code for the user
        referral_code = self.referral_logic.generate_referral_code(user)
        return referral_code

    def send_invitation_email(self, user, email, referral_code):
        # Send an invitation email to the friend with the referral code
        subject = f"Join {settings.SKill_Tree} and get rewarded!"
        message = f"Hi,\n\nYour friend {user.first_name} has invited you to join {settings.Skill_Tree}.\n" \
                  f"Use their referral code {referral_code} when you sign up to get a bonus reward.\n" \
                  f"Click the following link to sign up:\n" \
                  f"{settings.FRONTEND_URL}{reverse('signup')}?ref={referral_code}\n\n" \
                  f"Best regards,\nThe {settings.Skill_Tree} team"
        send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [email])

    def post(self, request: Request):
        serializer = ReferralRequestSerializer(data=request.data)
        if serializer.is_valid():
            # Get the email address of the friend to refer
            email = serializer.validated_data.get("email")

            # Check if the friend already has an account
            try:
                friend = User.objects.get(email=email)
                return Response(data="The email address is already registered", status=status.HTTP_400_BAD_REQUEST)
            except User.DoesNotExist:
                pass

            # Generate a referral code for the user and send an invitation email to the friend
            user = request.user
            referral_code = self.generate_referral_code(user)
            self.send_invitation_email(user, email, referral_code)

            return Response(data="An invitation email has been sent", status=status.HTTP_200_OK)

        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
