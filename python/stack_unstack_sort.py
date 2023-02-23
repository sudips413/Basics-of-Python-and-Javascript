# Unstack churn level and fill missing values with zero =>>>>>>>>>> churn is dataFrame
churn = churn.unstack('churn', fill_value=0)

# Sort by descending voice mail plan and ascending international plan
churn_sorted = churn.sort_index(level=['voice_mail_plan', 'international_plan'], ascending=[False, True])

# Print final DataFrame and observe pattern
print(churn_sorted)

# Stack the level type from churn
churn_stack = churn.stack(level='type')

# Fill the resulting missing values with zero 
churn_fill = churn_stack.fillna(0)

# Print churn_fill
print(churn_fill)

# Stack the level scope without dropping rows with missing values
churn_stack = churn.stack(level='scope',dropna=False)

# Fill the resulting missing values with zero
churn_fill = churn_stack.fillna(0)

# Print churn_fill
print(churn_fill)