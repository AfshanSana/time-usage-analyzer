import pandas as pd
import matplotlib.pyplot as plt


def load_data(file_path):
    df = pd.read_csv(file_path)
    return df


def validate_data(df):
    required_columns = {"activity", "hours"}

    if not required_columns.issubset(df.columns):
        raise ValueError("CSV must contain 'activity' and 'hours' columns.")

    if df["hours"].isnull().any():
        raise ValueError("'hours' column contains empty values.")

    if (df["hours"] < 0).any():
        raise ValueError("'hours' cannot be negative.")


def analyze_time(df):
    summary = df.groupby("activity")["hours"].sum().sort_values(ascending=False)
    total_hours = summary.sum()
    return summary, total_hours


def give_suggestions(summary):
    print("\nSuggestions:")

    if "social_media" in summary.index and summary["social_media"] > 12:
        print("- Social media usage is high. Try setting a daily limit.")
    else:
        print("- Social media usage is under control.")

    if "sleep" in summary.index and summary["sleep"] < 42:
        print("- Sleep looks low across the week. Aim for at least 6-8 hours daily.")
    else:
        print("- Sleep duration looks healthy.")

    if "exercise" in summary.index and summary["exercise"] < 3.5:
        print("- Try increasing exercise time during the week.")
    else:
        print("- Exercise time looks good.")

    if "study" in summary.index and summary["study"] < 20:
        print("- Study time can be improved for better productivity.")
    else:
        print("- Study time is consistent.")

    print("- Keep a balanced daily routine.")

def plot_time_usage(summary):
    summary.plot(kind="pie", autopct="%1.1f%%", figsize=(7, 7))
    plt.title("Time Usage Distribution")
    plt.ylabel("")
    plt.tight_layout()
    plt.show()
    
def daily_breakdown(df):
    if "day" in df.columns:
        return df.groupby(["day", "activity"])["hours"].sum()
    return None