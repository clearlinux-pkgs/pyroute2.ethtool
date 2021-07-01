#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pyroute2.ethtool
Version  : 0.6.4
Release  : 4
URL      : https://files.pythonhosted.org/packages/19/f2/62c8c2bd3647f04be348b8f74d15eafd616148d0ab662303a328893a6c96/pyroute2.ethtool-0.6.4.tar.gz
Source0  : https://files.pythonhosted.org/packages/19/f2/62c8c2bd3647f04be348b8f74d15eafd616148d0ab662303a328893a6c96/pyroute2.ethtool-0.6.4.tar.gz
Summary  : Python Netlink library: ethtool
Group    : Development/Tools
License  : Apache-2.0 GPL-2.0 GPL-2.0+
Requires: pyroute2.ethtool-license = %{version}-%{release}
Requires: pyroute2.ethtool-python = %{version}-%{release}
Requires: pyroute2.ethtool-python3 = %{version}-%{release}
Requires: pyroute2.core
BuildRequires : buildreq-distutils3
BuildRequires : pyroute2.core

%description
================
        
        PyRoute2 is a pure Python **netlink** library.
        
        This module provides Ethtool.
        
        links
        =====

%package license
Summary: license components for the pyroute2.ethtool package.
Group: Default

%description license
license components for the pyroute2.ethtool package.


%package python
Summary: python components for the pyroute2.ethtool package.
Group: Default
Requires: pyroute2.ethtool-python3 = %{version}-%{release}

%description python
python components for the pyroute2.ethtool package.


%package python3
Summary: python3 components for the pyroute2.ethtool package.
Group: Default
Requires: python3-core
Provides: pypi(pyroute2.ethtool)
Requires: pypi(pyroute2.core)

%description python3
python3 components for the pyroute2.ethtool package.


%prep
%setup -q -n pyroute2.ethtool-0.6.4
cd %{_builddir}/pyroute2.ethtool-0.6.4

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1623080291
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pyroute2.ethtool
cp %{_builddir}/pyroute2.ethtool-0.6.4/LICENSE.Apache.v2 %{buildroot}/usr/share/package-licenses/pyroute2.ethtool/cd9bad64b174708395f795bb92f7b4be7d996e8f
cp %{_builddir}/pyroute2.ethtool-0.6.4/LICENSE.GPL.v2 %{buildroot}/usr/share/package-licenses/pyroute2.ethtool/4cc77b90af91e615a64ae04893fdffa7939db84c
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pyroute2.ethtool/4cc77b90af91e615a64ae04893fdffa7939db84c
/usr/share/package-licenses/pyroute2.ethtool/cd9bad64b174708395f795bb92f7b4be7d996e8f

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
