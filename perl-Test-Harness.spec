#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%define		pdir	Test
%define		pnam	Harness
Summary:	Test::Harness - run Perl standard test scripts with statistics
Summary(pl.UTF-8):	Test::Harness - uruchamianie perlowych skryptów testowych ze statystykami
Name:		perl-Test-Harness
# NOTE: version 3.42 in perl-modules-5.28.0
Version:	3.42
Release:	0.1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Test/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	c794906473f88d6b74194e2d56f16bd6
URL:		http://search.cpan.org/dist/Test-Harness/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
Provides:	perl-TAP-Parser = %{version}
Obsoletes:	perl-TAP-Parser < 1.0
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

%{__rm} $RPM_BUILD_ROOT%{perl_vendorlib}/TAP/Harness/Beyond.pod
# for TAP::Harness developers
%{__rm} $RPM_BUILD_ROOT%{perl_vendorlib}/Test/HACKING.pod \
	$RPM_BUILD_ROOT%{_mandir}/man3/Test::HACKING.3pm

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes*
%attr(755,root,root) %{_bindir}/prove.pl
%{perl_vendorlib}/App/Prove.pm
%{perl_vendorlib}/App/Prove/*.pm
%{perl_vendorlib}/App/Prove/State/*.pm
%{perl_vendorlib}/App/Prove/State/Result/*.pm
%{perl_vendorlib}/TAP/Base.pm
%{perl_vendorlib}/TAP/Formatter/*.pm
%{perl_vendorlib}/TAP/Formatter/Console/*.pm
%{perl_vendorlib}/TAP/Formatter/File/*.pm
%{perl_vendorlib}/TAP/Harness.pm
%dir %{perl_vendorlib}/TAP/Harness
%{perl_vendorlib}/TAP/Harness/Env.pm
%{perl_vendorlib}/TAP/Object.pm
%{perl_vendorlib}/TAP/Parser.pm
%{perl_vendorlib}/TAP/Parser/*.pm
%{perl_vendorlib}/TAP/Parser/Iterator/*.pm
%{perl_vendorlib}/TAP/Parser/Result/*.pm
%{perl_vendorlib}/TAP/Parser/Scheduler/*.pm
%dir %{perl_vendorlib}/TAP/Parser/SourceHandler
%{perl_vendorlib}/TAP/Parser/SourceHandler/*.pm
%{perl_vendorlib}/TAP/Parser/YAMLish/*.pm
%{perl_vendorlib}/Test/Harness.pm
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
%{_mandir}/man3/TAP::Harness::Beyond.3pm*
%{_mandir}/man3/TAP::Harness::Env.3pm*
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
%{_mandir}/man3/TAP::Parser::SourceHandler.3pm*
%{_mandir}/man3/TAP::Parser::SourceHandler::Executable.3pm*
%{_mandir}/man3/TAP::Parser::SourceHandler::File.3pm*
%{_mandir}/man3/TAP::Parser::SourceHandler::Handle.3pm*
%{_mandir}/man3/TAP::Parser::SourceHandler::Perl.3pm*
%{_mandir}/man3/TAP::Parser::SourceHandler::RawTAP.3pm*
%{_mandir}/man3/TAP::Parser::YAMLish::Reader.3pm*
%{_mandir}/man3/TAP::Parser::YAMLish::Writer.3pm*
%{_mandir}/man3/Test::Harness.3pm*
