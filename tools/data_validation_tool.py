import pandas as pd


def validate_event_log(file):
    df = pd.read_csv(file)

    required_columns = ["case_id", "activity", "timestamp"]
    missing_columns = [col for col in required_columns if col not in df.columns]

    if missing_columns:
        return {
            "valid": False,
            "error": f"Missing required columns: {missing_columns}"
        }

    df["timestamp"] = pd.to_datetime(df["timestamp"], errors="coerce")

    summary = {
        "valid": True,
        "total_events": len(df),
        "total_cases": df["case_id"].nunique(),
        "total_activities": df["activity"].nunique(),
        "activities": df["activity"].unique().tolist(),
        "missing_values": df[required_columns].isnull().sum().to_dict(),
        "start_time": str(df["timestamp"].min()),
        "end_time": str(df["timestamp"].max())
    }

    return summary
    