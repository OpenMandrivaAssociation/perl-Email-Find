%define upstream_name 	 Email-Find
%define upstream_version 0.10

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:	Email-Find perl module
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://www.cpan.org/%{upstream_name}
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Email/%{upstream_name}-%{upstream_version}.tar.bz2

BuildRequires:	perl-Email-Valid
BuildRoot: 	%{_tmppath}/%{name}-%{version}-%{release}
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
%setup -q -n %{upstream_name}-%{upstream_version}

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
