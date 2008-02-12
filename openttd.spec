Name: openttd
Version: 0.5.3
Release: %mkrel 1
Summary: An open source clone of the Microprose game "Transport Tycoon Deluxe" game
Summary(pt_BR): Um clone do jogo "Transport Tycoon Deluxe" da Microprose.
Group: Games/Other
Group(pt_BR): Jogos
Group(es): Juegos
License: GPL
URL: http://www.openttd.org
Source: http://prdownloads.sourceforge.net/openttd/%{name}-%{version}-source.tar.bz2
Source1: openttd.desktop
BuildRequires: alsa-lib-devel
BuildRequires: esound-devel
BuildRequires: libpng-devel
BuildRequires: SDL-devel
BuildRequires: libz-devel
BuildRequires: X11-devel
Buildroot: %{_tmppath}/%{name}-%{version}-root

%description
OpenTTD is an open source clone of the Microprose game "Transport Tycoon
Deluxe" game.
Note: OpenTTD requires these data files from the original Windows version
of Transport Tycoon Deluxe in order to function:
  - sample.cat
  - trg1r.grf
  - trgcr.grf
  - trghr.grf
  - trgir.grf
  - trgtr.grf
If you have the original game, just copy these files into
%{_datadir}/games/openttd/data  and have fun :)

%description -l pt_BR
OpenTTD é uma clone do jogo "Transport Tycoon Deluxe" da Microprose.
Obs: OpenTTD requer os seguintes arquivos da versão Windows do Transport Tycoon
Deluxe original para funcionar:
  - sample.cat
  - trg1r.grf
  - trgcr.grf
  - trghr.grf
  - trgir.grf
  - trgtr.grf
Se você tem o jogo original, copie estes arquivos para
%{_datadir}/games/openttd/data e divirta-se :)

#-------------------------------------------------------------------------------

%prep
rm -rf %{buildroot}

%setup -q -n %{name}-%{version}
echo "
WITH_NETWORK:=1
INSTALL:=1
PREFIX:=%{_prefix}
BINARY_DIR:=games
DATA_DIR:=share/games/openttd
USE_HOMEDIR:=~
PERSONAL_DIR:=.openttd
SECOND_DATA_PATH:=
CUSTOM_LANG_PATH:=
WITH_ZLIB:=1
WITH_SDL:=1.2.8
WITH_PNG:=1.2.8
UNIX:=1
SDL-CONFIG:=sdl-config
CONFIG_INCLUDED:=yes
CONFIG_VERSION:=6
" > Makefile.config

%build
%make

%install
make install DEST_DIR:=%{buildroot}
mkdir -p %{buildroot}%{_datadir}/icons/hicolor/32x32/apps
mkdir -p %{buildroot}%{_datadir}/icons/hicolor/64x64/apps
mv %{buildroot}%{_prefix}/openttd.32.xpm %{buildroot}%{_datadir}/icons/hicolor/32x32/apps/openttd.xpm
mv %{buildroot}%{_prefix}/openttd.64.png %{buildroot}%{_datadir}/icons/hicolor/64x64/apps/openttd.png
rm -f %{buildroot}%{_prefix}/openttd.32.bmp

# desktop file
mkdir -p %{buildroot}%{_datadir}/applications
install -m 0644 %{_sourcedir}/openttd.desktop %{buildroot}%{_datadir}/applications/

%clean
rm -rf %{buildroot}

%files
%defattr(0644,root,root,0755)
%attr(0755,root,root) %{_prefix}/games/openttd
%dir %{_datadir}/games/openttd
%{_datadir}/games/openttd/*
%{_datadir}/icons/hicolor/32x32/apps/openttd.xpm
%{_datadir}/icons/hicolor/64x64/apps/openttd.png
%{_datadir}/applications/openttd.desktop
