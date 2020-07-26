# [Image Classification App](https://hub.docker.com/r/shriawesome/cifar_classification)

A web app to Classify image based on CIFAR dataset.

It uses Convolution Neural Network trained on CIFAR dataset to classify images.

## Usage
You can run following commands to get the app running.

	docker pull shriawesome/cifar_classification:latest
		
	docker run -d -p 80:80 -v stats:/home/app/stats shriawesome/cifar_classification:latest

Get app in your browser by visiting `http://localhost`.

## Contributors
* [Shrikant Kendre](https://github.com/shriawesome)