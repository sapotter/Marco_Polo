#!/bin/bash

# STYLE_COLOR
RED="\033[0;31m"
LIGHT_GREEN="\033[1;32m"
NC="\033[0m" # No Color
BOLD="\033[1m"

OS_NAME=$(uname)

usage() {
    cat <<EOT
$(echo -e ${BOLD}NAME${NC})
    $(basename "$0") -- Create macOS App bundle

$(echo -e ${BOLD}SYNOPSIS${NC})
    $(basename "$0") [-m] [-b | -d | -o | -w] [-s [spec-path]] [-h]

$(echo -e ${BOLD}OPTIONS${NC})
    -m Run py-makespec. Default: pyinstaller.
    -b Specify the macOS CFBundleIdentifier if an application bundle
       is created. Default: org.hauptman-woodward.polo.
    -d Create a directory containing tha application and its supporting
       components. Default.
    -o Create a single file application.
    -w Create a macOS application bundle.
    -s Specify the "spec" file directory path. Default: ./macOS.
    -h Help.

$(echo -e ${BOLD}Examples${NC})
EOT
}

# shellcheck disable=SC2223
: ${RUNNER:=pyinstaller --clean -y}
# shellcheck disable=SC2223
: ${SPEC_PATH:=macOS}
# shellcheck disable=SC2223
: ${BUNDLE_ID:=org.hauptman-woodward.polo}


while getopts "bdmows:h" option; do
    case $option in
        b)
            bundle="--osx-bundle-identifier ${BUNDLE_ID}"
            ;;
        d)
            onedir="--onedir"
            ;;
        m)
            RUNNER="pyi-makespec"
            ;;
        s)
            SPEC_PATH=$OPTARG
            ;;
        o)
            onefile="--onefile"
            ;;
        w)
            windowed="--windowed"
            ;;
        h|*)
            usage
            exit 1
    esac
done
shift "$((OPTIND - 1))"

if [ "$makespec" ]; then RUNNER="pyi-makespec"; fi

CMD="$RUNNER $bundle $onedir $onefile $windowed --specpath ${SPEC_PATH}"
# Trim extra spaces
CMD=$(echo "$CMD" | \
    awk '{ gsub(/[[:space:]]{2,}/, " "); print $0; }' | \
    awk '{ gsub(/^[[:space:]]+|[[:space:]]+$/, ""); print $0; }')

# py2app borked on missing libpython3.7m.dylib. Even this fix worked
# but the build failed regardless.

# pyinstall is quite happy without it.

#POLO_ENV=/usr/local/Caskroom/miniconda/base/envs/polo
#
#if [ ! -e $POLO_ENV/lib/libpython3.7.a ]; then
#  pushd $POLO_ENV/lib && ln -s libpython3.7m.a libpython3.7.a && popd || exit 1;
#fi
#if [ ! -e $POLO_ENV/lib/libpython3.7.dylib ]; then
#  pushd $POLO_ENV/lib && ln -s libpython3.7m.dylib libpython3.7.dylib && popd || exit 1;
#fi

declare -i errors=0
if [ "$(basename "$(pwd)")" != "Marco_Polo" ]; then
    echo "ERROR: pyinstaller-macos.sh must be run in the Marco_Polo project root directory."
    _=$((errors++))
fi
if [ "${CONDA_DEFAULT_ENV:-notpolo}" = "notpolo" ]; then
    echo "ERROR: activate required conda environment with : conda activate polo"
    _=$((errors++))
fi
[ $((errors)) -gt 0 ] && exit 1
PYINSTALLER_INSTALLED=$(conda list -c pyinstaller | awk '/pypi\/pypi::pyinstaller-[[:digit:]]/ { print $0 }')
if [ "${PYINSTALLER_INSTALLED:-notinstalled}" = "notinstalled" ]; then
    echo "Install pyinstaller with: pip install pyinstaller"
    exit 1
fi

$CMD --collect-all tensorflow \
--hidden-import pptx \
--add-data ../src/data:data --add-data ../src/astor:astor \
--add-data ../src/unrar:unrar --add-data ../src/templates:templates \
--icon ../macOS/application.icns \
src/Polo.py
