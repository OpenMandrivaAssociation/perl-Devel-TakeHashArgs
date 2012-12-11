%define upstream_name    Devel-TakeHashArgs
%define upstream_version 0.005

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	6

Summary:	Make a hash out of args when they are passed as key/value pairs
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Devel/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Exporter)
BuildRequires:	perl(Module::Build::Compat)
BuildRequires:	perl(Test::More)

BuildArch:	noarch

%description
The module is a short utility I made after being sick and tired of writing
redundant code to make a hash out of args when they are passed as key/value
pairs including setting their defaults and checking for mandatory
arguments.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc README META.yml Changes
%{_mandir}/man3/*
%{perl_vendorlib}/*


%changelog
* Mon Apr 18 2011 Funda Wang <fwang@mandriva.org> 0.5.0-5mdv2011.0
+ Revision: 654946
- rebuild for updated spec-helper

* Sat Feb 13 2010 Jérôme Quelin <jquelin@mandriva.org> 0.5.0-4mdv2011.0
+ Revision: 505272
- rebuild using %%perl_convert_version

* Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 0.005-3mdv2010.0
+ Revision: 430410
- rebuild

* Fri Aug 08 2008 Thierry Vignaud <tv@mandriva.org> 0.005-2mdv2009.0
+ Revision: 268429
- rebuild early 2009.0 package (before pixel changes)

* Wed Apr 16 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.005-1mdv2009.0
+ Revision: 194849
- update to new version 0.005
- update to new version 0.005

* Sat Apr 12 2008 Olivier Thauvin <nanardon@mandriva.org> 0.004-1mdv2009.0
+ Revision: 192623
- import perl-Devel-TakeHashArgs


