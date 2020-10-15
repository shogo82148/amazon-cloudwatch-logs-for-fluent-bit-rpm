Summary: A Fluent Bit output plugin for CloudWatch Logs
Name: amazon-cloudwatch-logs-for-fluent-bit
Version: 1.4.0
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
git -C amazon-cloudwatch-logs-for-fluent-bit checkout -f "v1.4.0"

# workaround for go.mod: checksum mismatch
# verifying github.com/aws/amazon-kinesis-firehose-for-fluent-bit@v1.4.1/go.mod: checksum mismatch
# 	downloaded: h1:LV5vSM9R3vODyhZM9jdUWLThms4Chcio46SUff6XfBY=
# 	go.sum:     h1:2hixxBh6Xygvxe6x/PSUTphh8dZ0WptVty98ftZIhAU=
GOSUMDB=off \
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
* Thu Sep 17 2020 Ichinose Shogo <shogo82148@gmail.com> - 1.4.0-1
- bump up to v1.4.0
- update Go to 1.15.2

* Sat Jul 18 2020 Ichinose Shogo <shogo82148@gmail.com> - 1.3.0-1
- bump up to v1.3.0
- update Go to 1.14.6

* Mon Mar 23 2020 Ichinose Shogo <shogo82148@gmail.com> - 1.2.0-2
- update Go to 1.14.1

* Thu Mar 12 2020 Ichinose Shogo <shogo82148@gmail.com> - 1.2.0-1
- bump up to v1.2.0
- update Go to 1.14

* Tue Jan 14 2020 Ichinose Shogo <shogo82148@gmail.com> - 1.1.1-1
- bump up to v1.1.1
- update Go to 1.13.6

* Fri Dec 13 2019 Ichinose Shogo <shogo82148@gmail.com> - 1.1.0-1
- bump up to v1.1.0
- update Go to 1.13.5

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
