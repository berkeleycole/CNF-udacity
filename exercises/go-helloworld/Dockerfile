# FROM golang:alpine
# WORKDIR /go/src/app
# COPY . /go/src/app
# RUN go build -o helloworld
# EXPOSE 6111
# CMD ["./helloworld"]


FROM golang:alpine

WORKDIR /go/src/app

ADD . .

RUN go build  -o helloworld

EXPOSE 6111

CMD ["./helloworld"]
