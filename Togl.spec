Summary:	Togl - Tk OpenGL Widget
Summary(pl):	Togl - Biblioteka widgetów dla Tk
Name:		Togl
Version:	1.6
Release:	2
Copyright:	Other
Group:		Libraries
Group(de):	Libraries
Group(es):	Bibliotecas
Group(fr):	Librairies
Group(pl):	Biblioteki
Source0:	%{name}-%{version}beta2.tar.gz
Source1:	%{name}-Makefile.PLD
Patch0:		%{name}-tkInit.patch
URL:		http://www.ssec.wisc.edu/~brianp/Togl.html
Requires:	OpenGL
BuildRequires:	tk >= 8.0
BuildRequires:	tcl >= 8.0
BuildRequires:	XFree86-OpenGL-devel >= 4.0.1
Buildroot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define 	_noautoreqdep	libGL.so.1 libGLU.so.1
%define		_prefix		/usr/X11R6

%description

%description -l pl

%package devel
Summary:	Togl devel
Summary(pl):	Togl - czê¶æ dla programistów
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki

%description devel

%description devel -l pl

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

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc LICENSE
%attr(755,root,root) %{_libdir}/libtogl.so.1.3
%attr(644,root,root) %{_libdir}/togl.o

%files devel
%defattr(644,root,root,755)
%attr(644,root,root) %{_includedir}/togl.h
%attr(755,root,root) %{_examplesdir}/%{name}-%{version}/*[^togl.c]
%attr(644,root,root) %{_examplesdir}/%{name}-%{version}/*.c
