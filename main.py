import serial
import time

def snake_configuration(ser, device_type, gigEth_intf_count, tenGigEth_intf_count = 0):
    print(b'\nconf\n')
    vlans = (gigEth_intf_count + tenGigEth_intf_count)/2
    print(b'vlan 1-' + str(vlans))#ser.write(b'vlan 1-' + str(vlans))
    print(b'\n')#ser.write(b'\n')
    if device_type == 'QSR':
        for i in range(1, vlans, 1):
            if i <= gigEth_intf_count:
                print(b'interface gigabitethernet0/1/' + str(i))#ser.write(b'interface gigabitethernet0/1/' + str(i))
            else:
                print(b'interface tengigabitethernet0/1/' + str(i))#ser.write(b'interface tengigabitethernet0/1/' + str(i))
            print(b'no shutdown\n'#ser.write(b'no shutdown\n'
                      b'switchport\n'
                      b'switchport mode access\n')
            if (i == 1) or (i == vlans):
                print(b'switchport access vlan ' + str(vlans*2))#ser.write(b'switchport access vlan ' + str(vlans*2))
            else:
                print(b'switchport access vlan ' + str(i/2))#ser.write(b'switchport access vlan ' + str(i/2))
            print(b'\n!\n')#ser.write(b'\n!\n')
        print(b'exit\n'#ser.write(b'exit\n'
                  b'commit\n'
                  b'confirm\n')
    elif device_type == 'QSW':
        for i in range(1, vlans, 1):
            print(b'interface ethernet 1/0/' + str(i))#ser.write(b'interface ethernet 1/0/' + str(i))
            print(b'switchport mode access\n')#ser.write(b'switchport mode access\n')
            if (i == 1) or (i == vlans):
                print(b'switchport access vlan ' + str(vlans*2))#ser.write(b'switchport access vlan ' + str(vlans*2))
            else:
                print(b'switchport access vlan ' + str(i/2))#ser.write(b'switchport access vlan ' + str(i/2))
            print(b'\n!\n')#ser.write(b'\n!\n')
        print(b'exit\n')#ser.write(b'exit\n')

def configuring_QSR(port, baudrate=115200, timeout=1):
    try:
        ser = serial.Serial(port, baudrate, timeout=timeout)
        print(b"\n")
        while True:
            response = ser.read(100)
            if 'User name:' in response.decode():
                print(b"admin\nadmin\n")
                break
            elif '#' in response.decode():
                break
            print(b"\n")
        print(b"show version\n")
        response = ser.read_until("#").decode()
        print("Версия устройства:")
        print(response[response.find('show version')+14::])
    except serial.SerialException as e:
        print(f"Ошибка подключения: {e}")
        return 0
    gigEth_intf_count = input ("\n\nУкажите число портов устройства типа gigabitEthernet: ")
    tenGigEth_intf_coun = input ("Укажите число портов устройства типа tebGigabitEthernet: ")
    print("Импортирую конфигурацию по заданным параметрам...")

def configuring_QSW(port, baudrate=9600, timeout=1):
    #try:
    ser = 'prikol'# serial.Serial(port, baudrate, timeout=timeout)
    print(b"\n")
    '''while True:
        #response = ser.read(100)
        #print(response.decode())
        if '>' in response.decode():
            print(b"enable\n")
            break
        elif '#' in response.decode():
            break
        print(b"\n")'''
    print(b"show version\n")
    #response = ser.read_until("#").decode()
    print("Версия устройства:")
    #print(response[response.find('show version')+14::])
    """except serial.SerialException as e:
        print(f"Ошибка подключения: {e}")
        return 0"""
    intf_count = input ("\n\nУкажите число портов устройства: ")
    print("Импортирую конфигурацию по заданным параметрам...")
    snake_configuration(ser, 'QSW', intf_count)
    

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
    