from fastapi import APIRouter

from app.services.monday_service import MondayService
from app.config import DEALS_BOARD_ID, WORKORDER_BOARD_ID

router = APIRouter(prefix="/monday", tags=["Monday"])

service = MondayService()


@router.get("/me")
def get_me():
    return service.get_me()


@router.get("/deals")
def get_deals():
    return service.get_board(DEALS_BOARD_ID)


@router.get("/workorders")
def get_workorders():
    return service.get_board(WORKORDER_BOARD_ID)