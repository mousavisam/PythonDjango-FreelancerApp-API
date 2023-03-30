
from rest_framework.viewsets import ViewSet
from rest_framework.request import Request
from main.logic.referral.referral_logic import ReferralLogic
from main.shared.based_response.common_response import CreateResponse


class ReferralSerializer(serializers.Serializer):
    email = serializers.EmailField()


class ReferralController(ViewSet):

    def __init__(self):
        super().__init__()
        self.referral_logic = ReferralLogic()

    def post(self, request: Request):
        serializer = ReferralSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email']
            self.referral_logic.send_referral_email(
                from_user=request.user,
                email=email
            )
            return CreateResponse()
        else:
            return CreateResponse(success=False, errors=serializer.errors)
