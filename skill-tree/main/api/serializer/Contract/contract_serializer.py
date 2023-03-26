from rest_framework import serializers

from main.model.contract_entity import Contract


class ContractSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contract
        fields = ['proposal', 'delivery_time_in_day', 'payment_amount', 'payment_type', 'start_time']


class GetContractSerializer(serializers.ModelSerializer):
    proposal = serializers.SerializerMethodField()

    class Meta:
        model = Contract
        fields = ['proposal', 'delivery_time_in_day', 'payment_amount', 'payment_type', 'start_time', 'end_time',
                  'status', 'creation_time']

    def get_proposal(self, obj):
        return obj.proposal.task.title
