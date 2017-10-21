from flask import request, url_for, redirect, Response
from flask_api import FlaskAPI, status, exceptions

import hashlib

app = FlaskAPI(__name__)


urls = {

}

@app.route("/", methods=['POST'])
def new_url():
    """
    Create short url.
    """
    if request.method == 'POST':
        #validate request.body
        print request.url
        original_url = request.data.get('url')
        if not original_url:
            return Response('No url to shorten was provided', 401)
        short_url = hashlib.sha224(request.data.get('url')).hexdigest()
        urls[short_url] = request.data.get('url')
        print urls
        return {'shortened_url': request.url + short_url}, status.HTTP_201_CREATED

@app.route("/<string:hash>/", methods=['GET'])
def redirect_to_original_url(hash):
    """
    Redirect to original url.
    """
    print urls
    if hash not in urls:
        raise exceptions.NotFound()
    return redirect(urls[hash], code=302)


if __name__ == "__main__":
    app.run(debug=True)
