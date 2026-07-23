import requests

from app.config import (
    MONDAY_API_KEY,
    DEALS_BOARD_ID,
    WORKORDER_BOARD_ID,
)

from app.services.data_cleaner import DataCleaner


class MondayService:

    BASE_URL = "https://api.monday.com/v2"

    def __init__(self):

        self.headers = {
            "Authorization": MONDAY_API_KEY,
            "Content-Type": "application/json",
        }

    def execute_query(self, query: str):

        try:

            response = requests.post(
                self.BASE_URL,
                json={"query": query},
                headers=self.headers,
                timeout=30,
            )

            response.raise_for_status()

            result = response.json()

            if "errors" in result:
                raise Exception(result["errors"])

            return result

        except requests.exceptions.RequestException as e:
            raise Exception(f"Monday API Request Failed: {e}")

    def get_me(self):

        query = """
        query {
            me {
                id
                name
                email
            }
        }
        """

        return self.execute_query(query)

    def get_board_raw(self, board_id):
        """
        Fetch raw board data including column definitions.
        """

        query = f"""
        query {{
            boards(ids: {board_id}) {{

                id
                name

                columns {{
                    id
                    title
                }}

                items_page(limit: 500) {{

                    items {{

                        id
                        name

                        column_values {{
                            id
                            text
                            value
                        }}

                    }}

                }}

            }}
        }}
        """

        return self.execute_query(query)

    def get_board_dataframe(self, board_id):

        result = self.get_board_raw(board_id)

        df = DataCleaner.board_to_dataframe(result)

        print("\n==============================")
        print("Monday Board Columns")
        print("==============================")

        print(df.columns.tolist())

        print("\nFirst Five Rows:\n")

        print(df.head())

        print("==============================\n")

        return df

    def get_board(self, board_id):

        df = self.get_board_dataframe(board_id)

        return df.to_dict(orient="records")

    def get_deals(self):

        return self.get_board_dataframe(DEALS_BOARD_ID)

    def get_workorders(self):

        return self.get_board_dataframe(WORKORDER_BOARD_ID)