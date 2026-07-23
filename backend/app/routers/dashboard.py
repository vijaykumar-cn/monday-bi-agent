from fastapi import APIRouter

from app.services.analytics import Analytics
from app.services.monday_service import MondayService

router = APIRouter(
    prefix="/dashboard",
    tags=["Dashboard"]
)

service = MondayService()


@router.get("/")
def dashboard():

    df = service.get_deals()

    return Analytics.dashboard_summary(df)