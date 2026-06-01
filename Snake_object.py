Snake_object

import plotly.express as px
import pandas as pd
import numpy as np

# Generate sales data for multiple products and regions
np.random.seed(42)
products = ['Product A', 'Product B', 'Product C', 'Product D']
regions = ['North', 'South', 'East', 'West']
months = pd.date_range('2024-01-01', '2024-12-31', freq='ME')

data_list = []
for product in products:
    for region in regions:
        for month in months:
            # Different products have different patterns
            base = {'Product A': 50000, 'Product B': 35000,
                    'Product C': 45000, 'Product D': 30000}[product]

            # Regional variation
            regional_mult = {'North': 1.1, 'South': 0.9,
                           'East': 1.2, 'West': 1.0}[region]

            # Trend and noise
            month_num = month.month
            sales = base * regional_mult * (1 + 0.1 * np.sin(month_num/6 * np.pi)) + np.random.normal(0, 3000)

            data_list.append({
                'date': month,
                'product': product,
                'region': region,
                'sales': max(sales, 10000)
            })

df_sales = pd.DataFrame(data_list)

# Create faceted line chart
fig = px.line(df_sales,
              x='date',
              y='sales',
              color='region',
              facet_col='product',
              facet_col_wrap=2,  # 2 columns, multiple rows
              title='Sales Performance by Product and Region - 2024',
              labels={'sales': 'Monthly Sales ($)', 'date': 'Month'},
              height=800)

# Update all subplot titles
fig.for_each_annotation(lambda a: a.update(text=a.text.split('=')[1]))

# Format y-axes
fig.update_yaxes(tickformat='$,.0f')

# Improve facet spacing
fig.update_layout(
    showlegend=True,
    legend=dict(
        title='Region',
        orientation='v',
        yanchor='top',
        y=1,
        xanchor='left',
        x=1.02
    )
)

fig.show()

