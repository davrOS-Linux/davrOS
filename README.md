![davrOS](images/davros_logo_banner_lower.png)
# davrOS 
Popular British Science Fiction Linux Distro. A Post-Install script for Arch Linux written in Python.

(Not yet suitable for production usage)
## Install
Run this on an Arch Linux base install:
```shell
curl -fsSL https://davros.netlify.app/davros > davros
chmod +x davros && ./davros
```
**Warning**: Configuration and other files may be deleted, only use davrOS on a blank slate just in case.\
**Note**: Installation will be network intensive and may take time.
## Upgrade davrOS
Run this as root on your davrOS system. This will also work on any other Arch-Based distro but it will just install and upgrade packages that davrOS installs by default.
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
**Note**: Upgrading may be network intensive and may take time.
## Info
| Component Type         | davrOS Component        |
|------------------------|-------------------------|
| Base                   | [Arch Linux](https://archlinux.org/) x86_64 |
| Desktop(s)             | `hyprland`, cinnamon coming soon |
| Display Manager(s)     | `lightdm`, `sddm`, `ly` |
| Supported Architecture | x86_64                  |
| Font                   | [Hermit](https://www.programmingfonts.org/#hermit): [Nerd Font](https://www.nerdfonts.com) |
| Shell                  | `zsh`                   |
| Theme(s)               | [Catppuccin](https://github.com/catppuccin/catppuccin) Mocha |

## OS Comparison
|                                        | davrOS                   | ChimeraOS  | SteamOS 3.x  | HoloISO                | Garuda Linux                          |
|----------------------------------------|--------------------------|------------|--------------|------------------------|---------------------------------------|
| Based on                               | Arch Linux               | Arch Linux | Arch Linux   | SteamOS 3.x/Arch Linux | Arch Linux                            |
| Desktop                                | Hyprland                 | Gnome      | KDE Plasma   | KDE Plasma             | [Full List](https://garudalinux.org/) |
| Display manager                        | SDDM/GDM/LightDM/ly/None | ?          | SDDM Wayland | SDDM Wayland           | SDDM                                  |
| Officially Supported?                  | 🔴                        | 🔴          | 🟢            | 🔴                      | 🔴                                     |
| Atomic updates                         | 🟢                        | 🟢          | 🔴            | 🔴                      | 🟢                                     |
| Read-write root filesystem             | 🟢                        | 🔴          | ~            | 🟢                      | 🟢                                     |
| Custom partitioning                    | 🟢                        | 🔴          | 🔴            | 🟢                      | 🟢                                     |
| General hardware support               | 🟢                        | 🟢          | 🔴            | 🟠                      | 🟢                                     |
| Up-to-date base packages               | 🟢                        | 🟢          | 🔴            | 🔴                      | 🟢                                     |
| Can be used without Steam              | 🟢                        | 🔴          | 🔴            | 🔴                      | 🟢                                     |
| Installable on Deck (without keyboard) | 🔴 - Not Planned          | 🟢          | 🟢            | 🟢                      | 🟢                                     |
| Remote app installation                | 🟢                        | 🟢          | 🔴            | 🔴                      | 🔴                                     |
| Built-in Epic Games support            | 🟢                        | 🟢          | 🔴            | 🔴                      | 🔴                                     |
| Built-in GOG support                   | 🟢                        | 🟢          | 🔴            | 🔴                      | 🔴                                     |
| Built-in Amazon Games support          | 🟢                        | 🟢          | 🔴            | 🔴                      | 🔴                                     |
| Built-in emulation support             | 🟢                        | 🟢          | 🔴            | 🔴                      | 🔴                                     |
| Additional game tweaks                 | 🔴                        | 🟢          | 🔴            | 🔴                      | 🔴                                     |
| Additional artwork                     | 🔴 - Planned              | 🟢          | 🔴            | 🔴                      | 🔴                                     |
| Built-in GE Proton                     | 🔴 - Planned              | 🟢          | 🔴            | 🔴                      | Installable in Garuda Gamer           |
| Full source publicly hosted            | 🟢                        | 🟢          | 🔴            | 🔴                      | 🟢                                     |
| Forkable infrastructure                | 🟢                        | 🟢          | 🔴            | 🔴                      | 🟢                                     |
| Production Ready                       | 🔴                        | 🟢          | 🟠            | 🟢                      | 🟢                                     |

## Hall of Fame
### Neofetch Output
![neofetch output](images/showcase/neofetch_v3.png)
## Useful Resources
- [davrOS Website](https://davros.netlify.app)
- [Hyprland Wiki](https://wiki.hyprland.org/)
- [Arch Wiki](https://wiki.archlinux.org/)
- Inspired by the [TARDIS](https://gitlab.com/notnapoleon1/tardis) Post-Install Script

## Support Me
If you would like to support me financially, then go ahead. The following link is the best way to do so.

[![ko-fi](https://ko-fi.com/img/githubbutton_sm.svg)](https://ko-fi.com/W7W8DSYQB)

## Credits
### General
[yuckdevchan](https://github.com/yuckdevchan) is the Main Developer of [davrOS](https://github.com/yuckdevchan/davrOS)

### Art

[Ken Vermette](https://kver.ca/) created the [Original Canopée Wallpaper](https://kver.ca/2016/12/plasma-5-9-wallpaper-canopee/)

### Software Components Used in davrOS
_Credit to both these contributors and everyone else who has made contributions to these projects._

[yuckdevchan](https://github.com/yuckdevchan) authored the post install scripts and configuration files for [davrOS](https://github.com/yuckdevchan/davrOS)

[Vaxry](https://github.com/vaxerski) created [Hyprland](https://github.com/hyprwm/Hyprland)

[Roman Perepelitsa](https://github.com/romkatv) created [zsh4humans](https://github.com/romkatv/zsh4humans)

[dylanaraps](https://github.com/dylanaraps) created [neofetch](https://github.com/dylanaraps/neofetch)

## Licensing
Remember, davrOS is free software.
davrOS is licensed under the [GPL version 2](https://www.gnu.org/licenses/old-licenses/gpl-2.0.html) <b>only</b>.

If you would like, you can support davrOS by starring it right here, for free, on GitHub!
