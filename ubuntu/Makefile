VERSION = ubuntu
NAMESPACE = simonshyu
IMAGE_NAME = wrk_lua

all: build

build: Dockerfile
	docker build -t $(NAMESPACE)/$(IMAGE_NAME):$(VERSION) .

push:
	docker push $(NAMESPACE)/$(IMAGE_NAME):$(VERSION)