# Go2Web
CLI application for surfing the internet.

# Usage
In order to test the application it is necessary to perform several steps:

* install all the necessary requirements from `requirements.txt`:
    ```
    pip install -r requirements.txt
    ```

* create the executable of the script:
    ```
    pyinstaller --onefile go2web.py
    ```

* the resulting executable will appear in the `dist` folder; you can launch it and use the following commands:
    ```
    go2web -u <URL> # make an HTTP request to the specified URL and print the response
    go2web -s <search-term> # make an HTTP request to google search the term or multiple terms and print top 10 results
    go2web -h # show this help
    ```

# Demo
![demo](https://github.com/lavanda888boy/Go2Web/assets/112694991/6a4a10bc-65d3-4b09-b7b8-3f22df757df5)
