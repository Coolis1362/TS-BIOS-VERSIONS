import time
import keyboard
import os

def ts_bios_100_boot():
    for step in range(100):
        print("#", end="", flush=True)
        time.sleep(0.05)
        if keyboard.is_pressed('esc'):
            os.system('cls')
            boot()
        else:
            continue

    os.system('cd C:\\Users\\tadeo\\OneDrive\\Desktop\\LOCAL\\USERS\\TS-DOS\\ADMIN_USER\\BOOT')
    os.system('ts-dos')

def boot():
    while True:
        print("OPTIONS:"
              "\nTS-DOS"
              "\nTS-KERNEL 1.0.0")

        INPUT = input('BOOT>> ')
        if INPUT == "TS-DOS":
            os.system('cls')
            os.system('cd C:\\Users\\tadeo\\OneDrive\\Desktop\\LOCAL\\USERS\\TS-DOS\\ADMIN_USER\\BOOT')
            os.system('ts-dos')

        elif INPUT == "TS-KERNEL 1.0.0":
            os.system('cd C:\\Users\\tadeo\\OneDrive\\Desktop\\TS-KERNEL VERSIONS\\TS-KERNEL 1.0.0\\root\\boot')
            os.system('ts-distro-distro_name')


if __name__ == "__main__":
    ts_bios_100_boot()