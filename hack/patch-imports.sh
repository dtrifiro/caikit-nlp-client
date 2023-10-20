#!/bin/sh
tmp_file=$(mktemp ${1}.XXXXX)
# Absolute path to this script
script=$(readlink -f "$0")
# Absolute path this script is in
script_ath=$(dirname "$script")

awk -f ${script_ath}/patch-imports.awk ${1} 1>"${tmp_file}" && mv ${tmp_file} ${1} && rm -f ${tmpfile}

