#!/bin/bash
# Display all HTTP methods the server will accept
curl -sI "$1" | grep "Allow:" | cut -d " " -f2-
#!/bin/bash
# Display all HTTP methods the server will accept
curl -sI "$1" | grep "Allow:" | cut -d " " -f2-
