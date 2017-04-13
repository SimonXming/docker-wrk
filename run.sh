docker run -it --net=host --rm && \
    --entrypoint=/bin/bash && \
    -v $(pwd)/data:/data && \
    simonshyu/wrk_lua:ubuntu