#!/bin/bash

DB_SERVER_HOST="{{ DATABASE_HOST }}"
SECRET="$(openssl rand -base64 30)"

cat <<- 'EOF' > /etc/httpd/conf.d/zz-cb-phpmyadmin.conf
<Directory /usr/share/phpMyAdmin/>
    AddDefaultCharset UTF-8
    <IfModule mod_authz_core.c>
        <RequireAny>
            Require all granted
            # Require ip 127.0.0.1
            # Require ip ::1
        </RequireAny>
    </IfModule>
</Directory>
EOF


cat <<-'EOF' > /etc/phpMyAdmin/config.inc.php
<?php
$i = 0;
$i++;
$cfg['Servers'][$i]['verbose'] = 'mariadb';
$cfg['Servers'][$i]['port'] = '';
$cfg['Servers'][$i]['socket'] = '';
$cfg['Servers'][$i]['connect_type'] = 'tcp';
$cfg['Servers'][$i]['auth_type'] = 'cookie';
$cfg['Servers'][$i]['user'] = 'root';
$cfg['Servers'][$i]['password'] = '';
$cfg['DefaultLang'] = 'en';
$cfg['ServerDefault'] = 1;
$cfg['UploadDir'] = '';
$cfg['SaveDir'] = '';
EOF

cat <<-EOF >> /etc/phpMyAdmin/config.inc.php
\$cfg['Servers'][\$i]['host'] = '$DB_SERVER_HOST';
\$cfg['blowfish_secret'] = '$SECRET';
?>
EOF
