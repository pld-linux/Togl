Summary:	Togl - Tk OpenGL Widget
Summary(pl):	Togl - Biblioteka widgetÛw dla Tk
Name:		Togl
Version:	1.6
Release:	2
License:	Open Source (see LICENSE file for details)
Group:		Libraries
Group(de):	Libraries
Group(es):	Bibliotecas
Group(fr):	Librairies
Group(pl):	Biblioteki
Group(pt_BR):	Bibliotecas
Group(ru):	‚…¬Ã…œ‘≈À…
Group(uk):	‚¶¬Ã¶œ‘≈À…
#Source0:	http://prdownloads.sf.net/Togl/%{name}-%{version}.tar.gz
#...but there is only 1.5
Source0:	%{name}-%{version}beta2.tar.gz
Source1:	%{name}-Makefile.PLD
Patch0:		%{name}-tkInit.patch
URL:		http://togl.sf.net/
Requires:	OpenGL
BuildRequires:	tk >= 8.0
BuildRequires:	tcl >= 8.0
BuildRequires:	XFree86-OpenGL-devel >= 4.0.1
Buildroot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define 	_noautoreqdep	libGL.so.1 libGLU.so.1
%define		_prefix		/usr/X11R6

%description
Togl is a Tk widget for OpenGL rendering.

%description -l pl
Togl jest widgetem Tk do renderowania OpenGL.

%package devel
Summary:	Togl devel
Summary(pl):	Togl - czÍ∂Ê dla programistÛw
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(es):	Desarrollo/Bibliotecas
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Group(pt_BR):	Desenvolvimento/Bibliotecas
Group(ru):	Ú¡⁄“¡¬œ‘À¡/‚…¬Ã…œ‘≈À…
Group(uk):	Úœ⁄“œ¬À¡/‚¶¬Ã¶œ‘≈À…

%description devel
Header files and examples for Togl.

%description devel -l pl
Pliki nag≥Ûwkowe i przyk≥ady do Togl.

%prep
%setup -q
%patch -p0

%build
install %{SOURCE1} .
mv -f %{name}-Makefile.PLD Makefile
%{__make} RPM_OPT_FLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_libdir},%{_includedir},%{_examplesdir}/%{name}-%{version}}
#%{__make} prefix=$RPM_BUILD_ROOT%{_prefix} install

install libtogl.so.1.3 $RPM_BUILD_ROOT%{_libdir}
install double gears index overlay texture $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
install togl.c $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
install togl.o $RPM_BUILD_ROOT%{_libdir}
install togl.h $RPM_BUILD_ROOT%{_includedir}

gzip -9nf LICENSE README

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc LICENSE.gz README.gz
%attr(755,root,root) %{_libdir}/libtogl.so.1.3
%attr(644,root,root) %{_libdir}/togl.o

%files devel
%defattr(644,root,root,755)
%attr(644,root,root) %{_includedir}/togl.h
%attr(755,root,root) %{_examplesdir}/%{name}-%{version}/*[^togl.c]
%attr(644,root,root) %{_examplesdir}/%{name}-%{version}/*.c
