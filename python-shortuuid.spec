#
# This is template for pure python modules (noarch)
# use template-specs/python-ext.spec for binary python packages
#
#
# Conditional build:
# %%bcond_with	doc	# don't build doc
%bcond_without	tests	# do not perform "make test"
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

# NOTE: 'module' should match the python import path, not the egg name
%define 	module	shortuuid
Summary:	Generator library for concise, unambiguous and URL-safe UUIDs
Summary(pl.UTF-8):	Biblioteka generacji jednoznacznych UUIDów dla URLi
# Name must match the python module/package name (as on pypi or in 'import' statement)
Name:		python-%{module}
Version:	0.4.3
Release:	1
License:	BSD
Group:		Libraries/Python
Source0:	https://pypi.python.org/packages/e9/41/d867be1470af87dd8af1b3462e5eae44f78ffd33cec54630d40ca6b2d0bd/shortuuid-%{version}.tar.gz
# Source0-md5:	4f70db8174c0b7b8cad36de48b529947
URL:		https://github.com/stochastic-technologies/shortuuid/
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
%if %{with python2}
BuildRequires:	python-modules
BuildRequires:	python-pep8
%endif
%if %{with python3}
BuildRequires:	python3-modules
BuildRequires:	python3-pep8
%endif
Requires:	python-modules
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Library that generates short, pretty, unambiguous unique IDs by using
an extensive, case-sensitive alphabet and omitting similar-looking
letters and numbers.

%description -l pl.UTF-8
Biblioteka która generuje krótkie, ładne, jednoznaczne i unikalne IDy
używając obszernego, uwzlgedniającego wielkość liter alfabetu i
omijając podbone znaki i liczby.

%package -n python3-%{module}
Summary:	Generator library for concise, unambiguous and URL-safe UUIDs
Summary(pl.UTF-8):	Biblioteka generacji jednoznacznych UUIDów dla URLi
Group:		Libraries/Python
Requires:	python3-modules

%description -n python3-%{module}
Library that generates short, pretty, unambiguous unique IDs by using
an extensive, case-sensitive alphabet and omitting similar-looking
letters and numbers.

%description -n python3-%{module} -l pl.UTF-8
Biblioteka która generuje krótkie, ładne, jednoznaczne i unikalne IDy
używając obszernego, uwzlgedniającego wielkość liter alfabetu i
omijając podbone znaki i liczby.

%package apidocs
Summary:	%{module} API documentation
Summary(pl.UTF-8):	Dokumentacja API %{module}
Group:		Documentation

%description apidocs
API documentation for %{module}.

%description apidocs -l pl.UTF-8
Dokumentacja API %{module}.

%prep
%setup -q -n %{module}-%{version}

%build
%if %{with python2}
%py_build %{?with_tests:test}
%endif

%if %{with python3}
%py3_build %{?with_tests:test}
%endif

%if %{with doc}
cd docs
%{__make} -j1 html
rm -rf _build/html/_sources
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc README.rst
%{py_sitescriptdir}/%{module}
%if "%{py_ver}" > "2.4"
%{py_sitescriptdir}/%{module}-%{version}-py*.egg-info
%endif
%endif

%if %{with python3}
%files -n python3-%{module}
%defattr(644,root,root,755)
%doc README.rst
%{py3_sitescriptdir}/%{module}
%{py3_sitescriptdir}/%{module}-%{version}-py*.egg-info
%endif

%if %{with doc}
%files apidocs
%defattr(644,root,root,755)
%doc docs/_build/html/*
%endif
