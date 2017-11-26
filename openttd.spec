%define extra %{nil}

Name:		openttd
Version:	1.7.1
Release:	%{?%{extra}:1.%{extra}.}1
Summary:	An open source clone of the Microprose game "Transport Tycoon Deluxe" game
Group:		Games/Strategy
License:	GPLv2
URL:		http://www.openttd.org
Source0:	http://binaries.openttd.org/releases/%{version}/%{name}-%{version}%{?%{extra}:-%{extra}}-source.tar.xz
Patch0:		openttd-1.4.4-compile.patch
BuildRequires:	pkgconfig(fontconfig)
BuildRequires:	pkgconfig(freetype2)
BuildRequires:	pkgconfig(liblzma)
BuildRequires:	pkgconfig(libpng)
BuildRequires:	pkgconfig(sdl)
BuildRequires:	pkgconfig(zlib)
BuildRequires:	ccache
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
%setup -q -n %{name}-%{version}%{?%{extra}:-%{extra}}
%apply_patches

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

