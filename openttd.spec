Name: openttd
Version: 0.7.1
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
OpenTTD � uma clone do jogo "Transport Tycoon Deluxe" da Microprose.
Obs: OpenTTD requer os seguintes arquivos da vers�o Windows do Transport Tycoon
Deluxe original para funcionar:
  - sample.cat
  - trg1r.grf
  - trgcr.grf
  - trghr.grf
  - trgir.grf
  - trgtr.grf
Se voc� tem o jogo original, copie estes arquivos para
%{_datadir}/games/openttd/data e divirta-se :)

#-------------------------------------------------------------------------------

%prep
rm -rf %{buildroot}

%setup -q -n %{name}-%{version}
./configure --prefix-dir=%{_prefix}

%build
%make

%install
make INSTALL_DIR=%{buildroot} install
rm -rf %{buildroot}%{_prefix}/share/pixmaps

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
%{_datadir}/applications/openttd.desktop
%{_datadir}/doc/openttd/32bpp.txt
%{_datadir}/icons/hicolor/128x128/apps/openttd.png
%{_datadir}/icons/hicolor/16x16/apps/openttd.png
%{_datadir}/icons/hicolor/256x256/apps/openttd.png
%{_datadir}/icons/hicolor/32x32/apps/openttd.png
%{_datadir}/icons/hicolor/48x48/apps/openttd.png
%{_datadir}/icons/hicolor/64x64/apps/openttd.png
%{_docdir}/openttd/multiplayer.txt
%{_docdir}/openttd/COPYING
%{_docdir}/openttd/changelog.txt
%{_docdir}/openttd/known-bugs.txt
%{_docdir}/openttd/obg_format.txt
%{_docdir}/openttd/readme.txt
%{_mandir}/man6/openttd.6.lzma
