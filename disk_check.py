# Simple HDD checker I use before laptop repairs
# Helps me and students confirm drive size quickly
import wmi
c = wmi.WMI()
print("=== HDD/SSD Health Check ===")
for disk in c.Win32_DiskDrive():
    print(f"Drive: {disk.Caption}")
    for partition in disk.associators("Win32_DiskDriveToDiskPartition"):
        for logical_disk in partition.associators("Win32_LogicalDiskToPartition"):
            print(f"  {logical_disk.Caption} Size: {int(logical_disk.Size)/1024**3:.1f} GB")
print("\nUsed during laptop diagnostics at EasyClinic IT Solutions")
