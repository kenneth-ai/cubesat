function StartConnect () {
    serial.redirect(
    SerialPin.P14,
    SerialPin.P15,
    BaudRate.BaudRate115200
    )
    custom.setAddr(MyAddr.ADDR)
    BME280.Address(BME280_I2C_ADDRESS.ADDR_0x76)
    OLED12864_I2C.init(60)
}
function GetPM10 (DisplayHeight: number) {
    OLED12864_I2C.showString(
    0,
    DisplayHeight - 1,
    "PM 1.0 : ",
    1
    )
    OLED12864_I2C.showNumber(
    70,
    DisplayHeight - 1,
    custom.gainParticleConcentration_ugm3(MyType.STANDARD, MyEnum.PM1_0),
    1
    )
    basic.pause(100)
}
function i2c_write () {
    serial.writeLine("101")
    serial.writeString("" + Environment.dht11value(Environment.DHT11Type.DHT11_temperature_C, DigitalPin.P2) + ",")
    serial.writeString("" + Environment.dht11value(Environment.DHT11Type.DHT11_humidity, DigitalPin.P2) + ",")
    serial.writeString("" + Math.round(pins.analogReadPin(AnalogReadWritePin.P1) / 10) + ",")
    serial.writeString("" + input.compassHeading() + ",")
    serial.writeString("" + input.lightLevel() + ",")
    serial.writeString("" + custom.gainParticleConcentration_ugm3(MyType.STANDARD, MyEnum.PM2_5) + ",")
    serial.writeString("102")
}
function GetGas (DisplayHeight: number) {
    OLED12864_I2C.showString(
    0,
    DisplayHeight - 1,
    "Gas : ",
    1
    )
    OLED12864_I2C.showNumber(
    70,
    DisplayHeight - 1,
    pins.analogReadPin(AnalogReadWritePin.P1),
    1
    )
    basic.pause(100)
}
function GetTemp (DisplayHeight: number) {
    OLED12864_I2C.showString(
    0,
    DisplayHeight - 1,
    "Temp : ",
    1
    )
    OLED12864_I2C.showNumber(
    70,
    DisplayHeight - 1,
    Environment.dht11value(Environment.DHT11Type.DHT11_temperature_C, DigitalPin.P2),
    1
    )
    basic.pause(100)
}
function GetPM25 (DisplayHeight: number) {
    OLED12864_I2C.showString(
    0,
    DisplayHeight - 1,
    "PM 2.5 : ",
    1
    )
    OLED12864_I2C.showNumber(
    70,
    DisplayHeight - 1,
    custom.gainParticleConcentration_ugm3(MyType.STANDARD, MyEnum.PM2_5),
    1
    )
    basic.pause(100)
}
function GetHum (DisplayHeight: number) {
    OLED12864_I2C.showString(
    0,
    DisplayHeight - 1,
    "Hum : ",
    1
    )
    OLED12864_I2C.showNumber(
    70,
    DisplayHeight - 1,
    Environment.dht11value(Environment.DHT11Type.DHT11_humidity, DigitalPin.P2),
    1
    )
    basic.pause(100)
}
basic.forever(function () {
	
})
loops.everyInterval(3000, function () {
	
})
