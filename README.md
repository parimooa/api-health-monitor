# Api-Health-Monitor
Dashboard for API Health check using FASTAPI and VUEJS

# Starting Dummy API services
Create API 1 to 4 using Docker compose file. This will bring up all the services starting from
Port 8050-8054

     cd apis
     docker-compose build
     docker-compose up -d

### HealthCheck Routes for API's

API1 `http://localhost:8050/healthcheck`

API2 `http://localhost:8051/healthcheck`

API3 `http://localhost:8052/healthcheck`

API4 `http://localhost:8053/healthcheck`

# API HEALTH MONITOR APP
### Execute using docker
    cd api-health-monitor-dashboard
    docker-compose build
    docker-compose up -d
    
Navigate to `http://localhost:9000` for dashboard 

<img width="1600" alt="ahm_screenshot" src="https://user-images.githubusercontent.com/11467145/103464949-b4f9bf00-4d2f-11eb-8ca1-f10d414dbc10.png">
