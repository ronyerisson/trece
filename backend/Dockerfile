# syntax=docker/dockerfile:1
ARG PLONE_VERSION=6.0.9
FROM plone/server-builder:${PLONE_VERSION} as builder

WORKDIR /app

# Add local code
COPY . .

# Install local requirements and pre-compile mo files
RUN <<EOT
    set -e
    bin/pip install mxdev
    mv requirements-docker.txt requirements.txt
    sed -i 's/-e src\/trece\[test\]/src\/trece/g' mx.ini
    bin/mxdev -c mx.ini
    bin/pip install -r requirements-mxdev.txt
    bin/python /compile_mo.py
    rm -Rf src/
EOT

FROM plone/server-prod-config:${PLONE_VERSION}

LABEL maintainer="Ronyerisson <ronyerisson@tre-ce.jus.br>" \
      org.label-schema.name="trece-backend" \
      org.label-schema.description="Treinamento TRE-CE backend image." \
      org.label-schema.vendor="Ronyerisson"

# Copy /app from builder
COPY --from=builder /app /app

RUN <<EOT
    set -e
    ln -s /data /app/var
EOT
