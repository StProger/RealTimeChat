from fastapi import FastAPI

def create_app():
    return FastAPI(
        title="FastAPI + Kafka + Websockets Chat App",
        docs_url="/api/docs",
        description="A simple Kafka + DDD chat",
        debug=True
    )