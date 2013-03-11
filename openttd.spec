Name:		openttd
Version:	1.2.3
Release:	2
Summary:	An open source clone of the Microprose game "Transport Tycoon Deluxe" game
Group:		Games/Strategy
License:	GPLv2
URL:		http://www.openttd.org
Source:		http://binaries.openttd.org/releases/%{version}/%{name}-%{version}-source.tar.xz
BuildRequires:	pkgconfig(fontconfig)
BuildRequires:	pkgconfig(freetype2)
BuildRequires:	pkgconfig(liblzma)
BuildRequires:	pkgconfig(libpng)
BuildRequires:	pkgconfig(sdl)
BuildRequires:	pkgconfig(zlib)
BuildRequires:	icu-devel
BuildRequires:	liblzo-devel
BuildRequires:	unzip
BuildRequires:	ccache
BuildRequires:	desktop-file-utils
Requires:	TiMidity++
Requires:	openttd-opengfx >= 0.4.4
Requires:	openttd-opensfx
Requires:	openttd-openmsx

%description
OpenTTD is an open source clone of the Microprose game "Transport Tycoon
Deluxe" game.

%prep
%setup -q

%build
export CFLAGS="%{optflags}"
export CXXFLAGS="%{optflags}"
export LDFLAGS="%{ldflags}"

./configure \
	--prefix-dir=%{_prefix} \
	--install-dir=%{buildroot} \
	--with-ccache --enable-debug

%make VERBOSE=1

%install
%makeinstall_std

#cleanup
rm -rf %{buildroot}%{_datadir}/pixmaps

# fix desktop file
desktop-file-install --dir=%{buildroot}%{_datadir}/applications \
	--add-category=StrategyGame \
	--remove-key=Version \
	%{buildroot}%{_datadir}/applications/openttd.desktop

%files
%doc *.txt COPYING
%{_gamesbindir}/openttd
%{_gamesdatadir}/openttd
%{_datadir}/applications/openttd.desktop
%{_iconsdir}/hicolor/*/apps/openttd.png
%{_mandir}/man6/openttd.*

