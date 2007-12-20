%define module 	Email-Find
%define version 0.10
%define release %mkrel 1

Summary:	Email-Find perl module
Name: 		perl-%{module}
Version: 	%{version}
Release: 	%{release}
License:	GPL or Artistic
Group:		Development/Perl
Url:		http://www.cpan.org
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Email/%{module}-%{version}.tar.bz2
BuildRequires:	perl-devel >= 0:5.600
BuildRequires:	perl-Email-Valid
BuildRoot: 	%{_tmppath}/%{name}-buildroot
BuildArch:	noarch

%description
Email::Find is a module for finding a *subset* of RFC 822 email
addresses in arbitrary text (see the section on "CAVEATS"). The
addresses it finds are not guaranteed to exist or even actually be email
addresses at all (see the section on "CAVEATS"), but they will be valid
RFC 822 syntax.

Email::Find will perform some heuristics to avoid some of the more
obvious red herrings and false addresses, but there's only so much which
can be done without a human.

%prep
%setup -q -n %{module}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%{__make}
make test

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README Changes
%{perl_vendorlib}/Email/Find*
%{_mandir}/*/*


