Name:		texlive-booktabs
Version:	53402
Release:	1
Summary:	Publication quality tables in LaTeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/booktabs
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/booktabs.r53402.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/booktabs.doc.r53402.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/booktabs.source.r53402.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package enhances the quality of tables in LaTeX, providing
extra commands as well as behind-the-scenes optimisation.
Guidelines are given as to what constitutes a good table in
this context. From version 1.61, the package offers longtable
compatibility.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/booktabs
%doc %{_texmfdistdir}/doc/latex/booktabs
#- source
%doc %{_texmfdistdir}/source/latex/booktabs

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
