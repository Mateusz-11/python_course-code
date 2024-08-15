from datetime import date, timedelta

start = date.today()
diff = timedelta(days=7)
end = start + diff
print(end.strftime('%d.%m.%y'))