#
# Conditional build:
%bcond_with	tests	# perform "make test"

%include	/usr/lib/rpm/macros.perl
%define		pdir	Test
%define		pnam	Harness
Summary:	Test::Harness - run Perl standard test scripts with statistics
Summary(pl):	Test::Harness - uruchamianie perlowych skryptów testowych ze statystykami
Name:		perl-Test-Harness
Version:	2.40
Release:	1
License:	GPL or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	a7f10313231909a20e37f224114da762
BuildRequires:	perl-devel >= 5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Devel-CoreStack
BuildRequires:	perl-Test-Pod >= 0.95
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Test::Harness - module that runs perl standard test scripts with
statistics.

%description -l pl
Test::Harness - modu³ uruchamiaj±cy standardowe perlowe skrypty
testowe ze statystykami.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes NOTES
%attr(755,root,root) %{_bindir}/prove
%{perl_vendorlib}/%{pdir}/*
%{_mandir}/man1/*
%{_mandir}/man3/*
