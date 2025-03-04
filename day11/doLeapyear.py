def is_leap_year(year):
    isLeap = True
    if year%4==0:
        isLeap = True
    else:
        isLeap = False
    if year%100==0:
        isLeap = False
    if year%400==0:
        isLeap = True
    return isLeap


print(is_leap_year(2000))