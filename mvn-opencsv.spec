#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : mvn-opencsv
Version  : 2.3
Release  : 1
URL      : https://repo1.maven.org/maven2/net/sf/opencsv/opencsv/2.3/opencsv-2.3.jar
Source0  : https://repo1.maven.org/maven2/net/sf/opencsv/opencsv/2.3/opencsv-2.3.jar
Source1  : https://repo1.maven.org/maven2/net/sf/opencsv/opencsv/2.3/opencsv-2.3.pom
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0
Requires: mvn-opencsv-data = %{version}-%{release}

%description
No detailed description available

%package data
Summary: data components for the mvn-opencsv package.
Group: Data

%description data
data components for the mvn-opencsv package.


%prep

%build

%install
mkdir -p %{buildroot}/usr/share/java/.m2/repository/net/sf/opencsv/opencsv/2.3
cp %{SOURCE0} %{buildroot}/usr/share/java/.m2/repository/net/sf/opencsv/opencsv/2.3

mkdir -p %{buildroot}/usr/share/java/.m2/repository/net/sf/opencsv/opencsv/2.3
cp %{SOURCE1} %{buildroot}/usr/share/java/.m2/repository/net/sf/opencsv/opencsv/2.3


%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/java/.m2/repository/net/sf/opencsv/opencsv/2.3/opencsv-2.3.jar
/usr/share/java/.m2/repository/net/sf/opencsv/opencsv/2.3/opencsv-2.3.pom
