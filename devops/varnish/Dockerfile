# syntax=docker/dockerfile:1
FROM varnish:7.4

LABEL maintainer="Ronyerisson <ronyerisson@tre-ce.jus.br>" \
      org.label-schema.name="trece-varnish" \
      org.label-schema.description="Treinamento TRE-CE Varnish image." \
      org.label-schema.vendor="Ronyerisson"

COPY etc/varnish.vcl /etc/varnish/default.vcl
