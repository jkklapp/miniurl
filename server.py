from flask import request, url_for, redirect, Response
from flask_api import FlaskAPI, status, exceptions

from utils import shortify, is_valid
from db import DB

app = FlaskAPI(__name__)
app.config.from_pyfile('settings/dev.py')
app.config.from_envvar('MINIURL_SETTINGS', silent=True)
db = DB(app.config)

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
        db.store(short_url, original_url)
        base = request.url

        return {'shortened_url': base + short_url}, status.HTTP_201_CREATED

@app.route("/<short_url>", methods=['GET'])
def redirect_to_original_url(short_url):
    """
    Redirect to original url.
    """
    original_url = db.fetch(short_url)
    if not original_url:
        raise exceptions.NotFound()
    return redirect(original_url, code=302)


if __name__ == "__main__":
    app.run(debug=True)
