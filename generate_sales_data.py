
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# определение параметров для генерации данных
num_records = 10000 # какое количество записей будет сгенерированно
start_date = datetime(2023, 1, 1)
end_date = datetime(2023, 12, 31)

product_categories = ['Electronics', 'Clothing', 'Home Goods', 'Books', 'Food & Beverage']
regions = ['North', 'South', 'East', 'West']

# генерация данных
data = []
for i in range(num_records):
    sale_date = start_date + timedelta(days=np.random.randint(0, (end_date - start_date).days))
    category = np.random.choice(product_categories)
    region = np.random.choice(regions)
    sales_amount = round(np.random.uniform(10, 1000), 2)
    cost_of_goods = round(sales_amount * np.random.uniform(0.4, 0.8), 2) # 40-80% от sales_amount
    profit = round(sales_amount - cost_of_goods, 2)

    data.append({
        'Sale Date': sale_date.strftime('%Y-%m-%d'),
        'Product Category': category,
        'Region': region,
        'Sales Amount': sales_amount,
        'Cost of Goods': cost_of_goods,
        'Profit': profit
    })

df = pd.DataFrame(data)

# сохранение
df.to_csv('sales_data.csv', index=False)

print(f'Сгенерировано {num_records} записей о продажах и сохранено в файле sales_data.csv')


