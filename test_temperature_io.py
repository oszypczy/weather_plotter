from temperature_io import (
    read_from_json,
    Measure,
    add_measure_to_json,
    EmptyArgumentsError
)
from io import StringIO
from datetime import datetime
import argparse
from pytest import raises


def test_read_from_json():
    data = '[{"city": "London", "date": "2023-01-25 12:00", "temperature": -2}]' # noqa 551
    handle = StringIO(data)
    measurments = read_from_json(handle)
    assert measurments[0].city == "London"
    assert measurments[0].temperature == -2
    assert measurments[0].date == datetime(2023, 1, 25, 12, 0)


def test_create_measure():
    measure = Measure('Toruń', 10, "2022-02-22 13:50")
    assert measure.city == 'Toruń'
    assert measure.temperature == 10
    assert measure.date.year == 2022
    assert measure.date.month == 2
    assert measure.date.day == 22
    assert str(measure.date) == "2022-02-22 13:50:00"


def test_add_measure_to_json_missing_arguments():
    handle = StringIO()
    args = argparse.Namespace(city="Toruń", date="2022-02-22 13:50") # noqa 551
    with raises(EmptyArgumentsError):
        add_measure_to_json(handle, args, [])
