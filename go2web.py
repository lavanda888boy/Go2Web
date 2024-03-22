import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-u", help="Make an HTTP request to the specified URL and print the response")
    parser.add_argument("-s", nargs='+', help="Make an HTTP request to search the term using your favorite search engine and print top 10 results")

    args = parser.parse_args()
    print(args.s)

if __name__ == "__main__":
    main()
