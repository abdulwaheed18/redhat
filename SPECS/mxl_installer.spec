#
# spec file for package mcafee-installer 
#
# Copyright (c) 2013 Mcafee Team



#set macro attributes
%define _topdir	 	/usr/src/redhat
%define _tmppath        /usr/src/redhat/tmp

%define name	        mfe-cloudsso-sl-installer
%define version         1.0.0
%define release	        1


Name:  			%{name}
Version: 		%{version}
Release:                %{release}

BuildRoot: 		%{_tmppath}/installer
BuildArch: 		noarch
Prefix: 		/opt

Group: 			MXLogic
Vendor: 		MXLogic
Packager: 		Support <support@mxlogic.com>
License: 		commercial


Source: %{name}-%{version}.tar.gz

Summary: Contains the apache tomcat server with the deploy script and mxlcloudsso.war.

BuildRoot: %{_tmppath}/installer

%description
Tomcat server that is used to run the web application program.

%prep
%setup -q -n mfe-cloudsso-sl-installer

%build

%install

#remove if exist 
rm -rf $RPM_BUILD_ROOT

mkdir -p $RPM_BUILD_ROOT/%{name}/apache-tomcat-7.0.34

# copying file for installation
cp -r apache-tomcat-7.0.34/. $RPM_BUILD_ROOT/%{name}/apache-tomcat-7.0.34
cp deploy.sh $RPM_BUILD_ROOT/%{name}
cp mxlcloudsso.war $RPM_BUILD_ROOT/%{name}/apache-tomcat-7.0.34/webapps/


%post
#start the tomcat after the installation
chmod 500 $RPM_BUILD_ROOT/%{name}/apache-tomcat-7.0.34/bin/*.sh
sh $RPM_BUILD_ROOT/%{name}/apache-tomcat-7.0.34/bin/startup.sh

%clean
#clean the temporary installation folder
rm -rf $RPM_BUILD_ROOT

%files
# The file section, it has to be exact, matching all files.
# Here you have the power to implement all rights, even if they are different in the tar.gz

%defattr(-,root,root)
%attr(0755,root,root) /%{name}/*


%changelog
