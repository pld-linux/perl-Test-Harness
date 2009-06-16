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
Version:	3.17
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Test/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	d4b9f3bf6bd7fdc9f03c66a352a2c0da
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
%{__perl} Build.PL \
	destdir=$RPM_BUILD_ROOT \
	installdirs=vendor
./Build

%{?with_tests:./Build test}

%install
rm -rf $RPM_BUILD_ROOT

./Build install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -a examples $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
mv $RPM_BUILD_ROOT%{_bindir}/prove{,.pl}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Test/*.pm
%{_mandir}/man3/*
%{_examplesdir}/%{name}-%{version}
%attr(755,root,root) %{_bindir}/prove.pl
%{_mandir}/man1/prove.1p*
%{perl_vendorlib}/App/*.pm
%{perl_vendorlib}/App/Prove/*.pm
%{perl_vendorlib}/App/Prove/State/*.pm
%{perl_vendorlib}/App/Prove/State/Result/*.pm
%{perl_vendorlib}/TAP/*.pm
%{perl_vendorlib}/TAP/Formatter/*.pm
%{perl_vendorlib}/TAP/Formatter/Console/*.pm
%{perl_vendorlib}/TAP/Formatter/File/*.pm
%{perl_vendorlib}/TAP/Parser/*.pm
%{perl_vendorlib}/TAP/Parser/Iterator/*.pm
%{perl_vendorlib}/TAP/Parser/Result/*.pm
%{perl_vendorlib}/TAP/Parser/Scheduler/*.pm
%{perl_vendorlib}/TAP/Parser/Source/*.pm
%{perl_vendorlib}/TAP/Parser/YAMLish/*.pm
