"""
Detrox Yapay Zekâ Komuta Paneli — minimal web sunucusu (Railway için).
Tek statik dosya (index.html) servis eder. İsteğe bağlı HTTP Basic Auth:
PANEL_USER ve PANEL_PASS ortam değişkenleri ayarlanırsa panel parola ister;
ayarlanmazsa panel herkese açıktır. Sağlık kontrolü: /healthz
"""
import os
from functools import wraps
from flask import Flask, send_from_directory, Response, request

app = Flask(__name__)
HERE = os.path.dirname(os.path.abspath(__file__))

PANEL_USER = os.environ.get("PANEL_USER")
PANEL_PASS = os.environ.get("PANEL_PASS")


def _authorized(auth):
    return bool(auth) and auth.username == PANEL_USER and auth.password == PANEL_PASS


def guard(view):
    @wraps(view)
    def wrapped(*args, **kwargs):
        # Parola yalnızca her iki değişken de tanımlıysa devreye girer
        if PANEL_USER and PANEL_PASS and not _authorized(request.authorization):
            return Response(
                "Bu panel için yetki gerekli.",
                401,
                {"WWW-Authenticate": 'Basic realm="Detrox Komuta Paneli"'},
            )
        return view(*args, **kwargs)

    return wrapped


@app.route("/")
@guard
def index():
    return send_from_directory(HERE, "index.html")


@app.route("/healthz")
def healthz():
    return "ok", 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", "8080")))
