## Python 3 GRPC template

A [cookiecutter](https://cookiecutter.readthedocs.io/en/latest/README.html) (project template) for creating gRPC services in Python 3

* Powered by [cruft](https://cruft.github.io/cruft/) which lets you create templates and update them in projects later as you make changes to the template



### Usage

Make sure you have [`cruft`](https://github.com/cruft/cruft) installed using [`Install Cruft`](https://github.com/cruft/cruft#installation)

Create a new project:

```sh
cruft create https://github.com/usernames/sentieopy3_template
```

The CLI interface will ask some basic questions, such the name of the project, and then generate the boilerplate code

After that you can make it a proper git repo:

```sh
cd <your-project-slug>
git init
git add .
git commit -m "Initial project structure from cruft template"
```

You can get the updates into your project with:

```sh
cruft update
```

Setup Sentieo GRPC Application 
https://sentieo.atlassian.net/wiki/spaces/E2/pages/2160263177/How+to+setup+a+GRPC+service


