%global packname  RCurl
%global rlibdir  %{_libdir}/R/library

Name:             R-%{packname}
Version:          1.95.4.1
Release:          1
Summary:          General network (HTTP/FTP/...) client interface for R
Group:            Sciences/Mathematics
License:          BSD
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
<<<<<<< HEAD
Source0:          http://cran.r-project.org/src/contrib/RCurl_1.95-3.tar.gz
=======
Source0:          http://cran.r-project.org/src/contrib/RCurl_1.95-4.1.tar.gz
>>>>>>> auto_update
Requires:         R-methods R-bitops R-Rcompression R-XML
BuildRequires:    R-devel Rmath-devel texlive-collection-latex
BuildRequires:    R-methods R-bitops R-Rcompression R-XML
BuildRequires:    curl-devel

%description
The package allows one to compose general HTTP requests and provides
convenient functions to fetch URIs, get & post forms, etc. and process the
results returned by the Web server. This provides a great deal of control
over the HTTP/FTP/... connection and the form of the request while
providing a higher-level interface than is available just using R socket
connections.  Additionally, the underlying implementation is robust and
extensive, supporting FTP/FTPS/TFTP (uploads and downloads), SSL/HTTPS,
telnet, dict, ldap, and also supports cookies, redirects, authentication,

%prep
%setup -q -c -n %{packname}

%build

%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/html
%doc %{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/CurlSSL
%{rlibdir}/%{packname}/HTTPErrors
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/enums
%{rlibdir}/%{packname}/examples
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/libs
<<<<<<< HEAD
=======

>>>>>>> auto_update
