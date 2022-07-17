from app.api.common.base_response import BaseResponse


class HelloKnockKnock:
    def hello_knock_knock(self, api_version='v1'):
        return BaseResponse().set_success_response(data_body={'message': "service is up"})
