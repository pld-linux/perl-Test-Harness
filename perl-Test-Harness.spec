%include	/usr/lib/rpm/macros.perl
%define		pdir	Test
%define		pnam	Harness
Summary:	Test::Harness Perl module
Summary(cs):	Modul Test::Harness pro Perl
Summary(da):	Perlmodul Test::Harness
Summary(de):	Test::Harness Perl Modul
Summary(es):	Módulo de Perl Test::Harness
Summary(fr):	Module Perl Test::Harness
Summary(it):	Modulo di Perl Test::Harness
Summary(ja):	Test::Harness Perl ¥â¥¸¥å¡¼¥ë
Summary(ko):	Test::Harness ÆÞ ¸ðÁÙ
Summary(no):	Perlmodul Test::Harness
Summary(pl):	Modu³ Perla Test::Harness
Summary(pt):	Módulo de Perl Test::Harness
Summary(pt_BR):	Módulo Perl Test::Harness
Summary(ru):	íÏÄÕÌØ ÄÌÑ Perl Test::Harness
Summary(sv):	Test::Harness Perlmodul
Summary(uk):	íÏÄÕÌØ ÄÌÑ Perl Test::Harness
Summary(zh_CN):	Test::Harness Perl Ä£¿é
Name:		perl-Test-Harness
Version:	2.26
Release:	2
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

%description -l cs
Modul Test::Harness pro Perl.

%description -l da
Perlmodul Test::Harness.

%description -l de
Test::Harness Perl Modul.

%description -l es
Módulo de Perl Test::Harness.

%description -l fr
Module Perl Test::Harness.

%description -l it
Modulo di Perl Test::Harness.

%description -l ja
Test::Harness Perl ¥â¥¸¥å¡¼¥ë

%description -l ko
Test::Harness ÆÞ ¸ðÁÙ.

%description -l no
Perlmodul Test::Harness.

%description -l pl
Test::Harness - modu³ uruchamiaj±cy standardowe perlowe skrypty
testowe ze statystykami.

%description -l pt
Módulo de Perl Test::Harness.

%description -l pt_BR
Módulo Perl Test::Harness.

%description -l ru
íÏÄÕÌØ ÄÌÑ Perl Test::Harness.

%description -l sv
Test::Harness Perlmodul.

%description -l uk
íÏÄÕÌØ ÄÌÑ Perl Test::Harness.

%description -l zh_CN
Test::Harness Perl Ä£¿é

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL
%{__make}

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
