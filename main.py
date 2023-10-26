def convert_to_minutes(weeks, days, hours, minutes):
    total_minutes = (weeks * 7 * 24 * 60) + (days * 24 * 60) + (hours * 60) + minutes
    return total_minutes


def curried_converter(weeks):
    def curried_days(days):
        def curried_hours(hours):
            def curried_minutes(minutes):
                return convert_to_minutes(weeks, days, hours, minutes)
            return curried_minutes
        return curried_hours
    return curried_days

def extract_integers(item):
    return list(filter(str.isdigit, item.split()))


data = [
    "3 minggu 3 hari 7 jam 21 menit",
    "5 minggu 5 hari 8 jam 11 menit",
    "7 minggu 1 hari 5 jam 33 menit",
]

result = []

for item in data:
    integers = extract_integers(item)
    total_minutes = curried_converter(int(integers[0]))(int(integers[1]))(int(integers[2]))(int(integers[3]))
    result.append(integers)

for values in result:
    print(values)
