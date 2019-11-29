# CS3012 - Software Engineering: Individual Project

## Project Structure

| Branch | Content |
| - | - |
| `master` *(current)* | Contains the *Social Graph* aspect of the project. This consists of the Python crawler and the JavaScript web application. |
| `ghaccess` | Contains the *GitHub Access* aspect of the project. Basically just a simple query of the GitHub API via Python. |

## Live Demonstration

The live web application can be accessed [here](http://34.254.197.70).

## Running the Application

### Environment Variables

The following environment variables must be set before the crawler or web app can be run:

| Name | Description |
| - | - |
| `GH_API_TOKEN` | GitHub API access token |
| `GH_DB_SERVER` | Database server |
| `GH_DB_USER` | Database username |
| `GH_DB_PASS` | Database password |
| `GH_DB_NAME` | Database schema name |

### Building the Database

The MySQL database can be built by executing the scripts in the `database/` folder.

### Running the Crawler

Start the crawler from within the `crawler/` folder by running the following command:

`python3 crawler.py`

### Deploying the Webapp

Start an Apache server using XAMPP and root it in the `webapp/` folder.

## Reference Material

- [D3.js Force-Directed Graph](https://observablehq.com/@d3/force-directed-graph)
- [D3.js Basic Scatter Graph](https://www.d3-graph-gallery.com/graph/scatter_basic.html)
