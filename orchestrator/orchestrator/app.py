# SPDX-License-Identifier: MIT
# (c) 2019 The TJHSST Director 4.0 Development Team & Contributors

from flask import Flask, request

from . import settings
from .views.database import database_blueprint
from .views.docker import docker_blueprint
from .views.files import files as files_blueprint
from .views.nginx import nginx as nginx_blueprint
from .views.nginx_static import nginx_static as nginx_static_blueprint

app = Flask(__name__)
app.register_blueprint(docker_blueprint)
app.register_blueprint(files_blueprint)
app.register_blueprint(nginx_blueprint)
app.register_blueprint(nginx_static_blueprint)
app.register_blueprint(database_blueprint)

app.config.update(settings.FLASK_CONFIG)


@app.route("/ping")
def ping_page() -> str:
    """Checks whether the orchestrator is functional.

    Returns a provided message or else "Pong".
    """

    return request.args.get("message", "Pong")


if __name__ == "__main__":
    app.run()
