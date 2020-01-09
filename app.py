import responder
import requests
import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

api = responder.API()


@api.route('/')
def hello_world(req, resp):
    resp.text = "hello"


@api.route('/shock')
def shock(req, resp):
    if req.method == 'get':
        resp.media = {'Message': 'POST Method Only'}
    if req.method == 'post':
        requests.get(os.environ.get("SHOCK_URL"))
        resp.media = {'success': True}


@api.route('/test')
def test(req, resp):
    print("test_shock")


if __name__ == '__main__':
    api.run()
