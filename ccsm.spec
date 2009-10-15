%define name ccsm
%define version 0.8.4
%define rel 1
%define git 0

%if  %{git}
%define srcname %{name}-%{git}.tar.lzma
%define distname %{name}
%define release %mkrel 0.%{git}.%{rel}
%else
%define srcname %{name}-%{version}.tar.bz2
%define distname %{name}-%{version}
%define release %mkrel %{rel}
%endif

Name: %name
Version: %version
Release: %release
Summary: Compiz Config Settings Manager
Group: System/X11
URL: http://www.compiz-fusion.org/
Source: http://releases.compiz-fusion.org/%{version}/%{srcname}
License: GPL
BuildRoot: %{_tmppath}/%{name}-root
BuildArch: noarch
BuildRequires: compiz-devel >= %{version}
BuildRequires: compizconfig-python-devel >= %{version}
BuildRequires: pygtk2.0-devel
BuildRequires: intltool
BuildRequires: desktop-file-utils
Requires(post): desktop-file-utils
Requires(postun): desktop-file-utils

Requires: compizconfig-python
Requires: pygtk2.0
Suggests: python-sexy

Obsoletes: gset-compiz
Obsoletes: beryl-settings
Obsoletes: beryl-settings-simple

%description
Configuration tool for Compiz when used with the ccp configuration plugin (default).

#----------------------------------------------------------------------------

%prep
%setup -q -n %{distname}

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

%clean
rm -rf %{buildroot}

%files -f %{name}.lang
%defattr(-,root,root)
%{_bindir}/%{name}
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/images
%{_datadir}/%{name}/images/*.png
%dir %{_datadir}/%{name}/icons
%{_datadir}/%{name}/icons
%dir %{py_puresitedir}/ccm
%{py_puresitedir}/ccm/*.py
%{py_puresitedir}/ccm/*.pyc
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_datadir}/icons/hicolor/*/apps/%{name}.svg
%{_datadir}/applications/%{name}.desktop
