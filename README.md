# Validate xml against xsd

## Pre-requirement

Install xmlschema package
    ```
    $ pip install xmlschema
    ```

## Steps

This folder contains a simple python script and xsd to validate scenario xml against xsd.

The workflow is simple and can be summarized in these few steps:

1. Place your scenario xml under root directory.
1. Run following command lines to remove unnecessary information:
    ```
    $ sed -i 's/ desc=".*"//g' hybrid_rt.xml (note: this will modify the given XML file in place)
    $ sed -i 's/ readonly=".*"//g' hybrid_rt.xml
    $ sed -i 's/ configurable=".*"//g' hybrid_rt.xml
    ```

1. Validate the xml against the xsd
    ```
    $ python3 val.py
    ```

