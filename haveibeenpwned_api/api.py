from flask import Flask, Response
from .pwned import Pwned

app = Flask(__name__)


@app.route('/range/<hash>')
def check_password(hash):
    # show the user profile for that user
    try:
        int(hash, 16)
    except ValueError:
        return Response("Not a hex number", 400)
    if len(hash) < 5:
        return Response("Anonymity set too large, min 5 digits", 400)

    p = Pwned("/srv/pwned.txt")
    res = p.lookup(hash)

    return '\n'.join(res)


def main():
    app.run(host='0.0.0.0')
