#
# spec file for package gradle
#
# Copyright (c) SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.
 
# Please submit bugfixes or comments via http://bugs.opensuse.org/
#
 
 
Name:           gradle
Version:        8.10.2
Release:        0
Summary:        Groovy-based build system
License:        Apache-2.0
Group:          Development/Tools/Building
Url:            http://www.gradle.org/
Source:         https://services.gradle.org/distributions/gradle-%{version}-bin.zip
BuildRequires:  unzip
BuildArch:      noarch
Requires(post): (update-alternatives or alternatives)
Requires(postun): (update-alternatives or alternatives)
Requires: java-devel
	
%define gpath %{_datadir}/%{name}-%{version}

%post
%{_sbindir}/update-alternatives --install '%{_datadir}/gradle' gradle-sdk '%{gpath}' 25
%{_sbindir}/update-alternatives --install '%{_bindir}/gradle' gradle '%{gpath}/bin/gradle' 25
 
%postun
%{_sbindir}/update-alternatives --remove gradle '%{gpath}/bin/gradle' || : 
%{_sbindir}/update-alternatives --remove gradle-sdk '%{gpath}' || : 
 

%description
A flexible Groovy-based build tool.
 
%prep
%setup -n %{name}-%{version}
 
%build
 
%install
%{__mkdir_p} %{buildroot}/%{_datadir}
%{__rm} bin/gradle.bat
%{__cp} -r ../%{name}-%{version} %{buildroot}/%{_datadir}/
 
%files
%defattr(-,root,root)
%ghost /etc/alternatives/gradle
%ghost /etc/alternatives/gradle-sdk
%ghost %{_bindir}/gradle
%ghost %{_datadir}/gradle
%doc LICENSE NOTICE
%dir %{_datadir}/%{name}-%{version}
%{_datadir}/%{name}-%{version}/*
%exclude %{_datadir}/%{name}-%{version}/LICENSE
%exclude %{_datadir}/%{name}-%{version}/NOTICE
 
%changelog
