import uvicorn
from fastapi import FastAPI


from producer.db import engine
from producer import models
from producer.routes import router

models.Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(router)


if __name__ == '__main__':
    uvicorn.run('app:app', reload=True, port=8000)