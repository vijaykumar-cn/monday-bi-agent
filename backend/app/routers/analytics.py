from fastapi import APIRouter

from app.config import DEALS_BOARD_ID
from app.services.analytics import Analytics
from app.services.data_cleaner import DataCleaner
from app.services.monday_service import MondayService

router = APIRouter(
    prefix="/analytics",
    tags=["Analytics"],
)

service = MondayService()


@router.get("/pipeline")
def pipeline():

    board = service.get_board_raw(DEALS_BOARD_ID)

    df = DataCleaner.board_to_dataframe(board)

    return Analytics.pipeline_summary(df)


@router.get("/sector")
def sector():

    board = service.get_board_raw(DEALS_BOARD_ID)

    df = DataCleaner.board_to_dataframe(board)

    return Analytics.revenue_by_sector(df)


@router.get("/stage")
def stage():

    board = service.get_board_raw(DEALS_BOARD_ID)

    df = DataCleaner.board_to_dataframe(board)

    return Analytics.pipeline_by_stage(df)


@router.get("/owners")
def owners():

    board = service.get_board_raw(DEALS_BOARD_ID)

    df = DataCleaner.board_to_dataframe(board)

    return Analytics.top_owners(df)