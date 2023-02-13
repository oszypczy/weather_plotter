import json
from datetime import datetime
from matplotlib import pyplot as plt


class EmptyArgumentsError(Exception):
    pass


def read_from_json(handle):
    measurements = []
    data = json.load(handle)
    for item in data:
        city = item['city']
        temperature = item['temperature']
        date = item['date']
        mesure = Measure(city, temperature, date)
        measurements.append(mesure)
    return measurements


def add_measure_to_json(handle, args, measurments):
    try:
        data = [{'city': args.city, 'date': args.date, 'temperature': args.temperature}] # noqa 551
    except Exception:
        raise EmptyArgumentsError("Date, temperature and city must be given in order to add measurment to database") # noqa 551
    for measure in measurments:
        city = measure.city
        temperature = measure.temperature
        date = str(measure.date)
        measure_data = {
            'city': city,
            'date': date,
            'temperature': temperature
        }
        data.append(measure_data)
    json.dump(data, handle, indent=2)


def save_graph(measurments, file):
    measurments = sorted(measurments, key=lambda x: x.date)
    set_of_towns = set([measure.city for measure in measurments])
    for each_town in set_of_towns:
        x_axis = [measure.date for measure in measurments if measure.city == each_town] # noqa 551
        y_axis = [measure.temperature for measure in measurments if measure.city == each_town] # noqa 551
        plt.plot(x_axis, y_axis, 'o-', label=each_town)
    plt.title(label='Temperature in different cities')
    plt.xticks(rotation=30, color='teal')
    plt.yticks(color='teal')
    plt.xlabel(xlabel='Date')
    plt.ylabel(ylabel='Temperatures in ℃')
    plt.legend()
    plt.grid(True)
    if file:
        plt.savefig(f'{file}.png')
    else:
        plt.savefig('plot.png')


class Measure:
    def __init__(self, city, temperature, date):
        self.city = city
        self.temperature = int(temperature)
        self.date = datetime.fromisoformat(date)
