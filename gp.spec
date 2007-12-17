%define name gp
%define version 0.26
%define release %mkrel 3

Summary: A set of basic utilities for manipulating DNA / RNA / protein sequences
Name: %name
Version: %version
Release: %release
License: GPL
Group: Sciences/Chemistry
URL: http://www.bioinformatics.org/genpak
Source: %name-%version.tar.bz2

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

