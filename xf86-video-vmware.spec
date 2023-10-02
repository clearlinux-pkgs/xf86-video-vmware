#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xE23B7E70B467F0BF (office@who-t.net)
#
Name     : xf86-video-vmware
Version  : 13.4.0
Release  : 239
URL      : https://www.x.org/releases/individual/driver/xf86-video-vmware-13.4.0.tar.xz
Source0  : https://www.x.org/releases/individual/driver/xf86-video-vmware-13.4.0.tar.xz
Source1  : https://www.x.org/releases/individual/driver/xf86-video-vmware-13.4.0.tar.xz.sig
Summary  : No detailed summary available
Group    : Development/Tools
License  : ICU MIT
Requires: xf86-video-vmware-lib = %{version}-%{release}
Requires: xf86-video-vmware-license = %{version}-%{release}
Requires: xf86-video-vmware-man = %{version}-%{release}
BuildRequires : pkgconfig(fontsproto)
BuildRequires : pkgconfig(libdrm)
BuildRequires : pkgconfig(libudev)
BuildRequires : pkgconfig(pciaccess)
BuildRequires : pkgconfig(x11)
BuildRequires : pkgconfig(xext)
BuildRequires : pkgconfig(xorg-macros)
BuildRequires : pkgconfig(xorg-server)
BuildRequires : pkgconfig(xproto)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
All Rights Reserved
The code here may be used/distributed under the terms of the standard
XFree86 license.

%package lib
Summary: lib components for the xf86-video-vmware package.
Group: Libraries
Requires: xf86-video-vmware-license = %{version}-%{release}

%description lib
lib components for the xf86-video-vmware package.


%package license
Summary: license components for the xf86-video-vmware package.
Group: Default

%description license
license components for the xf86-video-vmware package.


%package man
Summary: man components for the xf86-video-vmware package.
Group: Default

%description man
man components for the xf86-video-vmware package.


%prep
%setup -q -n xf86-video-vmware-13.4.0
cd %{_builddir}/xf86-video-vmware-13.4.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1674573784
unset LD_AS_NEEDED
export GCC_IGNORE_WERROR=1
export CFLAGS="-O3 -g -fopt-info-vec "
unset LDFLAGS
export CFLAGS="$CFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz "
export FCFLAGS="$FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz "
export FFLAGS="$FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz "
export CXXFLAGS="$CXXFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz "
%configure --disable-static
make  %{?_smp_mflags}

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1674573784
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/xf86-video-vmware
cp %{_builddir}/xf86-video-vmware-%{version}/COPYING %{buildroot}/usr/share/package-licenses/xf86-video-vmware/03ea29adcade375c21ecb3c2f31f6496520c694f || :
%make_install

%files
%defattr(-,root,root,-)

%files lib
%defattr(-,root,root,-)
/usr/lib64/xorg/modules/drivers/vmware_drv.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/xf86-video-vmware/03ea29adcade375c21ecb3c2f31f6496520c694f

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man4/vmware.4
