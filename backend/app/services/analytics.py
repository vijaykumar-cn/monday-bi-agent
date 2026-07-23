import pandas as pd


class Analytics:

    @staticmethod
    def pipeline_summary(df: pd.DataFrame):
        """
        Returns overall pipeline metrics.
        """

        total_deals = len(df)

        pipeline_value = 0
        average_deal = 0

        if "Masked Deal value" in df.columns:

            df["Masked Deal value"] = pd.to_numeric(
                df["Masked Deal value"],
                errors="coerce"
            ).fillna(0)

            pipeline_value = df["Masked Deal value"].sum()
            average_deal = df["Masked Deal value"].mean()

        return {
            "total_deals": total_deals,
            "pipeline_value": float(pipeline_value),
            "average_deal_size": round(float(average_deal), 2)
        }

    @staticmethod
    def revenue_by_sector(df: pd.DataFrame):
        """
        Revenue grouped by sector.
        """

        if (
            "Sector/service" not in df.columns
            or "Masked Deal value" not in df.columns
        ):
            return {}

        df["Masked Deal value"] = pd.to_numeric(
            df["Masked Deal value"],
            errors="coerce"
        ).fillna(0)

        revenue = (
            df.groupby("Sector/service")["Masked Deal value"]
            .sum()
            .sort_values(ascending=False)
        )

        return revenue.to_dict()

    @staticmethod
    def pipeline_by_stage(df: pd.DataFrame):
        """
        Number of deals in each stage.
        """

        if "Deal Stage" not in df.columns:
            return {}

        return (
            df["Deal Stage"]
            .fillna("Unknown")
            .value_counts()
            .to_dict()
        )

    @staticmethod
    def top_owners(df: pd.DataFrame):
        """
        Top deal owners.
        """

        if "Owner code" not in df.columns:
            return {}

        return (
            df["Owner code"]
            .fillna("Unknown")
            .value_counts()
            .head(10)
            .to_dict()
        )

    @staticmethod
    def open_deals(df: pd.DataFrame):
        """
        Count open deals.
        """

        if "Deal Status" not in df.columns:
            return 0

        return int(
            df[
                df["Deal Status"]
                .fillna("")
                .str.lower()
                .str.contains("open")
            ].shape[0]
        )

    @staticmethod
    def deals_by_status(df: pd.DataFrame):
        """
        Count deals by status.
        """

        if "Deal Status" not in df.columns:
            return {}

        return (
            df["Deal Status"]
            .fillna("Unknown")
            .value_counts()
            .to_dict()
        )

    @staticmethod
    def deal_probability(df: pd.DataFrame):
        """
        Count deals by closure probability.
        """

        if "Closure Probability" not in df.columns:
            return {}

        return (
            df["Closure Probability"]
            .fillna("Unknown")
            .value_counts()
            .to_dict()
        )

    @staticmethod
    def sector_distribution(df: pd.DataFrame):
        """
        Number of deals in each sector.
        """

        if "Sector/service" not in df.columns:
            return {}

        return (
            df["Sector/service"]
            .fillna("Unknown")
            .value_counts()
            .to_dict()
        )

    @staticmethod
    def dashboard_summary(df: pd.DataFrame):
        """
        Returns a dashboard-friendly summary.
        """

        return {
            "pipeline": Analytics.pipeline_summary(df),
            "revenue_by_sector": Analytics.revenue_by_sector(df),
            "pipeline_by_stage": Analytics.pipeline_by_stage(df),
            "top_owners": Analytics.top_owners(df),
            "open_deals": Analytics.open_deals(df),
            "deal_status": Analytics.deals_by_status(df),
            "closure_probability": Analytics.deal_probability(df),
            "sector_distribution": Analytics.sector_distribution(df),
        }