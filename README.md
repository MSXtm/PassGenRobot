# <p align="center">  تولید کننده رمز خوانا برای تلگرام #
<p align="right"> .با کمک این ربات رمز های قدرتمند و خوانا برای برنامه ها یا وبسایت ها ایجاد کنید
<p align="right"> هم اکنون امتحان کنید: https://t.me/PassGenRobot

### <p align="right">  چند ویژگی ###

<p align="right"> تولید رمز با پیچیدگی های مختلف *
<p align="right"> قابلیت ساخت رمز سفارشی *
<p align="right"> حالت اینلاین * 

### <p align="right"> نیازمندی ها ###
* Python 3.7+  
* [aiogram](https://github.com/aiogram/aiogram) – وبسرویس ربات تلگرام
* [TinyDB](https://github.com/msiemens/tinydb) – استفاده از دیتابیس ها خیلی سریع و ساده 
* [XKCD-password-generator](https://github.com/redacted/XKCD-password-generator) – تولید رمز ها

<p align="right"> برای نصب تمامی موارد موردنیاز از دستور زیر کمک بگیرید.
<p align="center"> `pip install -r requirements.txt`

### Presets
 ![Presets](img/readme_presets.png)

`/generate_weak` – 2 words, no separators between words  
`/generate_normal` – 3 words, no separators between words, second word is CAPITALIZED  
`/generate_strong` – 3 words, random CAPITALIZATION, random number as separator between words   
`/generate_stronger` – Same as "strong", but using 4 words    
`/generate_insane` – 4 words, second one CAPITALIZED, separators, prefixes and suffixes  

### Customized Passwords

![Customized Passwords](img/readme_settings.png)  

With `/settings` command you can customize generated passwords. Currently supported settings are number of words (2 to 8), prefixes and suffices in the beginning and in the end of password and separators between words in password. Then just use `/generate` command to create password based on your settings.

### Inline mode

![Inline mode](img/readme_inline.png)

You can also use this bot in inline mode. An indicator on the left shows rough password complexity (green is good, red is not).

