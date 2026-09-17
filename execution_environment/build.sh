#!/usr/bin/env bash
# Build the Fourth Estate execution environment image.
#
#   ./build.sh [TAG]        default TAG: fourth-estate-ee:latest
#
# Prefers requirements-lock.yml (exact pins, from generate-lock.sh) over
# requirements.yml (version floors) so production builds are reproducible.
set -euo pipefail

cd "$(dirname "$0")"

TAG="${1:-fourth-estate-ee:latest}"

command -v ansible-builder >/dev/null 2>&1 || {
  echo "ansible-builder is not available. Install it first:" >&2
  echo "  pip install ansible-builder>=3.0" >&2
  exit 1
}

# Assemble a build context so execution-environment.yml can always reference
# 'requirements.yml' while we choose floors vs. lock here.
ctx="$(mktemp -d)"
trap 'rm -rf "$ctx"' EXIT
cp execution-environment.yml requirements.txt bindep.txt "$ctx/"

if [ -f requirements-lock.yml ]; then
  echo "==> Using requirements-lock.yml (exact pins)"
  cp requirements-lock.yml "$ctx/requirements.yml"
else
  echo "==> No requirements-lock.yml found; using requirements.yml (version floors)."
  echo "==> For reproducible agency-wide builds, run ./generate-lock.sh first."
  cp requirements.yml "$ctx/requirements.yml"
fi

ansible-builder build \
  --file "$ctx/execution-environment.yml" \
  --context "$ctx/context" \
  --tag "$TAG" \
  --verbosity 2

echo "==> Built $TAG"
echo "==> Push it to your private registry / Automation Hub, then register it"
echo "    in Automation Controller (Administration -> Execution Environments)"
echo "    and set it on the job templates that run this repository."
