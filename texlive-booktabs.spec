%global tl_name booktabs
%global tl_revision 77682

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.61803398
Release:	%{tl_revision}.1
Summary:	Publication quality tables in LaTeX
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/booktabs
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/booktabs.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/booktabs.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/booktabs.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package enhances the quality of tables in LaTeX, providing extra
commands as well as behind-the-scenes optimisation. Guidelines are given
as to what constitutes a good table in this context. From version 1.61,
the package offers longtable compatibility.

