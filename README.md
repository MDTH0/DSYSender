## HELLO IF YOU ARE ON WINDOWS YOU CAN USE LUNATII'S MOD WITHOUT THIS KINDA THING EVEN WITH DSYV2 - NO NEED FOR THIS - JUST GET LUNATII'S MOD AND DSY V2
 
hello welcome to the very cool dsysender helper which basically can take a payload and deliver to dsy on port 6969. it is a pyinstaller app.

the release folder is /dist
or the releases tab on the right

This mod as of right now makes the Resident Evil 4 Remake Adaptive Triggers and Resident Evil Requiem Adaptive Triggers Mods by Lunatii work on Linux, with DSY-V2. Hoping to Support more games (such as Red Dead Redemption 2, God of War, and other games that mod in Dualsense. That said there is a chance they will already work with DSYSender, I just have not been able to test yet. If anyone does end up trying a game not listed and it works please let me know in the Nexus Comments or Github discussions.

uh drop the files from /dist into the folder that contains the dualsensex payload and it should send them to dsy after launching dsySenderRun.sh or grab a release version and just extract the folder then copy paste those to the dualsensex payload folder

hopefully it can work with other mods such as the re4 dualsense mod for linux users because that would be gret(ill update re4 status once ive tested).

please let me know of any bugs or issues

thanks, MDTH0

the mods this was made for ( both by lunatiii):

https://www.nexusmods.com/residentevil42023/mods/5813

https://www.nexusmods.com/residentevilrequiem/mods/42

This is a Pyinstaller mod that runs a script that takes the values from Lunatii's mod and sends it through to port 6969, to be received by DualsenseY. It is run through a sh script in your console



Setup



First install dualsenseY-v2: (i installed it on cachy os from source and worked pretty good besides a couple small pkg things i had to change)
https://github.com/WujekFoliarz/DualSenseY-v2 (DualSenseY-v2)

1. Install ReFramework by Praydog
https://www.nexusmods.com/residentevilrequiem/mods/13 (reframework by praydog)

2. Install Lunatii's mod:
https://www.nexusmods.com/residentevilrequiem/mods/42 (resident evil requiem dualsenseX mod by Lunatii)

3. Install this mod and put the three files it has in it's tar.gz folder (must be extracted) in {gamefolder}/reframework/data/DualsenseX (you should see a file called payload.json, make sure the three files from this are in there)

IF you want you can view and build from source yourself on the github:
DSYSender Github

After installed launch the script and launch the game or vice versa- just make sure dualsense Y-v2 is open before launching the script.



Supported Games:


DSYSender RE Requiem Nexus:
https://www.nexusmods.com/residentevilrequiem/mods/46

DSYSender RE4 Nexus:
now up!
https://www.nexusmods.com/residentevil42023/mods/5821

