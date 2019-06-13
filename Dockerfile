FROM parseq/stepik-variant-calling-tools
RUN apt install python3-pip -y && apt install python3-dev -y
RUN pip3 install 'snakemake<=3.13.3'
