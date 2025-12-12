
from test_project.utils.http_client import get_json

def main():
    print("Fetching GitHub API status...")
    status = get_json("https://api.github.com")
    print("GitHub API Status:")
    print(status)

if __name__ == "__main__":
    main()
