# Практическое задание "Контроль целостности"
## Подготовленная виртуальная машина с Astra linux
Для выполнения данного задания был скачан образ Astra Linux и установлена версия системы "Смоленск"<br /><br />
![image](https://github.com/m0xeS/TOIB/blob/main/prz4/pics/sysinfo.png)
## Настройка и проверка мандатного контроля целостности
Для измнения конфигурации МКЦ в ОС Astra Linux необходимо воспользоваться утилитой Управление политикой безопасности<br /><br />
![image](https://github.com/m0xeS/TOIB/blob/main/prz4/pics/sec_policy.png)
В меню Режим эксперта можно непосредственно назначить уровни целостности для директорий. В качестве проверки правила NWU я обозначил 2 тестовые директории со следующими правами:<br /><br />
![image](https://github.com/m0xeS/TOIB/blob/main/prz4/pics/sec_pub.png)
![image](https://github.com/m0xeS/TOIB/blob/main/prz4/pics/sec_pub2.png)
Для проверки мандатного контроля необходимо зайти в учетную запись с атрибутом целостности уровня "Низкий".<br />
Здесь можно увидеть, что копирование файла с атрибутом ниже в папку с атрибутом выше не сработало - была получена ошибка доступа<br /><br />
![image](https://github.com/m0xeS/TOIB/blob/main/prz4/pics/error.png)
## Работа с режимом замкнутой программной среды
Для проверки работы режима ЗПС в Управлении политикой безопасности необходимо включить данные настройки:<br /><br />
![image](https://github.com/m0xeS/TOIB/blob/main/prz4/pics/zamkn.png)<br />
В качестве тестового файла был выбран Discord. Результат выполнения на скриншоте:<br /><br />
![image](https://github.com/m0xeS/TOIB/blob/main/prz4/pics/discord.png)
## Работа с утилитами контроля целостности и регламентного контроля целостности
### Использование `gostsum`
Утилита `gostsum` вычисляет хэш-сумму файлов в соответствии с ГОСТ Р 34.11-2012.<br /><br />
![image](https://github.com/m0xeS/TOIB/blob/main/prz4/pics/gostsum.png)
### Использование `afick`
`afick` - утилита, предназначенная для контроля целостности файловой системы ОС. Для корректной работы утилиты сначала создается БД утилиты:<br /><br />
![image](https://github.com/m0xeS/TOIB/blob/main/prz4/pics/afick.png)<br />
Изменим часть системных файлов для получения ответа от утилиты, перед этим сделав бэкап:<br /><br />
![image](https://github.com/m0xeS/TOIB/blob/main/prz4/pics/changes.png)
<br />
