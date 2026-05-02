import matplotlib.pyplot as plt
import pandas as pd

# Sample data for demonstration
categories = ['Food', 'Transport', 'Entertainment', 'Utilities']
spending = [250, 150, 100, 200]

# Create a pie chart for spending breakdown
plt.figure(figsize=(8, 6))
plt.pie(spending, labels=categories, autopct='%1.1f%%', startangle=140)
plt.title('Spending Breakdown by Category')
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.tight_layout()
plt.savefig('spending_breakdown.png')
plt.show()

# Create a line chart for spending over time
# Sample time data
dates = pd.date_range(start='2026-04-01', periods=10, freq='D')
spending_over_time = [30, 55, 80, 65, 90, 55, 75, 85, 100, 95]

plt.figure(figsize=(10, 5))
plt.plot(dates, spending_over_time, marker='o')
plt.title('Spending Over Time')
plt.xlabel('Date')
plt.ylabel('Amount Spent')
plt.xticks(rotation=45)
plt.grid()
plt.tight_layout()
plt.savefig('spending_over_time.png')
plt.show()