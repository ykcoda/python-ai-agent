import subprocess


with open("hosts.txt") as file:
    ips = file.read().splitlines()

    for ip in ips:
        try:
            command = f"ping -c 5 {ip}"
            output = subprocess.check_output(command.split())
            print(output.decode())
        except subprocess.CalledProcessError as e:
            print(f"{e}")

        print("#" * 50)
