import winreg
import os

GPU_path = r"SYSTEM\ControlSet001\Control\Class\{4d36e968-e325-11ce-bfc1-08002be10318}\0000"
CPU_path = r"HARDWARE\DESCRIPTION\System\CentralProcessor\0"

GPU_value = "NVIDIA GeForce RTX 2080"
CPU_value = "AMD Ryzen 9 7900X3D 12-Core Processor"

ArenaLauncher = "arena_breakout_infinite_launcher.exe"

def main():
    try:
        print("Changing GPU registry...")
        registry_key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, GPU_path, 0, winreg.KEY_WRITE)
        winreg.SetValueEx(registry_key, "DriverDesc", 0, winreg.REG_SZ, GPU_value)

        print("Changing GPU registry succeeded!")

    except Exception as err:
        print("Changing GPU registry failed :(")
        print("Error:", err)


    try:
        print("Changing CPU registry...")
        registry_key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, CPU_path, 0, winreg.KEY_WRITE)
        winreg.SetValueEx(registry_key, "ProcessorNameString", 0, winreg.REG_SZ, CPU_value)

        print("Changing CPU registry succeeded!")

    except Exception as err:
        print("Changing CPU registry failed :(")
        print("Error:", err)


    try:
        print("Start Arena launcher...")
        os.system("arena_breakout_infinite_launcher.exe")
        print("All done. GG :)")

    except Exception as err:
        print("Couldn't launch Arena launcher. Please run it manually.")
        print("Error:", err)


main()
