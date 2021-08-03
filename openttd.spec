%global debug_package %{nil}
#define _disable_lto 1
#global ldflags %{ldflags} -fuse-ld=bfd
#define extra RC1

Name:		openttd
Version:	1.11.2
Release:	2
Summary:	An open source clone of the Microprose game "Transport Tycoon Deluxe" game
Group:		Games/Strategy
License:	GPLv2
URL:		http://www.openttd.org
Source0:	https://cdn.openttd.org/openttd-releases/%{version}/%{name}-%{version}-source.tar.xz
Patch1:		openttd-1.10.1-glibc-2.31.patch
BuildRequires:	cmake
BuildRequires:	grfcodec
BuildRequires:	pkgconfig(allegro)
BuildRequires:	pkgconfig(fontconfig)
BuildRequires:	pkgconfig(freetype2)
BuildRequires:	pkgconfig(fluidsynth)
BuildRequires:	pkgconfig(liblzma)
BuildRequires:	pkgconfig(libpng)
BuildRequires:	pkgconfig(sdl2)
BuildRequires:	pkgconfig(zlib)
BuildRequires:	icu-devel
BuildRequires:	lzo-devel
BuildRequires:	unzip
BuildRequires:	desktop-file-utils
Requires:	TiMidity++
Requires:	openttd-opengfx >= 0.5.5
Requires:	openttd-opensfx
Requires:	openttd-openmsx

%description
OpenTTD is an open source clone of the Microprose game "Transport Tycoon
Deluxe" game.

%prep
%autosetup -p1 -n %{name}-%{version}

%build
export CFLAGS="%{optflags}"
export CXXFLAGS="%{optflags}"
export LDFLAGS="%{ldflags}"

%cmake

%make_build

%install
%make_install -C build

#cleanup
rm -rf %{buildroot}%{_datadir}/pixmaps

# fix desktop file
desktop-file-install --dir=%{buildroot}%{_datadir}/applications \
	--add-category=StrategyGame \
	--remove-key=Version \
	%{buildroot}%{_datadir}/applications/openttd.desktop

%files
%doc *.txt
%doc %{_docdir}/openttd
%{_gamesbindir}/openttd
%{_gamesdatadir}/openttd
%{_datadir}/applications/openttd.desktop
%{_iconsdir}/hicolor/*/apps/openttd.png
%{_mandir}/man6/openttd.*

