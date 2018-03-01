# THE MAINEST FILE
import numpy as np

start_t_rides = []
length_rides = []
processed = set()
k = 0
t = 0
bonus = 0

def choose_best(car):
    best_s = 0
    best_l = 0
    best_is = 0
    best_il = 0

    for i in range(k):
        if i <= len(start_t_rides):
            continue

        if start_t_rides[i][0] in processed:
            del start_t_rides[i]
            continue

        if t > start_t_rides[i][5]:
            processed.add(start_t_rides[i][0])
            del start_t_rides[i]
            continue

        dist = ride_length(car['x'], car['y'], start_t_rides[i][1], start_t_rides[i][2])
        if t + dist + start_t_rides[i][7] >= start_t_rides[i][6]:
            continue

        score = start_t_rides[i][7]
        if t + dist <= start_t_rides[i][5]:
            score += bonus

        if score > best_s:
            best_s = score
            best_is = i

        if i <= len(length_rides):
            continue

        if length_rides[i][0] in processed:
            del length_rides[i]
            continue

        if t > length_rides[i][5]:
            processed.add(length_rides[i][0])
            del length_rides[i]
            continue

        dist = ride_length(car['x'], car['y'], length_rides[i][1], length_rides[i][2])
        if t + dist + length_rides[i][7] >= length_rides[i][6]:
            continue

        score = length_rides[i][7]
        if t + dist <= length_rides[i][5]:
            score += bonus

        if score > best_l:
            best_l = score
            best_il = i

    if best_s > best_l:
        processed.add(start_t_rides[best_is][0])
        pom = start_t_rides[best_is][0]
        del start_t_rides[best_is]
        return pom
    else:
        length_rides[best_il][0]
        processed.add(length_rides[best_il][0])
        pom = length_rides[best_il][0]
        del length_rides[best_il]
        return pom

def ride_length(sx, sy, tx, ty):
    xlen = np.absolute(sx - tx)
    ylen = np.absolute(sy - ty)
    return xlen + ylen

def write_output(path, *args):
    with open(path, 'w') as f:
        f.write("best output")
        f.write('\n')

if __name__ == '__main__':
    """
    READING INPUT
    """
    rows, columns, cars, nrides, bonus, steps = [int(x) for x in input().split()]
    rides = []
    for i in range(nrides):
        start_x, start_y, end_x, end_y, start_t, end_t = [int(x) for x in input().split()]
        rides.append([i, start_x, start_y, end_x, end_y, start_t, end_t, ride_length(start_x, start_y, end_x, end_y)])

    free_car = [{'time': 0, 'x': 0, 'y': 0, 'rides': []} for c in range(cars)]
    start_t_rides = sorted(rides, key = lambda x: x[5])
    length_rides = sorted(rides, key = lambda x: x[7])

    k = int(round(np.sqrt(len(rides))))

    for t in range(steps):
        for car in free_car:
            if len(processed) >= nrides:
                break
            if car['time'] <= t:
                best_index = choose_best(car)
                car['rides'].append(best_index)
                car['time'] = ride_length(car['x'], car['y'], rides[best_index][1], rides[best_index][2]) + rides[best_index][7] + t
                car['x'] = rides[best_index][3]
                car['y'] = rides[best_index][4]

    with open('out.txt', 'w') as f:
        for car in free_car:
            f.write(str(len(car['rides'])))
            f.write(' ')
            f.write(' '.join(str(x) for x in car['rides']))
            f.write('\n')
