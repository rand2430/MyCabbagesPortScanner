"""This program was designed by Joshua Randall to scan ports on a targeted
computer to determine which are open. It also compiles all open ports and errors to
a text file."""

import socket
import datetime
import time
import os
from concurrent.futures import ThreadPoolExecutor

display_results = {}
full_results = {}


def port_scan(ip, port):
    """
    This is the port scan function. It attempts to connect to each port,
    and logs the result in display_results{} and full_results{} . If the port is open, it writes it
    into the file.
    """
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        s.connect((ip, port))
    except:
        try:
            connection = s.connect_ex((ip, port))
        except connection == 10061:
            full_results.update({port: f" Is Closed # {connection}\n"})
            display_results.update({port: "Closed"})
        except connection == 10060:
            full_results.update({port: f" Timed Out   Error # {connection}\n"})
            display_results.update({port: "Closed"})
        else:
            full_results.update({port: f" Error # {connection}\n"})
            display_results.update({port: "Closed"})

    else:
        full_results.update({port: "**********Open**********\n"})
        display_results.update({port: "**********Open**********"})
        file.write(str(target) + ":" + str(port) + "   Open\n")


print("\n" + "*"*112)
print("*"*50 + "MY CABBAGES!" + "*"*50)
print("*"*112)
print("\nThanks for starting me up!\n")

progress = "running"

while progress == "running":
    Zhu_li_do_the_thing = input("Do you want to scan a computer now? Y/N\n").lower()

    while Zhu_li_do_the_thing == "y":
        """
        Start timestamp and file path for records
        """
        timestamp = datetime.datetime.now()
        hostname = input("What is the host name of the computer you want to scan?\n")
        file = open("Joshua Randall  port scan on " + timestamp.strftime("%d%B%Y at %I%M %S%p") + ".txt", "w")
        file.write("Joshua Randall's Port Scanner:\n\n")

        try:
            """
            Testing to see if it is a valid hostname.
            """
            socket.gethostbyname(hostname)
        except:
            """
            Log DNS error
            """
            file.write("On " + datetime.datetime.now().strftime("%d%B%Y at %I:%M:%S%p") + "\n")
            file.write(f"Attempted scan on target:{hostname} failed due to DNS resolving error")
            print(f"Error resolving DNS for {hostname}.")
            print(f"Error has been logged at {os.path.abspath(file.name)}.\n")
            file.close()
        else:
            """
            Valid Hostname confirmed. Getting further information for the scan
            """
            target = socket.gethostbyname(hostname)
            print("All right, we will target " + hostname, "at " + target)

            """
            Getting input for port range and ensuring input is an integer.
            Confirming input is integer and first_port is lower than last_port.
            """
            i = True
            while i:
                j = True
                while j:
                    try:
                        first_port = int(input("\nLets get your port range. What port would you like to start at?\n"))
                    except:
                        print("That was an invalid input. Please use numerical value for ports.")
                    else:
                        j = False

                k = True
                while k:
                    try:
                        last_port = int(input("What port would you like to end at?\n")) + 1
                    except:
                        print("That was an invalid input. Please use numerical value for ports.")
                    else:
                        if first_port > (last_port-1):
                            print("Invalid port range. I need the last port to be the larger than the first.")
                            k = False
                        else:
                            k = False
                            i = False

            print("Starting port scan on computer at " + target + "\n")
            print("Depending on the range of ports selected, this could take a few minutes.\n")

            start = time.perf_counter()
            start_time = datetime.datetime.now().strftime("%d%B%Y at %I%M%p")
            file.write("Port scan for " + hostname + "at" + target + " on " + timestamp.strftime("%d%B%Y at %I%M%p") + "\n\n")
            file.write("Open Ports:\n")

            """
            Threading function to increase speed
            """
            with ThreadPoolExecutor(max_workers=500) as executor:
                for target_port in range(first_port, last_port):
                    executor.submit(port_scan, target, target_port)

            """
            Print out display_results{} in order.
            """
            key = first_port
            while key <= (last_port - 1):
                print(hostname, " Port: ", key, display_results[key])
                key += 1

            """
            Add full List of Ports and statuses to file
            """
            file.write("\nFull list of ports scanned:\n")
            key2 = first_port
            while key2 <= (last_port - 1):
                file.write(str(target) + ":" + str(key2) + str(full_results[key2]))
                key2 += 1

            """
            Cleaning up!
            """

            end = time.perf_counter()
            end_time = datetime.datetime.now().strftime("%d%B%Y at %I%M%p")
            scan_time = end - start
            print("Scan is complete")
            print("Start time was: " + str(start_time))
            print("End time was: " + str(end_time))
            print(f"Total scan time was: {round(scan_time, 2)} second(s)")
            print(f"This scan was logged in a text file at {os.path.abspath(file.name)}")
            file.write("\nTotal scan time was: " + str(round(scan_time, 2)) + " seconds.")
            file.close()

        Zhu_li_do_the_thing = input("Do you want to try another to scan another target? Y/N\n").lower()

    if Zhu_li_do_the_thing == "n":
        print("Sounds good! Have a great rest of your day!")
        progress = "done"

    else:
        print("Please type in: Y for yes, N for no. Let's try again.")
