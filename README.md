![davrOS](images/davros_logo_banner_lower.png)
# davrOS 
Popular British Science Fiction Linux Distro.

Not yet suitable for production usage.
## Install
Run this <b>as root</b> on any Arch Linux based distro:
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
Note: Installation will be network intensive and may take time.
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
Note: Upgrading may be network intensive and may take time.
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
[Original Canopée Wallpaper](https://raw.githubusercontent.com/yuckdevchan/davrOS/main/images/wallpapers/Canopee%20with%20Branding.png) by [Ken Vermette](https://kver.ca/)

## Licensing
Remember, davrOS is free software.
davrOS is licensed under the [GPL v2](https://www.gnu.org/licenses/old-licenses/gpl-2.0.html) <b>only</b>.

If you would like, you can support davrOS by starring it right here, for free, on GitHub!
