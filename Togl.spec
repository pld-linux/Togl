Summary:	Togl - Tk OpenGL Widget
Summary(pl):	Togl - Biblioteka widgetów dla Tk
Name:		Togl
Version:	1.6
Release:	2
License:	Open Source (see LICENSE file for details)
Group:		Libraries
#Source0:	http://dl.sourceforge.net/togl/%{name}-%{version}.tar.gz
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

%description
Togl is a Tk widget for OpenGL rendering.

%description -l pl
Togl jest widgetem Tk do renderowania OpenGL.

%package devel
Summary:	Togl devel
Summary(pl):	Togl - czê¶æ dla programistów
Group:		Development/Libraries

%description devel
Header files and examples for Togl.

%description devel -l pl
Pliki nag³ówkowe i przyk³ady do Togl.

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
#%%{__make} prefix=$RPM_BUILD_ROOT%{_prefix} install

install libtogl.so.1.3 $RPM_BUILD_ROOT%{_libdir}
install double gears index overlay texture $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
install togl.c $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
install togl.o $RPM_BUILD_ROOT%{_libdir}
install togl.h $RPM_BUILD_ROOT%{_includedir}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc LICENSE README
%attr(755,root,root) %{_libdir}/libtogl.so.1.3
%attr(644,root,root) %{_libdir}/togl.o

%files devel
%defattr(644,root,root,755)
%attr(644,root,root) %{_includedir}/togl.h
%attr(755,root,root) %{_examplesdir}/%{name}-%{version}/*[^togl.c]
%attr(644,root,root) %{_examplesdir}/%{name}-%{version}/*.c
