import re
from system_1942 import in_1942, out_1942
from system_1965_1 import in_1965_1, out_1965_1
from system_1965_2 import in_1965_2, out_1965_2
from system_1965_3 import in_1965_3, out_1965_3
from system_1965_4 import in_1965_4, out_1965_4
from system_1965_5 import in_1965_5, out_1965_5
from system_1992 import in_1992, out_1992
from system_2000 import in_2000, out_2000
from BL_Kras_do_BL_WGS import from_BL_Kras_to_BL_WGS
from BL_WGS_do_BL_Kras import from_BL_WGS_to_BL_Kras


# ze stpni na dziesiętne, separatorem punktów musi być ; albo enter
DIRECTIONS = {'N': 1, 'S': -1, 'E': 1, 'W': -1}

def parse_dms_point(point_string):
    pattern = r'(\d+)°(\d+)\'([\d\.]+)"([NSWE])(\d+)°(\d+)\'([\d\.]+)"([NSWE])'
    match = re.match(pattern, point_string)
    
    if match:
        degrees_lat, minutes_lat, seconds_lat, direction_lat, degrees_lon, minutes_lon, seconds_lon, direction_lon = match.groups()
        
        decimal_lat = (float(degrees_lat) + float(minutes_lat) / 60 + float(seconds_lat) / 3600) * DIRECTIONS[direction_lat]
        decimal_lon = (float(degrees_lon) + float(minutes_lon) / 60 + float(seconds_lon) / 3600) * DIRECTIONS[direction_lon]
        
        return [decimal_lat, decimal_lon]
    else:
        raise ValueError("Invalid DMS format: " + point_string)

def dms_to_decimal(dms_string):
    dms_string = re.sub(r'[\n]+', ';', dms_string)
    dms_string = re.sub(r'[\s]+', '', dms_string)
    dms_string = re.sub(r'[,]', '', dms_string).upper()
    dms_string = dms_string.strip(';')

    point_strings = re.split(r';|\n', dms_string)
    decimal_coordinates_list = [parse_dms_point(point_string) for point_string in point_strings]
    
    return decimal_coordinates_list


# wyjście w stopniach
def decimal_to_dms(decimal_coords):
    dms_coords = []
    # Funkcja dla szerokości geograficznej
    def convert_to_dms_lat(decimal_coord):
        degrees = int(decimal_coord)
        minutes_float = (decimal_coord - degrees) * 60
        minutes = int(minutes_float)
        seconds = (minutes_float - minutes) * 60
        return degrees, minutes, seconds

    # Funkcja dla długości geograficznej
    def convert_to_dms_lon(decimal_coord):
        degrees = int(decimal_coord)
        minutes_float = (decimal_coord - degrees) * 60
        minutes = int(minutes_float)
        seconds = (minutes_float - minutes) * 60
        return degrees, minutes, seconds

    # Przekształcenie współrzędnych dziesiętnych na stopnie, minuty i sekundy
    for coord in decimal_coords:

        degrees_lat, minutes_lat, seconds_lat = convert_to_dms_lat(coord[0])
        degrees_lon, minutes_lon, seconds_lon = convert_to_dms_lon(coord[1])

        # Określenie kierunków
        direction_lat = 'N' if degrees_lat >= 0 else 'S'
        direction_lon = 'E' if degrees_lon >= 0 else 'W'

        # Sformatowanie wyniku
        dms_coords.append(f"{abs(degrees_lat)}°{minutes_lat}'{seconds_lat:.1f}\"{direction_lat} {abs(degrees_lon)}°{minutes_lon}'{seconds_lon:.1f}\"{direction_lon}")

    return dms_coords


# WYTYCZNE: separatorem musi być kropka, a oddzielenie x od y musi być za pomocą, osobne współrzędne za pomocą entera albo ;
def demacial_text_format(tekst):
    # usuwam spacje i zamieniam przecinki na średniki
    tekst = tekst.replace(' ', '').replace(';', '\n').replace(',', ';')

    # dziele tekst na listy używając znaku nowej linii i usuwam puste elementy
    listy = [element for element in re.split(r'[\n]', tekst) if element]

    coordynaty = [list(map(float, data.split(';'))) for data in listy]

    return coordynaty


