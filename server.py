from flask import request, url_for, redirect, Response
from flask_api import FlaskAPI, status, exceptions

from utils import shortify, is_valid
from db import store, fetch

app = FlaskAPI(__name__)

@app.route("/", methods=['POST'])
def new_url():
    """
    Create short url.
    """
    if request.method == 'POST':
        original_url = request.data.get('url')
        if not original_url:
            return Response('No url to shorten was provided', 401)
        if not is_valid(original_url):
            return Response('No valid url to was provided', 401)

        short_url = shortify(original_url)
        store(short_url, original_url)
        base = request.url

        return {'shortened_url': base + short_url}, status.HTTP_201_CREATED

@app.route("/<string:hash>/", methods=['GET'])
def redirect_to_original_url(hash):
    """
    Redirect to original url.
    """
    if hash not in urls:
        raise exceptions.NotFound()
    return redirect(urls[hash], code=302)


if __name__ == "__main__":
    app.run(debug=True)
