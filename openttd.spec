%define extra %{nil}

Name:		openttd
Version:	1.9.0
Release:	%{?%{extra}:1.%{extra}.}1
Summary:	An open source clone of the Microprose game "Transport Tycoon Deluxe" game
Group:		Games/Strategy
License:	GPLv2
URL:		http://www.openttd.org
Source0:	http://binaries.openttd.org/releases/%{version}/%{name}-%{version}%{?%{extra}:-%{extra}}-source.tar.xz
Patch0:		openttd-1.4.4-compile.patch
Patch1:		openttd-1.8.0-icu-61.patch
BuildRequires:	pkgconfig(fontconfig)
BuildRequires:	pkgconfig(freetype2)
BuildRequires:	pkgconfig(liblzma)
BuildRequires:	pkgconfig(libpng)
BuildRequires:	pkgconfig(sdl)
BuildRequires:	pkgconfig(zlib)
BuildRequires:	icu-devel
BuildRequires:	lzo-devel
BuildRequires:	unzip
BuildRequires:	desktop-file-utils
Requires:	TiMidity++
Requires:	openttd-opengfx >= 0.4.6
Requires:	openttd-opensfx
Requires:	openttd-openmsx

%description
OpenTTD is an open source clone of the Microprose game "Transport Tycoon
Deluxe" game.

%prep
%autosetup -p1 -n %{name}-%{version}%{?%{extra}:-%{extra}}

%build
export CFLAGS="%{optflags}"
export CXXFLAGS="%{optflags}"
export LDFLAGS="%{ldflags}"

./configure \
	--prefix-dir=%{_prefix} \
	--install-dir=%{buildroot} \
	--enable-debug

%make_build VERBOSE=1

%install
%make_install

#cleanup
rm -rf %{buildroot}%{_datadir}/pixmaps

# fix desktop file
desktop-file-install --dir=%{buildroot}%{_datadir}/applications \
	--add-category=StrategyGame \
	--remove-key=Version \
	%{buildroot}%{_datadir}/applications/openttd.desktop

%files
%doc *.txt COPYING
%doc %{_docdir}/openttd
%{_gamesbindir}/openttd
%{_gamesdatadir}/openttd
%{_datadir}/applications/openttd.desktop
%{_iconsdir}/hicolor/*/apps/openttd.png
%{_mandir}/man6/openttd.*

