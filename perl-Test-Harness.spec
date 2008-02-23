#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Test
%define		pnam	Harness
Summary:	Test::Harness - run Perl standard test scripts with statistics
Summary(pl.UTF-8):	Test::Harness - uruchamianie perlowych skryptów testowych ze statystykami
Name:		perl-Test-Harness
# NOTE: version 2.64 in perl-modules-5.10.0
Version:	3.09
Release:	2
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Test/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	40196584ddb987cadb7144a7d171bf4f
URL:		http://search.cpan.org/dist/Test-Harness/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Test::Harness - module that runs perl standard test scripts with
statistics.

%description -l pl.UTF-8
Test::Harness - moduł uruchamiający standardowe perlowe skrypty
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

mv $RPM_BUILD_ROOT%{_bindir}/prove{,.pl}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes*
%attr(755,root,root) %{_bindir}/prove.pl
%{perl_vendorlib}/App/*
%{perl_vendorlib}/Test/*
%{perl_vendorlib}/TAP/*
%{_mandir}/man1/*
%{_mandir}/man3/*
