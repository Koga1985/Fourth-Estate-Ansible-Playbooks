# ans_ci_pipelines

Scaffold CI for GitHub Actions or GitLab CI.

## Requirements

- Ansible 2.15+
- No additional Ansible collections required (uses `ansible.builtin`), unless noted below.

## Role Variables

All variables below are defined in `defaults/main.yml`. "Required" marks values that ship as a placeholder you must replace (e.g. `CHANGE_ME`); everything else has a working default.

| Variable | Default | Required | Description |
|----------|---------|----------|-------------|
| `apply_changes` | `false` | No | Common settings |
| `artifacts_dir` | `"/tmp/ansible-artifacts"` | No | — |
| `validate_certs` | `true` | No | — |
| `repo_root` | `"."` | No | — |
| `controller_host` | `"{{ lookup('env', 'CONTROLLER_HOST') \| default('https://controller....` | No | Controller connection |
| `controller_oauthtoken` | `"{{ lookup('env', 'CONTROLLER_OAUTH_TOKEN') \| default('') }}"` | No | — |
| `controller_username` | `"{{ lookup('env', 'CONTROLLER_USERNAME') \| default('') }}"` | No | — |
| `controller_password` | `"{{ lookup('env', 'CONTROLLER_PASSWORD') \| default('') }}"` | No | — |
| `ci_platform` | `"gitlab"` | No | CI/CD Platform Selection gitlab, github, jenkins, azure_devops |
| `gitlab_ci_enabled` | `true` | No | GitLab CI Configuration |
| `gitlab_url` | `"https://gitlab.example.mil"` | No | — |
| `gitlab_token` | `"{{ lookup('env', 'GITLAB_TOKEN') \| default('') }}"` | No | — |
| `gitlab_project_path` | `"fourth-estate/ansible-automation"` | No | — |
| `gitlab_ci_stages` | `(see defaults/main.yml)` | No | — |
| `gitlab_ci_variables` | `(see defaults/main.yml)` | No | — |
| `github_actions_enabled` | `false` | No | GitHub Actions Configuration |
| `github_url` | `"https://github.com"` | No | — |
| `github_token` | `"{{ lookup('env', 'GITHUB_TOKEN') \| default('') }}"` | No | — |
| `github_org` | `"fourth-estate"` | No | — |
| `github_repo` | `"ansible-automation"` | No | — |
| `github_workflows_dir` | `".github/workflows"` | No | — |
| `jenkins_enabled` | `false` | No | Jenkins Configuration |
| `jenkins_url` | `"https://jenkins.example.mil"` | No | — |
| `jenkins_user` | `"ansible-ci"` | No | — |
| `jenkins_token` | `"{{ lookup('env', 'JENKINS_TOKEN') \| default('') }}"` | No | — |
| `jenkins_jobs` | `(see defaults/main.yml)` | No | — |
| `azure_devops_enabled` | `false` | No | Azure DevOps Configuration |
| `azure_devops_org` | `"fourth-estate"` | No | — |
| `azure_devops_project` | `"ansible-automation"` | No | — |
| `azure_devops_token` | `"{{ lookup('env', 'AZURE_DEVOPS_TOKEN') \| default('') }}"` | No | — |
| `ci_pipeline_lint_enabled` | `true` | No | CI Pipeline Configuration |
| `ci_pipeline_test_enabled` | `true` | No | — |
| `ci_pipeline_build_ee_enabled` | `true` | No | — |
| `ci_pipeline_deploy_enabled` | `false` | No | — |
| `ansible_lint_config_path` | `".ansible-lint"` | No | Linting Configuration |
| `ansible_lint_rules` | `(see defaults/main.yml)` | No | — |
| `molecule_scenarios` | `(see defaults/main.yml)` | No | Testing Configuration |
| `ansible_test_sanity` | `true` | No | — |
| `ansible_test_units` | `true` | No | — |
| `ansible_test_integration` | `false` | No | — |
| `ee_build_on_commit` | `false` | No | Build Configuration |
| `ee_build_on_tag` | `true` | No | — |
| `ee_registry` | `"registry.example.mil"` | No | — |
| `ee_registry_username` | `"{{ lookup('env', 'REGISTRY_USERNAME') \| default('') }}"` | No | — |
| `ee_registry_password` | `"{{ lookup('env', 'REGISTRY_PASSWORD') \| default('') }}"` | No | — |
| `deploy_to_controller` | `true` | No | Deployment Configuration |
| `deploy_on_main_branch` | `true` | No | — |
| `deploy_environments` | `(see defaults/main.yml)` | No | — |
| `notifications_enabled` | `true` | No | Notification Configuration |
| `notification_channels` | `(see defaults/main.yml)` | No | — |
| `fourth_estate_content_signing` | `true` | No | Fourth Estate Specific Settings |
| `fourth_estate_compliance_checks` | `true` | No | — |
| `fourth_estate_audit_logging` | `true` | No | — |

## Example Playbook

```yaml
- name: Use ans_ci_pipelines
  hosts: all
  gather_facts: false
  roles:
    - role: ans_ci_pipelines
      vars:
        apply_changes: false   # set true to apply
```

## License

MIT
