# CS3012 - Software Engineering: Individual Project

## Project Structure

| Branch | Content |
| - | - |
| `master` | Contains the *Social Graph* aspect of the project. This consists of the Python Flask web application and D3.js visualisation. |
| `ghaccess` *(current)* | Contains the *GitHub Access* aspect of the project. Basically just a simple query of the GitHub API via Python. |

## Running `ghaccess.py`

### Windows

Install PyGithub via Pip:

```
python -m pip install PyGithub
```

Add your GitHub API token as an environment variable:

```
set GH_API_TOKEN={YOUR_API_TOKEN_HERE}
```

### Linux

Install PyGithub via Pip:

```
pip install PyGithub
```

Add your GitHub API token as an environment variable:

```
export GH_API_TOKEN={YOUR_API_TOKEN_HERE}
```
