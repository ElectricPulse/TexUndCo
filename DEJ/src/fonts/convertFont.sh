#!/usr/local/bin/bash

function parseArgs() {
	if [ "$#" != "1" ]; then
		true
		return
	fi
	arg="$1"
	srcDir="$(dirname "$arg")"
	srcFilename="$(basename "$arg")"
	srcFile="$srcDir/$srcFilename"
	srcFileBase="$srcDir/$(echo "$srcFilename" | sed 's#.otf##')"
	outPrefix=main
	outFileBase="$srcDir/$outPrefix"

	if [ "$(file -ib "$srcFile")" != "application/vnd.ms-opentype; charset=binary" ]; then
		true
		return
	fi

	false
}

if parseArgs $@; then
	echo "Invalid args"
	exit 1
fi

otftotfm -e texnansx --name "$(basename "$srcDir")" --directory "$srcDir" "$srcFile"
mv "$srcDir"/*.pfb "$outFileBase.pfb"
mv "$srcDir"/*.enc "$outFileBase.enc"
