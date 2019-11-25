#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : adapt-parser
Version  : 0.3.4
Release  : 10
URL      : https://files.pythonhosted.org/packages/01/80/2a437b4b59ada21209a420e44d9597d13f3853df3f16040d3077e1a7976a/adapt-parser-0.3.4.tar.gz
Source0  : https://files.pythonhosted.org/packages/01/80/2a437b4b59ada21209a420e44d9597d13f3853df3f16040d3077e1a7976a/adapt-parser-0.3.4.tar.gz
Summary  : A text-to-intent parsing framework.
Group    : Development/Tools
License  : Apache-2.0
Requires: adapt-parser-python = %{version}-%{release}
Requires: adapt-parser-python3 = %{version}-%{release}
Requires: pyee
Requires: six
BuildRequires : buildreq-distutils3
BuildRequires : pyee
BuildRequires : six

%description
[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](LICENSE.md) [![CLA](https://img.shields.io/badge/CLA%3F-Required-blue.svg)](https://mycroft.ai/cla) [![Team](https://img.shields.io/badge/Team-Mycroft_Core-violetblue.svg)](https://github.com/MycroftAI/contributors/blob/master/team/Mycroft%20Core.md) ![Status](https://img.shields.io/badge/-Production_ready-green.svg)

%package python
Summary: python components for the adapt-parser package.
Group: Default
Requires: adapt-parser-python3 = %{version}-%{release}

%description python
python components for the adapt-parser package.


%package python3
Summary: python3 components for the adapt-parser package.
Group: Default
Requires: python3-core

%description python3
python3 components for the adapt-parser package.


%prep
%setup -q -n adapt-parser-0.3.4
cd %{_builddir}/adapt-parser-0.3.4

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1574698802
# -Werror is for werrorists
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
