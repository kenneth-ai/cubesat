def StartConnect():
    serial.redirect(SerialPin.P14, SerialPin.P15, BaudRate.BAUD_RATE115200)
    custom.set_addr(MyAddr.ADDR)
    BME280.address(BME280_I2C_ADDRESS.ADDR_0X76)
    OLED12864_I2C.init(60)
def GetPM10(DisplayHeight: number):
    OLED12864_I2C.show_string(0, DisplayHeight + 1, "PM 1.0 : ", 1)
    OLED12864_I2C.show_number(70,
        DisplayHeight + 1,
        custom.gainParticleConcentration_ugm3(MyType.STANDARD, MyEnum.PM1_0),
        1)
    basic.pause(100)
def i2c_write():
    serial.write_line("101")
    serial.write_string("" + str(Environment.dht11value(Environment.DHT11Type.DHT11_TEMPERATURE_C, DigitalPin.P2)) + ",")
    serial.write_string("" + str(Environment.dht11value(Environment.DHT11Type.DHT11_HUMIDITY, DigitalPin.P2)) + ",")
    serial.write_string("" + str(Math.round(pins.analog_read_pin(AnalogReadWritePin.P1) / 10)) + ",")
    serial.write_string("" + str(input.compass_heading()) + ",")
    serial.write_string("" + str(input.light_level()) + ",")
    serial.write_string("" + str(custom.gainParticleConcentration_ugm3(MyType.STANDARD, MyEnum.PM2_5)) + ",")
    serial.write_string("102")
def GetGas(DisplayHeight2: number):
    OLED12864_I2C.show_string(0, DisplayHeight2 + 1, "Gas : ", 1)
    OLED12864_I2C.show_number(70,
        DisplayHeight2 + 1,
        pins.analog_read_pin(AnalogReadWritePin.P1),
        1)
    basic.pause(100)
def GetTemp(DisplayHeight3: number):
    OLED12864_I2C.show_string(0, DisplayHeight3 + 1, "Temp : ", 1)
    OLED12864_I2C.show_number(70,
        DisplayHeight3 + 1,
        Environment.dht11value(Environment.DHT11Type.DHT11_TEMPERATURE_C, DigitalPin.P2),
        1)
    basic.pause(100)
def GetPM25(DisplayHeight4: number):
    OLED12864_I2C.show_string(0, DisplayHeight4 + 1, "PM 2.5 : ", 1)
    OLED12864_I2C.show_number(70,
        DisplayHeight4 + 1,
        custom.gainParticleConcentration_ugm3(MyType.STANDARD, MyEnum.PM2_5),
        1)
    basic.pause(100)
def GetHum(DisplayHeight5: number):
    OLED12864_I2C.show_string(0, DisplayHeight5 + 1, "Hum : ", 1)
    OLED12864_I2C.show_number(70,
        DisplayHeight5 + 1,
        Environment.dht11value(Environment.DHT11Type.DHT11_HUMIDITY, DigitalPin.P2),
        1)
    basic.pause(100)
Screen = 0
strip: neopixel.Strip = None
StartConnect()
OLED12864_I2C.show_string(0, 0, "CubeSat 3.0", 1)
basic.pause(5000)

def on_forever():
    global strip, Screen
    strip = neopixel.create(DigitalPin.P16, 4, NeoPixelMode.RGB)
    Screen += 0
    if Screen < 4:
        OLED12864_I2C.clear()
        GetTemp(1)
        GetHum(2)
    elif Screen > 4:
        OLED12864_I2C.clear()
        GetGas(1)
        GetPM10(1)
        GetPM25(1)
        if Screen >= 8:
            Screen = 0
basic.forever(on_forever)

def on_every_interval():
    strip.show_color(neopixel.colors(NeoPixelColors.RED))
    i2c_write()
    strip.show_color(neopixel.colors(NeoPixelColors.GREEN))
    basic.pause(100)
    strip.show_color(neopixel.colors(NeoPixelColors.BLACK))
    music.stop_all_sounds()
    music.ring_tone(932)
    basic.pause(100)
    music.stop_all_sounds()
    strip.show_color(neopixel.colors(NeoPixelColors.GREEN))
    basic.pause(100)
    strip.show_color(neopixel.colors(NeoPixelColors.RED))
loops.every_interval(3000, on_every_interval)
