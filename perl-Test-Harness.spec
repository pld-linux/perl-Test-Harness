%include	/usr/lib/rpm/macros.perl
%define	pdir	Test
%define	pnam	Harness
Summary:	Test-Harness perl module
Summary(pl):	Modu³ perla Test-Harness
Name:		perl-%{pdir}-%{pnam}
Version:	2.21
Release:	1
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildRequires:	perl-Devel-CoreStack
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
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf Changes NOTES TODO

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%{perl_privlib}/Test/Harness.pm
%{perl_privlib}/Test/Harness
%{_mandir}/man3/*
