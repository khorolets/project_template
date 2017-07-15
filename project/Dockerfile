FROM khorolets/python3.5django

WORKDIR /opt/www

COPY "./requirements.txt" "./requirements.txt"

RUN cd /opt/www && \
    pip3 install -r requirements.txt

COPY "./" "./"

EXPOSE 8000

RUN mkdir /opt/media_root \
    && chown -R nobody "." \
    && chown -R nobody /opt/media_root

RUN chmod +x /opt/www/docker-entrypoint.sh

USER nobody

WORKDIR /opt/www

ENTRYPOINT ["/opt/www/docker-entrypoint.sh"]
