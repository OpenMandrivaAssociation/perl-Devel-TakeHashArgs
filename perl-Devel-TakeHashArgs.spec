%define upstream_name    Devel-TakeHashArgs
%define upstream_version 0.005

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 5

Summary:    make a hash from @_ and set defaults in subs while checking that all mandatory arguments are present
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Devel/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Exporter)
BuildRequires: perl(Module::Build::Compat)
BuildRequires: perl(Test::More)

BuildArch: noarch
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}

%description
The module is a short utility I made after being sick and tired of writing
redundant code to make a hash out of args when they are passed as key/value
pairs including setting their defaults and checking for mandatory
arguments.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README META.yml Changes
%{_mandir}/man3/*
%perl_vendorlib/*
