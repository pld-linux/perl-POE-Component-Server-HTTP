#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	POE
%define	pnam	Component-Server-HTTP
Summary:	POE::Component::Server::HTTP - foundation of a POE HTTP Daemon
Summary(pl):	POE::Component::Server::HTTP - podstawa demona HTTP dla POE
Name:		perl-POE-Component-Server-HTTP
Version:	0.04
Release:	1
# same as [perl-]POE (same as perl)
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	d6713f8064552b8ab5c192b182461bc7
BuildRequires:	perl-devel >= 5.6
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-POE
BuildRequires:	perl-libwww
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
POE::Component::Server::HTTP (PoCo::HTTPD) is a framework for building
custom HTTP servers based on POE. It is loosely modeled on the ideas
of apache and the mod_perl/Apache module.

%description -l pl
POE::Component::Server::HTTP (PoCo::HTTPD) to szkielet do tworzenia
w³asnych serwerów HTTP opartych na POE. Jest swobodnie ukszta³towany
na ideach Apache'a i modu³u mod_perl.

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
%doc Changes README
%{perl_vendorlib}/%{pdir}/*/*/*
%{_mandir}/man3/*
