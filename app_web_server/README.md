# Application & Web Server SRG Hardening

Ansible roles implementing the DISA **Application Server SRG** and
**Web Server SRG** for common middleware.

## Roles

| Role | SRG | Target |
|------|-----|--------|
| [`apache_web_server_srg`](roles/apache_web_server_srg/) | Web Server SRG (`SRG-APP-*-WSR-*`) | Apache HTTP Server |
| [`tomcat_app_server_srg`](roles/tomcat_app_server_srg/) | Application Server SRG V4R4 (`SRG-APP-*-AS-*`) | Apache Tomcat |

Both are **safe by default** (assessment / check mode) until you pass
`-e apply_changes=true`. See each role's README for the grab-and-go quick start.

> SRGs are generic baselines. For IIS, see `windows/roles/win_iis`. For
> WebLogic/JBoss/WildFly, fork `tomcat_app_server_srg` and adjust the XML paths —
> the SRG control set is the same.
