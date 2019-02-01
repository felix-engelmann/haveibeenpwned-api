from flask import Flask, Response
from .pwnd import Pwnd

app = Flask(__name__)

@app.route('/range/<hash>')
def check_password(hash):
    # show the user profile for that user
    try:
        query = int(hash, 16)
    except:
        return Response("Not a hex number", 400)
    if len(hash) < 5:
        return Response("Anonymity set too large, min 5 digits", 400)

    p = Pwnd("../first-prep.txt")
    res = p.lookup(hash)

    return '\n'.join(res)