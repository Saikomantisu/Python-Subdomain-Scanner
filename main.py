import requests

print("""
╭━━━╮╱╱╭╮╱╱╱╭╮╱╱╱╱╱╱╱╱╱╱╱╱╱╭━━━╮
┃╭━╮┃╱╱┃┃╱╱╱┃┃╱╱╱╱╱╱╱╱╱╱╱╱╱┃╭━╮┃
┃╰━━┳╮╭┫╰━┳━╯┣━━┳╮╭┳━━┳┳━╮╱┃╰━━┳━━┳━━┳━╮╭━╮╭━━┳━╮
╰━━╮┃┃┃┃╭╮┃╭╮┃╭╮┃╰╯┃╭╮┣┫╭╮╮╰━━╮┃╭━┫╭╮┃╭╮┫╭╮┫┃━┫╭╯
┃╰━╯┃╰╯┃╰╯┃╰╯┃╰╯┃┃┃┃╭╮┃┃┃┃┃┃╰━╯┃╰━┫╭╮┃┃┃┃┃┃┃┃━┫┃
╰━━━┻━━┻━━┻━━┻━━┻┻┻┻╯╰┻┻╯╰╯╰━━━┻━━┻╯╰┻╯╰┻╯╰┻━━┻╯
            </Developed By HeX_006>
""")

print()
domain = input("Enter The Website You Want To Scan: ")
http_or_https = input("Enter 1 For HTTP or Enter 2 For HTTPS: ")
print()

# opening the file
file = open('list.txt', 'r')
# reading the file
subdomain = file.read()
# add to a dic
subdomain = subdomain.splitlines()
subdomain_list = []


def http():
    # runing a for loop to the subdomain dic
    for subdomains in subdomain:
        # making the Complete URL
        url = f"http://{subdomains}.{domain}"

        try:
            # sending a request
            requests.get(url)

        # if ConnectionError pass
        except requests.ConnectionError:
            print("[-] Undiscovered Subdomain: " + url)
            pass

        else:
            subdomain_list.append("[+] Discovered Subdomain: " + url + "\r\n")
            print("[+] Discovered Subdomain: " + url)


def https():
    # runing a for loop to the subdomain dic
    for subdomains in subdomain:
        # making the Complete URL
        url = f"https://{subdomains}.{domain}"

        try:
            # sending a request
            requests.get(url)

        # if ConnectionError pass
        except requests.ConnectionError:
            print("[-] Undiscovered Subdomain: " + url)
            pass

        else:
            subdomain_list.append("[+] Discovered Subdomain: " + url + "\r\n")
            print("[+] Discovered Subdomain: " + url)


if http_or_https == "1":
    http()
elif http_or_https == "2":
    https()

for subdomain_lists in subdomain_list:
    discoveredSubdomainFile = open("Discovered Subdomain.txt", 'a')
    discoveredSubdomainFile.write(subdomain_lists)
discoveredSubdomainFile.close()

print()

print("[**] Scaning Finshed [**]")
