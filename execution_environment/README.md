# Fourth Estate Execution Environment

An [Execution Environment](https://docs.ansible.com/ansible/latest/getting_started_ee/index.html)
(EE) is the container image Ansible Automation Platform runs playbooks inside.
This directory builds **an image for the platform you actually run** — or, if
you run several from one controller, for exactly those — with a pinned
toolchain.

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

## Why it builds per platform

You do not take this repository whole. You take the directory for the platform
you run — `cohesity/`, or `pure_storage/`, or `cisco/` — and nothing else.

An image built from the union of all 79 `requirements.yml` files carries 58
collections. A Cohesity site needs **four** of them. The other 54 are Dragos,
Claroty, Cisco, VMware and the rest: never loaded, but present in the image, in
its attack surface, and in everything you have to review when a collection has
a CVE.

So `build.sh` takes the platform:

| Platform | Collections in its image |
|---|---|
| `cohesity` | 4 |
| `pure_storage` | 5 |
| `cisco` | 13 |
| `vmware` | 7 |
| `operational_technology` | 6 |
| `--all` (every platform) | 58 |

`--all` still exists and is the right answer when one controller runs playbooks
from several directories. It is the wrong default, which is what it used to be.

## Contents

| File | Purpose |
|------|---------|
| `compose-requirements.py` | Merges a platform's `requirements.yml` files to the highest declared version floor. Everything else here calls it |
| `execution-environment.yml` | ansible-builder v3 definition (base image, ansible-core pin, dependency wiring) |
| `requirements.yml` | The `--all` union, committed so it is reviewable (58 collections). CI fails if it drifts from what the platform files compose to |
| `requirements-lock-<platform>.yml` | Exact version pins for one platform, transitive dependencies included. Generated, not hand-edited. Absent until you run `generate-lock.sh` |
| `requirements.txt` | Python packages **not** supplied by the collections themselves (WinRM, Kerberos, network transports) |
| `bindep.txt` | System packages (compilers, `krb5-devel`, `libssh-devel`, `sshpass`) |
| `build.sh` | Builds the image for a platform; prefers that platform's lock file when present |
| `generate-lock.sh` | Resolves a platform's version floors into exact pins (needs Galaxy access) |

## Building

```bash
pip install ansible-builder>=3.0
cd execution_environment

./build.sh --list                   # the platforms you can name

./build.sh --platform cohesity      # -> fourth-estate-ee-cohesity:latest
./build.sh --platform cisco --tag registry.example.mil/fourth-estate-ee-cisco:1.1.0
./build.sh --platform cisco --platform infoblox   # one image for both
./build.sh --all                    # -> fourth-estate-ee:latest, all 58
```

`build.sh` composes that platform's requirements, assembles a temporary build
context, and picks the pinned `requirements-lock-<platform>.yml` when it exists,
falling back to version floors otherwise. It prints which one it used and how
many collections the image will carry.

To see what would go in without building anything:

```bash
./compose-requirements.py --platform cohesity
```

### Base image

The definition defaults to `ee-minimal-rhel9` from `registry.redhat.io`, which
requires a Red Hat registry login:

```bash
podman login registry.redhat.io
```

Without an AAP subscription, edit `execution-environment.yml` and switch to the
commented-out `quay.io/ansible/community-ee-base` line.

## Locking versions

A composition carries version *floors* (`>=`), inherited from the platform
requirements files. Floors are not reproducible: two builds a month apart can
produce different collection sets.

On a machine with Galaxy access:

```bash
./generate-lock.sh --platform cohesity   # writes requirements-lock-cohesity.yml
git add requirements-lock-cohesity.yml
```

Lock files are named after what went into them, matching the image `build.sh`
produces from the same arguments, so one platform's lock cannot be applied to
another platform's image by accident. `--all` writes the unsuffixed
`requirements-lock.yml`.

Commit the lock file. Every agency that builds from that tag then gets an
identical collection set, and `build.sh` uses it automatically.

Regenerate the lock whenever that platform's `requirements.yml` changes.

**No lock file is committed here.** Generating one needs egress to
`galaxy.ansible.com`, which this repository's CI does not have. Generate and
commit the locks for the platforms you run — that is the supply-chain control
described above, and until you do, your builds resolve floors afresh each time.

## Automation Hub collections

Two collections — `ansible.controller` and `ansible.hub` — have no stable
release on community Galaxy; certified builds ship only from Red Hat
Automation Hub. They are flagged by the `# automation-hub-only:` marker line in
`ansible/requirements.yml`, the same convention
`scripts/generate_online_baseline.sh` uses.

The marker is carried onto a composition only when that composition actually
includes the collection, so **this affects the `ansible` platform and `--all`,
and no other platform**. Building `--platform cohesity` needs no Automation Hub
access at all.

Where it does apply: configure your Automation Hub server and token in
`ansible.cfg` before building, or drop those two entries if you are not managing
AAP itself from this EE. `generate-lock.sh` degrades gracefully — if Hub is not
configured it locks everything else and tells you what it skipped.

## Using it in Automation Controller

1. Push the image to your private registry or Automation Hub.
2. In Controller: **Administration → Execution Environments → Add**, pointing at
   the image and its pull credential.
3. Set that EE on the job templates that run this platform's playbooks. A
   per-platform image means a job template gets the EE for the platform it
   automates — a Cohesity template does not run inside an image carrying the
   Cisco and VMware collections.

Two related settings matter as much as the EE itself:

- **Pin the project to a release tag, not `main`.** A project tracking `main`
  with *Update Revision on Launch* enabled turns every commit here into an
  immediate change in your control plane. Pin to a tag and review
  [`docs/CHANGELOG.md`](https://github.com/Koga1985/Fourth-Estate-Ansible-Playbooks/blob/main/docs/CHANGELOG.md) before moving it.
- **Credentials belong in Controller**, injected at launch — not in inventory
  files or `vars`. See [Credentials and secrets](../README.md#credentials-and-secrets).

## Verifying an image

```bash
podman run --rm fourth-estate-ee-cohesity:latest ansible --version
podman run --rm fourth-estate-ee-cohesity:latest ansible-galaxy collection list
```

The second command lists the resolved collection set — compare it against
`requirements-lock-cohesity.yml` to confirm the image matches the lock it was
built from, and against `./compose-requirements.py --platform cohesity` to
confirm nothing unexpected came along as a transitive dependency.
