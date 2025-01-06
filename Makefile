.PHONY: build run clean

IMAGE_NAME = simple-code-reviewer
PORT = 7860

build:
	docker build -t $(IMAGE_NAME) .

run:
	docker run -p $(PORT):$(PORT) \
		-v $(HOME)/.config/gcloud:/root/.config/gcloud \
		--rm -it \
		$(IMAGE_NAME)

clean:
	docker rmi $(IMAGE_NAME) 
