#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xC1F5D3CDF5176580 (thellstrom@vmware.com)
#
Name     : xf86-video-vmware
Version  : 13.3.0
Release  : 56
URL      : https://www.x.org/releases/individual/driver/xf86-video-vmware-13.3.0.tar.bz2
Source0  : https://www.x.org/releases/individual/driver/xf86-video-vmware-13.3.0.tar.bz2
Source99 : https://www.x.org/releases/individual/driver/xf86-video-vmware-13.3.0.tar.bz2.sig
Summary  : X.org vmware video driver
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
%setup -q -n xf86-video-vmware-13.3.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1553178587
unset LD_AS_NEEDED
export CFLAGS="-O3 -g -fopt-info-vec "
unset LDFLAGS
export LDFLAGS="${LDFLAGS} -fno-lto"
%configure --disable-static
make  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1553178587
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/xf86-video-vmware
cp COPYING %{buildroot}/usr/share/package-licenses/xf86-video-vmware/COPYING
%make_install

%files
%defattr(-,root,root,-)

%files lib
%defattr(-,root,root,-)
/usr/lib64/xorg/modules/drivers/vmware_drv.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/xf86-video-vmware/COPYING

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man4/vmware.4
