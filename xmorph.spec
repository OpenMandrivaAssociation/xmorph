%define lib_major	0
%define lib_name_orig	%mklibname morph
%define lib_name	%{lib_name_orig}%{lib_major}

Summary:	An X Window System tool for creating morphed images
Name:		xmorph
Version:	20060817
Release:	2
Epoch:		2
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

%package -n %{lib_name}
Summary:	Internal library required for xmorph/gtkmorph
Provides:	%{lib_name_orig}
Group:		Graphics

%package -n %{lib_name}-devel
Summary:	Headers and static libraries required for xmorph/gtkmorph development
Requires:	%{lib_name} = %{epoch}:%{version}-%{release}
Provides:	%{lib_name_orig}-devel = %{EVRD}
Provides:	%{name}-devel = %{EVRD}
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
%configure2_5x --without-morph --with-gtk=2 --disable-static
%make

%install
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

%files -f %{name}.lang
%doc ABOUT-NLS AUTHORS README HISTORY NEWS
%{_bindir}/*
%{_mandir}/*/*
%{_datadir}/applications/mandriva-*.desktop
%{_infodir}/*
%{_miconsdir}/*.png
%{_iconsdir}/*.png
%{_liconsdir}/*.png
%{_datadir}/xmorph

%files -n %{lib_name}
%_libdir/*.so.*

%files -n %{lib_name}-devel
%doc TODO
%{_libdir}/*.so
%{_prefix}/include/*



%changelog
* Mon Sep 28 2009 Frederic Crozat <fcrozat@mandriva.com> 2:20060817-1mdv2010.0
+ Revision: 450531
- Release 20060817
- Patch0: fix build with latest gcc

  + Thierry Vignaud <tvignaud@mandriva.com>
    - rebuild
    - rebuild
    - rebuild

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Thu Dec 20 2007 Thierry Vignaud <tvignaud@mandriva.com> 2:20030527-4mdv2008.1
+ Revision: 135804
- auto-convert XDG menu entry
- BR x11-data-bitmaps
- BR xaw-devel
- try building w/o static libs
- kill re-definition of %%buildroot on Pixel's request
- kill prereq
- kill file require on ldconfig & install-info
- use %%mkrel
- import xmorph


* Thu Jun 02 2005 Nicolas Lécureuil <neoclust@mandriva.org> 20030527-4mdk
- Rebuild

* Mon Mar 01 2004 Pascal Terjan <pterjan@mandrake.org> 20030527-3mdk
- fix DEP (due to epoch)
 
* Mon Dec 08 2003 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 20030527-2mdk
- fix DIRM
- minor spec fixes
- remove redundant buildrequires

* Sun Dec 07 2003 Franck Villaume <fvill@freesurf.fr> 20030527-1mdk
- mv to the last version
- add BuildRequires : XFree86
- don't need patch gnome1 anymore

* Fri Jan 17 2003 Gwenole Beauchesne <gbeauchesne@mandrakesoft.com> 20010220-10mdk
- Update Patch0 (gnome1) so that we don't need automake
- Use %%mklibname, Provides: *-devel in addition to lib*-devel

* Tue Jun 04 2002 Olivier Thauvin <thauvin@aerov.jussieu.fr> 20010220-9mdk
- add BuildRequires gettext-devel (need by aclocal)
- png icons

* Fri Feb 15 2002 David BAUDENS <baudens@mandrakesoft.com> 20010220-8mdk
- BuildRequires gcc-cpp and not gcc-3.0-cpp
- Requires %%version-%%release and not only %%version
- Add missing files

* Sat Jan 19 2002 Stefan van der Eijk <stefan@eijk.nu> 20010220-7mdk
- BuildRequires

* Mon Jan  7 2002 Frederic Crozat <fcrozat@mandrakesoft.com> 20010220-6mdk
- Fix conflict with menu install (Thanks to Gregoire Favre)

* Fri Jan  4 2002 Frederic Crozat <fcrozat@mandrakesoft.com> 20010220-5mdk
- Patch0: fix compilation with GNOME1 platform

* Tue Aug  7 2001 Gwenole Beauchesne <gbeauchesne@mandrakesoft.com> 20010220-4mdk
- Sanitize spec file (s/Serial/Epoch/, BuildRequires)
- Renamed icons sources to something more consistent
- Integrated Source1 to spec file (menu entry)

* Wed Aug 01 2001 Stefan van der Eijk <stefan@eijk.nu> 20010220-3mdk
- fix BuildRequires
- s/Copyright/License/

* Wed Apr 25 2001 Geoffrey Lee <snailtalk@mandrakesoft.com> 20010220-2mdk
- Make it build on the Alpha platform.
- Bzip2 the source a.k.a. save some space on the SRPM CD. ;-)

* Wed Mar 14 2001 Jeff Garzik <jgarzik@mandrakesoft.com> 20010220-1mdk
- Update to latest SourceForge version, to fix glib problems.
  (Old one was over a year old and had tons of bugs.  <nudge> redhog)
- More docs.
- Use more standard version number scheme.  Update 'Serial' to handle this.
- Clean spec completely, xmorph includes autoconf support now.
- Create new sub-packages libmorph0, libmorph0-devel.
- Install info documentation.

* Mon Dec 11 2000 Egil Moeller <redhog@mandrakesoft.com> 2000.03.03-7mdk
- Defined GIMP_ENABLE_COMPAT_CRUFT as a cludge not to have to have to
  upport all of this sh*t code to the new gimplib (Without it, it does
  not compile anymore) (It will break again anyway, with gimplib 1.2,
  but I hope, I hope, that the xmorph author fixes this until then)...

* Mon Oct 02 2000 Daouda Lo <daouda@mandrakesoft.com> 2000.03.03-6mdk
- icons should be transparents!
- macrozifications

* Tue Aug 08 2000 Frederic Lepied <flepied@mandrakesoft.com> 2000.03.03-5mdk
- automatically added BuildRequires

* Wed May 03 2000 dam's <damien@mandrakesoft.com> 2000.03.03-4mdk
- Corrected icones.

* Tue Apr 18 2000 dam's <damien@mandrakesoft.com> 2000.03.03-3mdk
- Convert gif icon to xpm.

* Mon Apr 17 2000 dam's <damien@mandrakesoft.com> 2000.03.03-2mdk
- Added menu entry.

* Tue Mar 28 2000 dam's <damien@mandrakesoft.com> 2000.03.03-1mdk
- Update to 2000mar03

* Fri Nov 12 1999 dam's <damien@mandrakesoft.com>
- Mandrake release

* Thu May 06 1999 Bernhard Rosenkraenzer <bero@mandrakesoft.com>
- Mandrake adaptions

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com> 
- auto rebuild in the new build environment (release 7)

* Thu Dec 17 1998 Michael Maher <mike@redhat.com>
- built package for 6.0

* Thu Aug 13 1998 Jeff Johnson <jbj@redhat.com>
- build root

* Fri May 08 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Mon Jul 21 1997 Erik Troan <ewt@redhat.com>
- built against glibc
