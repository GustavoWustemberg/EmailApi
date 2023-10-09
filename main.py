from configApi import app
from routes.routeEmail import RouteEmail


def __init__():
    RouteEmail()

    app.debug = False

    app.run(port=3333)

__init__()