legend = [
    ("Power", "pwr"),
    ("Ground", "gnd"),
    ("GPIO", "gpio"),
    ("SPI", "spi"),
    ("UART", "uart"),
    ("I2C", "i2c"),
    ("PWM", "pwm"),
    ("Analog", "analog"),
    ("Audio In", "audio-in"),
    ("Audio Out", "audio-out"),
    ("System Control", "sys"),
    ("Debug", "debug"),
    ("USB", "usb"),
    ("Not Connected", "nc"),
]

audio_out_body = {"body": {"width": 150}}
audio_in_body = {"body": {"width": 110}}
id_body = {"body": {"width": 30}}
uart_body = {"body": {"width": 100}}
pwm_body = {"body": {"width": 50}}

# Pinlabels

upper_header_left =[
    [
        ("11", "id", id_body),
        ("Boot", "sys"),
    ],
    [
        ("12", "id", id_body),
        ("Power-En", "sys"),
    ],
    [
        ("13", "id", id_body),
        ("+1.8V (out)", "pwr", {"body": {"width": 110}}),
    ],
    [
        ("14", "id", id_body),
        ("VIN (in)", "pwr", {"body": {"width": 110}}),
    ],
    [
        ("15", "id", id_body),
        ("Left Line-out +", "audio-out", audio_out_body),
    ],
    [
        ("16", "id", id_body),
        ("Left Line-out -", "audio-out", audio_out_body),
    ],
    [
        ("17", "id", id_body),
        ("Right Line-out +", "audio-out", audio_out_body),
    ],
    [
        ("18", "id", id_body),
        ("Right Line-out -", "audio-out", audio_out_body),
    ],
    [("19", "id", id_body), ("NC", "nc")]
]

upper_header_right =[
    [
        ("1", "id", id_body),
        ("Left Speaker +", "audio-out", audio_out_body),
    ],
    [
        ("2", "id", id_body),
        ("Left Speaker -", "audio-out", audio_out_body),
    ],
    [
        ("3", "id", id_body),
        ("Right Speaker +", "audio-out", audio_out_body),
    ],
    [
        ("4", "id", id_body),
        ("Right Speaker -", "audio-out", audio_out_body),
    ],
    [
        ("5", "id", id_body),
        ("Not Reset", "sys"),
    ],
    [
        ("6", "id", id_body),
        ("GND", "gnd"),
    ],
    [
        ("7", "id", id_body),
        ("USB D-", "usb"),
    ],
    [
        ("8", "id", id_body),
        ("USB D+", "usb"),
    ],
    [
        ("9", "id", id_body),
        ("GND", "gnd"),
    ],
    [
        ("10", "id", id_body),
        ("+3.3V (out)", "pwr", {"body": {"width": 110}}),
    ],
]

