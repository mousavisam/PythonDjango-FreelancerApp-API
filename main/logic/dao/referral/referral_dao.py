from main.model.referral_entity import Referral
from main.model.user_entity import User


class ReferralDao:

    def insert_referral(self, referee: User, referer: User) -> None:
        Referral.objects.create(referee=referee, referer=referer)
