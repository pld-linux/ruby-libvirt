Summary:	Ruby bindings for libvirt
Name:		ruby-libvirt
Version:	0.4.0
Release:	1
License:	LGPL v2+
Group:		Development/Languages
Source0:	http://libvirt.org/ruby/download/%{name}-%{version}.tgz
# Source0-md5:	868a8ba57b6a699f443fc2a7a3f7374b
URL:		http://libvirt.org/ruby/
BuildRequires:	libvirt-devel >= 0.4.0
BuildRequires:	rpm-rubyprov
BuildRequires:	rpmbuild(macros) >= 1.656
BuildRequires:	ruby-devel
BuildRequires:	ruby-rubygems
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Ruby bindings for libvirt.

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
%{ruby_vendorarchdir}/_libvirt.so
