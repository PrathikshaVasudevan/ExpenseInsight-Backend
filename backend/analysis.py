import pandas as pd

def clean(filepath):
    try:
        df = pd.read_csv(filepath)
    except FileNotFoundError:
        raise FileNotFoundError(f"File not found: {filepath}")
    except Exception as e:
        raise Exception(f"Error reading file: {e}")

    required_columns = {"Date", "Category", "Amount"}
    if not required_columns.issubset(df.columns):
        raise ValueError("CSV must contain Date, Category, Amount columns")

    df["Amount"] = pd.to_numeric(df["Amount"],errors="coerce")
    df["Date"] = pd.to_datetime(df["Date"],format="%Y-%m-%d",errors="coerce")
    df["Category"] = df["Category"].str.strip().str.title()

    df = df.dropna(subset=["Amount","Date","Category"])
    df = df.drop_duplicates()
    df = df[df["Amount"]>0]
    df = df.sort_values(by=["Date"])

    return df

def totalspending(df):
    total = df["Amount"].sum()
    return total

def categoryanalysis(df):
    total_amount = df["Amount"].sum()
    group_category = df.groupby("Category")["Amount"].sum()
    summarycategory = group_category.reset_index()
    summarycategory["Percentage"] = (summarycategory["Amount"] / total_amount) * 100
    summarycategory_sorted = summarycategory.sort_values(by=["Amount"], ascending=False)

    return summarycategory_sorted


def weeklyanalysis(df):
    df["Week"] = df["Date"].dt.isocalendar().week

    group_weekly = df.groupby("Week")["Amount"].sum().reset_index()
    total_amount = df["Amount"].sum()

    group_weekly["Percentage"] = (group_weekly["Amount"] / total_amount) * 100
    weekly_sorted = group_weekly.sort_values(by=["Week"])

    return weekly_sorted


