input_data = [
    ['Moscow', 'Paris', '14:55'],
    ['London', 'Magadan', '05:40'],
    ['Rome', 'Paris', '20:10']
]


def time_to_secs(str_time: str):
    hours, minutes = map(int, str_time.split(':'))
    seconds = (hours * 60 + minutes) * 60
    return seconds


def first_flights(fly_data: list[list[str]]):
    flights = dict()
    for row in fly_data:
        from_, to_, time_ = row
        curr_secs = time_to_secs(time_)
        if to_ not in flights:
            flights[to_] = time_
        else:
            fly_secs = time_to_secs(flights.get(to_))
            if curr_secs < fly_secs:
                flights[to_] = time_

    return flights


result = first_flights(fly_data=input_data)
for city, arrival_time in result.items():
    print(f'Самый ранний самолет в {city} прибывает в {arrival_time}')
