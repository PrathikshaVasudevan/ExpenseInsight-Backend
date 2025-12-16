
def alertmsg(previous_week, current_week,previous_week_percentage,current_week_percentage):
    if current_week > previous_week:
        return (
            f"⚠️ Overspending Alert: "
            f"You spent {current_week_percentage - previous_week_percentage:.2f}% more than last week."
        )
    else:
        return "✅ Good job! Your spending reduced compared to last week."

def high(highest_category,highest_category_percentage):
    return (
        f"Highest spending category: {highest_category} "
        f"({highest_category_percentage:.2f}% of total).Spend mindfully."
    )