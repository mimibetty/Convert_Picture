# Convert_Picture
Convert PNG to rgb matrix     and   rgb matrix to png


install library: 
pip install Pillow
```
Note: Pillow is a fork of PIL that adds some additional features and is more actively maintained. It can be used as a drop-in replacement for PIL.




How to create an exe file from python program?
To create an executable file from a Python program, you can use a tool called PyInstaller. PyInstaller is a cross-platform program, which means that you can use it on Windows, Linux, and macOS.

To create an executable file using PyInstaller, you can follow these steps:

Install PyInstaller by running the following command in your terminal or command prompt:

Copy
pip install pyinstaller
```

Navigate to the directory where your Python program is located.

Run the following command to create an executable file:

Copy
pyinstaller --onefile your_script_name.py
```

Replace `your_script_name.py` with the name of your Python script.

PyInstaller will create a new directory called dist in your current directory. Inside the dist directory, there will be an executable file with the same name as your script.

You can now distribute this executable file to others, and they can run your Python program without needing to install Python or any dependencies.

Note that PyInstaller may not work for every Python program, especially if your program has complex dependencies or uses C extensions. In that case, you may need to explore other tools like cx_Freeze or py2exe.
