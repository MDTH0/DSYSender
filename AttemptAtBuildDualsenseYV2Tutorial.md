**Oh yeah make sure you have cmake installed --:  
i just got it from the cachy os package installer**

  
  
1. cd \{your directory here\}, mine is: ~/


2. Clone the source:  
git clone [https://github.com/WujekFoliarz/DualSenseY-v2.git](https://github.com/WujekFoliarz/DualSenseY-v2.git) \{replace directory here if wanted\} -\> your directory, mine is  the home folder, so ill leave it blank


3. Check dependencies:  
pacman -Ss appindicator  
pacman -Ss openssl

if any are missing take note of that and try to install them from your distro repository but, for example on cachyos they’re now using libayatana-appindicator instead


4. go into the directory:

cd \{clone folder\}  
mine is ~/DualSenseY-v2/

  
4. attempt build:   
cmake -S . -B build -DCMAKE\_BUILD\_TYPE=Release  
cmake --build build -j"$(nproc)"  


  
5. I get this error:  
CMake Error at /usr/share/cmake/Modules/FindPkgConfig.cmake:1093 (message):   
 The following required packages were not found:   
  
  - appindicator3-0.1   
  
Call Stack (most recent call first):   
 /usr/share/cmake/Modules/FindPkgConfig.cmake:1166 (\_pkg\_check\_modules\_internal)   
 thirdparty/traypp/CMakeLists.txt:16 (pkg\_check\_modules) 

  
6. Now i remove old failed builds:

rm -rf build


6. I have to replace a dependency in the cmake lists as the error shows me, so i run this:  
sed -i 's/\\bappindicator3-0\\.1\\b/ayatana-appindicator3-0.1/g' thirdparty/traypp/CMakeLists.txt


7. Back to step 4 and hope it works!  
  
8. and it doesnt so i then replace the bad headers with the proper ones:

command 1:
grep -R --line-number 'libappindicator/app-indicator.h' thirdparty/traypp

command 2:
sed -i 's#<libappindicator/app-indicator.h>#<libayatana-appindicator/app-indicator.h>#g' \
        thirdparty/traypp/tray/include/core/linux/tray.hpp

My DualsenseY-V2 is now installed after I go back to step 4 this time. Though there’s a lot of different distros I hope this can help you get DualsenseY-V2 installed!

When it's installed, in whichever directory the source is in (mine was in ~/DualsenseY-V2) there is now a folder in that directory called "build" and in it there is an Executable "DualsenseY".

MDTH0
