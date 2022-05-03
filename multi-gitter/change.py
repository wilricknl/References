#!/usr/bin/env python3

def main():
    license = open("LICENSE", "r+")
    content = license.read()
    license.seek(0)
    license.write(content.replace("2022", "2023"))
    license.truncate()
    license.close()


if __name__=="__main__":
    main()
