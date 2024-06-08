THIS APPLICATION IS FREE AND NOT FOR SALE.

Auto Wallpaper
Wallpaper app for diskless solutions. Randomize wallpaper or assign one based on IP on windows startup.

Tested on Windows 10 22H2 with CCBoot and PanCafe Pro.
This should work on any Windows 10 installation and any diskless solution provided that there is no wallpaper override like one in PanCafe Pro. If there is wallpaper override, you should delete the wallpaper.

INSTRUCTIONS

1. On your diskless server, copy extracted folder to your gamedisk.

2. Boot one client as super user.

3. On your client, delete existing uploaded wallpaper. If you are not using any billing software, skip this step.
  
	a. For those using PanCafe Pro, go to C:\Program Files (x86)\PanGroup\PanCafe Pro Client\upload (or wherever you installed it) and delete wall.bmp.

	b. For other billing software, go to their respective folder and delete the uploaded wallpaper.

4. Make the program run on startup.
   
	a. On your client, navigate to Auto Wallpaper folder.

	b. Right click on autoWallpaper.exe and click send to Desktop.

	c. On your Desktop, right click the created shortcut and click cut.

	d. Search for Run or simply press Win+R

	e. Type in "shell:startup" then hit enter.

	f. On the folder that opened, right click then paste. You should see the shortcut to autoWallpaper.exe. Right click > properties > compatibility > check run as admin.

5. You can now shutdown your client pc and disable super user. Be sure to save the changes.
    
6. Setting up the app.
   
	a. On your server, navigate to your gamedisk and create a folder Wallpaper. This is where you will place all your wallpapers. If you want PC number based wallpaper, name the wallpaper as follows; PC1.jpg, PC10.png, PC69.bmp, etc. If you want random wallpaper, filename does not matter.

	b. On your server, navigate to Auto Wallpaper folder.

	c. Right click on options.json then open with Notepad.

	d. Change "wallpaperDir" value and input the location of the folder you created in step 6a. USE THE DRIVE LETTER THAT APPEARS ON YOUR CLIENT, NOT ON SERVER. Also use double "\\" as separator instead of one, for example, "Z:\\\Wallpapers\\\Joke dito talaga".

	e. Change "mode" value to "random" if you want random wallpaper and "perPC" if you want a specific wallpaper per pc.

	f. Change "startIp" value to IP address of your PC1. Don't forget the "".

		{
		
			"wallpaperDir" : "Z:\\Wallpapers\\Joke dito talaga",

			"mode" : "perPC",

			"startIp" : "192.168.100.201"
			
		}

  	g. Save.
