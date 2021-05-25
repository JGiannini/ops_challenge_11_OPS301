#!/usr/bin/env python3

# Author: Jamie Giannini

# Objectives: Install Psutil and create a Python script that fetches this information using Psutil:

# [X] Time spent by normal processes executing in user mode
# [X] Time spent by processes executing in kernel mode
# [X] Time when system was idle
# [X] Time spent by priority processes executing in user mode
# [X] Time spent waiting for I/O to complete.
# [X] Time spent for servicing hardware interrupts
# [X] Time spent for servicing software interrupts
# [X] Time spent by other operating systems running in a virtualized environment
# [X] Time spent running a virtual CPU for guest operating systems under the control of the Linux kernel

import psutil
import os

#Return system CPU times as a named tuple. Every attribute represents the seconds the CPU has spent in the given mode. The attributes availability varies depending on the platform:
#print(psutil.cpu_times())
cpu_times=psutil.cpu_times()
print("\nAll data (for reference):")
print(cpu_times)

#Get time spent by normal processes executing in user mode
get_user = cpu_times.user
print("\nTime spent by normal processes executing in user mode:")
print(str(get_user) + " seconds")

#Time spent by processes executing in kernel mode
get_system = cpu_times.system
print("\nTime spent by processes executing in kernel mode:")
print(str(get_system) + " seconds")

#Time when system was idle
get_idle = cpu_times.idle
print("\nTime when system was idle:")
print(str(get_idle) + " seconds")

#Time spent by priority processes executing in user mode
get_nice = cpu_times.nice
print("\nTime spent by priority processes executing in user mode:")
print(str(get_nice) + " seconds")

#Time spent waiting for I/O to complete
get_io = cpu_times.iowait
print("\nTime spent waiting for I/O to complete:")
print(str(get_io) + " seconds")

#Time spent for servicing hardware interrupts
get_irq = cpu_times.irq
print("\nTime spent for servicing hardware interrupts:")
print(str(get_irq) + " seconds")

#Time spent for servicing software interrupts
get_softirq = cpu_times.softirq
print("\nTime spent for servicing software interrupts:")
print(str(get_softirq) + " seconds")

#Time spent by other operating systems running in a virtualized environment
get_steal = cpu_times.steal
print("\nTime spent by other operating systems running in a virtualized environment:")
print(str(get_steal) + " seconds")

#Time spent running a virtual CPU for guest operating systems under the control of the Linux kernel
get_guest = cpu_times.guest
print("\nTime spent running a virtual CPU for guest operating systems under the control of the Linux kernel:")
print(str(get_guest) + " seconds\n")

#Store to file (extra)
cpu_data = open("cpu_data.txt", "w+") #w means write to file, + means read and write

cpu_info = [get_user, get_system]

cpu_data.write("PSUtil data:\n")
for i in cpu_info:
    cpu_data.write("%d\n" % (i+1))

    
cpu_data.close() 



#documentation: https://psutil.readthedocs.io/en/latest/
