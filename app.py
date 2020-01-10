import responder
import requests
import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

api = responder.API()


@api.route('/shock')
def shock(req, resp):
    if req.method == 'get':
        resp.media = {'message': 'POST Method Only'}
    if req.method == 'post':
        requests.get(os.environ.get("SHOCK_URL"))
        resp.media = {'success': True}


if __name__ == '__main__':
    api.run(port=6666)
