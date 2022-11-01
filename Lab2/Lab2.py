import statistics

def display_main_menu():
    print("Enter some numbers separated by commas (e.g. 5,63,23)")

def get_user_input():
    txt = input().split(",")
    for i in range(0, len(txt)):
        txt[i] = float(txt[i])
    return (txt)
def calc_average(txt):
    total = 0
    for i in range(0, len(txt)):
        total += txt[i]
    avg = total/len(txt)
    return (avg)

def find_min_max(txt):
    mm = [0,0]
    mm[0] = min(txt)
    mm[1] = max(txt)
    return (mm)
def sort_temperature(txt):
    sort = txt.sort()
    return (sort)
def calc_median_temperature(txt):
    med = statistics.median(txt)
    return (med)

display_main_menu()
txt = get_user_input()
avg = calc_average(txt)
print ("The average is: " + str(avg))
mm = find_min_max(txt)
print ("The minimum is: " + str(mm[0]))
print ("The maximum is: " + str(mm[1]))
sort = sort_temperature(txt)
print ("Sorted list: " + str(sort))
med = calc_median_temperature(txt)
print ("The maximum is: " + str(med))