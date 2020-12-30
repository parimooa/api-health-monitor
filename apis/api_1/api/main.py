from fastapi import FastAPI

app = FastAPI()


@app.get("/healthcheck")
def health_check():
    return {'title': 'API 1',
            'ver': 1.0
            }
