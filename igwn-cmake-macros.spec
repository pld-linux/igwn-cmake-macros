Summary:	Collection of CMake functions used as a replacement for autoconf macros
Summary(pl.UTF-8):	Zbiór funkcji CMake służących jako zamienniki makr autoconfa
Name:		igwn-cmake-macros
Version:	1.5.0
Release:	1
License:	GPL v2+
Group:		Development/Libraries
Source0:	http://software.igwn.org/lscsoft/source/%{name}-%{version}.tar.gz
# Source0-md5:	07f8d0c4db2769d9933c2bca1b1759dd
URL:		http://software.igwn.org/
BuildRequires:	cmake >= 3.2
BuildRequires:	doxygen
BuildRequires:	rpm-build >= 4.6
BuildRequires:	rpmbuild(macros) >= 1.605
Requires:	cmake >= 3.2
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a collection of macros and scripts that were developed to aid
in the process of converting Autotools based projects into CMake.

%description -l pl.UTF-8
Zbiór makr i skryptów stworzonych w celu ułatwienia konwersji
projektów opartych na Autotools do CMake'a.

%package doc
Summary:	Documentation for IGWN CMake macros
Summary(pl.UTF-8):	Dokumentacja makr CMake'a IGWN
Group:		Documentation

%description doc
Documentation for IGWN CMake macros.

%description doc -l pl.UTF-8
Dokumentacja makr CMake'a IGWN.

%prep
%setup -q

# to make package noarch
%{__sed} -i -e '/^libdir=/d' config/igwncmake.pc.in

%build
install -d build
cd build
%cmake .. \
	-DCMAKE_INSTALL_DATADIR=share

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

# packaged as %doc
%{__rm} -r $RPM_BUILD_ROOT%{_docdir}/Developer

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog NEWS.md README.md
%{_datadir}/igwn-cmake
%{_npkgconfigdir}/igwncmake.pc

%files doc
%defattr(644,root,root,755)
%doc build/doc/Developer/html/{search,*.css,*.html,*.js,*.png}
