%define name gp
%define version 0.26
%define release 8

Summary: A set of basic utilities for manipulating DNA / RNA / protein sequences
Name: %name
Version: %version
Release: %release
License: GPL
Group: Sciences/Chemistry
URL: https://www.bioinformatics.org/genpak
Source: %name-%version.tar.bz2
BuildRoot: %_tmppath/%name-root

%description
This is a set of small programs for biologists working with sequence data. The
programs are written as a sort of `biological' extension to the standard Unix
tools (sed, awk, grep and the whole myriad of little, useful tools). They 
accept standard input and can spawn the data to standard output, so you can 
place them in a pipe as any other Unix command or use them in a cgi script.  
All programs are written in ANSI C, and are supposed to 1) aid manipulate 
large data sets in intensive batch processing, and 2) faciliate production of 
cgi-based local web servers providing some basic functions. 

%prep
%setup -q

%build
make CFLAGS="$RPM_OPT_FLAGS"

%install
mkdir -p $RPM_BUILD_ROOT/%_bindir
mkdir -p $RPM_BUILD_ROOT/%_datadir
mkdir -p $RPM_BUILD_ROOT/%_mandir/man1
mkdir -p $RPM_BUILD_ROOT/%_docdir
make TREE=$RPM_BUILD_ROOT/usr DATADIR=$RPM_BUILD_ROOT/%_datadir MANDIR=$RPM_BUILD_ROOT/%_mandir install

%clean
rm -fr $RPM_BUILD_ROOT

%files 
%defattr(-,root,root)
%doc README.TXT LICENSE.TXT CHANGES.TXT html
%_bindir/gp*
%_mandir/man1/*
%_datadir/genpak



%changelog
* Fri Dec 10 2010 Oden Eriksson <oeriksson@mandriva.com> 0.26-7mdv2011.0
+ Revision: 619221
- the mass rebuild of 2010.0 packages

* Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 0.26-6mdv2010.0
+ Revision: 429291
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 0.26-5mdv2009.0
+ Revision: 246528
- rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Mon Dec 17 2007 Thierry Vignaud <tv@mandriva.org> 0.26-3mdv2008.1
+ Revision: 126207
- kill re-definition of %%buildroot on Pixel's request
- import gp


* Thu Jan 05 2005 Lenny Cartier <lenny@mandriva.com> 0.26-3mdk
- rebuild

* Mon Feb 23 2004 Lenny Cartier <lenny@mandrakesoft.com> 0.26-2mdk
- rebuild

* Wed Jan 08 2003 Lenny Cartier <lenny@mandrakesoft.com> 0.26-1mdk
- from Austin Acton <aacton@yorku.ca> :
	- initial package for Mandrake 9
