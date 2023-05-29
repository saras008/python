data = {
    (1000, 10),
    (2000, 17),
    (3000, 9),
}

print('Revenue  |  Profit  |  Percent')

template = '{revenue:>7,} | {profit:>+7} | {percent:>7.2%}'

for revenue, profit in data:
    percent = profit / revenue
    row = template.format(revenue=revenue,profit=profit, percent=percent)
    print(row)