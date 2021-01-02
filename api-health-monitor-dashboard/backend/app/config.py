from pydantic import BaseSettings


class Settings(BaseSettings):
    app_name: str = "Health Monitor Dashboard"
    target_base_api_uri: str = "localhost"
    target_api_urls: list = [
        {"name": "API_1", "port": 8051},
        {"name": "API_2", "port": 8052},
        {"name": "API_3", "port": 8053},
        {"name": "API_4", "port": 8054}
    ]
    target_api_endpoint="healthcheck"
    health_monitor_api_port=8000