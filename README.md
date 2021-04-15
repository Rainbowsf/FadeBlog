# FadeBlog

О проекте:

Создана на Django 3.2(Python) и голом HTML,  с использованием ClassBasedViews, установленны: Pillow, asgiref, django-crispy-forms, pip, pytz, setuptools, sqlparse. Database:sqlite

В данной социальной сети подключены модели: Users(стандартная), Posts(обычная модель поста - заголовок, текст, автор, дата), followers(2 ключа - пользователь который подписывается и пользователь на которого подписываются, пока не до конца настроена)

В данном проекте предусмотрена возможность входа в систему(Login), всех неавторизованных пользователей переключает на страницу авторизации

Есть возможность посмотреть на список пользователей, зайти к каждому на стену и посмотреть его посты(ListView и DetailView)

Есть возможность зайти к себе на стену, добавлять посты через форму, просматривать свои посты(ListView и DetailView)

Есть возможность добровольного выхода из системы(Logout)

В дальнейшем планируется реализовать систему подписки через модель followers, а также отправку созданных постов на email пользователя
