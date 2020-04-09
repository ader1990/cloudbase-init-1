### Requirements ###

#### Clean Windows Server 2016 /2019 or Windows 10 install with latest updates

#### Python 3.7 installed and added to path (with pip installed).
    Download link: https://www.python.org/ftp/python/3.7.7/python-3.7.7-amd64.exe

#### Visual Studio 2015 Community installed, with the following components:
    - Programming Languages -> Visual C++ (all)
    - Windows and Web Development -> Windows 8.1 (only Tools and Windows SDKs)

    VS 2015 Download link (you need to be logged in to access it): https://download.my.visualstudio.com/db/en_visual_studio_community_2015_with_update_1_x86_x64_web_installer_8234321.exe
    If you prefer to not build pywin32, Visual Studio 2017 / 2019 can be used too.
    Reboot after VS installation is complete.

#### All the Python packages will be built and installed using pip flags: "--no-binary :all:"

## The full build of cloudbase-init (and dependencies) from sources takes around 10 minutes.

#### How to run:


```powershell
.\build_install_from_sources.ps1 `
    -CloudbaseInitRepoUrl "https://github.com/cloudbase/cloudbase-init" `
    -PyWin32RepoUrl "https://github.com/mhammond/pywin32" `
    -PyMiRepoUrl "https://github.com/cloudbase/PyMI" `
    -BuildDir "build"

```


#### Workflow of the script:
   - Download and set pip upper requirements from OpenStack
   - Create / clean temporary build directory
   - Build and install PyWin32 from sources
   - Build and install PyMI from sources
   - Build, install and create Cloudbase-Init binary from sources