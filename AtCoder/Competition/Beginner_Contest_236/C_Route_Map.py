n, m = map(int, input().split())
stations = input().split()
stop_stations = input().split()

hashtable = {}

for station in stations:
    hashtable[station] = False

for stop_station in stop_stations:
    hashtable[stop_station] = True

for key in hashtable:
    if hashtable[key] == True:
        print('Yes')
    else:
        print('No')