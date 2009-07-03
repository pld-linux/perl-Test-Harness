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
%{perl_vendorlib}/Test/*.pm
%{perl_vendorlib}/Test/*.pod
%{_mandir}/man1/prove.1p*
%{_mandir}/man3/App::Prove.3pm*
%{_mandir}/man3/App::Prove::State.3pm*
%{_mandir}/man3/App::Prove::State::Result.3pm*
%{_mandir}/man3/App::Prove::State::Result::Test.3pm*
%{_mandir}/man3/TAP::Base.3pm*
%{_mandir}/man3/TAP::Formatter::Base.3pm*
%{_mandir}/man3/TAP::Formatter::Color.3pm*
%{_mandir}/man3/TAP::Formatter::Console.3pm*
%{_mandir}/man3/TAP::Formatter::Console::ParallelSession.3pm*
%{_mandir}/man3/TAP::Formatter::Console::Session.3pm*
%{_mandir}/man3/TAP::Formatter::File.3pm*
%{_mandir}/man3/TAP::Formatter::File::Session.3pm*
%{_mandir}/man3/TAP::Formatter::Session.3pm*
%{_mandir}/man3/TAP::Harness.3pm*
%{_mandir}/man3/TAP::Object.3pm*
%{_mandir}/man3/TAP::Parser.3pm*
%{_mandir}/man3/TAP::Parser::Aggregator.3pm*
%{_mandir}/man3/TAP::Parser::Grammar.3pm*
%{_mandir}/man3/TAP::Parser::Iterator.3pm*
%{_mandir}/man3/TAP::Parser::Iterator::Array.3pm*
%{_mandir}/man3/TAP::Parser::Iterator::Process.3pm*
%{_mandir}/man3/TAP::Parser::Iterator::Stream.3pm*
%{_mandir}/man3/TAP::Parser::IteratorFactory.3pm*
%{_mandir}/man3/TAP::Parser::Multiplexer.3pm*
%{_mandir}/man3/TAP::Parser::Result.3pm*
%{_mandir}/man3/TAP::Parser::Result::Bailout.3pm*
%{_mandir}/man3/TAP::Parser::Result::Comment.3pm*
%{_mandir}/man3/TAP::Parser::Result::Plan.3pm*
%{_mandir}/man3/TAP::Parser::Result::Pragma.3pm*
%{_mandir}/man3/TAP::Parser::Result::Test.3pm*
%{_mandir}/man3/TAP::Parser::Result::Unknown.3pm*
%{_mandir}/man3/TAP::Parser::Result::Version.3pm*
%{_mandir}/man3/TAP::Parser::Result::YAML.3pm*
%{_mandir}/man3/TAP::Parser::ResultFactory.3pm*
%{_mandir}/man3/TAP::Parser::Scheduler.3pm*
%{_mandir}/man3/TAP::Parser::Scheduler::Job.3pm*
%{_mandir}/man3/TAP::Parser::Scheduler::Spinner.3pm*
%{_mandir}/man3/TAP::Parser::Source.3pm*
%{_mandir}/man3/TAP::Parser::Source::Perl.3pm*
%{_mandir}/man3/TAP::Parser::Utils.3pm*
%{_mandir}/man3/TAP::Parser::YAMLish::Reader.3pm*
%{_mandir}/man3/TAP::Parser::YAMLish::Writer.3pm*
%{_mandir}/man3/Test::HACKING.3pm*
%{_mandir}/man3/Test::Harness.3pm*
