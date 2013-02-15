%define pre	0
%define rel	1

%if %{pre}
# use lowercase %%pre in %%release
# because e.g. RC1 < beta1 (in ASCII R=82 and b=98)
%define lpre    %(echo %{pre} | tr A-Z a-z)
%define release	%mkrel -c %{lpre} %{rel}
%define sname	%{version}-%{pre}/%{name}-%{version}-%{pre}
%define dirn	%{name}-%{version}-%{pre}
%else
%define release	%{rel}
%define sname	%{version}/%{name}-%{version}
%define dirn %{name}-%{version}
%endif

Name:		openttd
Version:	1.2.3
Release:	%{release}

Summary:	An open source clone of the Microprose game "Transport Tycoon Deluxe" game
Group:		Games/Strategy
License:	GPLv2
URL:		http://www.openttd.org
Source:		http://binaries.openttd.org/releases/%{sname}-source.tar.xz

BuildRequires:	png-devel
BuildRequires:	SDL-devel
BuildRequires:	zlib-devel
BuildRequires:	liblzma-devel
BuildRequires:	freetype-devel
BuildRequires:	fontconfig-devel
BuildRequires:	liblzo-devel
BuildRequires:	icu-devel
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
%setup -q -n %{dirn}

%build
export CFLAGS="%{optflags}"
export CXXFLAGS="%{optflags}"
export LDFLAGS="%{ldflags}"

./configure \
	--prefix-dir=%{_prefix} \
	--install-dir=%{buildroot} \
	--with-ccache
%make VERBOSE=1

%install
%__rm -rf %{buildroot}
%makeinstall_std

#cleanup
%__rm -rf %{buildroot}%{_datadir}/pixmaps

# fix desktop file
desktop-file-install --dir=%{buildroot}%{_datadir}/applications \
        --add-category=StrategyGame \
        --remove-key=Version \
	%{buildroot}%{_datadir}/applications/openttd.desktop

%clean
%__rm -rf %{buildroot}

