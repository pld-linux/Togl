Summary:	Togl - Tk OpenGL Widget
Summary(pl):	Togl - Biblioteka widgetów dla Tk
Name:		Togl
Version:	1.6
Release:	1
Copyright:	Other
Group:		Libraries
Group(pl):	Biblioteki
Source0:	%{name}-%{version}beta2.tar.gz
Source1:	%{name}-Makefile.PLD
Patch0:		%{name}-tkInit.patch
URL:		http://www.ssec.wisc.edu/~brianp/Togl.html
BuildRequires:	tk >= 8.0
#Requires:	
Buildroot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define	_prefix	/usr/X11R6

%description

%description -l pl

%package devel
Summary:	Togl devel
Summary(pl):	Togl devel
Group:		Development/Libraries
Group(pl):	Programowanie/Biblioteki
%description devel
%description devel -l pl

%prep
%setup -q

%patch -p0

%build
install %{SOURCE1} .
mv %{name}-Makefile.PLD Makefile
%{__make} RPM_OPT_FLAGS="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_libdir},%{_includedir},%{_examplesdir}/%{name}-%{version}}
#%{__make} prefix=$RPM_BUILD_ROOT%{_prefix} install

install -s libtogl.so.1.3 $RPM_BUILD_ROOT%{_libdir}
cp double gears index overlay texture $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
install togl.c $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

install togl.h $RPM_BUILD_ROOT%{_includedir}

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc LICENSE
%attr(755,root,root) %{_libdir}/libtogl.so.1.3

%files devel
%defattr(644,root,root,755)
%attr(644,root,root) %{_includedir}/togl.h
%attr(755,root,root) %{_examplesdir}/%{name}-%{version}/*[^togl.c]
%attr(644,root,root) %{_examplesdir}/%{name}-%{version}/*.c
