# gimp_export565array
Gimp plugin for exporting image as an RGB565 array.

This GIMP plugin was developed specifically for the AWTRIX 2.0 LED Matrix Clock. The AWTRIX API allows sending bitmaps via JSON and MQTT to the LED matrix. The data needs to be in RGB565 integer format.
This plugin takes care of the conversion directly from GIMP.

# How to use
- Copy export565array.py into the GIMP plugin directory
- Start GIMP
- Open the file to be converted
- Flatten the image if it contains layers
- Make sure it is at the correct resolution for your application (Maximum 32x8 pixels for AWTRIX)
- File -> Export 565 Array
- Enter a filename, with path if necessary
- Click OK
