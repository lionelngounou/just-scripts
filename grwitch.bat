@echo off
echo Setting GRAILS_HOME

set _version=%1% 
set GRAILS_HOME=C:\grails\2.4.4

IF %_version:~0,1% == 3 (
	set GRAILS_HOME=C:\grails\3.0.10
)

echo Setting PATH for %GRAILS_HOME%
set PATH=%GRAILS_HOME%\bin;%PATH%

echo Display grails version
grails -version