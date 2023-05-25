![davrOS](images/davros_logo_banner_lower.png)
# davrOS
Popular British Science Fiction Linux Distro.
## Install
Run this as root on any Arch Linux based distro:
```shell
if command -v curl >/dev/null 2>&1; then
  curl -fsSL "https://davros.netlify.app/post-install.sh" > davros
  curl -fsSL "https://davros.netlify.app/pkg.txt" > pkg.txt
else
  wget "https://davros.netlify.app/post-install.sh"
  wget "https://davros.netlify.app/pkg.txt"
  mv post-install.sh davros
fi
chmod +x davros
./davros
```
## Upgrade davrOS
```shell
if command -v curl >/dev/null 2>&1; then
  curl -fsSL "https://davros.netlify.app/upgrade.sh" > davros
  curl -fsSL "https://davros.netlify.app/pkg.txt" > pkg.txt
else
  wget "https://davros.netlify.app/upgrade.sh"
  wget "https://davros.netlify.app/pkg.txt"
  mv upgrade.sh davros
fi
chmod +x davros
./davros
```
## Info
| Component Type         | davrOS Component  |
|------------------------|-------------------|
| Base                   | Arch Linux x86_64 |
| Desktop(s)             | `hyprland`        |
| Display Manager(s)     | `lightdm`         |
| Supported Architecture | x86_64            |
## Hall of Fame
### Neofetch Output
![neofetch output](images/showcase/neofetch_v3.png)
## Licensing
Remember, davrOS is free software.
davrOS is licensed under the [GPL v2](https://www.gnu.org/licenses/old-licenses/gpl-2.0.html) <b>only</b>.

If you would like, you can support davrOS by starring it right here, for free, on GitHub!