def output_text_converter(result):
    formatted_text = ""
    for row in result:
        formatted_row = ",".join([f"{x:.10f}" for x in row])
        formatted_text += formatted_row.replace(",", ",\t") + "\n"
    return formatted_text




######
system_1965_in = {"1": in_1965_1,
               "2": in_1965_2,
               "3": in_1965_3,
               "4": in_1965_4,
               "5": in_1965_5
               }

system_1965_out = {"1": out_1965_1,
               "2": out_1965_2,
               "3": out_1965_3,
               "4": out_1965_4,
               "5": out_1965_5
               }

input_format_functions = {
    "opcja1": in_1942,
    "opcja2": system_1965_in.get('zonerow1965in'), 
    "opcja3": in_1992,
    "opcja4": in_2000,
    "opcja5": None,
    "opcja6": None
}

output_format_functions = {
    "opcja1": out_1942,
    "opcja2": system_1965_out.get('zonerow1965out'),
    "opcja3": out_1992,
    "opcja4": out_2000,
    "opcja5": None,
    "opcja6": None
}


def data_converter(input_data):
    if input_data['formatblin'] == 1:
        coordinates = demacial_text_format(input_data['dataEntered'])
    else:
        coordinates = dms_to_decimal(input_data['dataEntered'])

    len_data = len(coordinates)

    input_format = input_data['inputCoordinateFormat']
    output_format = input_data['outputCoordinateFormat']

    entry_ellipse = 1 if input_format in ["opcja1", "opcja2", "opcja5"] else 2
    exit_ellipse = 1 if output_format in ["opcja1", "opcja2", "opcja5"] else 2

    #konwertowanie do układu BL
    if input_format == "opcja1":
        axial_1942_in = int(input_data['axial1942in'])
        for i in range(len_data):
            coordinates[i] = in_1942(coordinates[i][0], coordinates[i][1], axial_1942_in)

    elif input_format == "opcja2":
        zone_1965_in = input_data['zonerow1965in']
        for i in range(len_data):
            coordinates[i] = system_1965_in[zone_1965_in](coordinates[i][0], coordinates[i][1])
    
    elif input_format == "opcja3":
        for i in range(len_data):
            coordinates[i] = in_1992(coordinates[i][0], coordinates[i][1])
    
    elif input_format == "opcja4":
        axial_2000_in = int(input_data['axial2000in'])
        for i in range(len_data):
            coordinates[i] = in_2000(coordinates[i][0], coordinates[i][1], axial_2000_in)
   

    #konwertowanie BL do docelowej elipsoidy
    if entry_ellipse != exit_ellipse:
        if entry_ellipse == 1:
            for point in coordinates:
                from_BL_Kras_to_BL_WGS(point[0], point[1])
        else:
            for point in coordinates:
                from_BL_WGS_to_BL_Kras(point[0], point[1])
    

    # wynik w przypadku gdy oczekiwany jest układ BL
    if output_format in ['opcja5', 'opcja6']:
        if input_data['formatblout'] == '2':
            coordinates = decimal_to_dms(coordinates)      
        return coordinates
    
    # wynik gdy oczekiwany jest układ x,y
    if output_format == "opcja1":
        axial_1942_out = int(input_data['axial1942out'])
        for i in range(len_data):
            coordinates[i] = out_1942(coordinates[i][0], coordinates[i][1], axial_1942_out)

    elif output_format == "opcja2":
        zone_1965_out = input_data['zonerow1965out']
        for i in range(len_data):
            coordinates[i] = system_1965_out[zone_1965_out](coordinates[i][0], coordinates[i][1])
    
    elif output_format == "opcja3":
        for i in range(len_data):
            coordinates[i] = out_1992(coordinates[i][0], coordinates[i][1])
    
    elif output_format == "opcja4":
        axial_2000_out = int(input_data['axial2000out'])
        for i in range(len_data):
            coordinates[i] = out_2000(coordinates[i][0], coordinates[i][1], axial_2000_out)
    
    return coordinates