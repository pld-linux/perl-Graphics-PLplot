#
# Conditional build:
%bcond_with	tests		# "make test" requires running X and plplot-driver-xwin
#
%define		pdir	Graphics
%define		pnam	PLplot
%include	/usr/lib/rpm/macros.perl
Summary:	Graphics::PLplot - Perl interface to the PLplot plotting library
Name:		perl-Graphics-PLplot
Version:	0.03
Release:	2
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Graphics/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	95a1cfeef5522f963357b1a757e9ba08
Patch0:		fix-plplot-call.patch
URL:		http://search.cpan.org/dist/Graphics-PLplot/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	plplot-devel
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	plplot-driver-xwin
%endif
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module provides a perl interface to the PLplot plotting library
available from http://www.plplot.org. The interface is very similar
to the C interface except that:

 - Arrays are passed in by reference
 - If the number of elements in an array is required by the C function
   the perl interface calculates this automatically [eg plline]
 - Return values are returned and not supplied as arguments

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}
%patch0 -p1

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
%{perl_vendorarch}/Graphics/*.pm
%dir %{perl_vendorarch}/auto/Graphics/PLplot
%{perl_vendorarch}/auto/Graphics/PLplot/*.bs
%attr(755,root,root) %{perl_vendorarch}/auto/Graphics/PLplot/*.so
%{_mandir}/man3/*
