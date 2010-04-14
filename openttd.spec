Name:		openttd
Version:	1.0.0
Release:	%mkrel 2

Summary:	An open source clone of the Microprose game "Transport Tycoon Deluxe" game
Group:		Games/Strategy
License:	GPLv2
URL:		http://www.openttd.org
Source:		http://prdownloads.sourceforge.net/openttd/%{name}-%{version}-source.tar.bz2
Source1:	openttd.desktop

BuildRequires:	libpng-devel
BuildRequires:	SDL-devel
BuildRequires:	libz-devel
BuildRequires:	freetype-devel
BuildRequires:	fontconfig-devel
BuildRequires:	liblzo-devel
BuildRequires:	icu-devel
BuildRequires:	unzip
Requires:	TiMidity++
Requires:	openttd-opengfx
Requires:	openttd-opensfx
Requires:	openttd-openmsx
Buildroot:	%{_tmppath}/%{name}-%{version}-root

%description
OpenTTD is an open source clone of the Microprose game "Transport Tycoon
Deluxe" game.

%prep
%setup -q -n %{name}-%{version}

%build
%serverbuild
./configure --prefix-dir=%{_prefix}
%make

%install
rm -rf %{buildroot}
make INSTALL_DIR=%{buildroot} install

#cleanup
rm -rf %{buildroot}%{_prefix}/share/pixmaps

# desktop file
mkdir -p %{buildroot}%{_datadir}/applications
install -m 0644 %{SOURCE1} %{buildroot}%{_datadir}/applications/

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc *.txt COPYING
%{_gamesbindir}/openttd
%{_gamesdatadir}/openttd
%{_datadir}/applications/openttd.desktop
%{_datadir}/icons/hicolor/*/apps/openttd.png
%{_mandir}/man6/openttd.*
