Name:		ccsm
Version:	0.9.5.92
Release:	3
Summary:	Compiz Config Settings Manager
Group:		System/X11
URL:		https://www.compiz.org/
Source:		http://releases.compiz.org/%{version}/%{name}-%{version}.tar.bz2
License:	GPL

BuildArch:	noarch
BuildRequires:	desktop-file-utils
BuildRequires:	python
BuildRequires:	intltool
Requires(post):	desktop-file-utils
Requires(postun): desktop-file-utils

Requires:	compizconfig-python
Requires:	pygtk2.0
### Is this really needed???
Suggests:	python-sexy

%description
Configuration tool for Compiz when used with the ccp configuration plugin
(default).

#----------------------------------------------------------------------------

%prep
%setup -q

%build
python setup.py build --prefix=%{_prefix}

%install
rm -rf %{buildroot}
python setup.py install --prefix=%{_prefix} --root=%{buildroot}
rm -f %{buildroot}%{py_puresitedir}/*.egg-info

%find_lang %{name}


desktop-file-install \
  --vendor="" \
  --remove-category="Compiz" \
  --add-category="GTK" \
  --add-category="Settings" \
  --add-category="DesktopSettings" \
  --add-category="X-MandrivaLinux-CrossDesktop" \
  --dir %{buildroot}%{_datadir}/applications \
  %{buildroot}%{_datadir}/applications/%{name}.desktop

%files -f %{name}.lang
%{_bindir}/%{name}
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/images
%{_datadir}/%{name}/icons
%dir %{py_puresitedir}/ccm
%{py_puresitedir}/ccm/*.py
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_datadir}/icons/hicolor/*/apps/%{name}.svg
%{_datadir}/applications/%{name}.desktop


%changelog
* Fri Nov 04 2011 Matthew Dawkins <mattydaw@mandriva.org> 0.9.5.92-1
+ Revision: 717660
- added back BR intltool
- added BR python
- fixed BRs
- new version 0.9.5.92

* Tue May 03 2011 Oden Eriksson <oeriksson@mandriva.com> 0.8.4-4
+ Revision: 663356
- mass rebuild

* Tue Nov 02 2010 Funda Wang <fwang@mandriva.org> 0.8.4-3mdv2011.0
+ Revision: 591750
- rebuild for py2.7

* Tue Mar 16 2010 Oden Eriksson <oeriksson@mandriva.com> 0.8.4-2mdv2010.1
+ Revision: 522336
- rebuilt for 2010.1

* Thu Oct 15 2009 Colin Guthrie <cguthrie@mandriva.org> 0.8.4-1mdv2010.0
+ Revision: 457729
- New version: 0.8.4
- Harden buildrequires versions
- Remove pre 2009.0 post/pre scripts

* Sun Aug 09 2009 Oden Eriksson <oeriksson@mandriva.com> 0.8.2-2mdv2010.0
+ Revision: 413221
- rebuild

* Sun Mar 15 2009 Emmanuel Andry <eandry@mandriva.org> 0.8.2-1mdv2009.1
+ Revision: 355374
- New version 0.8.2

* Sun Feb 08 2009 Colin Guthrie <cguthrie@mandriva.org> 0.8.0-0.20090208.1mdv2009.1
+ Revision: 338490
- 0.8 pre-release snapshot

* Fri Dec 26 2008 Adam Williamson <awilliamson@mandriva.org> 0.7.8-1mdv2009.1
+ Revision: 319172
- 0.7.8 final

* Fri Sep 12 2008 Colin Guthrie <cguthrie@mandriva.org> 0.7.8-0.20080912.1mdv2009.0
+ Revision: 284292
- New snapshot
- Fix .desktop file

* Sun Jul 13 2008 Colin Guthrie <cguthrie@mandriva.org> 0.7.7-0.20080713.1mdv2009.0
+ Revision: 234343
- New snapshot
- New version: 0.7.6
- Make the description a bit better

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

* Fri May 23 2008 Colin Guthrie <cguthrie@mandriva.org> 0.7.5-0.20080522.1mdv2009.0
+ Revision: 210158
- Update to git snapshot

* Tue Apr 08 2008 Colin Guthrie <cguthrie@mandriva.org> 0.7.4-1mdv2009.0
+ Revision: 192370
- New version 0.7.4

* Mon Mar 17 2008 Colin Guthrie <cguthrie@mandriva.org> 0.7.2-2mdv2008.1
+ Revision: 188210
- Fix #38930 by updating icon cache properly

* Fri Mar 07 2008 Colin Guthrie <cguthrie@mandriva.org> 0.7.2-1mdv2008.1
+ Revision: 181122
- New version 0.7.2

* Fri Feb 22 2008 Olivier Blin <blino@mandriva.org> 0.6.99-0.20080218.2mdv2008.1
+ Revision: 173923
- suggest python-sexy

* Mon Feb 18 2008 Colin Guthrie <cguthrie@mandriva.org> 0.6.99-0.20080218.1mdv2008.1
+ Revision: 172310
- Update to git master for new compiz

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sat Oct 20 2007 Colin Guthrie <cguthrie@mandriva.org> 0.6.0-1mdv2008.1
+ Revision: 100718
- New upstream release: 0.6.0

* Fri Oct 19 2007 Colin Guthrie <cguthrie@mandriva.org> 0.6.0-0.20071018.1mdv2008.1
+ Revision: 100098
- Update snapshot from 0.6.0 branch for compiz 0.6.2

* Sun Sep 02 2007 Colin Guthrie <cguthrie@mandriva.org> 0.5.2-2mdv2008.0
+ Revision: 78197
- Fixes #33074 - fix .desktop categories
- Fix typo in desktop file handling

* Mon Aug 13 2007 Colin Guthrie <cguthrie@mandriva.org> 0.5.2-1mdv2008.0
+ Revision: 62613
- Official Release: 0.5.2

* Sun Aug 12 2007 Colin Guthrie <cguthrie@mandriva.org> 0.1.0-0.20070811.1mdv2008.0
+ Revision: 62128
- Update snapshot
- Make noarch now that the invalid configure is gone
- Install properly (fixes image display)

* Wed Aug 01 2007 Colin Guthrie <cguthrie@mandriva.org> 0.1.0-0.20070801.1mdv2008.0
+ Revision: 57837
- Updated snapshot

* Wed Jul 25 2007 Colin Guthrie <cguthrie@mandriva.org> 0.1.0-0.20070724.1mdv2008.0
+ Revision: 55251
- Update Snapshot

* Sat Jul 14 2007 Colin Guthrie <cguthrie@mandriva.org> 0.1.0-0.20070714.1mdv2008.0
+ Revision: 52119
- Update snapshot

* Sat Jul 07 2007 Colin Guthrie <cguthrie@mandriva.org> 0.1.0-0.20070707.1mdv2008.0
+ Revision: 49552
- Update Snapshot to 20070707
- Obsolete Beryl Settings and GSet Compiz
- Import ccsm

