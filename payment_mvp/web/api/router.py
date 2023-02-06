from fastapi.routing import APIRouter
from payment_mvp.web.api import echo
from payment_mvp.web.api import docs
from payment_mvp.web.api import monitoring

api_router = APIRouter()
api_router.include_router(monitoring.router)
api_router.include_router(docs.router)
api_router.include_router(echo.router, prefix="/echo", tags=["echo"])
