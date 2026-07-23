import pandas as pd


class DataCleaner:

    @staticmethod
    def board_to_dataframe(board_json):
        """
        Convert Monday board JSON into a clean Pandas DataFrame
        using the column TITLES instead of column IDs.
        """

        boards = board_json.get("data", {}).get("boards", [])

        if not boards:
            return pd.DataFrame()

        board = boards[0]

        # Map column IDs -> Column Titles
        column_map = {
            column["id"]: column["title"]
            for column in board["columns"]
        }

        items = board["items_page"]["items"]

        rows = []

        for item in items:

            row = {
                "item_id": item["id"],
                "item_name": item["name"],
            }

            for column in item["column_values"]:

                column_name = column_map.get(
                    column["id"],
                    column["id"]
                )

                row[column_name] = column["text"]

            rows.append(row)

        df = pd.DataFrame(rows)

        return DataCleaner.clean_dataframe(df)

    @staticmethod
    def clean_dataframe(df):

        if df.empty:
            return df

        # Replace missing values
        df.fillna("", inplace=True)

        # Remove duplicate rows
        df.drop_duplicates(inplace=True)

        # Strip whitespace from string columns
        for col in df.columns:
            if df[col].dtype == "object":
                df[col] = df[col].astype(str).str.strip()

        return df