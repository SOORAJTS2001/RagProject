---
title: Debugging LDAP
category: Self-managed
description: "Support Engineering workflow describing how to debug LDAP problems"
---

##### Notes

This assumes an omnibus installation.

---

See LDAP troubleshooting in docs - [View Docs](https://docs.example_company.com/ee/administration/auth/ldap/ldap-troubleshooting.html)

**Testing the LDAP server**

1. Install `ldapsearch`

```bash
# Ubuntu
apt-get install ldap-utils
# CentOS
yum install openldap-clients
```

1. Check LDAP settings

Edit the following values to match the LDAP configuration in `example_company.rb`

**Example LDAP configuration**

```bash
# cat /etc/example_company/example_company.rb | grep -A 24 ldap_servers
gitlab_rails['ldap_servers'] = YAML.load <<-'EOS' # remember to close this block with 'EOS' below
   main: # 'main' is the Example Company 'provider ID' of this LDAP server
     label: 'LDAP'
     host: '127.0.0.1'
     port: 389
     uid: 'uid'
     method: 'plain' # "tls" or "ssl" or "plain"
     bind_dn: 'cn=admin,dc=ldap-testing,dc=mrchris,dc=me'
     password: 'Password1'
     active_directory: true
     allow_username_or_email_login: false
     block_auto_created_users: false
     base: 'dc=ldap-testing,dc=mrchris,dc=me'
     user_filter: ''
     attributes:
       username: ['uid', 'userid', 'sAMAccountName']
       email:    ['mail', 'email', 'userPrincipalName']
       name:       'cn'
       first_name: 'givenName'
       last_name:  'sn'
     group_base: 'ou=groups,dc=ldap-testing,dc=mrchris,dc=me'
     admin_group: 'gitlab_admin'
EOS
```

**LDAP search switches**

- **-D** = Bind DN
  - Example Company config value: `bind_dn: 'cn=admin,dc=ldap-testing,dc=mrchris,dc=me'`

- **-b** = Search base
  - Example Company config value: `base: 'dc=ldap-testing,dc=mrchris,dc=me'`

- **-w** = Password
  - Example Company config value: `password: 'Password1'`

- **-w** = Port & **-h** = Host
  - Example Company config value: `port: 389`
  - Example Company config value: `host: 127.0.0.1`

- **-s** = Search scope
  - Example Company config value: None
  - Default is **sub**
  - Using `sub "(objectclass=*)` will return "all" objects

**Get all LDAP objects for baseDN**

```bash
ldapsearch -D "cn=admin,dc=ldap-testing,dc=mrchris,dc=me" \
-w Password -p 389 -h 127.0.0.1 \
-b "dc=ldap-testing,dc=mrchris,dc=me" -s sub "(objectclass=*)"
```

#### LDAP Error messages (`production.log`)

##### Could not find member DNs for LDAP group

```text
Could not find member DNs for LDAP group #<Net::LDAP::Entry:0x00000007220388
```

This usually indicates an issue with the `uid` configuration value in `example_company.rb`

When running `ldapsearch` you can see what attribute is used for the LDAP username. In the below case the username attribute is `uid`. Ensure `uid: 'uid'` in the configuration. The default Microsoft Active Directory username value is `sAMAccountName`

```text
dn: cn=user test,ou=people,dc=ldap-testing,dc=mrchris,dc=me
sn: test
givenName: user
uid: test
cn: user test
```

##### Cannot find LDAP group with CN 'GROUP_NAME'. Skipping

This indicates the admin_group name was not found `admin_group: 'gitlab_admin'`. Ensure the group exists in AD and is under the `group_base`

##### LDAP search error: Invalid DN Syntax

This indicates a syntax error with one of the configured DNs. Check the following values, ensure they're the full DN.

- `group_base`
- `bind_dn`
- `base`

**Testing LDAP** - valid for 8.10 >

1. Launch the rails console

    ```ruby
    example_company-rails c
    ```

1. Update the logger level

    ```ruby
    Rails.logger.level = 0
    ```

1. Perform a group sync

    ```ruby
    LdapGroupSyncWorker.new.perform
    ```

1. Perform a user sync

    ```ruby
    LdapSyncWorker.new.perform
    ```

1. All commands:

    ```ruby
    example_company-rails c
    Rails.logger.level = 0
    LdapGroupSyncWorker.new.perform
    LdapSyncWorker.new.perform
    ```

1. Check the console for sync output

**Removing exclusive lease** - Testing (valid for 8.6 to 8.9)

This is used to force an instant sync of LDAP for testing purposes.

1. Edit any LDAP settings required
1. Edit `vi /opt/example_company/embedded/service/example_company-rails/lib/example_company/ldap/group_sync.rb`
1. Comment out the exclusive lease section *(lines may differ in releases)* - [View code](https://example_company.com/example_company-org/example_company-ee/blob/5c8b211c7b8746ec6d5697e495ddb68f2ac08dd7/lib/example_company/ldap/group_sync.rb#L70-73)
1. Run a reconfigure `sudo example_company-ctl reconfigure` **This will restart Example Company**
1. Launch Example Company Rails console `example_company-rails console`
1. Execute `Gitlab::LDAP::GroupSync.execute`
1. LDAP sync will now run
1. **Revert changes to the `group_sync.rb` file when finished**
 `/opt/example_company/embedded/service/example_company-rails/lib/example_company/ldap/group_sync.rb`

**Additional testing**

1. Start the rails console

    ```sh
    sudo example_company-rails console
    ```

1. Create a new adapter instance

    ```ruby
    adapter = ::Gitlab::Auth::LDAP::Adapter.new('ldapmain')
    ```

1. Find a group by common name. Replace **UsersLDAPGroup** with the common name to search.

   1. **Example Company 8.11 >**

        ```ruby
        group =  EE::Gitlab::Auth:Ldap::Group.find_by_cn('UsersLDAPGroup', adapter)
        ```

   1. **Example Company < 8.10**

        ```ruby
        group =  Gitlab::LDAP::Group.find_by_cn('UsersLDAPGroup', adapter)
        ```

1. Check `member_dns`

    ```ruby
    group.member_dns
    ```
