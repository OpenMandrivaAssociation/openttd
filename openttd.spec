Name:		openttd
Version:	1.0.0
Release:	%mkrel 1
Summary:	An open source clone of the Microprose game "Transport Tycoon Deluxe" game
Summary(pt_BR):	Um clone do jogo "Transport Tycoon Deluxe" da Microprose.
Group:		Games/Other
Group(pt_BR):	Jogos
Group(es):	Juegos
License:	GPLv2
URL:		http://www.openttd.org
Source:		http://prdownloads.sourceforge.net/openttd/%{name}-%{version}-source.tar.bz2
Source1:	openttd.desktop
Source2:        http://bundles.openttdcoop.org/opengfx/releases/opengfx-0.2.3.zip
Source3:        http://bundles.openttdcoop.org/opensfx/releases/opensfx-0.2.3.zip
Source4:        http://bundles.openttdcoop.org/openmsx/releases/openmsx-0.2.1.zip
BuildRequires:	alsa-lib-devel
BuildRequires:	esound-devel
BuildRequires:	libpng-devel
BuildRequires:	SDL-devel
BuildRequires:	libz-devel
BuildRequires:	X11-devel
BuildRequires:	unzip
BuildRequires:  liblzo-devel
Requires:       TiMidity++
Buildroot:	%{_tmppath}/%{name}-%{version}-root

%description
OpenTTD is an open source clone of the Microprose game "Transport Tycoon
Deluxe" game.

%description -l pt_BR
OpenTTD é uma clone do jogo "Transport Tycoon Deluxe" da Microprose.

#-------------------------------------------------------------------------------

%prep
rm -rf %{buildroot}

%setup -q -n %{name}-%{version}


%build
%serverbuild
./configure --prefix-dir=%{_prefix}
%make

%install
make INSTALL_DIR=%{buildroot} install
rm -rf %{buildroot}%{_prefix}/share/pixmaps

# desktop file
mkdir -p %{buildroot}%{_datadir}/applications
install -m 0644 %{_sourcedir}/openttd.desktop %{buildroot}%{_datadir}/applications/

# gfx and sfx data
cd %{buildroot}%{_datadir}/games/%{name}/data
unzip %{SOURCE2}
unzip %{SOURCE3}
touch sample.cat

# msx data
cd %{buildroot}%{_datadir}/games/%{name}/gm
unzip %{SOURCE4}

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
%{_docdir}/openttd/obm_format.txt
%{_docdir}/openttd/obs_format.txt
%{_docdir}/openttd/readme.txt
%{_mandir}/man6/openttd.6.lzma
