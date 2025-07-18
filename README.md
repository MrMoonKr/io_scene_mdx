# io_scene_mdx
( In Development )  
( Not Working )  
( Don't Use )

- ...

## 개발 및 테스트 환경

- 시스템 ( Computer System )  

  - AMD Ryzen 9 5900X 12-Core Processor
  - 32G RAM
  - NVIDIA Geforce RTX 3080 10GB
  - SSD 2TB
  - Windows 11 64bit Korean

- 블렌더 ( Blender 4.4.3 )  

  - [Blender Download](https://www.blender.org/download/)  
    - [v4.4.3 for Windows](https://download.blender.org/release/Blender4.4/blender-4.4.3-windows-x64.msi)  
    - [v4.4.0 for Windows](https://download.blender.org/release/Blender4.4/blender-4.4.0-windows-x64.msi)  
    - 내장된 파이썬 버전은 Python v3.11.11 입니다.  

- 파이썬 ( Python 3.12 )  

  - [Python Download](https://www.python.org/downloads/)  
    - [v3.12.0 for Windows](https://www.python.org/ftp/python/3.12.0/python-3.12.0-amd64.exe)  
    - [v3.11.9 for Windows](https://www.python.org/ftp/python/3.11.9/python-3.11.9-amd64.exe)  

- 에디터 ( Editor, Intergrated Development Environment )  

  - [VS Code](https://visualstudio.microsoft.com/ko/free-developer-offers/)  
    - [Python Extension for VS Code](https://marketplace.visualstudio.com/items?itemName=ms-python.python)  
      - Python Interpreter Chooser  
      - Pylance  
      - Python Debugger  
      -  
    - [Blender Development](https://marketplace.visualstudio.com/items?itemName=JacquesLucke.blender-development)  
      - Blender: Start  
      - Blender: Stop  
      - Blender: Run Script  
      -  

- 패키지 매니저 ( Package Manager )
  - [pypi](https://pypi.org/)  
    - [검색](https://pypi.org/search/)  
    - ...
    ```
    $ pip --version
    $ pip --help
    ```
    ```
    $ pip install fake-bpy-module-latest
    $ pip list
    ```
    ```
    $ pip freeze >> requirements.txt
    $ pip install -r ./requirements.txt
    ```


## 사용된 패키지 목록

- fake-bpy-module
  - [pypi](https://pypi.org/project/fake-bpy-module/)  
    ```
    $ pip install fake-bpy-module-latest
    ```
  - [fake-bpy-module](https://github.com/nutti/fake-bpy-module)  
  - Fake Blender Python API module collection

- ...
  - [pypi]()  
  ```
  $ vcpkg add port ...
  ```
  - [...]()
  - ...  


## ...

---  
---  
---  




# Blender_WarCraft-3
2.9x* port of PavelBlend's mdx-importer<br>
<b>Now for both .mdl and mdx</b><br>
install by either dropping the "io_scene_warcraft_3" folder in <br>C:\Users\YOU_USER\AppData\Roaming\Blender Foundation\Blender\2.8X\scripts\addons<br>
or zipping "io_scene_warcraft_3" and in blender adding it throu Edit -> Preferences -> Add-ons -> Install...<br>
<br>
Animations is imported as actions and can be found in the armature properties under "Object Data Properties"->"WarCraft 3" or "Dope Sheet"->"Action Editor"->Dropdown next to "New"<br>
<br>
<br>

This version is tested and developed on 2.92


Generally this would be the same as Bogdans branch but with adjustments for my own purposes like generating names and structures.
