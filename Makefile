.PHONY: build run clean deploy

IMAGE_NAME = tmp-simple-code-reviewer
PORT = 8080
PROJECT_ID = $(shell gcloud config get-value project)

build:
	docker build -t $(IMAGE_NAME) .

run:
	docker run -p $(PORT):$(PORT) \
		-v $(HOME)/.config/gcloud:/root/.config/gcloud \
		--rm -it \
		$(IMAGE_NAME)

clean:
	docker rmi $(IMAGE_NAME)

deploy:
	gcloud builds submit --config cloudbuild.yaml
