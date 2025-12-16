import analysis
import alerts

try:
    df = analysis.clean("data/expenses.csv")

    total_spending = analysis.totalspending(df)

    category_analysis = analysis.categoryanalysis(df)
    highest_category = category_analysis.iloc[0]

    weekly_analysis = analysis.weeklyanalysis(df)

    previous_week = weekly_analysis.iloc[-2]["Amount"]
    current_week = weekly_analysis.iloc[-1]["Amount"]
    previous_week_percentage = weekly_analysis.iloc[-2]["Percentage"]
    current_week_percentage = weekly_analysis.iloc[-1]["Percentage"]

    print("Total Spending of this month: $", total_spending)

    print(alerts.high(highest_category["Category"], highest_category["Percentage"]))

    print(alerts.alertmsg(previous_week, current_week, previous_week_percentage, current_week_percentage))

except Exception as e:
    print("❌ Error:", e)