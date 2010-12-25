%define version	1.1.0
%define pre	beta1
%define rel	1

%if %pre
%define release	%mkrel -c %{pre} %{rel}
%define source	http://binaries.openttd.org/releases/%{version}-%{pre}/%{name}-%{version}-%{pre}-source.tar.gz
%define dirname	%{name}-%{version}-%{pre}
%else
%define release	%mkrel %{rel}
%define source	http://binaries.openttd.org/releases/%{version}/%{name}-%{version}-source.tar.gz
%define dirname %{name}-%{version}
%endif

Name:		openttd
Version:	%{version}
Release:	%{release}

Summary:	An open source clone of the Microprose game "Transport Tycoon Deluxe" game
Group:		Games/Strategy
License:	GPLv2
URL:		http://www.openttd.org
Source:		%{source}

BuildRequires:	libpng-devel
BuildRequires:	SDL-devel
BuildRequires:	libz-devel
BuildRequires:	liblzma-devel
BuildRequires:	freetype-devel
BuildRequires:	fontconfig-devel
BuildRequires:	liblzo-devel
BuildRequires:	icu-devel
BuildRequires:	unzip
BuildRequires:	ccache
Requires:	TiMidity++
Requires:	openttd-opengfx
Requires:	openttd-opensfx
Requires:	openttd-openmsx
Buildroot:	%{_tmppath}/%{name}-%{version}-root

%description
OpenTTD is an open source clone of the Microprose game "Transport Tycoon
Deluxe" game.

%prep
%setup -q -n %{dirname}

%build
export CFLAGS="%{optflags}"
export CXXFLAGS="%{optflags}"
export LDFLAGS="%{ldflags}"

./configure \
	--prefix-dir=%{_prefix} \
	--with-ccache
%make VERBOSE=1

%install
rm -rf %{buildroot}
%make INSTALL_DIR=%{buildroot} install

#cleanup
rm -rf %{buildroot}%{_datadir}/pixmaps

# fix desktop file
desktop-file-install --dir=%{buildroot}%{_datadir}/applications \
        --add-category=StrategyGame \
        --remove-key=Version \
	%{buildroot}%{_datadir}/applications/openttd.desktop

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
