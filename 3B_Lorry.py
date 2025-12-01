def get_highest_capacity(kayak, catamaran, target):
    kayak.sort(reverse=True)
    catamaran.sort(reverse=True)
    kayak_prefix = [0]
    catamaran_prefix = [0]
    best_choice_for_k = 0
    best_choice_for_c = 0
    for i in range(len(kayak)):
        kayak_prefix.append(kayak_prefix[-1] + kayak[i][0])

    for i in range(len(catamaran)):
        catamaran_prefix.append(catamaran_prefix[-1] + catamaran[i][0])

    best_capacity = 0
    max_catamarans_possible = min(len(catamaran), target // 2)
    set_of_vehicles = []
    for c in range(max_catamarans_possible+1):
        total_kayak = target - 2*c
        if total_kayak > len(kayak):
            continue
        best_kayak = kayak_prefix[total_kayak]
        best_catamaran = catamaran_prefix[c]
        if best_kayak + best_catamaran > best_capacity:
            best_capacity = best_kayak + best_catamaran
            best_choice_for_c = c
            best_choice_for_k = total_kayak

    for i in range(best_choice_for_k):
        set_of_vehicles.append(kayak[i][1])

    for i in range(best_choice_for_c):
        set_of_vehicles.append(catamaran[i][1])

    print(best_capacity)
    print(set_of_vehicles)

number_of_vehicles, target_volume = map(int, input().split())

kayak_capacities = []
catamaran_capacities = []
highest_capacities = 0

for rang in range(number_of_vehicles):
    vehicle_type, vehicle_carrying_capacity = map(int, input().split())
    if vehicle_type == 1:
        kayak_capacities.append((vehicle_carrying_capacity,rang+1))
    else:
        catamaran_capacities.append((vehicle_carrying_capacity,rang+1))

get_highest_capacity(kayak_capacities,catamaran_capacities, target_volume)