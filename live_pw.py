import psutil
import GPUtil
import time

# Function to estimate CPU power consumption
def get_cpu_power_usage():
    cpu_tdp = 65  # TDP of Ryzen 7 5700G in watts
    cpu_usage = psutil.cpu_percent(interval=1)
    return (cpu_usage / 100) * cpu_tdp

# Function to get GPU power consumption
def get_gpu_power_usage():
    gpus = GPUtil.getGPUs()
    total_power_usage = 0
    for gpu in gpus:
        if gpu.name == "NVIDIA GeForce GTX 1650":
            gpu_tdp = 75  # TDP of GTX 1650 OC in watts
            gpu_power = gpu.load * gpu_tdp
            total_power_usage += gpu_power
    return total_power_usage

# Function to get power usage of other components
def get_other_components_power_usage():
    # Estimated power consumption of RAM, SSD, HDD, and motherboard
    ram_power = 3 * 2  # 2 sticks of RAM at 3W each
    ssd_power = 2
    hdd_power = 6
    motherboard_power = 30
    return ram_power + ssd_power + hdd_power + motherboard_power

# Main function to calculate total power usage
def get_total_power_usage():
    cpu_power = get_cpu_power_usage()
    gpu_power = get_gpu_power_usage()
    other_power = get_other_components_power_usage()
    total_power = cpu_power + gpu_power + other_power
    return total_power

# Monitor power usage
while True:
    total_power_usage = get_total_power_usage()
    print(f"Total Power Usage: {total_power_usage:.2f} Watts")
    time.sleep(1)
