FROM alpine:3.4

RUN apk --no-cache update && \
    apk --no-cache add python py-pip py-setuptools bash ca-certificates groff less && \
    pip --no-cache-dir install awscli && \
    rm -rf /var/cache/apk/*
RUN mkdir /sourcefiles
WORKDIR /sourcefiles
RUN aws s3 cp s3://filestaging/ /sourcefiles/ --recursive
RUN chmod +x /sourcefiles/*
