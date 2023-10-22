<strong>Развёртывание Keycloak с использованием Docker</strong>\
<img src=https://github.com/m0xeS/TOIB/blob/main/lr1/pics/keycloak_compose.png>\
<strong>Развёртывание WordPress с использованием Docker</strong>\
<img src=https://github.com/m0xeS/TOIB/blob/main/lr1/pics/wp_compose.png>\
<strong>Панель входа в WordPress\
<img src=https://github.com/m0xeS/TOIB/blob/main/lr1/pics/wp_1st_login.png>\
<strong>Для дальнейшей реализации двухфакторной аутентификации был установлен плагин miniOrange SAML</strong>\
<img src=https://github.com/m0xeS/TOIB/blob/main/lr1/pics/wp_plugin.png>\
<strong>После установки плагина и скачивания необходимого .xml файла, его необходимо импортировать в Keycloak, изменить некоторые значения в соответствии с рекомендациями, описанных в руководствах, а также выполнить несколько действий для корректной настройки</strong>\
<img src=https://github.com/m0xeS/TOIB/blob/main/lr1/pics/wp_add.png>\
<img src=https://github.com/m0xeS/TOIB/blob/main/lr1/pics/wp_add2.png>\
<strong>После настройки необходимо скачать файл с метаинформацией из Keycloak и загрузить его в специальное поле в панели плагина WordPress</strong>\
<img src=https://github.com/m0xeS/TOIB/blob/main/lr1/pics/wp_add.png>\
<strong>После загрузки файла необходимо проверить корректность произведённых шагов при помощи подготовленного теста в панели плагина WordPress</strong>\
<img src=https://github.com/m0xeS/TOIB/blob/main/lr1/pics/wp_add.png>\
<strong>Теперь вход доступен также через Keycloak</strong>\
<img src=https://github.com/m0xeS/TOIB/blob/main/lr1/pics/wp_login2.png>\
<strong>После включения обязательной двухфакторной атутентификации при попытке аутентифицироваться отображается соответствующая страница настройки</strong>\
<img src=https://github.com/m0xeS/TOIB/blob/main/lr1/pics/1mob_auth.png>\
<strong>После настройки при дальнейших попытках входа отображается страница ввода одноразового кода при входе в аккаунт</strong>\
<img src=https://github.com/m0xeS/TOIB/blob/main/lr1/pics/otp.png>\
