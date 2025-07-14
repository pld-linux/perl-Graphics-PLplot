#
# Conditional build:
%bcond_with	tests	# functional tests (require running X and plplot-driver-xwin)
#
%define		pdir	Graphics
%define		pnam	PLplot
Summary:	Graphics::PLplot - Perl interface to the PLplot plotting library
Summary(pl.UTF-8):	Graphics::PLplot - perlowy interfejs do biblioteki rysującej PLplot
Name:		perl-Graphics-PLplot
Version:	0.03
Release:	18
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	https://www.cpan.org/modules/by-module/Graphics/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	95a1cfeef5522f963357b1a757e9ba08
Patch0:		fix-plplot-call.patch
URL:		https://metacpan.org/dist/Graphics-PLplot
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	plplot-devel
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	rpmbuild(macros) >= 1.745
%if %{with tests}
BuildRequires:	plplot-driver-xwin
%endif
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module provides a Perl interface to the PLplot plotting library
available from <http://www.plplot.org/>. The interface is very similar
to the C interface.

%description -l pl.UTF-8
Ten moduł dostarcza perlowy interfejs do bibioteki rysującej PLplot
dostępnej ze strony <http://www.plplot.org/>. Interfejs jest bardzo
podobny do interfejsu C.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}
%patch -P0 -p1

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} \
	CC="%{__cc}" \
	OPTIMIZE="%{rpmcflags}"

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{perl_vendorarch}/Graphics/PLplot.pm
%dir %{perl_vendorarch}/auto/Graphics/PLplot
%attr(755,root,root) %{perl_vendorarch}/auto/Graphics/PLplot/*.so
%{_mandir}/man3/Graphics::PLplot.3pm*
