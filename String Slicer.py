#Jakob McBroome
#BME 205

def slicer(string, a, b, c, d):
    '''One line function picks out sections of a string within given indices.'''
    return string[a:b+1] + " " + string[c:d+1]
    #+1 to ensure the last character is included

slicer("HumptyDumptysatonawallHumptyDumptyhadagreatfallAlltheKingshorsesandalltheKingsmenCouldntputHumptyDumptyinhisplaceagain", 22, 27, 97, 102)
slicer("w7LavQK4AChelydraPdrwvTMQIcJZzfJP7HvT5oxr7variusfSDU28KiOfTxkYrNQsst3qN68IhAP7EjIsUpFDWY5J32cP88ztaN94JnxkXXo5XEfXetye4jO5wnqMafe0UewTIE2EMxcWxGsSHpPV9osrRJxVAAYCcbTCArAFos3m4z38M.", 9, 16, 42, 47)

