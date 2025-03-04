# A Guide to ROS2 (ros2-tutorial-book)
A tutorial book started by the Fall 2024 RCOS group "Learn ROS through Python Turtle" to teach users ROS2 concepts and basics.

### Building the book
If you'd like to develop and/or build the "A Guide to ROS2" book, you should:

1. Clone this repository.
2. Run `pip install -r requirements.txt` (it is recommended you do this within a virtual environment).
3. (Optional) Edit the book's source files located in the `ros2-tutorial-book/` directory.
4. Run `jupyter-book clean ros2-tutorial-book/` to remove any existing builds.
5. Run `jupyter-book build ros2-tutorial-book/`.

A fully-rendered HTML version of the book will be built in `ros2-tutorial-book/_build/html/`.

### Hosting the book
Please see the [Jupyter Book documentation](https://jupyterbook.org/publish/web.html) to discover options for deploying a book online using services such as GitHub, GitLab, or Netlify.
You can see the website hosted as a GitHub Page by following this [link](https://alejandroobc.github.io/ros2-tutorial-book/).

For GitHub and GitLab deployment specifically, the [cookiecutter-jupyter-book](https://github.com/executablebooks/cookiecutter-jupyter-book) 
includes templates for, and information about, optional continuous integration (CI) workflow files to help easily and 
automatically deploy books online with GitHub or GitLab. For example, if you chose `github` for the `include_ci` cookiecutter option, 
your book template was created with a GitHub actions workflow file that, once pushed to GitHub, automatically renders 
and pushes your book to the `gh-pages` branch of your repo and hosts it on GitHub Pages when a push or pull request is made to the main branch.

## Contributors
We welcome and recognize all contributions. You can see a list of current contributors in the [contributors tab](https://github.com/AlejandrooBC/ros2-tutorial-book/graphs/contributors).

## Credits
This project is created using the excellent open source [Jupyter Book project](https://jupyterbook.org/) and the [executablebooks/cookiecutter-jupyter-book template](https://github.com/executablebooks/cookiecutter-jupyter-book).