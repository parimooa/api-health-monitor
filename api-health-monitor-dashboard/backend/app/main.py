from fastapi import Depends, FastAPI
from fastapi.middleware.cors import CORSMiddleware
import requests
from functools import lru_cache
from enum import Enum
import os
from json import JSONDecodeError
from . import config

app = FastAPI(
    title="API Health Monitor",
    description="Checks API health",
    version="0.1.0"
)
origins = ["http://localhost:9000", "http://localhost:8080"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@lru_cache()
def get_settings():
    return config.Settings()


# class APIServices(str, Enum):


def get_base_url():
    if os.environ.get('APP_ENV') == 'docker':
        base_url = 'host.docker.internal'
    else:
        base_url = 'localhost'
    return base_url


@app.get("/api/health/")
def get_all_api_health_status(settings: config.Settings = Depends(get_settings)):
    api_status_list = []
    for api in settings.target_api_urls:
        try:
            res = requests.get(f"http://{get_base_url()}:{api['port']}/{settings.target_api_endpoint}")
            if res.status_code == 200 and res.json() is not None:
                api_status_list.append({'name': api["name"], 'status': True})
            else:
                api_status_list.append({'name': api["name"], 'status': False})
        except Exception as e:
            print(f"Exception Error: {str(e)}")
            api_status_list.append({'name': api["name"], 'status': False})
    return api_status_list


@app.get("/api/health/{service}")
async def get_api_health_status(service: str, settings: config.Settings = Depends(get_settings)):
    """ Get API Health Status"""
    try:
        api = next(api for api in settings.target_api_urls if api['name'] == service)
        res = requests.get(f"http://{get_base_url()}:{api['port']}/{settings.target_api_endpoint}")
        return res.json()
    except JSONDecodeError:
        return {'name': service, 'status': False}
    except StopIteration:
        return {'error': f"{service} doesn't exist"}
