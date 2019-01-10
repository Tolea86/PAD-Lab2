"""
run "pip install flask", or run "pip install -r requirements/flask.txt"
"""

from flask import Flask, request, Response
from flask_cors import CORS, cross_origin
import requests

from .utils import UrlHandling, RoundRobin

HOSTS = ['http://127.0.0.1:8009/', 'http://192.168.43.42:8003/', 'http://192.168.43.42:8005/']
app = Flask(__name__)
c = RoundRobin(HOSTS)
NEXT_NODE = None
CORS(app)


@app.before_request
def find_next_node():
    global NEXT_NODE
    print(NEXT_NODE)
    NEXT_NODE = c.next_host()


@app.route('/<path:url>', methods=['GET'])
def mega_proxy_mastermind(url):
    url_to_send = UrlHandling.parse_url(url, NEXT_NODE)

    r = requests.get(url_to_send, params=request.args)
    return Response(r.text, content_type=r.headers['content-type'])


@app.route('/<path:url>', methods=['POST'])
def mega_proxy_mastermind_post(url):
    url_to_send = UrlHandling.parse_url(url, NEXT_NODE)

    r = requests.post(url_to_send, params=request.args, data=request.data, headers=request.headers)
    return Response(r.text, content_type=r.headers['content-type'])


@app.route('/<path:url>', methods=['PUT'])
def mega_proxy_mastermind_put(url):
    url_to_send = UrlHandling.parse_url(url, NEXT_NODE)

    r = requests.put(url_to_send, params=request.args, data=request.data, headers=request.headers)
    return Response(r.text, content_type=r.headers['content-type'])


@app.route('/<path:url>', methods=['DELETE'])
def mega_proxy_mastermind_delete(url):
    url_to_send = UrlHandling.parse_url(url, NEXT_NODE)

    r = requests.delete(url_to_send)
    return Response(r.text)
