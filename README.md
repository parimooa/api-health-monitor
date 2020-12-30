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