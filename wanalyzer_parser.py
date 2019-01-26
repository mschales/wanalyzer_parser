import os
import csv
class wanalyzer:
        def run_data(data):
                try:
                        for root, dirs, files in os.walk("./data"):
                                data_file = open("./data/" + files[int(data) - 1], mode="r")
                except:
                        print("File not found, please run command FILES")
                        return
                cur = 0
                wcount = 0
                for data in data_file:
                        cur+=1
                        results = data.split('|')
                        if 'WPA' not in results[4] and 'WEP' not in results[4] and 'WPA2' not in results[4]:
                                wcount+=1
                                print("(" + str(wcount) + ") " + results[1] + " - " + results[2])
                if (wcount > 0):                    
                        print("\nFound " + str(cur) + " wifi networks, including " + str(wcount) + " open and insecure wifi networks. Notify your system administrator about these results!\n")
                else:
                        print("\nFound " + str(cur) + " wifi networks, no insecure wifi networks were found! \n")

        def get_files():
                for root, dirs, files in os.walk("./data"):
                        fcount = 0
                        for wfile in files:
                                fcount+=1
                                print(str(fcount) + " | " + str(wfile))
                print("Usage: DATA [file] number, example DATA 2\n")

        def gen_file(new_file, file_name):
                try:
                        for root, dirs, files in os.walk("./data"):
                                data_file = open("./data/" + files[int(new_file)-1], mode="r")
                except:
                        print("File not found, please run command FILES")
                        return
                with open("./generated/" + file_name + ".csv", "w") as gen_file:
                        fieldnames = ['NAME', 'MAC', 'SECURITY']
                        writer = csv.DictWriter(gen_file, fieldnames=fieldnames)
                        writer.writeheader()
                        for data in data_file:
                                results = data.split('|')
                                if 'WPA' not in results[4] and 'WEP' not in results[4] and 'WPA2' not in results[4]:
                                        writer.writerow({'NAME':results[1], 'MAC':results[2], 'SECURITY':results[4]})
                gen_file.close
                print("File created")
                
        while (True):
                cmd = input("Enter command: ")
                if (str(cmd).lower() == "files"):
                        get_files()
                elif (str(cmd).lower().startswith("data")):
                        if len(str(cmd).split(" ")) < 2:
                            print("Usage: data [file_number]")
                            continue
                        run_data(str(cmd).split(" ")[1])
                elif (str(cmd).lower().startswith("generate") or str(cmd).lower().startswith("gen")):
                        if len(str(cmd).split(" ")) < 3:
                                print("Usage: generate (file_index) (file_name_to_create)")
                                continue
                        gen_file(str(cmd).split(" ")[1], str(cmd).split(" ")[2])
                elif (str(cmd).lower()) == "exit":
                        break