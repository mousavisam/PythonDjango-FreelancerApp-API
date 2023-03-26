from rest_framework import serializers

from ....model.proposal_entity import Proposal


class CreateProposalSerializer(serializers.ModelSerializer):
    task_id = serializers.IntegerField(min_value=1)

    class Meta:
        model = Proposal

        fields = ['delivery_time_in_day', 'payment_amount', 'description', 'task_id']


class GetProposalSerializer(serializers.ModelSerializer):
    task = serializers.SerializerMethodField()

    class Meta:
        model = Proposal

        fields = ['task', 'delivery_time_in_day', 'payment_amount', 'description',  'creation_time', 'status']

    def get_task(self, obj):
        return obj.title
