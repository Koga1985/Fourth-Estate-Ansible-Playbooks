#!/usr/bin/env bash
# Build a Fourth Estate execution environment image.
#
#   ./build.sh --platform cohesity              -> fourth-estate-ee-cohesity:latest
#   ./build.sh --platform cisco --tag my-ee:1.0
#   ./build.sh --platform cisco --platform infoblox
#   ./build.sh --all                            -> fourth-estate-ee:latest
#   ./build.sh --list                           -> the platforms you can name
#
# Customers take the directory for the platform they run, not the whole
# repository, so --platform builds an image carrying only that platform's
# collections. --all reproduces the every-platform image: correct when one
# controller runs playbooks from several directories, wasteful otherwise.
#
# Prefers a lock file (exact pins, from generate-lock.sh) over version floors,
# so production builds are reproducible. Lock files are per platform:
# requirements-lock-<platform>.yml, or requirements-lock.yml for --all.
set -euo pipefail

cd "$(dirname "$0")"

platforms=()
all=false
tag=""

while [ $# -gt 0 ]; do
  case "$1" in
    --platform) platforms+=("${2:?--platform needs a name}"); shift 2 ;;
    --all)      all=true; shift ;;
    --tag)      tag="${2:?--tag needs a value}"; shift 2 ;;
    --list)     exec ./compose-requirements.py --list ;;
    -h|--help)  sed -n '2,17p' "$0" | sed 's/^# \{0,1\}//'; exit 0 ;;
    *)          echo "unknown argument: $1 (try --help)" >&2; exit 2 ;;
  esac
done

if $all && [ "${#platforms[@]}" -gt 0 ]; then
  echo "--all and --platform are mutually exclusive" >&2; exit 2
fi
if ! $all && [ "${#platforms[@]}" -eq 0 ]; then
  echo "Name what to build: --platform <name> (repeatable), or --all." >&2
  echo "Run './build.sh --list' to see the platforms that declare requirements." >&2
  exit 2
fi

# Reject an unknown platform name before anything slower runs, so a typo costs
# a second rather than a failed build.
if ! $all; then
  known="$(./compose-requirements.py --list | awk '{print $1}')"
  for p in "${platforms[@]}"; do
    if ! grep -qx -- "$p" <<<"$known"; then
      echo "no such platform: $p" >&2
      echo "Run './build.sh --list' to see the platforms that declare requirements." >&2
      exit 2
    fi
  done
fi

command -v ansible-builder >/dev/null 2>&1 || {
  echo "ansible-builder is not available. Install it first:" >&2
  echo "  pip install ansible-builder>=3.0" >&2
  exit 1
}

# Name the image and its lock file after what went into it, so two images built
# from this directory cannot be confused for one another in a registry.
if $all; then
  slug=""
  compose_args=(--all)
else
  slug="-$(IFS=-; echo "${platforms[*]}")"
  compose_args=()
  for p in "${platforms[@]}"; do compose_args+=(--platform "$p"); done
fi
tag="${tag:-fourth-estate-ee${slug}:latest}"
lock="requirements-lock${slug}.yml"

# Assemble a build context so execution-environment.yml can always reference
# 'requirements.yml' while we choose here what that name resolves to.
ctx="$(mktemp -d)"
trap 'rm -rf "$ctx"' EXIT
cp execution-environment.yml requirements.txt bindep.txt "$ctx/"

if $all; then
  lock_hint="./generate-lock.sh --all"
else
  lock_hint="./generate-lock.sh$(printf -- ' --platform %s' "${platforms[@]}")"
fi

if [ -f "$lock" ]; then
  echo "==> Using $lock (exact pins)"
  cp "$lock" "$ctx/requirements.yml"
else
  echo "==> No $lock found; composing version floors from the platform's own requirements.yml."
  echo "==> For reproducible agency-wide builds, run '$lock_hint' first."
  ./compose-requirements.py "${compose_args[@]}" -o "$ctx/requirements.yml"
fi

count="$(grep -c '^  - name:' "$ctx/requirements.yml" || true)"
echo "==> $tag will carry $count collection(s)"

ansible-builder build \
  --file "$ctx/execution-environment.yml" \
  --context "$ctx/context" \
  --tag "$tag" \
  --verbosity 2

echo "==> Built $tag"
echo "==> Push it to your private registry / Automation Hub, then register it"
echo "    in Automation Controller (Administration -> Execution Environments)"
echo "    and set it on the job templates that run this platform's playbooks."
