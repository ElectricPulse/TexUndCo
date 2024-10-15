#!/bin/bash
location="$(dirname "$(realpath "$0")")"
viewer="$location/mupdf"
src="$location/src"
outDirname="$location/out"
texFilename=main.tex
texFile="$src/$texFilename"
pdfFile="$outDirname/$(echo "$texFilename" | sed 's#\.tex#\.pdf#')"

flags="-output-directory $outDirname -file-line-error -shell-escape"

if [ "$#" = 0 ]; then
	tmp="$(mktemp)"
	(cd "$src"; python main.py)
	(cd $src; texfot --quiet pdflatex $flags -interaction=nonstopmode "$texFile" >"$tmp")
	logFile="$(mktemp)"
	tail -n +2 "$tmp" | sed '$d' > "$logFile"
	rm "$tmp"

	if [ "$?" != 0 ] || [ "$(cat "$logFile" | perl -ne 'unless ($_ =~ /.*warning.*/i or $_ =~ /^,/) { print $_ }' | wc -l | tr -d ' ')" != 0 ]; then
		echo "Error encountered:"
		cat "$logFile"
		read -n 1
	fi

	rm "$logFile"
else
	(cd $src; pdflatex $flags "$texFile")
fi

if [ ! -f "$pdfFile" ]; then
	echo "No pdf generated"
	exit 1
fi
if pid="$(pgrep mupdf)"; then
	kill -HUP "$pid"
else
	echo "Reloaded"
	mupdf "$pdfFile" >/dev/null 2>&1 &
fi

exit 0
