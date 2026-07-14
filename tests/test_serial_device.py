from serial_device import SerialDevice

print("=== Création ===")

uart = SerialDevice("UART0")

print(uart)

print()

print("=== Activation ===")

uart.enable()

print(uart)

print()

print("=== Baudrate ===")

uart.set_baudrate(9600)

print("Baudrate :", uart.get_baudrate())

print()

print("=== Transmission ===")

uart.write(0, ord("A"))

uart.write(0, ord("B"))

print("TX Buffer :", uart.tx_buffer)

print("Transmit :", chr(uart.transmit()))

print("Transmit :", chr(uart.transmit()))

print("Transmit :", uart.transmit())

print()

print("=== Réception ===")

uart.receive(ord("H"))

uart.receive(ord("i"))

print("Disponible :", uart.available())

print(chr(uart.read(0)))

print(chr(uart.read(0)))

print("Disponible :", uart.available())

print()

print("=== Reset ===")

uart.reset()

print(uart)
