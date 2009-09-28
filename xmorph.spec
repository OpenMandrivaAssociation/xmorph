%define name		xmorph
%define release %mkrel 1
%define version 20060817
%define epoch		2
%define lib_major	0
%define lib_name_orig	%mklibname morph
%define lib_name	%{lib_name_orig}%{lib_major}

Summary:	An X Window System tool for creating morphed images
Name:		%{name}
Version:	%{version}
Release:	%{release}
Epoch:		%{epoch}
License:	GPL
Group:		Graphics
BuildRequires:	xaw-devel
BuildRequires:	bison
BuildRequires:	gettext-devel
BuildRequires:	gtk+2-devel
BuildRequires:	texinfo
# for X11/bitmaps/gray:
BuildRequires:	x11-data-bitmaps
URL:		http://sourceforge.net/projects/xmorph/
Source0:	xmorph_%{version}.tar.gz
Source2:	xmorph-icons.tar.bz2
# (fc) 20060817-1mdv fix build with latest gcc
Patch0:		xmorph-20060817-fixbuild.patch
BuildRoot:	%_tmppath/%name-%version-%release-buildroot

%package -n %{lib_name}
Summary:	Internal library required for xmorph/gtkmorph
Provides:	%{lib_name_orig}
Group:		Graphics

%package -n %{lib_name}-devel
Summary:	Headers and static libraries required for xmorph/gtkmorph development
Requires:	%{lib_name} = %{epoch}:%{version}-%{release}
Provides:	%{lib_name_orig}-devel, %{name}-devel
Group:		Graphics

%description
Xmorph is a digital image warping (aka morphing) program.  Xmorph
provides the tools needed and comprehensible instructions for you to
create morphs: changing one image into another.  Xmorph runs under the
X Window System.

Install the xmorph package if you need a program that will create
morphed images.

%description -n %{lib_name}
Internal library for xmorph and gtkmorph.

%description -n %{lib_name}-devel
Development headers and static libs for xmorph and gtkmorph.

%prep
%setup -q
%patch0 -p1 -b .fixbuild


%build
%configure2_5x --without-morph --with-gtk=2
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

#mdk menu 
mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications/
cat << EOF > %buildroot%{_datadir}/applications/mandriva-xmorph.desktop
[Desktop Entry]
Type=Application
Categories=Graphics;Viewer;
Name=Xmorph
Comment=Morphing software
Exec=gtkmorph
Icon=xmorph
EOF

#mdk icons
install -d $RPM_BUILD_ROOT%{_iconsdir}
tar xjvf %{SOURCE2} -C $RPM_BUILD_ROOT%{_iconsdir}

# find i18n files
%find_lang %{name}

%post
%_install_info %{name}.info
%if %mdkversion < 200900
%update_menus
%endif

%preun
%_remove_install_info %{name}.info

%if %mdkversion < 200900
%postun
%clean_menus
%endif

%if %mdkversion < 200900
%post -n %{lib_name} -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %{lib_name} -p /sbin/ldconfig
%endif
  
%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(-,root,root)
%doc ABOUT-NLS AUTHORS README HISTORY NEWS
%{_bindir}/*
%{_mandir}/*/*
%{_datadir}/applications/mandriva-*.desktop
%{_infodir}/*
%{_miconsdir}/*.png
%{_iconsdir}/*.png
%{_liconsdir}/*.png
%_libdir/*.la
%{_datadir}/xmorph

%files -n %{lib_name}
%defattr(-,root,root)
%_libdir/*.so.*

%files -n %{lib_name}-devel
%defattr(-,root,root)
%doc TODO
%{_libdir}/*.a
%{_libdir}/*.so
%{_prefix}/include/*