left_header = [
    [
        ("20", "id", id_body), ("GND", "gnd")
    ],
    [
        ("21", "id", id_body), ("GND", "gnd")
    ],
    [
        ("22", "id", id_body),
        ("GP29", "gpio"),
        ("SPI1 CSn", "spi"),
        ("UART0 RX", "uart", uart_body),
        ("I2C0 SCL", "i2c"),
        ("6B", "pwm", pwm_body),
        ("ADC3", "analog"),
    ],
    [
        ("23", "id", id_body),
        ("GP28", "gpio"),
        ("SPI1 RX", "spi"),
        ("UART0 TX", "uart", uart_body),
        ("I2C0 SDA", "i2c"),
        ("6A", "pwm", pwm_body),
        ("ADC2", "analog"),
    ],
    [
        ("24", "id", id_body),
        ("GP27", "gpio"),
        ("SPI1 TX", "spi"),
        ("UART1 RTS", "uart", uart_body),
        ("I2C1 SCL", "i2c"),
        ("5B", "pwm", pwm_body),
        ("ADC1", "analog"),
    ],
    [
        ("25", "id", id_body),
        ("GP26", "gpio"),
        ("SPI1 SCK", "spi"),
        ("UART1 CTS", "uart", uart_body),
        ("I2C1 SDA", "i2c"),
        ("5A", "pwm", pwm_body),
        ("ADC0", "analog"),
    ],
    [
        ("26", "id", id_body),
        ("GP25", "gpio"),
        ("SPI1 CSn", "spi"),
        ("UART1 RX", "uart", uart_body),
        ("I2C0 SCL", "i2c"),
        ("4B", "pwm", pwm_body)
    ],
    [
        ("27", "id", id_body),
        ("GP24", "gpio"),
        ("SPI1 RX", "spi"),
        ("UART1 TX", "uart", uart_body),
        ("I2C0 SDA", "i2c"),
        ("4A", "pwm", pwm_body)
    ],
    [
        ("28", "id", id_body),
        ("GP23", "gpio"),
        ("SPI0 TX", "spi"),
        ("UART1 RTS", "uart", uart_body),
        ("I2C1 SCL", "i2c"),
        ("3B", "pwm", pwm_body)
    ],
    [
        ("29", "id", id_body),
        ("GP22", "gpio"),
        ("SPI0 SCK", "spi"),
        ("UART1 CTS", "uart", uart_body),
        ("I2C1 SDA", "i2c"),
        ("3A", "pwm", pwm_body)
    ],
    [
        ("30", "id", id_body),
        ("GP21", "gpio"),
        ("SPI0 CSn", "spi"),
        ("UART1 RX", "uart", uart_body),
        ("I2C0 SCL", "i2c"),
        ("2B", "pwm", pwm_body),
    ],
        [
        ("31", "id", id_body),
        ("GP20", "gpio"),
        ("SPI0 RX", "spi"),
        ("UART1 TX", "uart", uart_body),
        ("I2C0 SDA", "i2c"),
        ("2A", "pwm", pwm_body)
    ],
    [
        ("32", "id", id_body),
        ("GP19", "gpio"),
        ("SPI0 TX", "spi"),
        ("UART0 RTS", "uart", uart_body),
        ("I2C1 SCL", "i2c"),
        ("1B", "pwm", pwm_body)
    ],
    [
        ("33", "id", id_body),
        ("GP18", "gpio"),
        ("SPI0 SCK", "spi"),
        ("UART0 CTS", "uart", uart_body),
        ("I2C1 SDA", "i2c"),
        ("1A", "pwm", pwm_body),
    ],
    [
        ("34", "id", id_body),
        ("GP17", "gpio"),
        ("SPI0 CSn", "spi"),
        ("UART0 RX", "uart", uart_body),
        ("I2C0 SCL", "i2c"),
        ("0B", "pwm", pwm_body),
    ],
]

right_header = [
    [
        ("68", "id", id_body),
        ("Right Headphone", "audio-out", audio_out_body),
    ],
    [
        ("67", "id", id_body),
        ("Left Headphone", "audio-out", audio_out_body),
    ],
    [
        ("66", "id", id_body),
        ("Jack Detect", "gpio", {"body": {"width": 110}}),
    ],
    [("65", "id", id_body), ("NC", "nc")],
    [("64", "id", id_body), ("NC", "nc")],
    [("63", "id", id_body), ("NC", "nc")],
    [("62", "id", id_body), ("NC", "nc")],
    [("61", "id", id_body), ("NC", "nc")],
    [("60", "id", id_body), ("NC", "nc")],
    [("59", "id", id_body), ("NC", "nc")],
    [
        ("58", "id", id_body),
        ("Left In 1", "audio-in", audio_in_body),
    ],
    [
        ("57", "id", id_body),
        ("Right In 1", "audio-in", audio_in_body),
    ],
    [
        ("56", "id", id_body),
        ("Right In 2", "audio-in", audio_in_body),
    ],
    [
        ("55", "id", id_body),
        ("Left In 2", "audio-in", audio_in_body),
    ],
    [
        ("54", "id", id_body),
        ("Left In 3", "audio-in", audio_in_body),
    ],
]

