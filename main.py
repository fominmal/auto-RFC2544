import serial
import time

def configuring_QSR(port, baudrate=115200, timeout=1):
    try:
        ser = serial.Serial(port, baudrate, timeout=timeout)
        ser.write(b"\n")
        while True:
            response = ser.read(100)
            if 'User name:' in response.decode():
                ser.write(b"admin\nadmin\n")
                break
            elif '#' in response.decode():
                break
            ser.write(b"\n")
        ser.write(b"show version\n")
        response = ser.read_until("#").decode()
        print("Версия устройства:")
        print(response[response.find('show version')+14::])
    except serial.SerialException as e:
        print(f"Ошибка подключения: {e}")
        return 0
    gigEth_intf_count = input ("\n\nУкажите число портов устройства типа gigabitEthernet: ")
    tenGigEth_intf_coun = input ("Укажите число портов устройства типа tebGigabitEthernet: ")
    print("Импортирую конфигурацию по заданным параметрам...")
    ser.write()

def configuring_QSW(port, baudrate=9600, timeout=1):
    try:
        ser = serial.Serial(port, baudrate, timeout=timeout)
        ser.write(b"\n")
        while True:
            response = ser.read(100)
            print(response.decode())
            if '>' in response.decode():
                ser.write(b"enable\n")
                break
            elif '#' in response.decode():
                break
            ser.write(b"\n")
        ser.write(b"show version\n")
        response = ser.read_until("#").decode()
        print("Версия устройства:")
        print(response[response.find('show version')+14::])
    except serial.SerialException as e:
        print(f"Ошибка подключения: {e}")
        return 0
    intf_count = input ("\n\nУкажите число портов устройства: ")
    print("Импортирую конфигурацию по заданным параметрам...")
    

if __name__ == "__main__":
    port = input("Укажите порт, к которому подключено ваше устройство: ")#'COM10'#
    device_type = input("Выберте тип устройства:\n" \
                        "1) QSR\n" \
                        "2) QSW\n" \
                        "Тип устройства:")
while device_type != '1' and device_type != '2':
    device_type = input("Пожалуйста, выберите 1 или 2 в соответствии с типом\nтестируемого устройства: ")
if device_type == '1':
    configuring_QSR(port)
elif device_type == '2':
    configuring_QSW(port)
    