%define _empty_manifest_terminate_build 0

Name:		openttd
Version:	15.0~beta2
Release:	1
Summary:	An open source clone of the Microprose game "Transport Tycoon Deluxe" game
Group:		Games/Strategy
License:	GPLv2
URL:		https://www.openttd.org
Source0:	https://cdn.openttd.org/openttd-releases/15.0-beta2/%{name}-15.0-beta2-source.tar.xz

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
%autosetup -p1 -n %{name}-15.0-beta2

%build
#ifarch %{x86_64}
# Workaround for clang 16.0.2 generating an unresolvable reference to
# _newgrf_textrefstack in openttd 13.1
#export CC=gcc
#export CXX=g++
#endif

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
%doc %{_docdir}/openttd
%{_gamesbindir}/openttd
%{_gamesdatadir}/openttd
%{_datadir}/applications/openttd.desktop
%{_iconsdir}/hicolor/*/apps/openttd.png
%{_mandir}/man6/openttd.*

