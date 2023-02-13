import sys
import argparse
from temperature_io import read_from_json, add_measure_to_json, save_graph
from datetime import datetime


class EmptyArgumentsError(Exception):
    pass


def main(arguments):
    parser = argparse.ArgumentParser()
    parser.add_argument("action", choices=['save', 'graph'])
    parser.add_argument("--date", help="Date must be given like: YYYY-MM-DD HH:MM") # noqa 551
    parser.add_argument("--temperature", type=int)
    parser.add_argument("--city")
    parser.add_argument('--from_time', help="Date must be given like: YYYY-MM-DD HH:MM") # noqa 551
    parser.add_argument("--to_time", help="Date must be given like: YYYY-MM-DD HH:MM") # noqa 551
    parser.add_argument('--file')
    args = parser.parse_args(arguments[1:])
    with open('temperature.json', 'r') as handle:
        if not handle.read():
            measurments = []
        else:
            handle.seek(0)
            measurments = read_from_json(handle)
    if args.action == 'save':
        if not all([args.city, args.temperature, args.date]):
            raise EmptyArgumentsError("Date, temperature and city must be given in order to add measurment to database") # noqa 551
        with open('temperature.json', 'w') as handle:
            add_measure_to_json(handle, args, measurments)
    if args.action == 'graph':
        if args.from_time:
            measurments = [measure for measure in measurments if measure.date > datetime.fromisoformat(args.from_time)] # noqa 551
        if args.to_time:
            measurments = [measure for measure in measurments if measure.date < datetime.fromisoformat(args.to_time)] # noqa 551
        save_graph(measurments, args.file)


if __name__ == '__main__':
    main(sys.argv)
