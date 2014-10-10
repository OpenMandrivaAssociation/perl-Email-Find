%define upstream_name 	 Email-Find
%define upstream_version 0.10

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3

Summary:	Email-Find perl module
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://www.cpan.org/%{upstream_name}
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Email/%{upstream_name}-%{upstream_version}.tar.bz2

BuildRequires:	perl-devel
BuildRequires:	perl(Email::Valid)
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
perl Makefile.PL INSTALLDIRS=vendor
make
make test

%install
%makeinstall_std

%files
%doc README Changes
%{perl_vendorlib}/Email/Find*
%{_mandir}/*/*

%changelog
* Wed Jul 29 2009 Jérôme Quelin <jquelin@mandriva.org> 0.100.0-1mdv2010.0
+ Revision: 403157
- rebuild using %%perl_convert_version

* Thu Jul 31 2008 Thierry Vignaud <tv@mandriva.org> 0.10-3mdv2009.0
+ Revision: 256753
- rebuild

* Thu Dec 20 2007 Olivier Blin <oblin@mandriva.com> 0.10-1mdv2008.1
+ Revision: 135833
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Thu Feb 01 2007 Stefan van der Eijk <stefan@mandriva.org> 0.10-1mdv2007.0
+ Revision: 115814
- 0.10

* Thu Nov 16 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.09-3mdv2007.1
+ Revision: 84635
- Import perl-Email-Find

* Sun Feb 05 2006 Stefan van der Eijk <stefan@eijk.nu> 0.09-3mdk
- Rebuild
- %%mkrel

* Mon Jan 17 2005 Stefan van der Eijk <stefan@mandrake.org> 0.09-2mdk
- yearly rebuild

