FROM php

WORKDIR /app

COPY . .

RUN apt-get update 
RUN docker-php-ext-install pdo_mysql
RUN apt-get install -y git zip unzip
RUN curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/local/bin --filename=composer
RUN composer require --dev phpunit/phpunit ^9

CMD php -S 0.0.0.0:8000