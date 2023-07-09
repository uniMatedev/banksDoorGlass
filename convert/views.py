from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import pint

# View function for the hello world endpoint
def hello_world(request):
    return HttpResponse("Hello, World!")

# View function for the convert_units endpoint
@csrf_exempt
def convert_units(request):
    if request.method == 'POST':
        data = request.POST
        value = float(data.get('value'))
        unit = data.get('unit')

        ureg = pint.UnitRegistry()

        # Convert the value to various units
        converted_values = {
            'feet': (value * ureg(unit)).to(ureg.feet).magnitude,
            'inches': (value * ureg(unit)).to(ureg.inch).magnitude,
            'meters': (value * ureg(unit)).to(ureg.meter).magnitude,
            'miles': (value * ureg(unit)).to(ureg.mile).magnitude,
            'kilometers': (value * ureg(unit)).to(ureg.kilometer).magnitude,
            'millimeters': (value * ureg(unit)).to(ureg.millimeter).magnitude,
            'centimeters': (value * ureg(unit)).to(ureg.centimeter).magnitude,
            'nautical miles': (value * ureg(unit)).to(ureg.nautical_mile).magnitude,
        }

        return JsonResponse(converted_values)

    return JsonResponse({'error': 'Invalid request'})

# View function for the convert_volume endpoint
@csrf_exempt
def convert_volume(request):
    if request.method == 'POST':
        data = request.POST
        value = float(data.get('value'))
        unit = data.get('unit')

        ureg = pint.UnitRegistry()

        # Define the 'cubic_meter' unit
        ureg.define('cubic_meter = meter**3')

        # Define a list of volume units
        volume_units = ['liter', 'milliliter', 'cubic_meter', 'cubic_centimeter', 'gallon', 'quart', 'pint']

        # Convert the value to various volume units
        converted_values = {}
        for volume_unit in volume_units:
            converted_value = (value * ureg(unit)).to(ureg(volume_unit)).magnitude
            converted_values[volume_unit] = converted_value

        return JsonResponse(converted_values)

    return JsonResponse({'error': 'Invalid request'})

# View function for the convert_area endpoint
@csrf_exempt
def convert_area(request):
    if request.method == 'POST':
        data = request.POST
        value = float(data.get('value'))
        unit = data.get('unit')

        ureg = pint.UnitRegistry()

        # Define the area units
        ureg.define('square_meter = meter**2')
        ureg.define('square_kilometer = kilometer**2')

        # Define a list of area units
        area_units = ['square_meter', 'square_kilometer', 'square_mile', 'square_foot', 'square_inch', 'hectare', 'acre']

        # Convert the value to various area units
        converted_values = {}
        for area_unit in area_units:
            converted_value = (value * ureg(unit)).to(ureg(area_unit)).magnitude
            converted_values[area_unit] = converted_value

        return JsonResponse(converted_values)

    return JsonResponse({'error': 'Invalid request'})

# View function for the convert_temperature endpoint
@csrf_exempt
def convert_temperature(request):
    if request.method == 'POST':
        data = request.POST
        value = float(data.get('value'))
        unit = data.get('unit')

        converted_values = {}

        if unit == 'celsius':
            converted_values['celsius'] = value
            converted_values['fahrenheit'] = (value * 9/5) + 32
            converted_values['kelvin'] = value + 273.15
        elif unit == 'fahrenheit':
            converted_values['celsius'] = (value - 32) * 5/9
            converted_values['fahrenheit'] = value
            converted_values['kelvin'] = (value + 459.67) * 5/9
        elif unit == 'kelvin':
            converted_values['celsius'] = value - 273.15
            converted_values['fahrenheit'] = (value * 9/5) - 459.67
            converted_values['kelvin'] = value

        return JsonResponse(converted_values)

    return JsonResponse({'error': 'Invalid request'})

# View function for the convert_time endpoint
@csrf_exempt
def convert_time(request):
    if request.method == 'POST':
        data = request.POST
        value = float(data.get('value'))
        unit = data.get('unit')

        ureg = pint.UnitRegistry()

        # Define a list of time units
        time_units = ['second', 'minute', 'hour', 'day', 'week', 'month', 'year']

        # Convert the value to various time units
        converted_values = {}
        for time_unit in time_units:
            converted_value = (value * ureg(unit)).to(ureg(time_unit)).magnitude
            converted_values[time_unit] = converted_value

        return JsonResponse(converted_values)

    return JsonResponse({'error': 'Invalid request'})

# View function for the convert_speed endpoint
@csrf_exempt
def convert_speed(request):
    if request.method == 'POST':
        data = request.POST
        value = float(data.get('value'))
        unit = data.get('unit')

        ureg = pint.UnitRegistry()

        # Define a list of speed units
        speed_units = ['meter/second', 'kilometer/hour', 'mile/hour', 'knot']

        # Convert the value to various speed units
        converted_values = {}
        for speed_unit in speed_units:
            converted_value = (value * ureg(unit)).to(ureg(speed_unit)).magnitude
            converted_values[speed_unit] = converted_value

        return JsonResponse(converted_values)

    return JsonResponse({'error': 'Invalid request'})

# View function for the convert_weight endpoint

@csrf_exempt
def convert_weight(request):
    if request.method == 'POST':
        data = request.POST
        value = float(data.get('value'))
        unit = data.get('unit')

        ureg = pint.UnitRegistry()

        # Define a list of weight/mass units
        weight_units = ['kilogram', 'pound', 'ounce', 'gram', 'metric_ton']

        # Convert the value to various weight/mass units
        converted_values = {}
        for weight_unit in weight_units:
            converted_value = (value * ureg(unit)).to(ureg(weight_unit)).magnitude
            converted_values[weight_unit] = converted_value

        return JsonResponse(converted_values)

    return JsonResponse({'error': 'Invalid request'})

# View function for the convert_energy endpoint
@csrf_exempt
def convert_energy(request):
    if request.method == 'POST':
        data = request.POST
        value = float(data.get('value'))
        unit = data.get('unit')

        ureg = pint.UnitRegistry()

        # Define a list of energy units
        energy_units = ['joule', 'calorie', 'kilowatt_hour']

        # Convert the value to various energy units
        converted_values = {}
        for energy_unit in energy_units:
            converted_value = (value * ureg(unit)).to(ureg(energy_unit)).magnitude
            converted_values[energy_unit] = converted_value

        return JsonResponse(converted_values)

    return JsonResponse({'error': 'Invalid request'})

# View function for the convert_pressure endpoint
@csrf_exempt
def convert_pressure(request):
    if request.method == 'POST':
        data = request.POST
        value = float(data.get('value'))
        unit = data.get('unit')

        ureg = pint.UnitRegistry()

        # Define a list of pressure units
        pressure_units = ['pascal', 'atmosphere', 'pound_force_per_square_inch']

        # Convert the value to various pressure units
        converted_values = {}
        for pressure_unit in pressure_units:
            converted_value = (value * ureg(unit)).to(ureg(pressure_unit)).magnitude
            converted_values[pressure_unit] = converted_value

        return JsonResponse(converted_values)

    return JsonResponse({'error': 'Invalid request'})
