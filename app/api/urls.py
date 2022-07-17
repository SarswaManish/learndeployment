from flask import Blueprint
from flask.views import MethodView

from app.api.views import HelloKnockKnock

api = Blueprint("api", __name__, url_prefix='/api/<version>/')


class Hello(MethodView):
    def get(self, version):
        return HelloKnockKnock().hello_knock_knock(api_version=version)


api.add_url_rule(
    "/hello",
    view_func=Hello.as_view('hello')
)

# http://127.0.0.1:5000/api/v1/hello
