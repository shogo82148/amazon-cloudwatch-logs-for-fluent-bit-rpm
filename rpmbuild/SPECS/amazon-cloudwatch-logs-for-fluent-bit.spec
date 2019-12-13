Summary: A Fluent Bit output plugin for CloudWatch Logs
Name: amazon-cloudwatch-logs-for-fluent-bit
Version: 1.1.0
Release: 1%{?dist}
URL: https://github.com/aws/amazon-cloudwatch-logs-for-fluent-bit
License: Apache v2.0
Group: Applications/File
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: gcc-c++, git, make

%description
A Fluent Bit output plugin for CloudWatch Logs

%prep

%build
rm -fr %{buildroot}
git clone https://github.com/aws/amazon-cloudwatch-logs-for-fluent-bit.git
git -C amazon-cloudwatch-logs-for-fluent-bit checkout -f "v1.1.0"
make -C amazon-cloudwatch-logs-for-fluent-bit release

%install

mkdir -p %{buildroot}/usr/local/lib/fluent-bit
install -m 644 -p amazon-cloudwatch-logs-for-fluent-bit/bin/cloudwatch.so \
    %{buildroot}/usr/local/lib/fluent-bit/cloudwatch.so

%clean
rm -fr %{buildroot}

%files
%defattr(-,root,root,-)
/usr/local/lib/fluent-bit/cloudwatch.so

%changelog
* Fri Dec 13 2019 Ichinose Shogo <shogo82148@gmail.com> - 1.1.0-1

* Wed Nov 27 2019 Ichinose Shogo <shogo82148@gmail.com> - 1.0.0-1
- bump up to v1.0.0
- update Go to 1.13.4

* Fri Oct 18 2019 Ichinose Shogo <shogo82148@gmail.com> - 0.0.0-4
- update Go 1.13.1
- update to b5dc2e

* Tue Jul 30 2019 Ichinose Shogo <shogo82148@gmail.com> - 0.0.0-3
- fix install path

* Tue Jul 30 2019 Ichinose Shogo <shogo82148@gmail.com> - 0.0.0-2
- update to 5dcefe from 6662a0
