# gimp_export565array
Gimp plugin for exporting image as an RGB565 array.

This GIMP plugin was developed specifically for the [AWTRIX 2.0 LED Matrix Clock](https://blueforcer.de/awtrix-2-0/). The AWTRIX API allows sending bitmaps via JSON and MQTT to the LED matrix. The data needs to be in RGB565 integer format.
This plugin takes care of the conversion directly from GIMP.

It is based on the exportC.py plugin from David Muriuki Karibe [https://github.com/Muriukidavid/gimp-plugins]

# How to use
- Copy export565array.py into the GIMP plugin directory
- Start GIMP
- Open the file to be converted
- Flatten the image if it contains layers
- Make sure it is at the correct resolution for your application (Maximum 32x8 pixels for AWTRIX)
- File -> Export 565 Array
- Enter a filename, with path if necessary
- Click OK

# Example Input

![Example Input Image](https://github.com/MrPozor/gimp_export565array/input_example.png "Example Input")

# Example Output

```
# Python code Exported from Gimp



"data": [0, 0, 51908, 0,
0, 51908, 0, 0,
64928, 0, 0, 0,
64480, 64480, 64480, 51908,
0, 0, 0, 51908,
65184, 0, 51908, 0,
65184, 51908, 0, 0,
65184,65184,65184,0
]
```
