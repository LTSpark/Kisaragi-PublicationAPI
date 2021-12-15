from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routes.publication_routes import publications_router

tags_metadata = [{
  "name": "Publications",
  "description": "Manage user publications"
}]

origins = ["*"]

app = FastAPI(
  title="API Publications Kisaragi",
  description="REST API to manage users publications on Kisaragi",
  version="0.0.1",
  open_api_tags=tags_metadata
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(publications_router)
