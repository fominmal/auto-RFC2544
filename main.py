import serial
import time

def connect_to_device(port, baudrate=9600, timeout=1):
    try:
        ser = serial.Serial(port, baudrate, timeout=timeout)
        command = "show version\n"
        ser.write(command.encode())
        time.sleep(1)
        response = ser.read(ser.in_waiting).decode()
        print("Ответ от устройства:")
        print(response)
        ser.close()
        print("Соединение закрыто")

    except serial.SerialException as e:
        print(f"Ошибка подключения: {e}")

if __name__ == "__main__":
    port = input("Укажите порт, к которому подключено ваше устройство: ")
    baudrate = input("Укажите baudrate подключения: ")

    connect_to_device(port)