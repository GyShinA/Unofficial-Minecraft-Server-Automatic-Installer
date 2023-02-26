print("Welcome to the unofficial Minecrraft Server installer for Microsoft Windows 10 and 11!")
print("Please note that this installer is not affiliated with Mojang or Microsoft in any way.")
print("Installer made by Patuiqx#1939, Dm me on Discord if you have any questions.")


print("-> Install server software")
print("[I1] Install Minecraft Server - Software: Purpur (Recommended)")
print("[I2] Install Minecraft Server - Software: Paper")
print("[I3] Install Minecraft Server - Software: Spigot (Performance issues)")
print("[I4] Install Minecraft Server - Software: CraftBukkit (Not Recommended)")


print("-> Information and settings")
print("[N1] Auto-Accept EULA? (Yes/No) [Not implemented yet]")
print("[N2] Auto-Create start script? (Default of: java -Xmx2024M -Xms2024M -jar server.jar nogui) (Yes/No)")


print("-> Exit")
print("[E1] Exit installer")

print("Would you like to change any setting?")
yesornot = input("Yes or No: ")
if yesornot == "Yes":
    option2 = input("Please select an option: ")
    if option2 == "N1":
        print("This setting is not implemented yet.")

    if option2 == "N2":
        val1 = input("Please enter the new value: ")
        if val1 == "Yes":
            print("Variable changed")
            acss = True

        if val1 == "No":
            print("Variable changed")
            acss = False

option = input("Please select an option: ")

if option == "I1":

    import os

    print("Installing Purpur...")
    os.system("curl -o server.jar https://api.purpurmc.org/v2/purpur/1.19.3/1921/download")
    print("Done!")
    if acss:
        print("Creating start script...")
        os.system("echo java -Xmx2024M -Xms2024M -jar server.jar nogui > start.bat")
        print("Done!")

    print("Please run the server once to generate the eula.txt file.")
    print("After that, you can close the server and edit the eula.txt file to accept the EULA.")
    print("After that, you can run the server again.")
    print("Have fun!")
    print("Press any key to exit...")
    input()
    exit()

if option == "I2":
    
        import os
    
        print("Installing Paper...")
        os.system("curl -o server.jar https://api.papermc.io/v2/projects/paper/versions/1.19.3/builds/420/downloads/paper-1.19.3-420.jar")
        print("Done!")
        if acss:
            print("Creating start script...")
            os.system("echo java -Xmx2024M -Xms2024M -jar server.jar nogui > start.bat")
            print("Done!")
    
        print("Please run the server once to generate the eula.txt file.")
        print("After that, you can close the server and edit the eula.txt file to accept the EULA.")
        print("After that, you can run the server again.")
        print("Have fun!")
        print("Press any key to exit...")
        input()
        exit()

if option == "I3":
        
            import os
        
            print("Installing Spigot...")
            os.system("curl -o server.jar https://download1592.mediafire.com/0gbeflva4uwgoAo6J0I9dSVi7nhwxCwNgVI1P56x4x2TrxxomgLW2dsf56mgv2ZwfzX5mzFPHMscJG3kWkC2aKlt/joc6nqzrf0x6cc5/spigot_jar.jar")
            print("Done!")
            if acss:
                print("Creating start script...")
                os.system("echo java -Xmx2024M -Xms2024M -jar server.jar nogui > start.bat")
                print("Done!")
        
            print("Please run the server once to generate the eula.txt file.")
            print("After that, you can close the server and edit the eula.txt file to accept the EULA.")
            print("After that, you can run the server again.")
            print("Have fun!")
            print("Press any key to exit...")
            input()
            exit()

if option == "I4":
                
    import os
                
    print("Installing CraftBukkit...")
    os.system("curl -o server.jar https://download.getbukkit.org/craftbukkit/craftbukkit-1.19.3.jar")
    print("Done!")
    if acss:
        print("Creating start script...")
        os.system("echo java -Xmx2024M -Xms2024M -jar server.jar nogui > start.bat")
        print("Done!")
                
    print("Please run the server once to generate the eula.txt file.")
    print("After that, you can close the server and edit the eula.txt file to accept the EULA.")
    print("After that, you can run the server again.")
    print("Have fun!")
    print("Press any key to exit...")
    input()
    exit()
