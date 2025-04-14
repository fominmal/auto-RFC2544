import serial
import time

def connect_to_device(port, baudrate=9600, timeout=1):
    try:
        # Открываем последовательный порт
        ser = serial.Serial(port, baudrate, timeout=timeout)
        print(f"Подключено к {port} с baudrate {baudrate}")

        # Пример отправки команды устройству
        command = "show version\n"
        ser.write(command.encode())

        # Чтение ответа от устройства
        time.sleep(1)  # Даем время устройству на ответ
        response = ser.read(ser.in_waiting).decode()
        print("Ответ от устройства:")
        print(response)

        # Закрываем последовательный порт
        ser.close()
        print("Соединение закрыто")

    except serial.SerialException as e:
        print(f"Ошибка подключения: {e}")

if __name__ == "__main__":
    # Укажите порт, к которому подключено ваше устройство
    port = "COM10"  # Для Windows, например
    # port = "/dev/ttyUSB0"  # Для Linux, например

    connect_to_device(port)