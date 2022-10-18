# Build Stage
FROM fuzzers/atheris:2.0.7-python3.9

# Install dependencies

ADD ./mayhem/fuzz_phone_parsing.py /fuzz_phone_parsing.py
RUN python3 -m pip install phonenumbers

CMD ["/fuzz_phone_parsing.py"]
