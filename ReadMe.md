# Text file uploader:

This API provides the following functionalities:

- User can upload and store text files
- The user can get one random line for a previously uploaded file along with details such as line number, file name and the letter which occurs most often in the line
- User can get 20 longest lines of the previously uploaded text file
- User can get 100 longest lines from the all uploaded text files

## Installations:

## Using docker

Install [docker](https://docs.docker.com) and [docker compose](https://docs.docker.com/compose)

Then run the following cmd from the root folder to start the web app

     docker-compose up

or to start the app in the background

     docker-compose -d

## Manually

Please use the following steps to run the app manually

1. Install [python 3.8](https://www.python.org/downloads) or higher
2. From the project root run `pipenv install` to install all dependencies
3. Then start pipenv by running `pipenv shell`
4. Then from [app](/app/) directory run cmd `python run.py` or `python3 run.py` to start the web app

## Usage

- After running the web app open any web browser and go to `http://localhost:8610`.
- Select and press the upload button to upload the file (only text files are allowed).
- Go to `http://localhost:8610/one-random-line` to get one random line from a previously uploaded file.
- It will return one random along with details such as line number, file name and the letter which occurs most often in the line if the request is `application/*`.
- It will return one random line of a previously uploaded file via HTTP as `text/plain,`
  `application/json` or `application/xml` depending on the request accept header (if provided).
- Go to `http://localhost:8610/twenty-longest-lines` to get the 20 longest lines of the previously uploaded text file.
- Go to `http://localhost:8610/hundred-longest-lines` to get 100 longest lines of the all uploaded text files.
- There are already a few sample text files in [uploaded_files](/app/api/uploaded_files/) for showing the above-requested data(if the user asks for data before uploading the text file).

- Note: if a previously uploaded text file contains less than 20 lines or all uploaded text files contain less than 100 lines then all lines are shown for respective requests.
