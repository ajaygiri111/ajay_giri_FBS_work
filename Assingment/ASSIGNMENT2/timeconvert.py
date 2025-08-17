# Convert the time entered in hh,min and sec into seconds.

houre = int(input("enter the hours"))
minutes = int(input("enter the minutes"))
seconds = int (input("enter the seconds"))

total_seconds = (houre * 3600) + (minutes * 60) + seconds

print(f'total_seconds:{total_seconds}')
