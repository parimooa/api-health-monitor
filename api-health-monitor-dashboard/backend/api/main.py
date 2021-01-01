from fastapi import FastAPI, Request, APIRouter
from fastapi.middleware.cors import CORSMiddleware
import requests
from enum import Enum
import os
from json import JSONDecodeError

app = FastAPI(
    title="HealthCheck",
    description="Checks API health",
    version="0.1.0"
)
origins = ["http://localhost:9000","http://localhost:8080"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



class APIServices(str, Enum):


def get_base_url():
    if os.environ.get('APP_ENV') == 'docker':
        base_url = 'host.docker.internal'
    else:
        base_url = 'localhost'
    return base_url


@app.get("/api/health/")
def get_all_api_health_status():
    api_status_list = []
    for service in services:
        try:
            res = requests.get(f"http://{get_base_url()}:{service['port']}/services/{service['name']}/")
            if res.status_code == 200 and res.json() is not None:
                api_status_list.append({'name': service["name"], 'status': True})
            else:
                api_status_list.append({'name': service["name"], 'status': False})
        except Exception as e:
            print(f"Exception Error: {str(e)}")
            api_status_list.append({'name': service["name"], 'status': False})
    return api_status_list


@app.get("/api/health/{service}")
async def get_api_health_status(service: WebUASServices):
    """ Get API Health Status"""
    try:
        api = next(serv for serv in services if serv['name'] == service)
        res = requests.get(f"http://{get_base_url()}:{api['port']}/services/{service}/")
        return res.json()
    except JSONDecodeError:
        return {'name': service, 'status': False}
    except StopIteration:
        return {'error': f"{service} doesn't exist"}
