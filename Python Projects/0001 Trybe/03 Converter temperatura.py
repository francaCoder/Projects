scales = ["CELSIUS", "FAHRENHEIT", "KELVIN"]
temp = float(input("How many degrees? ").strip())
o_scale = str(input("Origin scale: ")).strip().upper()
while o_scale not in scales:
    o_scale = str(input("Origin scale: ")).strip().upper()
d_scale = str(input("Desired scale: ")).strip().upper()
while d_scale not in scales or d_scale == o_scale:
    d_scale = str(input("Desired scale: ")).strip().upper()


def temperature_converter(temperature, origin_scale, desired_scale):
    if origin_scale == "CELSIUS":
        if desired_scale == "FAHRENHEIT":
            print((temperature * 1.8) + 32)
        else:
            print(273.15 + temperature)
    elif origin_scale == "FAHRENHEIT":
        if desired_scale == "CELSIUS":
            print((temperature - 32) / 1.8)
        else:
            print((temperature - 32) * 5/9 + 273.15)
    elif origin_scale == "KELVIN":
        if desired_scale == "CELSIUS":
            print(temperature - 273.15)
        else:
            print((temperature - 273.15) * 9/5 + 32)


temperature_converter(temp, o_scale, d_scale)


