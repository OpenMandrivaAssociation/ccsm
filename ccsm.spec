%define name ccsm
%define version 0.1.0
%define rel 1
%define git 20070724

%if  %{git}
%define srcname %{name}-%{git}
%define distname %{name}
%define release %mkrel 0.%{git}.%{rel}
%else
%define srcname %{name}-%{version}
%define distname %{name}-%{version}
%define release %mkrel %{rel}
%endif

Name: %name
Version: %version
Release: %release
Summary: Compiz Config Settings Manager
Group: System/X11
URL: http://www.compiz-fusion.org/
Source: %{srcname}.tar.bz2
License: GPL
BuildRoot: %{_tmppath}/%{name}-root
BuildRequires: compiz-devel
BuildRequires: compizconfig-python-devel
BuildRequires: pygtk2.0-devel
BuildRequires: intltool
BuildRequires: desktop-file-utils
Requires(post): desktop-file-utils
Requires(postun): desktop-file-utils

Requires: compizconfig-python
Requires: pygtk2.0

Obsoletes: gset-compiz
Obsoletes: beryl-settings
Obsoletes: beryl-settings-simple

%description
Compiz Config Settings Manager

#----------------------------------------------------------------------------

%prep
%setup -q -n %{distname}

%build
%if %{git}
  # This is a GIT snapshot, so we need to generate makefiles.
  sh autogen.sh -V
%endif
%configure2_5x --disable-mime-update
%make

%install
rm -rf %{buildroot}
%makeinstall_std
%find_lang %{name}

desktop-file-install \
  --vendor="" \
  --remove-category="Settings" \
  --add-category="X-MandrivaLinux-System-Configuration-Other" \
  --dir %{buildroot}%{_datadir}/applications \
  ${buildroot}%{_datadir}/applications/%{name}.desktop

%clean
rm -rf %{buildroot}

%post
%update_menus
%{update_desktop_database}

%postun
%clean_menus
%{clean_desktop_database}

#----------------------------------------------------------------------------

%files -f %{name}.lang
%defattr(-,root,root)
%{_bindir}/%{name}
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/images
%{_datadir}/%{name}/images/*.svg
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/applications/%{name}.desktop
