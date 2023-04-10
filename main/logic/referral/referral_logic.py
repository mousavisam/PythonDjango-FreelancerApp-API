from main.logic.dao.referral.referral_dao import ReferralDao
from main.model.user_entity import User


class ReferralLogic:
    def __init__(self) -> None:
        super().__init__()
        self.dao = ReferralDao()

    def insert_referral(self, referee: User, referer: User) -> None:
        return self.dao.insert_referral(referee=referee, referer=referer)