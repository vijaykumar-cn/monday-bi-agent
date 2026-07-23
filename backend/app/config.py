import os
from dotenv import load_dotenv

load_dotenv()

MONDAY_API_KEY = os.getenv("MONDAY_API_KEY")
NVIDIA_API_KEY = os.getenv("NVIDIA_API_KEY")

DEALS_BOARD_ID = os.getenv("DEALS_BOARD_ID")
WORKORDER_BOARD_ID = os.getenv("WORKORDER_BOARD_ID")