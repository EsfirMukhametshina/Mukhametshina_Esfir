money_capital = 10000
salary = 5000
spend = 6000
increase = 0.05

month = 0
money = 0
while money_capital > 6000:
    spend = spend * 1.05
    money = salary - spend
    money_capital = money_capital + money
    month = month + 1

print(month)