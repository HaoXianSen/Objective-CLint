#!/usr/bin/env bash
# format-objc-file.sh
# Formats an Objective-C file, replacing it without a backup.
# Copyright 2015 Square, Inc

set -o errexit
set -o nounset
set -o pipefail

export CDPATH=""
DIR=$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)
DRY_RUN=0
FILE=""

function help() {
	echo "$0 - formats an objc file"
	echo " "
	echo "$0 [options] file"
	echo " "
	echo "options:"
	echo "-h, --help     show brief help"
	echo "-d, --dry-run  output formatted file to STDOUT, instead of modifying it"
}

while test $# -gt 0; do
	case "$1" in
	-h | --help)
		help
		exit 0
		;;
	-d | --dry-run)
		DRY_RUN=1
		shift
		;;
	*)
		if [ -n "$FILE" ]; then
			echo "May only provide a single file"
			help
			exit 1
		fi
		FILE="$1"
		shift
		;;
	esac
done

if [ ! -e ".clang-format" ]; then
	echo "Couldn't find .clang-format file, unable to format files. Please setup this repo by running the setup-repo.sh script from your repo's top level."
	echo "Also, formatting scripts should be run from the repo's top level dir."
	exit 1
fi

if [ -z "$FILE" ]; then
	echo "Must provide a file to format"
	help
	exit 1
fi

function format_objc_file_dry_run() {
	# "#pragma Formatter Exempt" or "// MARK: Formatter Exempt" means don't format this file.
	# Read the first line and trim it.
	line="$(head -1 "$FILE" | xargs)"
	
	if [ "$line" == "#pragma Formatter Exempt" -o "$line" == "// MARK: Formatter Exempt" ]; then
		cat "$1"
		return
	fi

  # clang-format gets confused
  cpu=$(uname -m)
  python3=$(which python3)
 if [[ "${cpu}" == "x86_64" ]]; then
	(cat "$1") | 
	 ($python3 "$DIR"/../include/LiteralSymbolSpacer.py "$1") |
	 ($python3 "$DIR"/../include/InlineConstructorOnSingleLine.py "$1") |
	 ($python3 "$DIR"/../include/MacroSemicolonAppender.py "$1") |
	 ($python3 "$DIR"/../include/DoubleNewlineInserter.py "$1") |
	("$DIR"/clang-format-x86 -style=file ) |
	# 泛型取消多余的缩进
	($python3 "$DIR"/../include/GenericCategoryLinebreakIndentation.py "$1") |
	($python3 "$DIR"/../include/ParameterAfterBlockNewline.py "$1") |
	($python3 "$DIR"/../include/HasIncludeSpaceRemover.py "$1") |
	($python3 "$DIR"/../include/NewLineAtEndOfFileInserter.py "$1")
 else
	(cat "$1") | 
	 ($python3 "$DIR"/../include/LiteralSymbolSpacer.py "$1") |
	 ($python3 "$DIR"/../include/InlineConstructorOnSingleLine.py "$1") |
	 ($python3 "$DIR"/../include/MacroSemicolonAppender.py "$1") |
	 ($python3 "$DIR"/../include/DoubleNewlineInserter.py "$1") |
	("$DIR"/clang-format-arm64 -style=file) |
	# 泛型取消多余的缩进
	($python3 "$DIR"/../include/GenericCategoryLinebreakIndentation.py "$1") |
	($python3 "$DIR"/../include/ParameterAfterBlockNewline.py "$1") |
	($python3 "$DIR"/../include/HasIncludeSpaceRemover.py "$1") |
	($python3 "$DIR"/../include/NewLineAtEndOfFileInserter.py "$1")
 fi
	
}

function format_objc_file() {
	tempFile="$(mktemp)"
	status=0
	format_objc_file_dry_run "$1" >"$tempFile" || status=$?
	if [ $status -eq 0 ]; then
		mv "$tempFile" "$1"
	else
		rm -f "$tempFile"
		exit $status
	fi
}

if [ $DRY_RUN -eq 0 ]; then
	format_objc_file "$FILE"
else
	format_objc_file_dry_run "$FILE"
fi
