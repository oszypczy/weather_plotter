This script is a temperature measurement management system that has the following features:

- Reading temperature measurements from a JSON file 'temperature.json'
- Adding new temperature measurements to the JSON file 'temperature.json'
- Generating graphs of temperature measurements using matplotlib

The script takes command line arguments to specify the actions to be performed (either 'save' or 'graph'). If the action is 'save', then the user must also provide the city, date, and temperature as arguments. If the action is 'graph', then the user may also provide an optional 'from_time' and 'to_time' argument to specify the range of dates for which to display the temperature measurements.

The temperature measurements are stored in a JSON file in the following format:
[  {    "city": "city_name",    "date": "YYYY-MM-DD HH:MM",    "temperature": temperature_value  },  ...]

The temperature measurements are stored as instances of the Measure class, which takes the city, temperature, and date as arguments and saves them as class attributes.

The script also contains an EmptyArgumentsError class which is raised if the required arguments are not provided when saving a temperature measurement.

The script uses the argparse module to parse the command line arguments and the json module to read and write the temperature measurements to the JSON file. The matplotlib library is used to generate the graphs of the temperature measurements.
