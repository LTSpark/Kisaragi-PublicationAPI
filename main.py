from fastapi import FastAPI

from app.routes.publication_routes import publications_router

tags_metadata = [{
  "name": "Publications",
  "description": "Manage user publications"
}]

app = FastAPI(
  title="API Publications Kisaragi",
  description="REST API to manage users publications on Kisaragi",
  version="0.0.1",
  open_api_tags=tags_metadata
)

app.include_router(publications_router)
