Summary: A Fluent Bit output plugin for CloudWatch Logs
Name: amazon-cloudwatch-logs-for-fluent-bit
Version: 0.0.0
Release: 4%{?dist}
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
git clone --depth 10 https://github.com/aws/amazon-cloudwatch-logs-for-fluent-bit.git
git -C amazon-cloudwatch-logs-for-fluent-bit checkout b5dc2e67047da375dd5327e5a2d9cf5a2436219a
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
* Fri Oct 18 2019 Ichinose Shogo <shogo82148@gmail.com> - 0.0.0-4
- update Go 1.13.1
- update to b5dc2e

* Tue Jul 30 2019 Ichinose Shogo <shogo82148@gmail.com> - 0.0.0-3
- fix install path

* Tue Jul 30 2019 Ichinose Shogo <shogo82148@gmail.com> - 0.0.0-2
- update to 5dcefe from 6662a0
