from rest_framework import status
from rest_framework.response import Response

from main.api.serializer.system.system_serializer import ResponseSerializer
from main.model.vo.response.response_vo import ResponseVO


class CreateResponse(Response):
    def __init__(self):
        self.default_message = ResponseVO.create_successfully
        self.default_status = status.HTTP_201_CREATED
        response = ResponseSerializer(
            {ResponseVO.message: self.default_message, ResponseVO.status_code: self.default_status})
        super().__init__(data=response.data,
                         status=self.default_status)


class UpdateResponse(Response):
    def __init__(self):
        self.default_message = ResponseVO.update_successfully
        self.default_status = status.HTTP_201_CREATED
        response = ResponseSerializer(
            {ResponseVO.message: self.default_message, ResponseVO.status_code: self.default_status})
        super().__init__(data=response.data,
                         status=self.default_status)