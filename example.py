import ili9342c
color565 = ili9342c.color565
from machine import Pin, SPI
spi = SPI(miso=Pin(19), mosi=Pin(23, Pin.OUT), sck=Pin(18, Pin.OUT))
display = ili9342c.ILI934X(spi, cs=Pin(14), dc=Pin(27), rst=Pin(33), bl=Pin(32))
display.fill(color565(0x00, 0x00, 0x00))

display.fill_rectangle(150, 150, 40, 10, color565(0x00, 0xff, 0x00))
display.fill_rectangle(10, 10, 20, 60, color565(0x00, 0x00, 0xff))
display.fill_rectangle(200, 70, 50, 50, color565(0xff, 0x00, 0x00))
display.text('Hello,World!', 16, 128)
display.scroll(8)
display.scroll(8)

import sys
del sys.modules['ili9342c']
del sys
