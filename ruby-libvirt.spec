Summary:	Ruby bindings for libvirt
Summary(pl.UTF-8):	Wiązania języka Ruby do biblioteki libvirt
Name:		ruby-libvirt
Version:	0.5.2
Release:	1
License:	LGPL v2+
Group:		Development/Languages
Source0:	http://libvirt.org/ruby/download/%{name}-%{version}.tgz
# Source0-md5:	3e926f0a3ead7cc3483cb890be393e6c
URL:		http://libvirt.org/ruby/
BuildRequires:	libvirt-devel >= 0.4.0
BuildRequires:	rpm-rubyprov
BuildRequires:	rpmbuild(macros) >= 1.656
BuildRequires:	ruby-devel
BuildRequires:	ruby-rubygems
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Ruby bindings for libvirt.

%description -l pl.UTF-8
Wiązania języka Ruby do biblioteki libvirt.

%prep
%setup -q

%build
CC="%{__cc}" \
CFLAGS="%{rpmcflags}" \
rake build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{ruby_vendorlibdir},%{ruby_vendorarchdir}}
install -p lib/libvirt.rb $RPM_BUILD_ROOT%{ruby_vendorlibdir}
install -p ext/libvirt/_libvirt.so $RPM_BUILD_ROOT%{ruby_vendorarchdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc NEWS README
%{ruby_vendorlibdir}/libvirt.rb
%attr(755,root,root) %{ruby_vendorarchdir}/_libvirt.so
