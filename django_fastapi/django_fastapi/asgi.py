import os
from django.apps import apps
from django.conf import settings
from django.core.wsgi import get_wsgi_application


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_fastapi.settings")
apps.populate(settings.INSTALLED_APPS)


from fastapi import FastAPI
from fastapi.middleware.wsgi import WSGIMiddleware
from starlette.middleware.cors import CORSMiddleware

from dj_fp import handlers


def get_application() -> FastAPI:
    app = FastAPI(debug=settings.DEBUG)
    app.add_middleware(
        CORSMiddleware)
    #     allow_origins=settings.ALLOWED_HOSTS or ["*"],
    #     allow_credentials=True,
    #     allow_methods=["*"],
    #     allow_headers=["*"],

    app.include_router(handlers.router, prefix="/api")
    app.mount("/django", WSGIMiddleware(get_wsgi_application()))

    return app


app = get_application()
