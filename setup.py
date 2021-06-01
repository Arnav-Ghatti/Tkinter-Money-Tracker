from cx_Freeze import setup, Executable

setup(name = "Money Tracker App" ,
      version = "2.5.3" ,
      description = "" ,
      executables = [Executable("main.py")])