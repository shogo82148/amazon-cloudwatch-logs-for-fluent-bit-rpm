Summary: A Fluent Bit output plugin for CloudWatch Logs
Name: amazon-cloudwatch-logs-for-fluent-bit
Version: 0.0.0
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
git clone --depth 10 https://github.com/aws/amazon-cloudwatch-logs-for-fluent-bit.git
git -C amazon-cloudwatch-logs-for-fluent-bit checkout 5dcefed4096bf85b7fd22fbe0e1e589aa72a08df
make -C amazon-cloudwatch-logs-for-fluent-bit release

%install

mkdir -p %{buildroot}/etc/fluent-bit/plugins
install -m 644 -p amazon-cloudwatch-logs-for-fluent-bit/bin/cloudwatch.so \
    %{buildroot}/etc/fluent-bit/plugins/cloudwatch.so

%clean
rm -fr %{buildroot}

%files
%defattr(-,root,root,-)
/etc/fluent-bit/plugins/cloudwatch.so
