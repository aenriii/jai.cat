FROM python:3.12.0b4-bookworm

WORKDIR /root

COPY site.py .

ENTRYPOINT [ "python3", "site.py" ]