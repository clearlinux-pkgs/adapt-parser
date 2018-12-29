#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : adapt-parser
Version  : 0.3.2
Release  : 4
URL      : https://files.pythonhosted.org/packages/1f/a3/93973bbdd22bf4eb7eb5e8805c16ebb50b86e61b6fb774e97e8109f2aba2/adapt-parser-0.3.2.tar.gz
Source0  : https://files.pythonhosted.org/packages/1f/a3/93973bbdd22bf4eb7eb5e8805c16ebb50b86e61b6fb774e97e8109f2aba2/adapt-parser-0.3.2.tar.gz
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
[![Stories in Ready](https://badge.waffle.io/MycroftAI/adapt.png?label=ready&title=Ready)](https://waffle.io/MycroftAI/adapt)
Getting Started
===============
To take a dependency on Adapt, it's recommended to use virtualenv and pip to install source from github.

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
%setup -q -n adapt-parser-0.3.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1543514734
python3 setup.py build

%install
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