%files
%doc *.txt COPYING
%{_gamesbindir}/openttd
%{_gamesdatadir}/openttd
%{_datadir}/applications/openttd.desktop
%{_datadir}/icons/hicolor/*/apps/openttd.png
%{_mandir}/man6/openttd.*


%changelog
* Mon Jun 04 2012 Andrey Bondrov <abondrov@mandriva.org> 1.2.1-1mdv2011.0
+ Revision: 802274
- New version 1.2.1

* Mon Apr 16 2012 Andrey Bondrov <abondrov@mandriva.org> 1.2.0-1
+ Revision: 791280
- New version 1.2.0

* Sun Jan 22 2012 Andrey Bondrov <abondrov@mandriva.org> 1.1.5-1
+ Revision: 764907
- New version 1.1.5

* Sun Dec 25 2011 Andrey Bondrov <abondrov@mandriva.org> 1.1.4-1
+ Revision: 745124
- New version 1.1.4

* Mon Oct 03 2011 Andrey Bondrov <abondrov@mandriva.org> 1.1.3-1
+ Revision: 702514
- New version: 1.1.3

* Sun Jun 05 2011 Funda Wang <fwang@mandriva.org> 1.1.1-2
+ Revision: 682816
- rebuild for new icu

* Wed Jun 01 2011 Jani Välimaa <wally@mandriva.org> 1.1.1-1
+ Revision: 682352
- new version 1.1.1

* Wed May 18 2011 Jani Välimaa <wally@mandriva.org> 1.1.1-0.rc1.1
+ Revision: 676080
- new version 1.1.1 RC1

* Fri Apr 01 2011 Jani Välimaa <wally@mandriva.org> 1.1.0-1
+ Revision: 649668
- new version 1.1.0

* Sat Mar 19 2011 Jani Välimaa <wally@mandriva.org> 1.1.0-0.rc3.1
+ Revision: 646517
- new version 1.1.0 RC3

* Mon Mar 14 2011 Funda Wang <fwang@mandriva.org> 1.1.0-0.rc2.2
+ Revision: 644580
- rebuild for new icu

* Sat Mar 05 2011 Jani Välimaa <wally@mandriva.org> 1.1.0-0.rc2.1
+ Revision: 642059
- new version 1.1.0 RC2

* Sun Feb 27 2011 Funda Wang <fwang@mandriva.org> 1.1.0-0.rc1.2
+ Revision: 640484
- rebuild to obsolete old packages

* Sat Feb 19 2011 Jani Välimaa <wally@mandriva.org> 1.1.0-0.rc1.1
+ Revision: 638705
- new version 1.1.0 RC1

* Tue Feb 08 2011 Jani Välimaa <wally@mandriva.org> 1.1.0-0.beta5.1
+ Revision: 636939
- BR desktop-file-utils
- new version 1.1.0-beta5

* Sat Jan 22 2011 Jani Välimaa <wally@mandriva.org> 1.1.0-0.beta4.1
+ Revision: 632270
- new version 1.1.0 beta4

* Fri Jan 21 2011 Per Øyvind Karlsen <peroyvind@mandriva.org> 1.1.0-0.beta3.1
+ Revision: 631979
- fix define conflict

  + Jani Välimaa <wally@mandriva.org>
    - new version 1.1.0 beta3

* Sat Jan 01 2011 Jani Välimaa <wally@mandriva.org> 1.1.0-0.beta2.1mdv2011.0
+ Revision: 626980
- new version 1.1.0-beta2

* Sat Dec 25 2010 Jani Välimaa <wally@mandriva.org> 1.1.0-0.beta1.1mdv2011.0
+ Revision: 625106
- add liblzma-devel BR
- new version 1.1.0-beta1
- increase build time verbosity

* Sun Nov 21 2010 Jani Välimaa <wally@mandriva.org> 1.0.5-1mdv2011.0
+ Revision: 599391
- new version 1.0.5
  - fixes CVE-2010-4168

* Mon Nov 15 2010 Jani Välimaa <wally@mandriva.org> 1.0.5-0.RC2.1mdv2011.0
+ Revision: 597649
- new pre-release 1.0.5 RC2

* Sun Oct 31 2010 Jani Välimaa <wally@mandriva.org> 1.0.5-0.RC1.1mdv2011.0
+ Revision: 591247
- new version 1.0.5 RC1

* Wed Sep 15 2010 Jani Välimaa <wally@mandriva.org> 1.0.4-1mdv2011.0
+ Revision: 578682
- new version 1.0.4

* Tue Aug 31 2010 Jani Välimaa <wally@mandriva.org> 1.0.4-0.RC1.1mdv2011.0
+ Revision: 574876
- new version 1.0.4 RC1

* Sun Aug 01 2010 Jani Välimaa <wally@mandriva.org> 1.0.3-1mdv2011.0
+ Revision: 564216
- new version 1.0.3
- fixes CVE-2010-2534 and other bugs

* Wed Jul 21 2010 Jani Välimaa <wally@mandriva.org> 1.0.3-0.RC1.1mdv2011.0
+ Revision: 556310
- new version

* Sat Jul 10 2010 Jani Välimaa <wally@mandriva.org> 1.0.2-1mdv2011.0
+ Revision: 550024
- new version 1.0.2
- use upstream provided desktop file

* Sat May 01 2010 Jani Välimaa <wally@mandriva.org> 1.0.1-1mdv2010.1
+ Revision: 541417
- the final version of bugfix release 1.0.1

* Thu Apr 22 2010 Jani Välimaa <wally@mandriva.org> 1.0.1-0.RC2.1mdv2010.1
+ Revision: 537951
- new bugfix pre-release 1.0.1 RC2

* Sun Apr 18 2010 Jani Välimaa <wally@mandriva.org> 1.0.1-0.RC1.1mdv2010.1
+ Revision: 536493
- new bugfix pre-release 1.0.1 RC1
- improve .spec to ease building pre-releases

* Fri Apr 16 2010 Jani Välimaa <wally@mandriva.org> 1.0.0-3mdv2010.1
+ Revision: 535648
- fix compiler flags
- build with ccache

* Wed Apr 14 2010 Jani Välimaa <wally@mandriva.org> 1.0.0-2mdv2010.1
+ Revision: 534888
- clean and improve .spec a little bit
- fix BRs, remove unneeded and add needed
- opengfx, opensfx and openmsx are now in a separate packages
- fix .desktop file

* Tue Apr 06 2010 Jani Välimaa <wally@mandriva.org> 1.0.0-1mdv2010.1
+ Revision: 532112
- update opengfx and opensfx
- add openmsx and require TiMidity++ for sounds
- fix license
- add missing BR
- use compiler flags on build time

  + Olivier Faurax <ofaurax@mandriva.org>
    - New release: 1.0.0

  + Sandro Cazzaniga <kharec@mandriva.org>
    - fix mixed use of spaces and tabs
    - fix %%prep

* Mon Dec 28 2009 Gustavo Pichorim Boiko <boiko@mandriva.com> 1.0.0-0.beta1mdv2010.1
+ Revision: 483120
- Update to 1.0.0-beta 1 in order to completelly remove the dependency on the
  original game data files

* Sat Dec 12 2009 trem <trem@mandriva.org> 0.7.4-2mdv2010.1
+ Revision: 477848
- add missing file opengfx and opensfx

* Tue Aug 11 2009 Frederik Himpe <fhimpe@mandriva.org> 0.7.2-1mdv2010.0
+ Revision: 415138
- update to new version 0.7.2

* Wed Jun 10 2009 Frederik Himpe <fhimpe@mandriva.org> 0.7.1-1mdv2010.0
+ Revision: 384928
- Update to new version 0.7.1

* Wed Mar 18 2009 Zombie Ryushu <ryushu@mandriva.org> 0.6.3-2mdv2009.1
+ Revision: 357539
- Fix pixmap paths in the install stage

* Mon Dec 08 2008 Zombie Ryushu <ryushu@mandriva.org> 0.6.3-1mdv2009.1
+ Revision: 311782
- Fix pixmap paths in the install stage
- Fix pixmap paths
- Version bump to 0.6.3
- Version bump to 0.6.3

* Sun Aug 03 2008 Frederik Himpe <fhimpe@mandriva.org> 0.6.2-1mdv2009.0
+ Revision: 262435
- update to new version 0.6.2

* Thu Apr 10 2008 Gustavo Pichorim Boiko <boiko@mandriva.com> 0.6.0-1mdv2009.0
+ Revision: 192551
- New upstream release: 0.6.0

  + Thierry Vignaud <tv@mandriva.org>
    - fix description-line-too-long
    - kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Tue Oct 23 2007 Jérôme Soyer <saispo@mandriva.org> 0.5.3-1mdv2008.1
+ Revision: 101456
- New release
- New release

  + Thierry Vignaud <tv@mandriva.org>
    - fix summary-ended-with-dot

* Mon Jun 11 2007 Gustavo Pichorim Boiko <boiko@mandriva.com> 0.5.2-1mdv2008.0
+ Revision: 38038
- new upstream release: 0.5.2

* Thu May 03 2007 Gustavo Pichorim Boiko <boiko@mandriva.com> 0.5.1-1mdv2008.0
+ Revision: 21468
- Import openttd



* Thu May 03 2007 Gustavo Pichorim Boiko <boiko@mandriva.com> 0.5.1-1mdv2008.0
- Initial package for OpenTTD
