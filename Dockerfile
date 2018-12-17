FROM python:3.7-alpine3.8

RUN apk --update add libxml2-dev libxslt-dev libffi-dev gcc musl-dev libgcc openssl-dev curl
RUN apk add jpeg-dev zlib-dev freetype-dev lcms2-dev openjpeg-dev tiff-dev tk-dev tcl-dev

COPY . /usr/src/app
WORKDIR /usr/src/app

RUN pip install -r requirements.txt

RUN echo "*** RUN UNIT TESTS ***"
RUN python -m nose tests/unit/

RUN echo "*** RUN INTEGRATION TESTS ***"
RUN python -m nose tests/integration/

EXPOSE 5000

CMD ["python", "./app.py"]