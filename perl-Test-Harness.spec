#
# Conditional build:
# _without_tests - do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Test
%define		pnam	Harness
Summary:	Test::Harness - run perl standard test scripts with statistics
Summary(pl):	Test::Harness - uruchamianie perlowych skryptów testowych ze statystykami
Name:		perl-Test-Harness
Version:	2.26
Release:	3
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl >= 5.6
BuildRequires:	perl-Devel-CoreStack
BuildRequires:	rpm-perlprov >= 4.0.2-104
Conflicts:	perl-modules <= 5.6.1-36
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
%{__perl} Makefile.PL
%{__make}

%{!?_without_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes NOTES TODO
%{perl_privlib}/Test	
%{_mandir}/man3/*