lower_header_left = [
    [
        ("35", "id", id_body),
        ("GP8", "gpio"),
        ("SPI1 RX", "spi"),
        ("UART1 TX", "uart", uart_body),
        ("I2C0 SDA", "i2c"),
        ("4A", "pwm", pwm_body),
    ],
    [
        ("36", "id", id_body),
        ("GP9", "gpio"),
        ("SPI1 CSn", "spi"),
        ("UART1 RX", "uart", uart_body),
        ("I2C0 SCL", "i2c"),
        ("4B", "pwm", pwm_body),
    ],
    [
        ("37", "id", id_body),
        ("GP10", "gpio"),
        ("SPI1 SCK", "spi"),
        ("UART1 CTS", "uart", uart_body),
        ("I2C1 SDA", "i2c"),
        ("5A", "pwm", pwm_body),
    ],
    [
        ("38", "id", id_body),
        ("GP11", "gpio"),
        ("SPI1 TX", "spi"),
        ("UART1 RTS", "uart", uart_body),
        ("I2C1 SCL", "i2c"),
        ("5B", "pwm", pwm_body),
    ],
    [
        ("39", "id", id_body),
        ("GP12", "gpio"),
        ("SPI1 RX", "spi"),
        ("UART0 TX", "uart", uart_body),
        ("I2C0 SDA", "i2c"),
        ("6A", "pwm", pwm_body),
    ],
    [
        ("40", "id", id_body),
        ("GP13", "gpio"),
        ("SPI1 CSn", "spi"),
        ("UART0 RX", "uart", uart_body),
        ("I2C0 SCL", "i2c"),
        ("6B", "pwm", pwm_body),
    ],
    [
        ("41", "id", id_body),
        ("GP14", "gpio"),
        ("SPI1 SCK", "spi"),
        ("UART0 CTS", "uart", uart_body),
        ("I2C1 SDA", "i2c"),
        ("7A", "pwm", pwm_body),
    ],
    [
        ("42", "id", id_body),
        ("GP15", "gpio"),
        ("SPI1 TX", "spi"),
        ("UART0 RTS", "uart", uart_body),
        ("I2C1 SCL", "i2c"),
        ("7B", "pwm", pwm_body),
    ],
    [
        ("43", "id", id_body),
        ("GP16", "gpio"),
        ("SPI0 RX", "spi"),
        ("UART0 TX", "uart", uart_body),
        ("I2C0 SDA", "i2c"),
        ("0A", "pwm", pwm_body),
    ],
]

lower_header_right = [
    [
        ("44", "id", id_body),
        ("GP4", "gpio"),
        ("SPI0 RX", "spi"),
        ("UART1 TX", "uart", uart_body),
        ("I2C0 SDA", "i2c"),
        ("2A", "pwm", pwm_body),
    ],
    [
        ("45", "id", id_body),
        ("GP5", "gpio"),
        ("SPI0 CSn", "spi"),
        ("UART1 RX", "uart", uart_body),
        ("I2C0 SCL", "i2c"),
        ("2B", "pwm", pwm_body),
    ],
    [
        ("46", "id", id_body),
        ("I2C1 SDA", "i2c"),
    ],
    [
        ("47", "id", id_body),
        ("I2C1 SCL", "i2c"),
    ],
    [
        ("48", "id", id_body),
        ("SWCLK", "debug"),
    ],
    [
        ("49", "id", id_body),
        ("SWDIO", "debug"),
    ],
    [
        ("50", "id", id_body),
        ("NC", "nc"),
    ],
    [
        ("51", "id", id_body),
        ("Mic Bias", "pwr"),
    ],
    [
        ("52", "id", id_body),
        ("NC", "nc"),
    ],
    [
        ("53", "id", id_body),
        ("Right In 3", "audio-in", audio_in_body),
    ],
]


# Text

title = "<tspan class='h1'>Noise Nugget 2040 Devkit</tspan>"

description = """
"""
