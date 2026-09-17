# Fourth Estate Execution Environment

An [Execution Environment](https://docs.ansible.com/ansible/latest/getting_started_ee/index.html)
(EE) is the container image Ansible Automation Platform runs playbooks inside.
This directory builds **one image that can run any playbook in this
repository**, with a pinned toolchain.

## Why this exists

Without a published EE, every agency consuming this repository builds its own
image with its own collection versions. The consequence is that **the same
repository tag behaves differently in different environments**, and none of
those combinations are the one CI validated. A shared EE definition makes the
runtime part of the release rather than part of each customer's local setup.

It is also the strongest supply-chain control available here: pinning
collections to exact versions (see [Locking versions](#locking-versions))
means a hijacked or silently-republished Galaxy collection cannot enter an
agency's control plane through an unpinned version floor.

## Contents

| File | Purpose |
|------|---------|
| `execution-environment.yml` | ansible-builder v3 definition (base image, ansible-core pin, dependency wiring) |
| `requirements.yml` | Union of all 79 platform `requirements.yml` files, merged to the highest declared version floor (58 collections) |
| `requirements-lock.yml` | Exact version pins, including transitive dependencies. Generated, not hand-edited. Absent until you run `generate-lock.sh` |
| `requirements.txt` | Python packages **not** supplied by the collections themselves (WinRM, Kerberos, network transports) |
| `bindep.txt` | System packages (compilers, `krb5-devel`, `libssh-devel`, `sshpass`) |
| `build.sh` | Builds the image; prefers the lock file when present |
| `generate-lock.sh` | Resolves version floors into exact pins (needs Galaxy access) |

## Building

```bash
pip install ansible-builder>=3.0
cd execution_environment
./build.sh                          # -> fourth-estate-ee:latest
./build.sh registry.example.mil/fourth-estate-ee:1.1.0
```

`build.sh` assembles a temporary build context and picks the pinned
`requirements-lock.yml` when it exists, falling back to the version floors in
`requirements.yml` otherwise. It prints which one it used.

### Base image

The definition defaults to `ee-minimal-rhel9` from `registry.redhat.io`, which
requires a Red Hat registry login:

```bash
podman login registry.redhat.io
```

Without an AAP subscription, edit `execution-environment.yml` and switch to the
commented-out `quay.io/ansible/community-ee-base` line.

## Locking versions

The generated `requirements.yml` carries version *floors* (`>=`), inherited
from the platform requirements files. Floors are not reproducible: two builds a
month apart can produce different collection sets.

On a machine with Galaxy access:

```bash
./generate-lock.sh              # writes requirements-lock.yml
git add requirements-lock.yml
```

Commit the lock file. Every agency that builds from that tag then gets an
identical collection set, and `build.sh` uses it automatically.

Regenerate the lock whenever a platform's `requirements.yml` changes.

## Automation Hub collections

Two collections — `ansible.controller` and `ansible.hub` — have no stable
release on community Galaxy; certified builds ship only from Red Hat
Automation Hub. They are flagged by the `# automation-hub-only:` marker line in
`requirements.yml`, the same convention
`scripts/generate_online_baseline.sh` uses.

Either configure your Automation Hub server and token in `ansible.cfg` before
building, or comment those two entries out if you are not managing AAP itself
from this EE. `generate-lock.sh` already degrades gracefully: if Hub is not
configured it locks everything else and tells you what it skipped.

## Using it in Automation Controller

1. Push the image to your private registry or Automation Hub.
2. In Controller: **Administration → Execution Environments → Add**, pointing at
   the image and its pull credential.
3. Set that EE on the job templates that run this repository.

Two related settings matter as much as the EE itself:

- **Pin the project to a release tag, not `main`.** A project tracking `main`
  with *Update Revision on Launch* enabled turns every commit here into an
  immediate change in your control plane. Pin to a tag and review
  [`docs/CHANGELOG.md`](../docs/CHANGELOG.md) before moving it.
- **Credentials belong in Controller**, injected at launch — not in inventory
  files or `vars`. See [Credentials and secrets](../README.md#credentials-and-secrets).

## Verifying an image

```bash
podman run --rm fourth-estate-ee:latest ansible --version
podman run --rm fourth-estate-ee:latest ansible-galaxy collection list
```

The second command lists the resolved collection set — compare it against
`requirements-lock.yml` to confirm the image matches the lock it was built from.
